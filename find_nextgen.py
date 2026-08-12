import os
import re

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Find NextGen Strike and surrounding context
matches = list(re.finditer(r'NextGen Strike', js, re.IGNORECASE))
print(f"Found {len(matches)} matches for NextGen Strike")
for m in matches:
    start = max(0, m.start() - 150)
    end = min(len(js), m.end() + 150)
    print(f"\n--- Match at {m.start()} ---")
    print(js[start:end])
    print("---")

# Also find nextgen alone
matches2 = list(re.finditer(r'nextgen', js, re.IGNORECASE))
print(f"\nFound {len(matches2)} matches for nextgen")
for m in matches2:
    start = max(0, m.start() - 100)
    end = min(len(js), m.end() + 100)
    print(f"\n--- Match at {m.start()} ---")
    print(js[start:end])
    print("---")
