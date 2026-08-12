import os, re

js_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights\assets\index-86024637.js"
with open(js_path, 'r', encoding='utf-8') as f:
    txt = f.read()

m = re.search(r'Hfe\s*=\s*', txt)
if m:
    start = max(0, m.start() - 200)
    end = min(len(txt), m.end() + 500)
    print("--- Hfe definition ---")
    print(txt[start:end])

m2 = re.search(r'G\.jsx\(Hfe,\{\}\)', txt)
if m2:
    start = max(0, m2.start() - 400)
    end = min(len(txt), m2.end() + 400)
    print("\n--- Hfe Usage ---")
    print(txt[start:end])
