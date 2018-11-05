from PIL import Image, ImageDraw, ImageFont
import random, time
dab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] #trivial but works
a = random.choice(dab)
path = "images/"

image = Image.open(path+str(a)+".jpg")
image_width = image.size[0]
image_height = image.size[1]
shadowcolor = "black"
texttop = input("Top text? \n").upper()
textbot = input("Bottom text? \n").upper()
size = int(input("Font size? (48 recommended) \n"))
if size > 64:
    size = 64
fonttop = ImageFont.truetype("impact.ttf", size)
fontbot = ImageFont.truetype("impact.ttf", size)

while ImageDraw.Draw(image).textsize(texttop, fonttop)[0] >= image_width:
    size -= 10
    fonttop = ImageFont.truetype("impact.ttf", size)
while ImageDraw.Draw(image).textsize(textbot, fontbot)[0] >= image_width:
    size -= 10
    fontbot = ImageFont.truetype("impact.ttf", size)

def bottom_text(img, fonttop, fontbot, texttop, textbot, shadowcolor):
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(texttop, fonttop)
    x = (image_width-text_width)/2
    y = 0 + text_height*0.25
    draw.text((x - 1, y - 1), texttop, font=fonttop, fill=shadowcolor)
    draw.text((x + 1, y - 1), texttop, font=fonttop, fill=shadowcolor)
    draw.text((x - 1, y + 1), texttop, font=fonttop, fill=shadowcolor)
    draw.text((x + 1, y + 1), texttop, font=fonttop, fill=shadowcolor)
    draw.text((x, y), text=texttop, fill="white", font=fonttop)

    text_width, text_height = draw.textsize(textbot, fontbot)
    x1 = (image_width - text_width) / 2
    y1 = image_height - text_height*1.5
    draw.text((x1 - 1, y1 - 1), textbot, font=fontbot, fill=shadowcolor)
    draw.text((x1 + 1, y1 - 1), textbot, font=fontbot, fill=shadowcolor)
    draw.text((x1 - 1, y1 + 1), textbot, font=fontbot, fill=shadowcolor)
    draw.text((x1 + 1, y1 + 1), textbot, font=fontbot, fill=shadowcolor)
    draw.text((x1, y1), text=textbot, fill="white", font=fontbot)
    return img


bottom_text(image, fonttop, fontbot, texttop, textbot, shadowcolor)
image.show()
image.save("images/results/" + str(int(time.time())) + ".jpg")
