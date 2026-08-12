import os
import re

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")

with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

def find_surrounding(keyword):
    matches = [m.start() for m in re.finditer(re.escape(keyword), js_content, re.IGNORECASE)]
    for m in matches:
        start = max(0, m - 100)
        end = min(len(js_content), m + 100)
        print(f"--- {keyword} Context ---")
        print(js_content[start:end])
        print("-----------------------")

find_surrounding("Achievements")
find_surrounding("About")
find_surrounding("Services")
find_surrounding("navisights")
find_surrounding("9080168075")
find_surrounding("Instagram")
find_surrounding("linkedin")
