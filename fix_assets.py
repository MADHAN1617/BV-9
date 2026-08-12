import os

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")
css_path = os.path.join(dir_path, "assets", "index-19b034b7.css")

# 1. Update JS to fix 404s for 3D model and images
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Fix assets paths to point to the live server
js = js.replace('"/navisights-trike/', '"https://navisights.vercel.app/navisights-trike/')
js = js.replace('"/logo.png"', '"https://navisights.vercel.app/logo.png"')
js = js.replace('"/black-texture.png"', '"https://navisights.vercel.app/black-texture.png"')
js = js.replace('"/cubes.png"', '"https://navisights.vercel.app/cubes.png"')
js = js.replace('"/moto.png"', '"https://navisights.vercel.app/moto.png"')
js = js.replace('"/institutions/', '"https://navisights.vercel.app/institutions/')
js = js.replace('"/testimonials/', '"https://navisights.vercel.app/testimonials/')
js = js.replace('"/achievements/', '"https://navisights.vercel.app/achievements/')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Path patching complete!")
