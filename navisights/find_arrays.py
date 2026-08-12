import os
import re

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Find Dpe array (Vehicle Specification icons)
matches = list(re.finditer(r'Dpe\s*=\s*\[', js))
print(f"Found {len(matches)} Dpe definitions")
for m in matches:
    end = min(len(js), m.end() + 2000)
    print(f"\n--- Dpe at {m.start()} ---")
    print(js[m.start():end])
    print("---")

print("\n\n========================================\n")

# Find kpe array (Uses images)
matches2 = list(re.finditer(r'kpe\s*=\s*\[', js))
print(f"Found {len(matches2)} kpe definitions")
for m in matches2:
    end = min(len(js), m.end() + 3000)
    print(f"\n--- kpe at {m.start()} ---")
    print(js[m.start():end])
    print("---")
