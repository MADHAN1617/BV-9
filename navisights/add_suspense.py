import os

js_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights\assets\index-86024637.js"
with open(js_path, 'r', encoding='utf-8') as f:
    txt = f.read()

old_canvas_children = 'G.jsx(Hfe,{}),G.jsx(Vfe,{enableZoom:!0})'
new_canvas_children = 'G.jsx(J.Suspense,{fallback:null,children:G.jsx(Hfe,{})}),G.jsx(Vfe,{enableZoom:!0})'

if old_canvas_children in txt:
    txt = txt.replace(old_canvas_children, new_canvas_children)
    print("Wrapped Hfe inside React.Suspense successfully!")
else:
    print("Pattern not found, checking alternatives...")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(txt)
