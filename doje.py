from dogecore import get_doge

texttop = input("Top text? \n").upper()
textbot = input("Bottom text? \n").upper()
fontsize = int(input("Font size? (48 recommended) \n"))
if fontsize > 64:
    fontsize = 64

get_doge(texttop, textbot, fontsize, fontsize)