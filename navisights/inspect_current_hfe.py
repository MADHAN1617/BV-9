import os, re

js_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights\assets\index-86024637.js"
with open(js_path, 'r', encoding='utf-8') as f:
    txt = f.read()

m = re.search(r'Hfe\s*=\s*', txt)
if m:
    start = max(0, m.start() - 100)
    end = min(len(txt), m.end() + 400)
    print("--- Current Hfe & Gfe ---")
    print(txt[start:end])
