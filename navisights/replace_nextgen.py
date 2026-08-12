import os

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
js_path = os.path.join(dir_path, "assets", "index-86024637.js")

with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace all "NextGen Trike" with "Beyond Vision"
js = js.replace('NextGen Trike', 'Beyond Vision')

# Also replace "Team Navi" if present
js = js.replace('Team Navi', 'Team BV-9')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Replaced NextGen Trike -> Beyond Vision")
print("Replaced Team Navi -> Team BV-9")
