#----------SAMPLE----------#
"" #Research name, with either attack or research or special in front of it (ALL CAPS WORD: name)
["PRE"] = [""] # prerequisites
["DESC"] = """
Name reapeated
Type
Description
"""
["BUIL"] = [""] # for attacks, shows which buildings can use it 
["COST"] = 0 # cost to research
["EXEC"] = "" #executes this if there is a n exec only for SPECIAL items, must include a %i
# Type up in triple quote style, but using "\n" when done and single quotes
#----------SAMPLE----------#

"ATTACK: Basic Magics"
["PRE"] = ["Wizard Cottage OR Wizard Tower"]
['MAX'] = 30
["DESC"] = "\n--> Basic Magics <--\nASTRAL\nMAX Power: 30 MP\nThis is a fairly basic attack.\nIt has low power and no control.\nThe mana travels over astral lines and goes in a random direction at intersections.\n"
["BUIL"] = ["Wizards Cottage", "Village", "Mining Camp", "Castle", "Mage's Tent", "Wizards Tower"]
["COST"] = 200

"RESEARCH: Gem Mining"
["PRE"] = ["Village"]
["DESC"] = "\n--> Gem Mining <--\nResearch\nThis allows mining for gems and crystals.\nCurrently only a void crystal has been discovered.\nWith further research other gems might be found.\n"
["COST"] = 150

"RESEARCH: Resistance Spell"
["PRE"] = ["Void Crystal", "Library"]
["DESC"] = "Research\nBy studying the void crystal a spell can be researched\nthat allows for a miniature barrier similar to that of a\nvoid crystal to be enacted around a building\n"
["COST"] = 70

"SPECIAL: Build Village Schools"
["PRE"] = ["Village"]
["EXEC"] = 'player%i.buildings[ (choice[1][0], choice[1][1]) ][\'MP\'] += 5'
["DESC"] = "By buildings schools in the village, the amount of people learning wizardry increases in great numbers.\nThis will increase the MP rate of a village by 5"
["COST"] = 15

"SPECIAL: Upgrade Resistance Lvl 1"
["PRE"] = ["RESEARCH: Resistance Spell"]
["EXEC"] = 'player%i.buildings[ (choice[1][0], choice[1][1]) ][\'RES\'] += 2'
["DESC"] = "A spell has been researched that can create a miniature barrier over some objects.\nThis allows an upgrade of the resistance some objects by 2"
["COST"] = 20

"SPECIAL: Palisade"
["PRE"] = []
["EXEC"] = 'player%i.dest_building( choice[1][0], choice[1][1] )\nplayer%i.add_building(BUILDING["Palisade"].copy(), choice[1][0], choice[1][1] )'
["DESC"] = "Upgrades the barricade to a palisade"
["COST"] = 75

"SPECIAL: Wall"
["PRE"] = []
["EXEC"] = 'player%i.dest_building( choice[1][0], choice[1][1] )\nplayer%i.add_building(BUILDING["Wall"].copy(), choice[1][0], choice[1][1] )'
["DESC"] = "Upgrades the palisade to a wall"
["COST"] = 100

"SPECIAL: Wizard Tower"
["PRE"] = []
["EXEC"] = 'player%i.dest_building( choice[1][0], choice[1][1] )\nplayer%i.add_building(BUILDING["Wizard Tower"].copy(), choice[1][0], choice[1][1] )'
["DESC"] = "Upgrades the Wizards Cottage to a Wizard tower,\nfurthering you progress in magical research and allowing you to build new buildings"
["COST"] = 500

"SPECIAL: Mansion"
["PRE"] = []
["EXEC"] = 'player%i.dest_building( choice[1][0], choice[1][1] )\nplayer%i.add_building(BUILDING["MANSION"].copy(), choice[1][0], choice[1][1] )'
["DESC"] = "Upgrades the Village to a Mansion"
["COST"] = 500