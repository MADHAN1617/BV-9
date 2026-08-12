import os

js_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights\assets\index-86024637.js"
with open(js_path, 'r', encoding='utf-8') as f:
    txt = f.read()

# Fix Firebase settings
txt = txt.replace('BV-9-51596.firebaseapp.com', 'navisights-51596.firebaseapp.com')
txt = txt.replace('BV-9-51596', 'navisights-51596')

# Fix asset URLs
txt = txt.replace('https://BV-9.vercel.app', 'https://navisights.vercel.app')
txt = txt.replace('https://bv-9.vercel.app', 'https://navisights.vercel.app')

# Fix 3D GLTF model path inside URL
txt = txt.replace('/BV-9-trike/BV-9_trike_assy_file.gltf', '/navisights-trike/navisights_trike_assy_file.gltf')

# Fix social / external links that broke due to case-insensitive replace
txt = txt.replace('https://www.instagram.com/BV-9/', 'https://www.instagram.com/navisights/')
txt = txt.replace('NexGenTrike-BV-9o4vcFhb', 'NexGenTrike-NaviSightso4vcFhb')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(txt)

print("White screen fixes applied successfully.")
