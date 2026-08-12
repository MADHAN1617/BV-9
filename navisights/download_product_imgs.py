import os
import urllib.request

dir_path = r"C:\Users\Madhan\.gemini\antigravity\scratch\navisights"
base_url = "https://navisights.vercel.app"

spec_icons = [
    "control-system.png",
    "voice-recognition.png",
    "cloud-integration.png",
    "battery-charging.png"
]

uses_images = [
    "disabled-people.jpg",
    "ambulance.jpg",
    "self-driving-car.jpg",
    "plains-road.jpg"
]

# Also download black-grid-texture.png 
extra = ["black-grid-texture.png"]

all_files = spec_icons + uses_images + extra

for filename in all_files:
    filepath = os.path.join(dir_path, filename)
    url = f"{base_url}/{filename}"
    if not os.path.exists(filepath):
        print(f"Downloading {filename}...")
        try:
            urllib.request.urlretrieve(url, filepath)
            print(f"  Saved {filename}")
        except Exception as e:
            print(f"  Failed: {e}")
    else:
        print(f"Already exists: {filename}")

print("\nAll product images downloaded!")
