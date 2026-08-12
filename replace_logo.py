import os

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace any remaining visual "Navisights" strings
js = js.replace('BV 9', 'BV-9')
js = js.replace('Navisights', 'BV-9')
js = js.replace('NAVISIGHTS', 'BV-9')

# Replace logo.png with styled text if it's there
# Original: G.jsx("img",{src:"https://navisights.vercel.app/logo.png",className:"w-1/2 md:w-40",alt:"BV-9"})
# Let's replace the src of the logo with text
js = js.replace(
    'G.jsx("img",{src:"https://navisights.vercel.app/logo.png",className:"w-1/2 md:w-40",alt:"BV-9"})',
    'G.jsx("span",{className:"font-afacad-flux text-3xl md:text-4xl font-bold text-transparent bg-gradient-to-tr from-purple-800 to-red bg-clip-text",children:"BV-9"})'
)
js = js.replace(
    'G.jsx("img",{src:"https://navisights.vercel.app/logo.png",className:"w-44 mx-auto",alt:"BV-9"})',
    'G.jsx("span",{className:"font-afacad-flux text-4xl font-bold text-transparent bg-gradient-to-tr from-purple-800 to-red bg-clip-text mx-auto",children:"BV-9"})'
)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Text and logo replaced successfully!")
