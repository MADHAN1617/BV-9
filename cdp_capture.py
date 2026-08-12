import subprocess, time, json, urllib.request, os

chrome_cmd = [
    r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
    "--headless=new",
    "--remote-debugging-port=9222",
    "http://localhost:8080"
]

proc = subprocess.Popen(chrome_cmd)
time.sleep(2)
try:
    tabs = json.loads(urllib.request.urlopen("http://localhost:9222/json").read())
    print("CDP Connected successfully! Tabs:", len(tabs))
    for t in tabs:
        print("Tab:", t.get('url'), t.get('title'))
except Exception as e:
    print("Error connecting to CDP:", e)
finally:
    proc.kill()
