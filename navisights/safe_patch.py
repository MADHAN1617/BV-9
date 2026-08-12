import os

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")
css_path = os.path.join(dir_path, "assets", "index-19b034b7.css")
html_path = os.path.join(dir_path, "index.html")

# 1. Update JS
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Safe string replacements
js_content = js_content.replace('navisights2023@gmail.com', 'madhansekar537@gmail.com')
js_content = js_content.replace('+919080168075', '+917530075710')
js_content = js_content.replace('https://www.linkedin.com/in/sivanesh-k-s-6a9991218/', 'https://www.linkedin.com/in/madhan-sekar-b61870333')
js_content = js_content.replace('Navisights', 'BV 9')
js_content = js_content.replace('NAVISIGHTS', 'BV 9')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

# 2. Update HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

html_content = html_content.replace('Navisights', 'BV 9')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# 3. Update CSS to hide the unwanted sections and links
css_append = """
a[href="/about"], a[href="/achievements"], a[href="/services"] {
    display: none !important;
}
"""
with open(css_path, 'a', encoding='utf-8') as f:
    f.write(css_append)

print("Safe patching complete!")
