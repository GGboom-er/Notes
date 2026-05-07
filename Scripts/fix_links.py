import os
import re

sources_dir = r'Y:\GGbommer\scripts\Notes\Sources'

for root, _, files in os.walk(sources_dir):
    for f in files:
        if f.endswith('.md'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                
            original_content = content
            
            # 1. Clean up broken headers that look like:
            # | 链接 |      |
            # | :--- | ---- |
            # We replace them to standard:
            # | 链接 |
            # | :--- |
            content = re.sub(r'\|\s*链接\s*\|\s*\|\n\|\s*:-+\s*\|-+\s*\|', r'| 链接 |\n| :--- |', content)
            
            # 2. In rows, replace broken cells:
            # The broken format is like:
            # | [[RigLogic白皮书 | 打开]] |
            # Which is split into two cells due to the | character.
            # It usually looks like `[[RigLogic白皮书 ` in one cell, and ` 打开]]` in the next.
            # Example text: `[[RigLogic白皮书 ` | ` 打开]]`
            # Let's match the whole pattern spanning columns:
            # \[\[([^|\]]+?)\s*\|\s*打开\]\]
            # Wait, if the markdown table parser literally put a pipe in the source file, let's look at the source!
            # The source is: | [[Maya Python游戏与影视编程指南 | 打开]] |
            # So the pipe is right there.
            content = re.sub(r'\[\[\s*([^|\]]+?)\s*\|\s*打开\s*\]\]', r'[[\1]]', content)
            
            # Also occasionally there might be a trailing empty column if the header had 4 columns.
            # Example: | [[\1]] | |
            content = re.sub(r'(\[\[[^\]]+\]\]\s*\|)\s*\|(\r?\n)', r'\1\2', content)
            
            # 3. Replace paths in backticks like `y:\GGbommer\Rig\Learn_Facial`
            # With Obsidian internal links: [[Learn_Facial]]
            def path_replacer(match):
                full_path = match.group(1)
                basename = os.path.basename(full_path.strip('\\/')).strip()
                return f'[[{basename}]]'
                
            content = re.sub(r'`([A-Za-z]:\\[^`\n]+)`', path_replacer, content)
            
            if content != original_content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f'Fixed {f}')
