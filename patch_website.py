import os
import re

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")
html_path = os.path.join(dir_path, "index.html")

# Read JS
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Read HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

def patch_content(text):
    # Protect paths
    text = text.replace("/navisights-trike", "/__TEMP_DIR__")
    text = text.replace("navisights_trike", "__TEMP_FILE__")
    text = text.replace("navisights-51596", "__TEMP_FB__")
    
    # Replace texts
    text = text.replace("Navisights", "BV 9")
    text = text.replace("navisights", "bv 9")
    text = text.replace("NAVISIGHTS", "BV 9")
    
    # Restore paths
    text = text.replace("/__TEMP_DIR__", "/navisights-trike")
    text = text.replace("__TEMP_FILE__", "navisights_trike")
    text = text.replace("__TEMP_FB__", "navisights-51596")
    
    # Replace contacts
    text = text.replace("bv 92023@gmail.com", "madhansekar537@gmail.com")
    text = text.replace("navisights2023@gmail.com", "madhansekar537@gmail.com")
    text = text.replace("+919080168075", "+917530075710")
    text = text.replace("https://www.linkedin.com/in/sivanesh-k-s-6a9991218/", "https://www.linkedin.com/in/madhan-sekar-b61870333")
    
    # Remove navigation items
    # The pattern is something like {path:"/about",name:"About",icon:G.jsx(Db,{strokeWidth:1})},
    text = re.sub(r'\{path:"/about",name:"About",icon:[^}]+\},', '', text)
    text = re.sub(r'\{path:"/achievements",name:"Achievements",icon:[^}]+\},', '', text)
    text = re.sub(r'\{path:"/services",name:"Services",icon:[^}]+\},', '', text)

    # In case there are arrays without trailing commas:
    text = re.sub(r',\{path:"/about",name:"About",icon:[^}]+\}', '', text)
    text = re.sub(r',\{path:"/achievements",name:"Achievements",icon:[^}]+\}', '', text)
    text = re.sub(r',\{path:"/services",name:"Services",icon:[^}]+\}', '', text)

    return text

js_content_patched = patch_content(js_content)
html_content_patched = patch_content(html_content)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content_patched)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content_patched)

print("Patching complete!")
