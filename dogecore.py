from PIL import Image, ImageDraw, ImageFont
from random import choice
from os import listdir, makedirs
from os.path import exists, dirname, join
from  textwrap import wrap
import time
cwd_path = dirname(__file__)
images_path = join(cwd_path, "images")
results_path = join(cwd_path, "results")
image = Image.open(join(images_path, choice(listdir(images_path))))
image_width, image_height = image.size
draw = ImageDraw.Draw(image)
if not exists(results_path):
    makedirs(results_path)

def draw_text_with_shadow(x, y, text, font, shadow_color = "black", text_color = "white"):
    draw.text((x - 1, y - 1), text, font=font, fill=shadow_color)
    draw.text((x + 1, y - 1), text, font=font, fill=shadow_color)
    draw.text((x - 1, y + 1), text, font=font, fill=shadow_color)
    draw.text((x + 1, y + 1), text, font=font, fill=shadow_color)
    draw.text((x, y), text=text, font=font, fill=text_color)

def get_lines_and_offsets(lines, font):
    max_w = max([draw.textsize(l, font)[0] for l in lines])
    return [(line, (max_w - draw.textsize(line, font)[0]) // 2) for line in lines]

def draw_text(x, y, lines, font):
    for line, offset in get_lines_and_offsets(lines, font):
        draw_text_with_shadow(x + offset, y, line, font=font)
        y += int(draw.textsize(line, font)[1])

def max_width(font):
    mmm = "m"
    while draw.textsize(mmm, font)[0] < image_width:
        mmm += "m"
    return (len(mmm) - 1) * 1.5

def get_lines_and_dimensions(text, font):
    lines = wrap(text, width = max_width(font))
    text_width = max([draw.textsize(line, font)[0] for line in lines])
    text_height = draw.textsize(text, font)[1]
    return lines, text_width, text_height

def insert_text(fonttop, fontbot, texttop, textbot, shadow_color = "black"):
    toplines, text_width1, text_height1 = get_lines_and_dimensions(texttop, fonttop)
    x1 = (image_width - text_width1) / 2
    y1 = text_height1 * 0.25

    botlines, text_width2, text_height2 = get_lines_and_dimensions(textbot, fontbot)
    x2 = (image_width - text_width2) / 2
    y2 = image_height - y1 - len(botlines) * text_height2

    draw_text(x1, y1, toplines, fonttop)
    draw_text(x2, y2, botlines, fontbot)

def get_doge(texttop, textbot, fontsize):
    fonttop = ImageFont.truetype("impact.ttf", fontsize)
    fontbot = ImageFont.truetype("impact.ttf", fontsize)
    insert_text(fonttop, fontbot, texttop, textbot)
    image.show()
    image.save(join(results_path, str(int(time.time())) + ".jpg"))