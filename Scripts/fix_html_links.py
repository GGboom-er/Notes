import os
import re
import urllib.parse
import shutil

base_dir = r"Y:\GGbommer\scripts\Notes\Sources\Library\HTML"
index_file = r"Y:\GGbommer\scripts\Notes\🌐 Web文章索引.md"

html_mapping = {
    "🔧 Maya API 开发（27篇）": "Maya_API_Dev",
    "🐍 Python & 开发环境（12篇）": "Python_Tools",
    "🦴 绑定技术（10篇）": "Rigging_Tech",
    "😀 面部 & MetaHuman（4篇）": "Face_MetaHuman",
    "📐 数学（7篇）": "Math_Graphics",
    "🌊 Ziva & 动力学（3篇）": "Dynamics_Simulation",
    "🔖 参考 & 其他（5篇）": "Ref_Others"
}

# 1. Move files & fix tags
for ch_folder, en_folder in html_mapping.items():
    ch_path = os.path.join(base_dir, ch_folder)
    en_path = os.path.join(base_dir, en_folder)
    if os.path.exists(ch_path):
        os.makedirs(en_path, exist_ok=True)
        for f in os.listdir(ch_path):
            if f.endswith(".md"):
                src = os.path.join(ch_path, f)
                dst = os.path.join(en_path, f)
                with open(src, "r", encoding="utf-8") as file:
                    content = file.read()
                content = content.replace(f"tags: [html, {ch_folder}]", f"tags: [html, {en_folder}]")
                content = content.replace(f"归属分类**：{ch_folder}", f"归属分类**：{en_folder}")
                with open(dst, "w", encoding="utf-8") as file:
                    file.write(content)
                os.remove(src)
        try:
            os.rmdir(ch_path)
        except Exception:
            pass

# 2. Build Map from URL to Markdown relative path
url_to_md = {}
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".md"):
            md_path = os.path.join(root, f)
            with open(md_path, "r", encoding="utf-8") as file:
                content = file.read()
                # Use string find instead of complex regex to be safe
                prefix = "Y:\\GGbommer\\Lib\\Http\\"
                idx = content.find(prefix)
                if idx != -1:
                    end_idx = content.find("`", idx)
                    if end_idx != -1:
                        local_name = content[idx + len(prefix) : end_idx].replace("\\", "/")
                        rel_path = "Sources/Library/HTML/" + os.path.basename(root) + "/" + f
                        url_to_md[local_name.lower()] = rel_path.replace("\\", "/")

# 3. Update Web文章索引.md
with open(index_file, "r", encoding="utf-8") as f:
    index_content = f.read()

def replace_link(match):
    text = match.group(1)
    url = match.group(2)
    decoded_url = urllib.parse.unquote(url)
    prefix = "y:/ggbommer/lib/http/"
    idx = decoded_url.lower().find(prefix)
    if idx != -1:
        local_name = decoded_url[idx+len(prefix):]
        if local_name.lower() in url_to_md:
            # Obsidian wikilink or standard markdown link
            # Since standard markdown links are better for external markdown parsers, we use that
            # and escape spaces
            new_path = url_to_md[local_name.lower()].replace(" ", "%20")
            return f"[{text}]({new_path})"
    return match.group(0)

new_index_content = re.sub(r"\[([^\]]+)\]\((file:///[^\)]+)\)", replace_link, index_content)

with open(index_file, "w", encoding="utf-8") as f:
    f.write(new_index_content)

print(f"Updated links using {len(url_to_md)} mappings.")
