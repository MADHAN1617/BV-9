import os, re

js_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights\assets\index-86024637.js"
with open(js_path, 'r', encoding='utf-8') as f:
    txt = f.read()

print("Original size:", len(txt))

# 1. Remove ALL Bv9ErrorBoundary class definitions anywhere in file
eb_pattern = r'class Bv9ErrorBoundary extends J\.Component\{constructor\(e\)\{super\(e\);this\.state=\{hasError:!1\}\}static getDerivedStateFromError\(e\)\{return\{hasError:!0\}\}componentDidCatch\(e\)\{console\.warn\("3D Model Notice:",e\)\}render\(\)\{return this\.state\.hasError\?null:this\.props\.children\}\};'
txt = re.sub(eb_pattern, '', txt)

# 2. Remove Bv9ErrorBoundary wrapper around Suspense
txt = txt.replace(
    'G.jsx(Bv9ErrorBoundary,{children:G.jsx(J.Suspense,{fallback:null,children:G.jsx(Hfe,{})})})',
    'null'
)
# Also handle other possible wrapping patterns
txt = txt.replace(
    'G.jsx(J.Suspense,{fallback:null,children:G.jsx(Hfe,{})})',
    'null'
)
# And the original bare pattern
txt = txt.replace('G.jsx(Hfe,{})', 'null')

print("After removing ErrorBoundary/Suspense/3D size:", len(txt))

# 3. Also completely neutralize Hfe so it just returns null no matter what
old_hfe = 'Hfe=()=>{const{scene:n}=wS("https://navisights.vercel.app/navisights-trike/navisights_trike_assy_file.gltf");return G.jsx("primitive",{rotation:[0,1.3,0],object:n,scale:30,position:[0,-10,0]})}'
new_hfe = 'Hfe=()=>null'
if old_hfe in txt:
    txt = txt.replace(old_hfe, new_hfe)
    print("Hfe neutralized to return null!")
else:
    # Try to find it with regex
    m = re.search(r'Hfe=\(\)=>\{const\{scene:n\}=wS\([^\)]+\);return G\.jsx[^}]+\}\}', txt)
    if m:
        txt = txt[:m.start()] + 'Hfe=()=>null' + txt[m.end():]
        print("Hfe neutralized via regex!")
    else:
        print("WARNING: Hfe pattern not found - searching for any wS call...")
        for m in re.finditer(r'Hfe=', txt):
            print("  Found Hfe= at", m.start(), ":", txt[m.start():m.start()+200])

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(txt)

print("Done! Final size:", len(txt))
