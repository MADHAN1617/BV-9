import subprocess, time, json, urllib.request

# Check if we can run Chrome / Edge in headless mode to capture console logs
chrome_cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--remote-debugging-port=9222",
    "http://localhost:8080"
]

# If Chrome is not found, try Edge or Brave
edge_paths = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe"
]

browser_exe = None
for p in edge_paths:
    if os.path.exists(p):
        browser_exe = p
        break

print("Browser found:", browser_exe)

if browser_exe:
    proc = subprocess.Popen([browser_exe, "--headless=new", "--remote-debugging-port=9222", "http://localhost:8080"])
    time.sleep(3)
    try:
        # Get target websocket URL
        tabs = json.loads(urllib.request.urlopen("http://localhost:9222/json").read())
        print("Tabs available:", len(tabs))
        print("Tab info:", tabs)
    except Exception as e:
        print("CDP Connect error:", e)
    finally:
        proc.kill()
