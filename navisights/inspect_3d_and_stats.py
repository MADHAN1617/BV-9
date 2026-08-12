import os, re

js_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights\assets\index-86024637.js"
with open(js_path, 'r', encoding='utf-8') as f:
    txt = f.read()

print("--- 3D MODEL MATCHES ---")
for m in re.finditer(r'gltf', txt, re.IGNORECASE):
    start = max(0, m.start() - 100)
    end = min(len(txt), m.end() + 100)
    print("Match:", txt[start:end])
    print("="*40)

print("\n--- KM/HR STATS MATCHES ---")
for m in re.finditer(r'Maximum Speed', txt, re.IGNORECASE):
    start = max(0, m.start() - 150)
    end = min(len(txt), m.end() + 150)
    print("Match:", txt[start:end])
    print("="*40)
