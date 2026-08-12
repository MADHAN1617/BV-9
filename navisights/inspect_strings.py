import os
import re

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")
html_path = os.path.join(dir_path, "index.html")

# Update HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

html_content = html_content.replace('Navisights', 'BV 9')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# Update JS
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Replace Navisights
js_content = js_content.replace('Navisights', 'BV 9')
js_content = js_content.replace('navisights', 'bv 9')

def extract_context(text, keyword, padding=100):
    matches = [m.start() for m in re.finditer(re.escape(keyword), text, re.IGNORECASE)]
    results = []
    for m in matches:
        start = max(0, m - padding)
        end = min(len(text), m + len(keyword) + padding)
        results.append(text[start:end])
    return results

print("Achievements Contexts:")
for c in extract_context(js_content, 'Achievements', 50):
    print("---", c)

print("\nServices Contexts:")
for c in extract_context(js_content, 'Services', 50):
    print("---", c)
    
print("\nContact Contexts (LinkedIn/Email/Phone):")
for c in extract_context(js_content, 'linkedin.com', 50):
    print("---", c)
for c in extract_context(js_content, '@gmail.com', 50):
    print("---", c)
for c in extract_context(js_content, 'mail', 50):
    print("---", c)
for c in extract_context(js_content, '+91', 50):
    print("---", c)
