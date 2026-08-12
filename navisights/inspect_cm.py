import os, re

js_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights\assets\index-86024637.js"
with open(js_path, 'r', encoding='utf-8') as f:
    txt = f.read()

m = re.search(r'CM\s*=\s*', txt)
if m:
    start = max(0, m.start() - 50)
    end = min(len(txt), m.end() + 600)
    print(txt[start:end])
else:
    print("CM definition not found directly with CM = ")
    # Let's search targetNumber
    m2 = re.search(r'targetNumber', txt)
    if m2:
        start = max(0, m2.start() - 300)
        end = min(len(txt), m2.end() + 300)
        print(txt[start:end])
