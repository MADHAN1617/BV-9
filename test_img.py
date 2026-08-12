from PIL import Image

img = Image.open('moto_orig.png')
pixels = img.load()
width, height = img.size

# Find the bounding box of the rocket (ignoring the text at the bottom)
# The text is probably below Y=800. Let's find the first non-black pixel from the bottom.
bottom_y = 0
for y in range(height-1, -1, -1):
    for x in range(width):
        r, g, b = pixels[x, y][:3]
        if r > 10 or g > 10 or b > 10:
            # print(f"Non-black pixel at Y={y}")
            pass

# Actually let's just blank out from Y=950 downwards and see if it looks clean.
# I'll just write a script to do the drawing and see if the user likes it.
