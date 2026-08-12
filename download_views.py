import os
import urllib.request

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"

# Download all product view images
for i in range(1, 9):
    filename = f"view-{i}.jpg"
    url = f"https://navisights.vercel.app/{filename}"
    filepath = os.path.join(dir_path, filename)
    if not os.path.exists(filepath):
        print(f"Downloading {filename}...")
        try:
            urllib.request.urlretrieve(url, filepath)
            print(f"  Saved {filename}")
        except Exception as e:
            print(f"  Failed: {e}")
    else:
        print(f"Already exists: {filename}")

print("\nDone downloading product images!")
