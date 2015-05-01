from os import getcwd
from random import random

def cipher(char, change = 1, sign = "+", add_char = "<>\n\t"):
    pos = "Kjcf4IOdetx8STr3DN16Lay 2FGPZ07Wh9QEYbBiVlsuAUXCgmqopvk5wzRJHnM" + add_char
    if char in pos:
        exec "num = pos.find(char) %s %i" % (sign, int(change))
        while num >= len(pos) or num < 0:
            if num >= len(pos):
                num -= len(pos)
            elif num < 0:
                num += len(pos)
        char = pos[num]
    elif char == "\n": char = "\t"
    elif char == "\t": char = "\n"
    return char

def savegame(name, info, tocipher = True, loc = getcwd(), ext = ".txt"):
    if "." not in name:
        name += ext
    if tocipher:
        info1, info2 = "", ""
        for char in info:
            num = int(random() * 10)
            info1 += "%i" %(num)
            info2 += cipher(char, change = num)
        info = info1 + "EORN" + info2
    save = open("%s\\%s" % (loc, name), "w")
    save.write(info)
    save.close()

def loadgame(name, tocipher = True, loc = getcwd(), ext = ".txt"):
    if "." not in name:
        name += ext
    load = open("%s\\%s" % (loc, name), "r")
    info = load.read()
    if tocipher:
        old_info = info[info.find("EORN") + 4:]
        changes = info[:info.find("EORN")]
        info = ""
        for loc in range(len(old_info)):
            info += cipher(old_info[loc], sign = "-", change = changes[loc])
    return info