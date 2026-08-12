import os
import re

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the specific phrase
js_new = re.sub(r'think\s+mobility\s*,\s*think\s+BV-9', 'Think Mobility, Think Beyond Vision', js, flags=re.IGNORECASE)
js_new = re.sub(r'think\s+mobility\s+think\s+BV-9', 'Think Mobility Think Beyond Vision', js_new, flags=re.IGNORECASE)
js_new = re.sub(r'think\s+mobility\s*,\s*think\s+NaviSights', 'Think Mobility, Think Beyond Vision', js_new, flags=re.IGNORECASE)
js_new = re.sub(r'think\s+mobility\s+think\s+NaviSights', 'Think Mobility Think Beyond Vision', js_new, flags=re.IGNORECASE)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_new)

print("Tagline updated!")
