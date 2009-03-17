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

"Wizard Cottage"
["TYPE"] = "B"
["PRE"] = [""]
["SYMB"] = "C"
["IMAGE"] = []
["HP"] = 150
["MAXHP"] = 150
["MP"] = 50
["RES"] = 0
["FIX"] = 2
["COST"] = 0
["OPT"] = ["SPECIAL: Wizard Tower"]
["DESC"] = ""

"Wizard Tower"
["TYPE"] = "B"
["PRE"] = [""]
["SYMB"] = "C"
["IMAGE"] = []
["HP"] = 200
["MAXHP"] = 200
["MP"] = 75
["RES"] = 3
["FIX"] = 3
["COST"] = 0
["OPT"] = ["SPECIAL: Upgrade Resistance Lvl 1"]
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
["OPT"] = ["SPECIAL: Build Village Schools", "SPECIAL: Upgrade Resistance Lvl 1"]
["DESC"] = ""

"Mining Camp"
["TYPE"] = "B"
["PRE"] = ["RESEARCH: Gem Mining"]
["SYMB"] = "M"
["IMAGE"] = []
["HP"] = 5
["MAXHP"] = 15
["MP"] = 10
["RES"] = 0
["FIX"] = 3
["COST"] = 50
["OPT"] = ["SPECIAL: Upgrade Resistance Lvl 1"]
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
["OPT"] = ["SPECIAL: Upgrade Resistance Lvl 1"]
["DESC"] = ""

"Mage's Tent"
["TYPE"] = "B"
["PRE"] = ["Wizard Tower"]
["SYMB"] = "*"
["IMAGE"] = []
["HP"] = 1
["MAXHP"] = 1
["MP"] = 0
["RES"] = 4
["FIX"] = 0
["COST"] = 50
["OPT"] = ["SPECIAL: Upgrade Resistance Lvl 1"]
["DESC"] = ""

"Castle"
["TYPE"] = "B"
["PRE"] = ["Wizard Tower", "Mining Camp"]
["SYMB"] = "#"
["IMAGE"] = []
["HP"] = 50
["MAXHP"] = 75
["MP"] = 20
["RES"] = 0
["FIX"] = 5
["COST"] = 100
["OPT"] = ["SPECIAL: Upgrade Resistance Lvl 1"]
["DESC"] = ""

"Library"
["TYPE"] = "B"
["PRE"] = ["Wizard Tower"]
["SYMB"] = "L"
["IMAGE"] = []
["HP"] = 10
["MAXHP"] = 1000
["MP"] = 30
["RES"] = 0
["FIX"] = 25
["COST"] = 150
["OPT"] = []
["DESC"] = ""

"Mansion"
["TYPE"] = "B"
["PRE"] = ["Wizard Tower"]
["SYMB"] = "^"
["IMAGE"] = []
["HP"] = 20
["MAXHP"] = 25
["MP"] = 50
["RES"] = 0
["FIX"] = 3
["COST"] = 130
["OPT"] = []
["DESC"] = ""

"Barricade"
["TYPE"] = "BAL"
["PRE"] = ["UPDATE"]
["SYMB"] = "WWW"
["IMAGE"] = []
["HP"] = 10
["MAXHP"] = 50
["MP"] = 0
["RES"] = 0
["FIX"] = 2
["COST"] = 25
["OPT"] = ["SPECIAL: Palisade", "SPECIAL: Upgrade Resistance Lvl 1"]
["DESC"] = ""

"Palisade"
["TYPE"] = "BAL"
["PRE"] = ["UPDATE"]
["SYMB"] = "WWW"
["IMAGE"] = []
["HP"] = 15
["MAXHP"] = 100
["MP"] = 0
["RES"] = 0
["FIX"] = 4
["COST"] = 100
["OPT"] = ["SPECIAL: Wall", "SPECIAL: Upgrade Resistance Lvl 1"]
["DESC"] = ""

"Wall"
["TYPE"] = "BAL"
["PRE"] = ["UPDATE"]
["SYMB"] = "WWW"
["IMAGE"] = []
["HP"] = 20
["MAXHP"] = 200
["MP"] = 0
["RES"] = 0
["FIX"] = 3
["COST"] = 200
["OPT"] = ["SPECIAL: Upgrade Resistance Lvl 1"]
["DESC"] = ""