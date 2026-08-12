import os, re

js_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights\assets\index-86024637.js"
with open(js_path, 'r', encoding='utf-8') as f:
    txt = f.read()

print("--- Root mount search ---")
for m in re.finditer(r'getElementById\s*\(\s*["\']root["\']\s*\)', txt):
    start = max(0, m.start() - 200)
    end = min(len(txt), m.end() + 200)
    print(txt[start:end])
    print("="*40)
