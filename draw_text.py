from PIL import Image, ImageDraw, ImageFont
import os

img = Image.open('moto_orig.png').convert("RGBA")
draw = ImageDraw.Draw(img)
width, height = img.size

# Erase the bottom half of the image where the text is.
# The text seems to start around Y=850. Let's blank from 850 to the bottom.
draw.rectangle([(0, 850), (width, height)], fill=(0, 0, 0, 255))

# Try to find a bold font in Windows
try:
    font = ImageFont.truetype("arialbd.ttf", 150)
except:
    font = ImageFont.load_default()

# We need to draw:
# Line 1: "Think " (white) "Mobility" (yellow)
# Line 2: "Think " (red) "Beyond Vision" (white)

def draw_text_centered(draw, text_parts, y_pos, font, total_width):
    # Calculate total text width
    total_text_width = 0
    for text, color in text_parts:
        left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
        total_text_width += (right - left)
    
    # Calculate starting x
    current_x = (total_width - total_text_width) // 2
    
    # Draw parts
    for text, color in text_parts:
        draw.text((current_x, y_pos), text, font=font, fill=color)
        left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
        current_x += (right - left)

line1 = [("Think ", (255, 255, 255, 255)), ("Mobility", (255, 223, 0, 255))]
line2 = [("Think ", (255, 50, 50, 255)), ("Beyond Vision", (255, 255, 255, 255))]

draw_text_centered(draw, line1, 950, font, width)
draw_text_centered(draw, line2, 1150, font, width)

img.save('moto.png')
print("Saved moto.png successfully!")
