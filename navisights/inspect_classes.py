import os, re

js_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights\assets\index-86024637.js"
with open(js_path, 'r', encoding='utf-8') as f:
    txt = f.read()

print("--- Class search ---")
for m in re.finditer(r'class\s+\w+', txt):
    start = max(0, m.start() - 30)
    end = min(len(txt), m.end() + 100)
    print(txt[start:end])
