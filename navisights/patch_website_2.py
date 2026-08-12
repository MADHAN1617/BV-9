import os
import re

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")

with open(js_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Safe replacements for contact info
text = text.replace("navisights2023@gmail.com", "madhansekar537@gmail.com")
text = text.replace("+919080168075", "+917530075710")
text = text.replace("https://www.linkedin.com/in/sivanesh-k-s-6a9991218/", "https://www.linkedin.com/in/madhan-sekar-b61870333")

# Replace Display name
text = text.replace("Navisights", "BV 9")
text = text.replace("NAVISIGHTS", "BV 9")

# Remove nav items. Use regex to be flexible with component names like Db, Pb, Rb
# {path:"/about",name:"About",icon:G.jsx(Db,{strokeWidth:1})}
text = re.sub(r',\{path:"/about",name:"About",icon:[a-zA-Z0-9_.]+\([a-zA-Z0-9_]+,\{strokeWidth:1\}\)\}', '', text)
text = re.sub(r'\{path:"/about",name:"About",icon:[a-zA-Z0-9_.]+\([a-zA-Z0-9_]+,\{strokeWidth:1\}\)\},', '', text)

text = re.sub(r',\{path:"/achievements",name:"Achievements",icon:[a-zA-Z0-9_.]+\([a-zA-Z0-9_]+,\{strokeWidth:1\}\)\}', '', text)
text = re.sub(r'\{path:"/achievements",name:"Achievements",icon:[a-zA-Z0-9_.]+\([a-zA-Z0-9_]+,\{strokeWidth:1\}\)\},', '', text)

text = re.sub(r',\{path:"/services",name:"Services",icon:[a-zA-Z0-9_.]+\([a-zA-Z0-9_]+,\{strokeWidth:1\}\)\}', '', text)
text = re.sub(r'\{path:"/services",name:"Services",icon:[a-zA-Z0-9_.]+\([a-zA-Z0-9_]+,\{strokeWidth:1\}\)\},', '', text)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Patching JS complete!")
