import os

js_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights\assets\index-86024637.js"
with open(js_path, 'r', encoding='utf-8') as f:
    txt = f.read()

# Define ModelErrorBoundary class component in minified React format
error_boundary_code = 'class Mfe extends J.Component{constructor(e){super(e);this.state={hasError:!1}}static getDerivedStateFromError(e){return{hasError:!0}}componentDidCatch(e){console.warn("3D Model Notice:",e)}render(){return this.state.hasError?null:this.props.children}};'

# Target Hfe and Gfe
old_hfe = 'Hfe=()=>{const{scene:n}=wS("/navisights-trike/navisights_trike_assy_file.gltf");return G.jsx("primitive",{rotation:[0,1.3,0],object:n,scale:30,position:[0,-10,0]})}'
new_hfe = error_boundary_code + 'Hfe=()=>{const{scene:n}=wS("https://navisights.vercel.app/navisights-trike/navisights_trike_assy_file.gltf");return G.jsx("primitive",{rotation:[0,1.3,0],object:n,scale:30,position:[0,-10,0]})}'

old_gfe = 'G.jsx(J.Suspense,{fallback:null,children:G.jsx(Hfe,{})})'
new_gfe = 'G.jsx(Mfe,{children:G.jsx(J.Suspense,{fallback:null,children:G.jsx(Hfe,{})})})'

if old_hfe in txt:
    txt = txt.replace(old_hfe, new_hfe)
    print("Updated Hfe gltf URL & added ModelErrorBoundary class!")

if old_gfe in txt:
    txt = txt.replace(old_gfe, new_gfe)
    print("Wrapped 3D Model in ErrorBoundary + Suspense!")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(txt)
