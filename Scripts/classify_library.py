import json
import re
import os

def normalize_text(text):
    if not text:
        return ""
    # Convert full-width to half-width characters
    mapping = {
        '（': '(',
        '）': ')',
        '：': ':',
        '—': '-',
        '–': '-',
        '·': '.'
    }
    for k, v in mapping.items():
        text = text.replace(k, v)
    # Remove all whitespace and convert to lowercase
    return re.sub(r'\s+', '', text).lower()

def parse_md_moc(file_path):
    data = {}
    current_category = None
    
    # Mapping section headers to target categories
    # PDF Categories mapping
    pdf_mapping = {
        "🦴 Maya 技术文档": "Maya_Tech_Docs",
        "🎭 面部绑定": "Facial_Rigging",
        "🦾 角色绑定与动画": "Character_Animation",
        "🧮 蒙皮算法（学术论文）": "Skinning_Algorithms",
        "⚡ 物理仿真": "Physics_Sim",
        "🧍 解剖学与造型": "Anatomy_Art",
        "🐍 Python": "Python_Dev",
        "🎮 游戏引擎与管线": "Engine_Pipeline",
        "🔧 工具文档": "Maya_Tech_Docs"
    }
    
    # HTML Categories mapping
    html_mapping = {
        "🔧 Maya API 开发": "Maya_API_Dev",
        "🐍 Python & 开发环境": "Python_Tools",
        "🦴 绑定技术": "Rigging_Tech",
        "😀 面部 & MetaHuman": "Face_MetaHuman",
        "📐 数学": "Math_Graphics",
        "🌊 Ziva & 动力学": "Dynamics_Simulation",
        "🔖 参考 & 其他": "Ref_Others"
    }
    
    all_mapping = {**pdf_mapping, **html_mapping}

    if not os.path.exists(file_path):
        return data

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for line in lines:
        # Detect category
        cat_match = re.search(r'^##\s+(.*)', line)
        if cat_match:
            raw_cat = cat_match.group(1).strip()
            # Clean category name (might have count like (27篇) or （27篇）)
            clean_cat = re.sub(r'\s*[\(（]\d+篇[\)）]', '', raw_cat).strip()
            current_category = all_mapping.get(clean_cat, clean_cat)
            continue
            
        # Detect table row
        # | Name | Desc | Link |
        table_match = re.search(r'^\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|', line)
        if table_match and current_category:
            name = table_match.group(1).strip()
            desc = table_match.group(2).strip()
            if name == "文件名" or name == "文章" or name.startswith("---"):
                continue
            data[name] = {
                "category": current_category,
                "detailed_desc": desc
            }
            
    return data

def guess_pdf_category(name):
    name_lower = name.lower()
    if any(k in name_lower for k in ["anatomy", "解剖", "figure", "body", "sculptor"]):
        return "Anatomy_Art"
    if any(k in name_lower for k in ["skin", "蒙皮", "deform", "decomposition", "ssdr"]):
        return "Skinning_Algorithms"
    if any(k in name_lower for k in ["face", "facial", "expression", "表情", "riglogic"]):
        return "Facial_Rigging"
    if any(k in name_lower for k in ["physics", "simulation", "pbd", "dynamics", "动力学", "仿真", "cloth", "hair"]):
        return "Physics_Sim"
    if any(k in name_lower for k in ["python", "pyqt", "pyside", "script"]):
        return "Python_Dev"
    if any(k in name_lower for k in ["engine", "ue4", "unreal", "pipeline", "管线", "堡垒之夜"]):
        return "Engine_Pipeline"
    if any(k in name_lower for k in ["rig", "anim", "绑定", "动画", "mgear", "skeleton"]):
        return "Character_Animation"
    return "Maya_Tech_Docs"

def guess_html_category(name, title):
    text = (name + " " + title).lower()
    if any(k in text for k in ["api", "plugin", "c++", "command", "node", "sdk"]):
        return "Maya_API_Dev"
    if any(k in text for k in ["python", "pyqt", "pyside", "pycharm", "cython", "numpy", "scipy"]):
        return "Python_Tools"
    if any(k in text for k in ["rig", "绑定", "joint", "skin", "weight", "matrix", "deform", "ik", "spline"]):
        return "Rigging_Tech"
    if any(k in text for k in ["face", "面部", "metahuman", "facs", "blendshape"]):
        return "Face_MetaHuman"
    if any(k in text for k in ["math", "数学", "vector", "matrix", "quaternion", "dot product", "矩阵", "向量"]):
        return "Math_Graphics"
    if any(k in text for k in ["ziva", "dynamic", "cloth", "simulation", "动力学", "仿真"]):
        return "Dynamics_Simulation"
    return "Ref_Others"

def main():
    raw_data_path = r'Y:\GGbommer\scripts\Notes\library_raw_data.json'
    pdf_moc_path = r'Y:\GGbommer\scripts\Notes\Sources\📚 PDF文献库索引.md'
    html_moc_path = r'Y:\GGbommer\scripts\Notes\Sources\🌐 Web文章索引.md'
    output_path = r'Y:\GGbommer\scripts\Notes\library_classified.json'

    with open(raw_data_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    pdf_moc = parse_md_moc(pdf_moc_path)
    html_moc = parse_md_moc(html_moc_path)

    results = []

    # Process PDFs
    for item in raw_data.get('pdf', []):
        name = item['name']
        path = item['path']
        
        # Normalize name for matching
        match_key = name.replace(".pdf", "").replace(".pptx", "").replace(".doc", "").strip()
        norm_name = normalize_text(match_key)
        
        found = False
        entry = None
        
        # Try matching
        for k, v in pdf_moc.items():
            norm_k = normalize_text(k)
            if norm_k == norm_name or norm_k in norm_name or norm_name in norm_k:
                entry = v
                found = True
                break
        
        if found:
            category = entry['category']
            detailed_desc = entry['detailed_desc']
            one_liner = detailed_desc.split('。')[0] if '。' in detailed_desc else detailed_desc
        else:
            category = guess_pdf_category(name)
            detailed_desc = ""
            one_liner = "自动分类：基于文件名的初步推断"
            
        results.append({
            "name": name,
            "path": path,
            "category": category,
            "one_liner": one_liner,
            "detailed_desc": detailed_desc,
            "type": "PDF"
        })

    # Process HTMLs
    for item in raw_data.get('http', []):
        name = item['name']
        path = item['path']
        title = item.get('title', '')
        
        norm_name = normalize_text(name)
        norm_title = normalize_text(title)
        
        found = False
        entry = None
        
        # Search in HTML MOC
        for k, v in html_moc.items():
            norm_k = normalize_text(k)
            if (norm_k and norm_k in norm_title) or (norm_title and norm_k in norm_title) or (norm_k and norm_k in norm_name):
                entry = v
                found = True
                break
        
        if found:
            category = entry['category']
            detailed_desc = entry['detailed_desc']
            one_liner = detailed_desc.split('。')[0] if '。' in detailed_desc else detailed_desc
        else:
            category = guess_html_category(name, title)
            detailed_desc = ""
            one_liner = "自动分类：基于标题的初步推断"

        results.append({
            "name": name,
            "path": path,
            "category": category,
            "one_liner": one_liner,
            "detailed_desc": detailed_desc,
            "type": "HTML"
        })

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"Successfully processed {len(results)} items.")

if __name__ == "__main__":
    main()
