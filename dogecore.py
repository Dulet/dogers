from PIL import Image, ImageDraw, ImageFont
from random import choice
from os import listdir, makedirs
from os.path import exists
import time
image = Image.open("images/" + choice(listdir("images")))
image_width, image_height = image.size
draw = ImageDraw.Draw(image)
if not exists("results"):
    makedirs("results")

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
    text_width1, text_height1 = draw.textsize(texttop, fonttop)
    x1 = (image_width - text_width1) / 2
    y1 = text_height1 * 0.25

    text_width2, text_height2 = draw.textsize(textbot, fontbot)
    x2 = (image_width - text_width2) / 2
    y2 = image_height - text_height2 * 1.5

    draw_text_with_shadow(x1, y1, texttop, fonttop, shadow_color)
    draw_text_with_shadow(x2, y2, textbot, fontbot, shadow_color)

def get_doge(texttop, textbot, fontsize):
    fonttop, fontbot = get_fonts(fontsize, texttop, textbot)
    insert_text(fonttop, fontbot, texttop, textbot)
    image.show()
    image.save("results/" + str(int(time.time())) + ".jpg")
