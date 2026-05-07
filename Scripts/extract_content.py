import os
import re
import traceback

print('Starting script...')

def process_tools(notes_dir):
    import ast
    tools_dir = os.path.join(notes_dir, 'Tools')
    processed = 0
    for root, _, files in os.walk(tools_dir):
        for f in files:
            if f.endswith('.md') and f != '0. 工具箱总览.md':
                path = os.path.join(root, f)
                try:
                    with open(path, 'r', encoding='utf-8') as f_in:
                        content = f_in.read()
                        
                    # find local path
                    match = re.search(r'file:///([A-Za-z]:/[^)]+)', content)
                    if not match:
                        continue
                        
                    local_path = match.group(1).replace('%20', ' ')
                    if not os.path.exists(local_path):
                        continue
                    
                    added_info = []
                    
                    if os.path.isdir(local_path):
                        # extract README
                        readme_path = os.path.join(local_path, 'README.md')
                        if os.path.exists(readme_path):
                            with open(readme_path, 'r', encoding='utf-8', errors='ignore') as r:
                                r_content = r.read().strip()
                                if r_content:
                                    added_info.append('### 📖 README\n\n' + r_content[:2000] + ('\n... (截断)' if len(r_content)>2000 else ''))
                        
                        # read python files for docstrings
                        py_files = [file for file in os.listdir(local_path) if file.endswith('.py')]
                        if py_files:
                            py_info = ['### 🐍 代码结构与接口']
                            for py in py_files[:3]:
                                py_path = os.path.join(local_path, py)
                                try:
                                    with open(py_path, 'r', encoding='utf-8', errors='ignore') as pf:
                                        tree = ast.parse(pf.read())
                                        doc = ast.get_docstring(tree)
                                        if doc:
                                            py_info.append(f'**{py}**:\n```text\n{doc[:500]}\n```')
                                        funcs = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
                                        classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
                                        if classes or funcs:
                                            class_str = ', '.join([f'`class {c}`' for c in classes[:5]])
                                            func_str = ', '.join([f'`def {func}()`' for func in funcs[:5]])
                                            py_info.append(f'- **{py}**: {class_str} {func_str}')
                                except Exception:
                                    pass
                            added_info.append('\n'.join(py_info))
                            
                    elif os.path.isfile(local_path) and local_path.endswith('.py'):
                         try:
                             with open(local_path, 'r', encoding='utf-8', errors='ignore') as pf:
                                 tree = ast.parse(pf.read())
                                 doc = ast.get_docstring(tree)
                                 py_info = ['### 🐍 脚本概要']
                                 if doc:
                                     py_info.append(f'```text\n{doc[:1000]}\n```')
                                 funcs = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
                                 if funcs:
                                     func_str = ', '.join([f'`{func}`' for func in funcs[:10]])
                                     py_info.append(f'**导出的主要函数**: {func_str}')
                                 added_info.append('\n'.join(py_info))
                         except Exception:
                             pass
                    
                    if added_info:
                        new_text = '\n\n'.join(added_info)
                        content = re.sub(r'文档缺失，请查看源码或本地目录内容。', new_text, content)
                        content = re.sub(r'文档缺失', new_text, content)
                        with open(path, 'w', encoding='utf-8') as f_out:
                            f_out.write(content)
                        processed += 1
                        
                except Exception as e:
                    pass
                    
    print(f'Processed {processed} Tool files.')

def process_html(notes_dir):
    from bs4 import BeautifulSoup
    from markdownify import markdownify as md
    html_dir = os.path.join(notes_dir, 'Sources', 'Library', 'HTML')
    processed = 0
    if not os.path.exists(html_dir): return
    for root, _, files in os.walk(html_dir):
        for f in files:
            if f.endswith('.md'):
                path = os.path.join(root, f)
                try:
                    with open(path, 'r', encoding='utf-8') as f_in:
                        content = f_in.read()
                    
                    if '### 📄 离线网页正文' in content:
                        continue
                        
                    match = re.search(r'file:///([A-Za-z]:/[^)]+\.html)', content, re.IGNORECASE)
                    if match:
                        local_path = match.group(1).replace('%20', ' ')
                        if os.path.exists(local_path):
                            with open(local_path, 'r', encoding='utf-8', errors='ignore') as hf:
                                html_text = hf.read()
                                soup = BeautifulSoup(html_text, 'html.parser')
                                for script in soup(['script', 'style', 'nav', 'footer']):
                                    script.decompose()
                                
                                md_text = md(str(soup), heading_style='ATX')
                                md_text = re.sub(r'\n{3,}', '\n\n', md_text).strip()
                                
                                if md_text:
                                    content += f'\n\n---\n### 📄 离线网页正文（摘要/摘录）\n\n'
                                    content += md_text[:5000] + ('\n\n... (原文过长，已截断)' if len(md_text)>5000 else '')
                                    
                                    with open(path, 'w', encoding='utf-8') as f_out:
                                        f_out.write(content)
                                    processed += 1
                except Exception as e:
                    pass
                    
    print(f'Processed {processed} HTML files.')

def process_pdf(notes_dir):
    import fitz # PyMuPDF
    pdf_dir = os.path.join(notes_dir, 'Sources', 'Library', 'PDF')
    processed = 0
    if not os.path.exists(pdf_dir): return
    for root, _, files in os.walk(pdf_dir):
        for f in files:
            if f.endswith('.md'):
                path = os.path.join(root, f)
                try:
                    with open(path, 'r', encoding='utf-8') as f_in:
                        content = f_in.read()
                        
                    if '### 📄 PDF 提取内容' in content:
                        continue
                        
                    match = re.search(r'file:///([A-Za-z]:/[^)]+\.pdf)', content, re.IGNORECASE)
                    if match:
                        local_path = match.group(1).replace('%20', ' ')
                        if os.path.exists(local_path):
                            try:
                                doc = fitz.open(local_path)
                                toc = doc.get_toc()
                                toc_md = []
                                if toc:
                                    toc_md.append('**文档目录**:')
                                    for lvl, title, page in toc[:20]:
                                        indent = "  " * (lvl-1)
                                        toc_md.append(f'{indent}- {title} (p.{page})')
                                    if len(toc) > 20:
                                        toc_md.append('- ... (余下目录省略)')
                                
                                text = doc[0].get_text('text') if len(doc) > 0 else ''
                                if len(doc) > 1: text += '\n' + doc[1].get_text('text')
                                
                                added_info = '\n\n---\n### 📄 PDF 提取内容\n\n'
                                if toc_md:
                                    added_info += '\n'.join(toc_md) + '\n\n'
                                
                                text = text.strip()
                                if text:
                                    added_info += '**前言/导读**:\n' + text[:2000] + ('\n... (截断)' if len(text)>2000 else '')
                                    
                                if toc_md or text:
                                    content += added_info
                                    with open(path, 'w', encoding='utf-8') as f_out:
                                        f_out.write(content)
                                    processed += 1
                                doc.close()
                            except Exception as doc_e:
                                pass
                except Exception as e:
                    pass
                    
    print(f'Processed {processed} PDF files.')

notes_dir = r'Y:\GGbommer\scripts\Notes'
process_tools(notes_dir)
process_html(notes_dir)
process_pdf(notes_dir)
print('Done!')
