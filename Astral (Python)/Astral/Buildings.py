#----------SAMPLE----------#
"" # Name of the building
["TYPE"] = "B" OR "AL" OR "BAL"
# tells it whether it can be built on astral lines or on building locations, or "blanks"
["PRE"] = [""] #Any prerequisites
["SYMB"] = "" #The Symbol for the Text version
# for astral lines show UP down first, then LEFT right
["IMAGE"] = {["Tree 1"] : "", ["Tree 2"] : "", ["Tree 3 - Spec 1"] : "", ["Tree 3 - Spec 2"] : "", ["Tree 3 - Spec 3"] : "", ["Tree 3 - Spec 4?"] : "", ["Tree 4 - Spec 1"] : "", ["Tree 4 - Spec 2"] : "", ["Tree 4 - Spec 3"] : "", ["Tree 4 - Spec 4?"] : ""} # images for the graphics version
# include LR and UD at the beggining of AL, so two of each picture
["HP"] = 150 #Hp when built
["MAXHP"] = 150 # max possible Hp (not including updates)
["MP"] = 50 # + MP per turn --- If mana gain is a percentage put "#%" with a num
["RES"] = 0 # any resistance
["FIX"] = 2 # cost to fix per Hp point
["COST"] = 500 # cost to build
["OPT"] = [""] # list of options this building gives, usually updates that are not global and only for this building
["DESC"] = "" # descriptions
#----------SAMPLE----------#

"Wizards Cottage"
["TYPE"] = "B"
["PRE"] = []
["SYMB"] = "C"
["IMAGE"] = []
["HP"] = 150
["MAXHP"] = 150
["MP"] = 50
["RES"] = 0
["FIX"] = 2
["COST"] = 500
["OPT"] = []
["DESC"] = ""

"Astral Line"
["TYPE"] = "AL"
["PRE"] = []
["SYMB"] = "|-"
["IMAGE"] = []
["HP"] = 1
["MAXHP"] = 1
["MP"] = 0
["RES"] = 4
["FIX"] = 0
["COST"] = 5
["OPT"] = []
["DESC"] = ""

"Village"
["TYPE"] = "B"
["PRE"] = []
["SYMB"] = "^"
["IMAGE"] = []
["HP"] = 10
["MAXHP"] = 10
["MP"] = 5
["RES"] = 0
["FIX"] = 2
["COST"] = 30
["OPT"] = ["SPECIAL: Build Village Schools"]
["DESC"] = ""

"Mining Camp"
["TYPE"] = "B"
["PRE"] = ["Village"]
["SYMB"] = "M"
["IMAGE"] = []
["HP"] = 5
["MAXHP"] = 10
["MP"] = 10
["RES"] = 5
["FIX"] = 3
["COST"] = 50
["OPT"] = []
["DESC"] = ""

"Void Crystal"
["TYPE"] = "B"
["PRE"] = ["RESEARCH: Gem Mining"]
["SYMB"] = "X"
["IMAGE"] = []
["HP"] = 5
["MAXHP"] = 5
["MP"] = 0
["RES"] = 5
["FIX"] = 2
["COST"] = 30
["OPT"] = []
["DESC"] = ""

"Wall"
["TYPE"] = "BAL"
["PRE"] = ["Mining Camp"]
["SYMB"] = "WWW"
["IMAGE"] = []
["HP"] = 10
["MAXHP"] = 100
["MP"] = 0
["RES"] = 0
["FIX"] = 3
["COST"] = 25
["OPT"] = []
["DESC"] = ""