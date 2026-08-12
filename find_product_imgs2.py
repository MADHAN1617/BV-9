import os
import re

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Wider search around product page heading
idx = 1385038
context = js[idx-1000:idx+3000]

# Find ALL src references
img_matches = re.finditer(r'src[=:]"([^"]*?)"', context)
for m in img_matches:
    print(f"src: {m.group(1)}")

print("\n\n--- Full product page section ---")
print(context[:2000])
