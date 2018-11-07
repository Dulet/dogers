#!/usr/bin/env python 
from sys import argv
from dogecore import get_doge
if len(argv) == 5:
    texttop, textbot, fontsizetopstr, fontsizebotstr = argv[1:]
    get_doge(texttop, textbot, int(fontsizetopstr), int(fontsizebotstr))
if len(argv) == 4:
    texttop, textbot, fontsizestr = argv[1:]
    get_doge(texttop, textbot, int(fontsizestr), int(fontsizestr))
elif len(argv) == 3:
    texttop, textbot = argv[1:]
    get_doge(texttop, textbot, 48, 48)
