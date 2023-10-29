import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
files = os.listdir("photo")
for photo in files:
    with Image.open("photo/"+photo) as image:

        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("Comfortaa-VariableFont_wght.ttf", 30)

        draw.text((10,10), "Some text", font=font, fill="white")

        image.save("result/"+photo)