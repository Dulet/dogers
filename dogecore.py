from PIL import Image, ImageDraw, ImageFont
from random import choice
from os import listdir, makedirs
from os.path import exists, dirname, join
from textwrap import wrap
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
    # the following lines draw the black tint around the text
    draw.text((x - 1, y - 1), text, font=font, fill=shadow_color)
    draw.text((x + 1, y - 1), text, font=font, fill=shadow_color)
    draw.text((x - 1, y + 1), text, font=font, fill=shadow_color)
    draw.text((x + 1, y + 1), text, font=font, fill=shadow_color)
    # draw the desired text
    draw.text((x, y), text=text, font=font, fill=text_color)

def get_lines_and_offsets(lines, font):
    max_w = max([draw.textsize(l, font)[0] for l in lines])
    return [(line, (max_w - draw.textsize(line, font)[0]) // 2) for line in lines]

def draw_text(x, y, lines, font):
    for line, offset in get_lines_and_offsets(lines, font):
        draw_text_with_shadow(x + offset, y, line, font=font)
        y += int(draw.textsize(line, font)[1])

def max_width(font):
    """ used to define how many letters can fit before making a new line """
    mmm = "m"
    while draw.textsize(mmm, font)[0] < image_width:
        mmm += "m"
    return (len(mmm) - 1) * 1.5

def get_lines_and_dimensions(text, font):
    lines = wrap(text, width = max_width(font))
    if len([draw.textsize(line, font)[0] > 0 for line in lines]):
        text_width = max([draw.textsize(line, font)[0] for line in lines])
        text_height = draw.textsize(text, font)[1]
        return lines, text_width, text_height


def insert_text(fonttop, fontbot, texttop, textbot, fontsize, shadow_color = "black"):
    """ so this heap of code below is used to redefine all needed values independently, if someone decides
        to make a caption lacking either top or bottom text. it is NOT exactly positioned the same as the "default"
        image, but at least it works.... """
    if not get_lines_and_dimensions(texttop, fonttop) and get_lines_and_dimensions(textbot, fontbot):
        # when there's no top text
        font = ImageFont.truetype("impact.ttf", fontsize)
        text_width, text_height = draw.textsize(texttop, font)
        x = (image_width - text_width) / 2
        y = 0 + text_height * 0.25
        draw_text(x, y, " ", fonttop) # draw empty string

        botlines, text_width2, text_height2 = get_lines_and_dimensions(textbot, fontbot)
        x2 = (image_width - text_width2) / 2
        y2 = (image_height - len(botlines) * text_height2)*0.95

        draw_text(x2, y2, botlines, fontbot) # draw remainder of text

        return

    if not get_lines_and_dimensions(textbot, fontbot) and get_lines_and_dimensions(texttop, fonttop):
        # when there's no bot text
        font = ImageFont.truetype("impact.ttf", fontsize)
        text_width, text_height = draw.textsize(textbot, font)
        x1 = (image_width - text_width) / 2
        y1 = image_height - text_height * 1.5

        draw_text(x1, y1, " ", fonttop) # draw empty string

        toplines, text_width1, text_height1 = get_lines_and_dimensions(texttop, fonttop)
        x3 = (image_width - text_width1) / 2
        y3 = text_height1 * 0.25

        draw_text(x3, y3, toplines, fonttop) # draw the remainder of text

        return

    if not get_lines_and_dimensions(textbot, fontbot) and not get_lines_and_dimensions(texttop, fonttop):
        return

    toplines, text_width1, text_height1 = get_lines_and_dimensions(texttop, fonttop)
    x1 = (image_width - text_width1) / 2
    y1 = text_height1 * 0.25

    botlines, text_width2, text_height2 = get_lines_and_dimensions(textbot, fontbot)
    x2 = (image_width - text_width2) / 2
    y2 = image_height - y1 - len(botlines) * text_height2

    draw_text(x1, y1, toplines, fonttop)
    draw_text(x2, y2, botlines, fontbot)

def get_doge(texttop, textbot, fontsizetop, fontsizebot):
    fonttop = ImageFont.truetype("impact.ttf", fontsizetop)
    fontbot = ImageFont.truetype("impact.ttf", fontsizebot)
    insert_text(fonttop, fontbot, texttop, textbot, fontsizetop)
    image.show()
    image.save(join(results_path, str(int(time.time())) + ".jpg"))