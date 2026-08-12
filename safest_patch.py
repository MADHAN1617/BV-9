import os

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")
html_path = os.path.join(dir_path, "index.html")

# Update HTML safely
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

html_content = html_content.replace('<title>Navisights</title>', '<title>BV 9</title>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# Update JS safely
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Contact info
js = js.replace('madhansekar537@gmail\.com', 'madhansekar537@gmail.com')
js = js.replace('\+917530075710', '+917530075710')
js = js.replace('https://www.linkedin.com/in/madhan-sekar-b61870333/', 'https://www.linkedin.com/in/madhan-sekar-b61870333')

# Visible names only
js = js.replace('About Navisights', 'About BV 9')
js = js.replace('Team Navisights', 'Team BV 9')
js = js.replace('S&S Navisights', 'S&S BV 9')
js = js.replace('alt:"Navisights"', 'alt:"BV 9"')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Safest patch applied!")

