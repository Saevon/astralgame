#----------SAMPLE----------#
"" #Research name, with either attack or research or special in front of it (ALL CAPS WORD: name)
["PRE"] = [""] # prerequisites
["DESC"] = """
Name reapeated
Type
Description
"""
["FUNC"] = "" #function name if it is an attack
["BUIL"] = [""] # for attacks, shows which buildings can use it 
["COST"] = 0 # cost to research
# Type up in triple quote style, but using "\n" when done and single quotes
#----------SAMPLE----------#

"ATTACK: Basic Magics"
["PRE"] = ["Wizards Cottage"]
["DESC"] = "\n--> Mana Overload <--\nASTRAL\nMAX Power: 30 MP\nThis is a fairly basic attack.\nIt has low power and no control.\nThe mana travels over astral lines and goes in a random direction at intersections.\n"
["FUNC"] = ""
["BUIL"] = ["Wizards Cottage", "Village", "Mining Camp"]
["COST"] = 200

"RESEARCH: Gem Mining"
["PRE"] = ["Mining Camp"]
["DESC"] = "n--> Gem Mining <--\nResearch\nThis allows mining for gems and crystals.\nCurrently only a void crystal has been discovered.\nWith further research other gems might be found.\n"
["COST"] = 150

"SPECIAL: Build Village Schools"
["PRE"] = [""]
["FUNC"] = "build_village_schools(x_loc, y_loc, player, '[\"MP\"] += 5')"
["COST"] = 15
