import os

js_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights\assets\index-86024637.js"
with open(js_path, 'r', encoding='utf-8') as f:
    txt = f.read()

eb_code = 'class Bv9ErrorBoundary extends J.Component{constructor(e){super(e);this.state={hasError:!1}}static getDerivedStateFromError(e){return{hasError:!0}}componentDidCatch(e){console.warn("3D Model Notice:",e)}render(){return this.state.hasError?null:this.props.children}};'

# Remove from bottom of file
txt = txt.replace(eb_code, '').replace('\n' + eb_code + '\n', '')

# Place right after var J=PU.exports;
target = 'var J=PU.exports;'
replacement = 'var J=PU.exports;' + eb_code

if target in txt:
    txt = txt.replace(target, replacement, 1)
    print("Bv9ErrorBoundary hoisted to top right after React initialization!")
else:
    print("Target var J=PU.exports; not found!")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(txt)
