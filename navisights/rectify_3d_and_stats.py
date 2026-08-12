import os

js_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights\assets\index-86024637.js"
with open(js_path, 'r', encoding='utf-8') as f:
    txt = f.read()

# 1. Rectify 3D model path and position
old_hfe = 'wS("https://navisights.vercel.app/navisights-trike/navisights_trike_assy_file.gltf")'
new_hfe = 'wS("/navisights-trike/navisights_trike_assy_file.gltf")'

txt = txt.replace(old_hfe, new_hfe)
txt = txt.replace('position:[-80,-30,10]', 'position:[0,-10,0]')

# 2. Fix stats number gradient class so text is visible (from-purple-800 to-red -> from-purple-500 to-pink-500)
txt = txt.replace('from-purple-800 to-red', 'from-purple-500 to-pink-500')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(txt)

print("3D Model path/position and Stats counter visibility rectified!")
