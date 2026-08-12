import os, re

js_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights\assets\index-86024637.js"
with open(js_path, 'r', encoding='utf-8') as f:
    txt = f.read()

m = re.search(r'Gfe\s*=\s*', txt)
if m:
    start = max(0, m.start() - 100)
    end = min(len(txt), m.end() + 600)
    print("--- Gfe Component JSX ---")
    print(txt[start:end])

print("\n--- Suspense usage search ---")
for m in re.finditer(r'Suspense', txt, re.IGNORECASE):
    start = max(0, m.start() - 50)
    end = min(len(txt), m.end() + 50)
    print(txt[start:end])
