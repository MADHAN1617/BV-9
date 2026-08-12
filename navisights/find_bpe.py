import os
import re

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Find Bpe array definition
matches = list(re.finditer(r'Bpe\s*=\s*\[', js))
print(f"Found {len(matches)} Bpe definitions")
for m in matches:
    end = min(len(js), m.end() + 500)
    print(f"\n--- Bpe at {m.start()} ---")
    print(js[m.start():end])
    print("---")
