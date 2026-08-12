import os
import re

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Find product image references near the product page area
# Look for image src near the NextGen area
idx = 1385038  # around the product heading
context = js[idx-500:idx+2000]

# Find all image references in this area
img_matches = re.finditer(r'src:"([^"]*?)"', context)
for m in img_matches:
    print(f"Image src: {m.group(1)}")

# Also find any product-related images
product_imgs = re.finditer(r'(?:product|trike|vehicle)[^"]*?\.(png|jpg|jpeg|webp|svg)', js, re.IGNORECASE)
for m in product_imgs:
    start = max(0, m.start() - 80)
    end = min(len(js), m.end() + 20)
    print(f"\nProduct image context: {js[start:end]}")
