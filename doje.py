from PIL import Image, ImageDraw, ImageFont
import time
from random import choice
from os import listdir
image = Image.open("images/" + choice(listdir("images")))
image_width, image_height = image.size
draw = ImageDraw.Draw(image)

def get_fonts(fontsize, texttop, textbot, fonttop_name = "impact.ttf", fontbot_name = "impact.ttf"):
    fonttop = ImageFont.truetype(fonttop_name, fontsize)
    fontbot = ImageFont.truetype(fontbot_name, fontsize)
    while draw.textsize(texttop, fonttop)[0] >= image_width:
        fontsize -= 5
        fonttop = ImageFont.truetype(fonttop_name, fontsize)
    while draw.textsize(textbot, fontbot)[0] >= image_width:
        fontsize -= 5
        fontbot = ImageFont.truetype(fontbot_name, fontsize)
    return fonttop, fontbot

def draw_text_with_shadow(x, y, text, font, shadow_color = "black", text_color = "white"):
    draw.text((x - 1, y - 1), text, font=font, fill=shadow_color)
    draw.text((x + 1, y - 1), text, font=font, fill=shadow_color)
    draw.text((x - 1, y + 1), text, font=font, fill=shadow_color)
    draw.text((x + 1, y + 1), text, font=font, fill=shadow_color)
    draw.text((x, y), text=text, font=font, fill=text_color)

def insert_text(fonttop, fontbot, texttop, textbot, shadow_color = "black"):
    text_width, text_height = draw.textsize(texttop, fonttop)
    x1 = (image_width-text_width)/2
    y1 = 0 + text_height*0.25
    draw_text_with_shadow(x1, y1, texttop, fonttop, shadow_color)

    text_width, text_height = draw.textsize(textbot, fontbot)
    x2 = (image_width - text_width) / 2
    y2 = image_height - text_height * 1.5
    draw_text_with_shadow(x2, y2, textbot, fontbot, shadow_color)

texttop = input("Top text? \n").upper()
textbot = input("Bottom text? \n").upper()
fontsize = int(input("Font size? (48 recommended) \n"))
if fontsize > 64:
    fontsize = 64
fonttop, fontbot = get_fonts(fontsize, texttop, textbot)
insert_text(fonttop, fontbot, texttop, textbot)
image.show()
image.save("images/results/" + str(int(time.time())) + ".jpg")
