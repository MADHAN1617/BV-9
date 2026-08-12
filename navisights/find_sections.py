import os
import re

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Find Vehicle Specification section
matches = list(re.finditer(r'Vehicle Specification', js, re.IGNORECASE))
print(f"Found {len(matches)} matches for Vehicle Specification")
for m in matches:
    start = max(0, m.start() - 300)
    end = min(len(js), m.end() + 1500)
    print(f"\n--- Match at {m.start()} ---")
    print(js[start:end])
    print("---")

print("\n\n========================================\n")

# Find Uses of the Beyond Vision section
matches2 = list(re.finditer(r'Uses of the', js, re.IGNORECASE))
print(f"Found {len(matches2)} matches for 'Uses of the'")
for m in matches2:
    start = max(0, m.start() - 300)
    end = min(len(js), m.end() + 1500)
    print(f"\n--- Match at {m.start()} ---")
    print(js[start:end])
    print("---")
