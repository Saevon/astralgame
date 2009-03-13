#----------SAMPLE----------#
"" #Research name, with either attack or research in front of it (ALL CAPS WORD: name)
["PRE"] = [""] # prerequisites
["DESC"] = """
Name reapeated
Type
Description
"""
["FUNC"] = "" #function name if it is an attack
["BUIL"] = [""] # for attacks, shows which buildings can use it 
# Type up in triple quote style, but using "\n" when done and single quotes
#----------SAMPLE----------#

"ATTACK: Mana Overload"
["PRE"] = ["Wizards Cottage"]
["DESC"] = "\n--> Mana Overload <--\nASTRAL\nMAX Power: 30 MP\nThis is a fairly basic attack.\nIt has low power and no control.\nThe mana travels over astral lines and goes in a random direction at intersections.\n"
["FUNC"] = ""
["BUIL"] = ["Wizards Cottage", "Village", "Mining Camp"]

"RESEARCH: Gem Mining"
["PRE"] = ["Mining Camp"]
["DESC"] = "n--> Gem Mining <--\nResearch\nThis allows mining for gems and crystals.\nCurrently only a void crystal has been discovered.\nWith further research other gems might be found.\n"
