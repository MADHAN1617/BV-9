import os

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Revert the moto.png path back to local so it serves the updated image
js = js.replace('"https://navisights.vercel.app/moto.png"', '"/moto.png"')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated moto.png path!")
