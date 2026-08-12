import os

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Make it much bigger, add letter spacing (tracking-widest), and a nice drop shadow/glow
new_class_1 = 'font-afacad-flux text-5xl md:text-7xl font-extrabold tracking-widest text-transparent bg-gradient-to-r from-purple-600 via-pink-500 to-red-500 bg-clip-text drop-shadow-[0_0_10px_rgba(236,72,153,0.8)]'
new_class_2 = 'font-afacad-flux text-6xl md:text-8xl font-extrabold tracking-widest text-transparent bg-gradient-to-r from-purple-600 via-pink-500 to-red-500 bg-clip-text drop-shadow-[0_0_15px_rgba(236,72,153,0.8)] mx-auto'

# Replace the previous text replacement
js = js.replace(
    'className:"font-afacad-flux text-3xl md:text-4xl font-bold text-transparent bg-gradient-to-tr from-purple-800 to-red bg-clip-text"',
    f'className:"{new_class_1}"'
)
js = js.replace(
    'className:"font-afacad-flux text-4xl font-bold text-transparent bg-gradient-to-tr from-purple-800 to-red bg-clip-text mx-auto"',
    f'className:"{new_class_2}"'
)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Logo styles updated successfully!")
