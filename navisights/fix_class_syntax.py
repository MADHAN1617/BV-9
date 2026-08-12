import os

js_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights\assets\index-86024637.js"
with open(js_path, 'r', encoding='utf-8') as f:
    txt = f.read()

# Remove improperly placed class Mfe
bad_class = 'class Mfe extends J.Component{constructor(e){super(e);this.state={hasError:!1}}static getDerivedStateFromError(e){return{hasError:!0}}componentDidCatch(e){console.warn("3D Model Notice:",e)}render(){return this.state.hasError?null:this.props.children}};'
txt = txt.replace(bad_class, '')

# Append class Mfe at the end of the file safely
class_def = '\nclass Mfe extends J.Component{constructor(e){super(e);this.state={hasError:!1}}static getDerivedStateFromError(e){return{hasError:!0}}componentDidCatch(e){console.warn("3D Model Notice:",e)}render(){return this.state.hasError?null:this.props.children}};\n'
txt = txt + class_def

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(txt)

print("Class syntax placement fixed!")
