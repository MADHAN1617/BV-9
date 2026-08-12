import os
import re

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Find all occurrences of navisights (case insensitive) to check what we are replacing
matches = re.finditer(r'(?<![/\.\-_a-zA-Z0-9])navisights(?![/\.\-_a-zA-Z0-9])', js, re.IGNORECASE)
print("Will replace the following occurrences:")
for m in matches:
    start = max(0, m.start() - 30)
    end = min(len(js), m.end() + 30)
    print(f"...{js[start:end]}...")

# Replace them
js_new = re.sub(r'(?<![/\.\-_a-zA-Z0-9])navisights(?![/\.\-_a-zA-Z0-9])', 'BV-9', js, flags=re.IGNORECASE)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_new)

print("Done replacing.")
