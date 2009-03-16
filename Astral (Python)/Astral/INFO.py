from SaveLoad import *
build = loadgame("Buildings", tocipher = False, ext = ".py")
resear = loadgame("Research", tocipher = False, ext = ".py")

resear = resear.split("\n\n")
build = build.split("\n\n")

if len(build[0]) >= 28 and build[0][:28] == "#----------SAMPLE----------#":
    build.remove(build[0])
if len(resear[0]) >= 28 and resear[0][:28] == "#----------SAMPLE----------#":
    resear.remove(resear[0])

BUILDING = {}
for item in build:
    item = item.split("\n")
    temp = {}
    for val in range(1, len(item)):
        exec "temp%s" % (item[val])
    temp["NAME"] = item[0].strip('"').strip("'")
    temp["OPT-DONE"] = []
    BUILDING[item[0].strip('"').strip("'")] = temp.copy()
    
RESEARCH = {}
for item in resear:
    item = item.split("\n")
    temp = {}
    for val in range(1, len(item)):
        exec "temp%s" % (item[val])
    temp["NAME"] = item[0].strip('"').strip("'")
    RESEARCH[item[0].strip('"').strip("'")] = temp.copy()

#Two important values
BUILDING
RESEARCH