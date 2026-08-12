import os, re

js_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights\assets\index-86024637.js"
with open(js_path, 'r', encoding='utf-8') as f:
    txt = f.read()

print("--- URLs ---")
urls = set(re.findall(r'https?://[^\s"\'\)\}\>]+', txt))
for u in sorted(urls):
    print(u)

print("\n--- FIREBASE / CONFIG SEARCH ---")
for m in re.finditer(r'BV-9', txt):
    start = max(0, m.start() - 30)
    end = min(len(txt), m.end() + 30)
    print(txt[start:end])
