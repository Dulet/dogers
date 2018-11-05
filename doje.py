from PIL import Image, ImageDraw, ImageFont
from random import choice
from os import listdir
path = "images/" + choice(listdir("images"))

image = Image.open(path)
image_width = image.size[0]
image_height = image.size[1]
shadowcolor = "black"
texttop = input("Top text? \n").upper()
textbot = input("Bottom text? \n").upper()
size = int(input("Font size? (48 recommended) \n"))
if size > 64:
    size = 64
font = ImageFont.truetype("impact.ttf", size)

def bottom_text(img, font, texttop, textbot, shadowcolor):
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(texttop, font)
    x = (image_width-text_width)/2
    y = 0 + text_height*0.25
    draw.text((x - 1, y - 1), texttop, font=font, fill=shadowcolor)
    draw.text((x + 1, y - 1), texttop, font=font, fill=shadowcolor)
    draw.text((x - 1, y + 1), texttop, font=font, fill=shadowcolor)
    draw.text((x + 1, y + 1), texttop, font=font, fill=shadowcolor)
    draw.text((x, y), text=texttop, fill="white", font=font)

    text_width, text_height = draw.textsize(textbot, font)
    x1 = (image_width - text_width) / 2
    y1 = image_height - text_height*1.5
    draw.text((x1 - 1, y1 - 1), textbot, font=font, fill=shadowcolor)
    draw.text((x1 + 1, y1 - 1), textbot, font=font, fill=shadowcolor)
    draw.text((x1 - 1, y1 + 1), textbot, font=font, fill=shadowcolor)
    draw.text((x1 + 1, y1 + 1), textbot, font=font, fill=shadowcolor)
    draw.text((x1, y1), text=textbot, fill="white", font=font)
    return img


bottom_text(image, font, texttop, textbot, shadowcolor)
image.show()
