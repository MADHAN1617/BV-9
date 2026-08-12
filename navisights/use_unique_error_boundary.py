import os

js_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights\assets\index-86024637.js"
with open(js_path, 'r', encoding='utf-8') as f:
    txt = f.read()

# Remove any old Mfe class definitions added
bad_class1 = 'class Mfe extends J.Component{constructor(e){super(e);this.state={hasError:!1}}static getDerivedStateFromError(e){return{hasError:!0}}componentDidCatch(e){console.warn("3D Model Notice:",e)}render(){return this.state.hasError?null:this.props.children}};\n'
bad_class2 = 'class Mfe extends J.Component{constructor(e){super(e);this.state={hasError:!1}}static getDerivedStateFromError(e){return{hasError:!0}}componentDidCatch(e){console.warn("3D Model Notice:",e)}render(){return this.state.hasError?null:this.props.children}};'

txt = txt.replace(bad_class1, '').replace(bad_class2, '')

# Replace Mfe with Bv9ErrorBoundary in JSX
txt = txt.replace('G.jsx(Mfe,{children:', 'G.jsx(Bv9ErrorBoundary,{children:')

# Append Bv9ErrorBoundary class definition
eb_code = '\nclass Bv9ErrorBoundary extends J.Component{constructor(e){super(e);this.state={hasError:!1}}static getDerivedStateFromError(e){return{hasError:!0}}componentDidCatch(e){console.warn("3D Model Notice:",e)}render(){return this.state.hasError?null:this.props.children}};\n'
txt = txt + eb_code

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(txt)

print("Updated with Bv9ErrorBoundary successfully!")
