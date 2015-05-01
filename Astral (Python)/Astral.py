#Maze is the class that creates a matrix like field
from Maze import Maze
from Player import *
from SaveLoad import *
from ConsoleColors import set_color
from Help import *
from INFO import BUILDING
from INFO import RESEARCH
from random import randint
from time import strftime
from GetFileDir import get_file_dir
from os import *

################################################################################
def replace(word, key1, key2):
    final_word = ""
    for char in word:
        if char == key1:
            final_word += key2
        else:
            final_word += char
    return final_word

################################################################################
def pos_dir(x_loc, y_loc):
    global field
    pos = []
    if field.cell(x_loc + 1, y_loc) != "":
        pos.append( "x_loc += 1" )
    elif (x_loc + 1) % 2 == 0 and y_loc % 2 == 0:
        pos.append( "x_loc += 1" )
    if field.cell(x_loc - 1, y_loc) != "":
        pos.append( "x_loc -= 1" )
    elif (x_loc - 1) % 2 == 0 and y_loc % 2 == 0:
        pos.append( "x_loc -= 1" )
    if field.cell(x_loc, y_loc + 1) != "":
        pos.append( "y_loc += 1" )
    elif x_loc % 2 == 0 and (y_loc + 1) % 2 == 0:
        pos.append( "y_loc += 1" )
    if field.cell(x_loc, y_loc - 1) != "":
        pos.append( "y_loc -= 1" )
    elif x_loc % 2 == 0 and (y_loc - 1) % 2 == 0:
        pos.append( "y_loc -= 1" )
    return pos

################################################################################
def clear(num = 15):
    for i in range(num):
        print "\n"
################################################################################	

game = False       # should the gameplay start?
fail = False       # for synx typing
MAX_NAME_LEN = 10  # max possible name for a player
MAX_COLOR_LEN = 10 # max possible name for a color
COLOR = 15         # the standard Menu coloring

DMG_COLOR = (80, 64, 112) # colors for hp damage levels

RESET_OPTIONS = ["15", "15", "0", "4", [["Red", "012"], ["Blue", "009"], ["Green", "010"], ["Yellow", "014"], ["Cyan", "011"]], [["Player 1", "Red"], ["Player 2", "Blue"], ["Player 3", "Green"], ["Player 4", "Yellow"]]]
# what the options file will reset itself to
    # saves it to the options file
    # [0] field size, (x)
    # [1] field size, (y)
    # [2] starting gold
    # [3] # of players
    # [4] possible colors, each divided by " - " and in the form "COLOR NAME<>Code"
    # [5] previously used players, each divided by " - " and in the form "PLAYER NAME<>COLOR NAME"

################################################################################
def clear(num = 15):
    """clear(...) --> None
    prints num blank lines in the console, effectively clearing the screen.
    num is an int"""
    for i in range(num):
        print "\n"

################################################################################
def color_num(color_name):
    """color_num(...) --> int
    Returns the value of the color with the name color_name, for windows console
    The num is taken from the colors list in options.
    if the color name is no in the options file it returns the standard COLOR
    color_name is a str
    """
    global options
    for color in range(len(options[4])):
        if options[4][color][0] == color_name:
            return int(options[4][color][1])
    return COLOR

################################################################################
def write_options(options):
    """write_options(...) --> None
    Writes the options file for this game, specific format needed
    options is a list"""
    for line in range(len(options[4])):
        options[4][line] = "<>".join(options[4][line])
    options[4] = " - ".join(options[4])
    for line in range(len(options[5])):
        options[5][line] = "<>".join(options[5][line])
    options[5] = " - ".join(options[5])
    options = "\n".join(options)
    savegame("options", options, ext = ".osf")
    
    options = options.split("\n")
    options[4] = options[4].split(" - ")
    for item in range(len(options[4])):
        options[4][item] = options[4][item].split("<>")
    options[5] = options[5].split(" - ")
    for item in range(len(options[5])):
        options[5][item] = options[5][item].split("<>")
    for i in range(options.count("")):
        options.remove("")
    return options
    
################################################################################
def options_menu():
    """options() --> OUTPUT
    prints off the options menu file to the command prompt and allows interaction
    """
    choice = ""
    global options
    global RESET_OPTIONS
            
    while choice != "0":
        try:
            options = loadgame("options", ext = ".osf").split("\n")
            options[4] = options[4].split(" - ")
        except:RESET_OPTIONS = write_options(RESET_OPTIONS)
        options = loadgame("options", ext = ".osf").split("\n")
        options[4] = options[4].split(" - ")
        for item in range(len(options[4])):
            options[4][item] = options[4][item].split("<>")
        options[5] = options[5].split(" - ")
        for item in range(len(options[5])):
            options[5][item] = options[5][item].split("<>")
        for i in range(options.count("")):
            options.remove("")
            

        clear()
        set_color(COLOR)
        print "--> OPTIONS <--\n"
        print "1) Field Size:      %s * %s" % (options[0], options[1])
        print "2) Starting Gold:   %s" % (options[2])
        print "3) Players:         %s" % (options[3])
        print "4) Add/Remove Colors"
        print "\nDefault Players:"
        for players in range(len(options[5])):
            print "%i) %s" % (5 + players, options[5][players][0]),
            print "%s: " % (" " * (MAX_NAME_LEN - len(options[5][players][0]))),
            
            color = color_num(options[5][players][1])
            print "%s" % (options[5][players][1].capitalize()),
            set_color(int(color))
            del color
            print "%s: " % (" " * (MAX_COLOR_LEN - len(options[5][players][1]))),
            print "SAMPLE"
            set_color(COLOR)
            
        print "\nS) Save Options File"
        print "L) Load Options File"
        print "RD) RESET TO DEFAULT"
        print "\n0) Quit"
        
        choice = raw_input("\n:").lower()
        ########################################################################
        if choice == "1":
            while choice != "3":
                clear()
                print "--> Field Size <--"
                print "1) Length: %s" % (options[0])
                print "2) Width:  %s" % (options[1])
                print "\n3) Quit"
                choice = raw_input("\n:")
                if choice == "1":
                    choice = raw_input("Set New Length\n:")
                    if choice.isdigit():
                        options[0] = choice
                elif choice == "2":
                    choice = raw_input("Set New Width\n:")
                    if choice.isdigit():
                        options[1] = choice
        ########################################################################       
        elif choice == "2":
            choice = raw_input("Set New Starting Gold\n:")
            if choice.isdigit():
                options[2] = choice
        ########################################################################
        elif choice == "3":
            print "\n\n(Max Number is 5)"
            choice = raw_input("Set New Number of Players\n:")
            if choice.isdigit() and int(choice) <= 5 and int(choice) > 1:
                options[3] = choice
                if len(options[5]) < int(choice):
                    for num in range(int(choice)):
                        if num >= len(options[5]):
                            options[5].append(["Player %i" % (num + 1), options[4][0][0]])
                if len(options[5]) > int(choice) and len(options[5]) > 2:
                    options[5] = options[5][:int(choice)]
        ########################################################################
        elif choice == "4":
            color_options()
        ########################################################################
        elif choice == "rd":
            options = RESET_OPTIONS[:4]
            options.append( [] )
            for item in RESET_OPTIONS[4][:]:
                options[4].append( item )
            options.append( [] )
            for item in RESET_OPTIONS[5][:]:
                options[5].append( item )
            
        ########################################################################
        elif choice == "s":
            for line in range(len(options[4])):
                options[4][line] = "<>".join(options[4][line])
            options[4] = " - ".join(options[4])
            for line in range(len(options[5])):
                options[5][line] = "<>".join(options[5][line])
            options[5] = " - ".join(options[5])
            options = "\n".join(options)
            savegame(raw_input("Enter File Name: "), options, ext = ".osf")
            
            options = options.split("\n")
            options[4] = options[4].split(" - ")
            for item in range(len(options[4])):
                options[4][item] = options[4][item].split("<>")
            options[5] = options[5].split(" - ")
            for item in range(len(options[5])):
                options[5][item] = options[5][item].split("<>")
            for i in range(options.count("")):
                options.remove("")
        ########################################################################
        elif choice == "l":
            try:
                if raw_input("Are you sure you wish to discard current options settings? (Y/N)\n:").lower() == "n":
                    loadgame()
                options = loadgame(raw_input("(Must be in the same folder as Astral.)\nEnter File Name: "), ext = ".osf")
                options = options.split("\n")
                options[4] = options[4].split(" - ")
                for item in range(len(options[4])):
                    options[4][item] = options[4][item].split("<>")
                options[5] = options[5].split(" - ")
                for item in range(len(options[5])):
                    options[5][item] = options[5][item].split("<>")
                for i in range(options.count("")):
                    options.remove("")
            except:raw_input("Load Failed\nPress Enter to Continue")
            
        ########################################################################
        elif choice != "0" and choice.isdigit() and int(choice) < 5 + int(options[3]):
            # Default Player Menu
            player = int(choice) - 5
            while choice != "3":
                clear()
                print "1) " + options[5][player][0]
                print "2) " + options[5][player][1]
                set_color(COLOR)
                print "\n3) Quit"
                choice = raw_input("\n:")
                if choice == "1":
                    name = raw_input("New Player Name\n:")
                    if len(name) > MAX_NAME_LEN:
                        print "Name too long, sorry for the inconvinience"
                    else:
                        options[5][player][0] = name
                        options = write_options(options)
                elif choice == "2":
                    current_colors()
                    color = raw_input("Choose New Player Color: ")
                    if color.isdigit and int(color) >= 0 and int(color) < len(options[4]):
                        options[5][player][1] = options[4][int(color)][0]
                    options = write_options(options)
        
        options = write_options(options)

################################################################################
def current_colors():
    print "--> Current Colors <--",
    for num in range(len(options[4])):
        set_color(int(options[4][num][1]))
        text = "\n%i) %s\nCode: %s" % (num, options[4][num][0].capitalize(), options[4][num][1])
        print text
        set_color(COLOR)
        
################################################################################  
def color_options():
    global options
    global choice
    choice = ""
    while choice != "4":
        clear()
        
        current_colors()
        print "\n\n--> Color Menu <--"
        print "1) Add Color"
        print "2) Remove Color"
        print "3) See Color List"
        print "\n4) Quit"
        #UPDATE: 3) Sort By
        
        choice = raw_input("\n:")
        ########################################################################
        if choice == "1":
            choice = "new"
            while choice != "3" and choice != "4":
                
                if choice == "new":
                    color = [raw_input("New Color Name\n:")]
                    color.append(raw_input("Value\n:"))
                if len(str(color[1])) < 3:
                    color[1] = "0" * (3 - len(str(color[1]))) + color[1]
                clear()
                print "--> YOUR NEW COLOR <--"
                print "\n\n1) " + color[0]
                if color[0] > MAX_COLOR_LEN:
                    print "The color name is too long\n"
                set_color(int(color[1]))
                print "SAMPLE"
                set_color(COLOR)
                print "2) Value: %s" % (color[1])
                print "\n3) Add This Color"
                print "\n4) Quit & Discard"
                choice = raw_input("\n:")
                
                if choice == "1":
                    color = [raw_input("New Color Name\n:")]
                    color.append(color[0])
                    
                elif choice == "2":
                    color = [color[0]]
                    color.append(raw_input("Value\n:"))
                    
                elif choice == "3":
                    if color[0] > MAX_COLOR_LEN:
                        options[4].append(color)
                        options = write_options(options)
                    else:
                        print "\nThe color name is too long"
                        raw_input("Press Enter to Continue")
                        

        ########################################################################    
        elif choice == "2":
            current_colors()
            choice = raw_input("\nWhich Color\n:").lower()
            y_nchoice = raw_input("Are you Sure? (Y/N)\n:").lower()
            
            if y_nchoice == "y" or y_nchoice == "yes":
                options[4] = options[4][:int(choice)] + options[4][int(choice) + 1:]
                options = write_options(options)
       
            choice = ""
        ########################################################################    
        elif choice == "3":
            clear()
            for num in range(256):
                set_color(num)
                print  "0" * (3 - len(str(num))) + str(num),
                set_color(COLOR)
                print " ",
                if num % 10 == 0:
                    print "\n"
            raw_input('\n\nPress Enter to Continue')
            

# BOOKMARKS:
# Search for it to find commands
# NEW GAME
# LOAD GAME
# GAMEPLAY
# SHOW FIELD
# PLAYER INFO
# FIX CONTINUE
# SELL CONTINUE
# BUILD CONTINUE
# BUILD
# BUILD PART 2
# STATS
# ALLY-MENU
# TRIBUTE
# RESEARCH
# FIX
# SELL
# INCOME
# CONSOLE
# END TURN
# SAVE
# LOAD

# Main Menu, loops until quit
################################################################################
choice = ""
set_color(COLOR)
while choice != "0" or choice.lower() == "quit":
    clear()
    print """
    --> Astral <--
    
    1) New Game
    2) Load Game
    3) Options
    4) Instructions
    
    0) Quit
    """
    choice = raw_input(":")
    
#NEW GAME
################################################################################
    if choice == "1":
        #creates the battle field
        # first opens the options file
        options = loadgame("options", ext = ".osf")
        options = options.split("\n")
        options[4] = options[4].split(" - ")
        for item in range(len(options[4])):
            options[4][item] = options[4][item].split("<>")
        options[5] = options[5].split(" - ")
        for item in range(len(options[5])):
            options[5][item] = options[5][item].split("<>")
        for i in range(options.count("")):
            options.remove("")
            
        options[0] = int(options[0])    
        options[1] = int(options[1])
        options[2] = int(options[2])
        options[3] = int(options[3])
        
        # makes an empty field
        field = Maze("#")
        field.clear(options[0], options[1], value = "")
        if (field.sizey() / 2) % 2 != 0:
            y_half = (field.sizey()) / 2 - 1
        else:
            y_half = field.sizey() - 1
        if (field.sizex() / 2) % 2 != 0:
            x_half = field.sizex() / 2 - 1
        else:
            x_half = field.sizex() - 2
            
        effect_field = Maze("#")
        effect_field.clear(options[0], options[1], value = "")
        
        attack_field = Maze("#")
        attack_field.clear(options[0], options[1], value = "")
            
        x = field.sizex()
        y = field.sizey()
        usable = [(0,0)] # Bottom Left
        usable.append((x - 1,y - 1)) # Top Right
        usable.append((0, y - 1)) # Top Left
        usable.append((x - 1, 0)) # Bottom Right
        usable.append((x_half, y_half)) # Middle Middle
        usable.append((0, y_half)) #Middle Left
        usable.append((x_half, 0)) # Bottom Middle
        usable.append((x_half, y - 1)) # Middle Right
        usable.append((x - 1, y_half)) #Top Middle

        ally_invite = {}
        for player in range(options[3]):
            myself = [player + 1]
            exec "player%i = Player(%i, options[5][player][1], options[5][player][0], gold = options[2], allies = myself[:])" % (player + 1, player + 1)
            exec "player%i.add_building(BUILDING['Wizard Cottage'].copy(), usable[player][0], usable[player][1])" % (player + 1)
            field.setcell(usable[player][0], usable[player][1], player + 1)
            ally_invite[player + 1] = []
        player1.gold += 50
        player = 1
        player1.turn = 1
        
        game = True
        did_player_attack = False
        clear()
        
#LOAD GAME
################################################################################
    elif choice == "2":
        # if game is loaded
        directory = getcwd()
        name = get_file_dir(cur_dir = getcwd() + "\Save Games", ext = ".sav")
        if name != None:
            save_data = loadgame(name, loc = getcwd(), ext = ".sav")
            exec save_data
            game = True
        chdir(directory)
        
################################################################################
    elif choice == "3":
        options_menu()
################################################################################   
    elif choice == "4":
        #instructions for the game
        help_menu("help")
################################################################################
    elif choice == "0" or choice.lower() == "quit":
        if raw_input("Are you sure you wish to quit?\n(Y/N)\n:").lower() == "n":
            choice = ""
        game = False
        
# GAMEPLAY
################################################################################  
    if game:
        
        #gameplay, options file is in this format:
            # [0] field size, (x)
            # [1] field size, (y)
            # [2] starting gold
            # [3] # of players
            # [4] possible colors, each divided by " - " and in the form "COLOR NAME<>Code"
            # [5] previously used players, each divided by " - " and in the form "PLAYER NAME<>COLOR NAME"
    
        choice = ""
        max_heal = 0
        # Loop for all players
        
        continue_option = False
        continue_building_till_stop = False
        x_loc = ""
        y_loc = ""
        direction = ""
        
        while choice != "quit" and choice != "q" and choice != "exit":
            
            # SHOW FIELD
            ####################################################################
            clear(num = 30)
            
            for y_value in range(field.sizey() - 1, -1, - 1):
                #changes numbers to be with 0 at the bottom
                print "\n%i" % (y_value),
                print " " * ( 2 - len(str(y_value))),
                for x_value in range(field.sizex()):
                    color_add = 0
                    # if there is a building add its symbol
                    if field.cell(x_value,y_value) != "":
                        play = int(field.cell(x_value,y_value))
                        exec "build_type = player%i.buildings[(%i,%i)]['TYPE'][:]" % (play, x_value, y_value)
                        sym = " "
                        # to show degree of damage
                        hp = 100
                        try:exec "hp = int(float(player%i.buildings[(%i,%i)]['HP']) / player%i.buildings[(%i,%i)]['MAXHP'] * 100)" % (play, x_value, y_value, play, x_value, y_value)
                        except:pass
                        if hp >= 100:color_add = 0
                        elif hp <= 99 and hp >= 66:color_add = DMG_COLOR[0]
                        elif hp <= 65 and hp >= 33:color_add = DMG_COLOR[1]
                        elif hp <= 32:color_add = DMG_COLOR[2]
                        
                        # for Astral Lines
                        if "AL" in build_type and ((x_value % 2 == 0 and y_value % 2 != 0) or (x_value % 2 != 0 and y_value % 2 == 0)):
                            exec "sym = player%i.buildings[(%i,%i)]['SYMB']" % (play, x_value, y_value)
                            exec "set_color(color_add + color_num(player%i.color))" % (play)
                            if (x_value % 2 == 0 and y_value % 2 != 0):
                                sym = sym[0]
                            elif (x_value % 2 != 0 and y_value % 2 == 0):
                                sym = sym[1]
                                
                        # for buildings
                        elif "B" in build_type and x_value % 2 == 0 and y_value % 2 == 0:
                            if "AL" in build_type:
                                exec "sym = player%i.buildings[(%i,%i)]['SYMB'][-1]" % (play, x_value, y_value)
                                exec "set_color(color_add + color_num(player%i.color))" % (play)
                            else:
                                exec "sym = player%i.buildings[(%i,%i)]['SYMB']" % (play, x_value, y_value)
                                exec "set_color(color_add + color_num(player%i.color))" % (play)
                        print sym,
                        print "",
                        set_color(COLOR)
                        
                    #if there is no building add 'empty' symbols for each square
                    elif x_value % 2 == 0 and y_value % 2 == 0:
                        # location for buildings
                        print ".",
                        print "",
                    elif x_value % 2 != 0 and y_value % 2 != 0:
                        # location for nothing...
                        print " ",
                        print "",
                    else:
                        # location for empty astral lines
                        print " ",
                        print "",
            
            # adds bottom numbers
            print "\n\n   ",
            for x_value in range(field.sizey()):
                print str(x_value) + " " * (2 - len(str(x_value))),

            # PLAYER INFO
            # player information, gold, color, whose turn it is
            print "\n"
            exec "player_color = player%i.color" % (player)
            exec "cur_gold = player%i.gold" % (player)
            exec "player_name = player%i.name" % (player)
                
            print "    %s  -  MP: %i  - " % (player_name, cur_gold),
            
            set_color(color_num(player_color))
            print "COLOR"
            set_color(COLOR)
            
            print "    Turn:",
            exec 'print player%i.turn' % (player)
            
            # possible choice for player input
            ####################################################################
            if not continue_option:
                # if the person misspelled somethin, not a known combination
                if fail:
                    set_color(012)
                    print ""
                    print "< This Was not a Known Key Combination, Please Check Your Spelling >",
                    set_color(COLOR)
                    fail = False
                print "\n\n",
                print "Type 'help' for general help with the game"
                choice = raw_input(": ")
              
                
                
            #ATTACK CONTINUE
            ####################################################################
            elif continue_option == "attack":
                #choose location
                temp = choice
                choice = ""
                if temp == "ATTACK: Basic Magics":
                    exec "allies = player%i.allies[:]" %(player)
                    for ally in allies:
                        exec "other_ally_list = player%i.allies[:]" % (ally)
                        if player not in other_ally_list:
                            allies.remove(ally)
                    if player not in allies:
                        allies.append(player)
                    allies.sort()
                    while 1 and x_loc == "" and y_loc == "":
                        
                        choice = raw_input("(Type 'cancel' to quit)\n(format: 'x,y')\nSelect Place to Attack From: ").lower()
                        if choice == "cancel" or choice == "quit" or choice == "q" or choice == "exit":
                            continue_option = False
                            choice = ""
                            break
                        
                        choice = choice.split(",")
                        can_use = False
                        if len(choice) == 2 and choice[0].isdigit() and choice[1].isdigit():
                            x_loc = int(choice[0])
                            y_loc = int(choice[1])
                            if field.cell(x_loc,y_loc) == player and attack_field.cell(x_loc,y_loc) == "":pass
                            elif attack_field.cell(x_loc,y_loc) != "":
                                set_color(12)
                                print "You already attacked with this building..."
                                raw_input("Press Enter to Continue: ")
                                set_color(COLOR)
                                choice = temp
                                x_loc = ""
                                y_loc = ""
                                break
                            else:
                                set_color(12)
                                print "Square Not Possible"
                                raw_input("Press Enter to Continue: ")
                                set_color(COLOR)
                                choice = temp
                                x_loc = ""
                                y_loc = ""
                                break
                    if field.cell(x_loc,y_loc) == player and attack_field.cell(x_loc,y_loc) == "":
                        choice = temp
                        continue_option = "attack2"
                    
            elif continue_option == "attack2":
                #choose direction
                print "LOC: %i, %i" % (x_loc, y_loc)
                possible = pos_dir(x_loc,y_loc)
                pos_input = {}
                if "x_loc += 1" in possible:
                    print "Right"
                    pos_input["right"] = "x_loc += 1"
                if "x_loc -= 1" in possible:
                    print "Left"
                    pos_input["left"] = "x_loc -= 1"
                if "y_loc += 1" in possible:
                    print "Up"
                    pos_input["up"] = "y_loc += 1"
                if "y_loc -= 1" in possible:
                    print "Down"
                    pos_input["down"] = "y_loc -= 1"
                    
                print " \nQuit"
                if len(possible) > 1:
                    dir_choice = raw_input("Which Direction: ").lower()
                    if dir_choice in pos_input.keys():
                        direction = pos_input[dir_choice]
                        continue_option = False
                    if dir_choice == "cancel":
                        continue_option = False
                        choice = ""
                    else:
                        choice = temp
                elif len(possible) == 1:
                    direction = possible[0]
                    continue_option = False
                else:
                    continue_option = "attack"
            # FIX CONTINUE
            #if one of the menu's need the map shown, all must end with "continue_option = False" and "choice = ''"
            ####################################################################  
            elif continue_option == "fix":
                exec "loc_building = player%i.buildings[ (choice[1][0], choice[1][1]) ].copy()" % (player)
                if max_heal == 0 and cur_gold / loc_building["FIX"] != 0:
                    while max_heal != "cancel":
                        exec "loc_building = player%i.buildings[ (choice[1][0], choice[1][1]) ].copy()" % (player)
                        print "COST Per HP: " + loc_building["FIX"] + " MP"
                        print "HP:          ",
                        print loc_building["HP"],
                        print "/",
                        print loc_building["MAXHP"]
                        max_heal = raw_input("Type Cancel to continue\nHeal How Much HP?\n: ")
                        if max_heal.isdigit():
                            max_heal = int(max_heal)
                            break
                elif max_heal == "max":
                    max_fix = (cur_gold / loc_building["FIX"])
                    max_hp = loc_building["MAXHP"] - loc_building["HP"]
                    if max_hp - max_fix < 0: max_heal = max_hp
                    elif max_hp - max_fix > 0: max_heal = max_fix
                if max_heal * loc_building["FIX"] <= cur_gold:
                    exec "player%i.buildings[ (choice[1][0], choice[1][1]) ]['HP'] += max_heal" % (player)
                    exec "player%i.gold -= max_heal * loc_building['FIX']" % (player)
                    print "You healed: %i HP" % (max_heal)
                    print "Using       %i MP" % (max_heal * loc_building["FIX"])
                    print "LOC:        (%i,  %i)" % (choice[1][0], choice[1][1])
                    print "NEW HP:    ",
                    exec "loc_building = player%i.buildings[ (choice[1][0], choice[1][1]) ].copy()" % (player)
                    print loc_building["HP"],
                    print "/",
                    print loc_building["MAXHP"]
                    raw_input("Press Enter to Continue: ")
                continue_option = False
                choice = ""
            
            # SELL CONTINUE
            ####################################################################
            elif continue_option == 'sell':
                exec "temp_cost = player%i.buildings[ (choice[1][0], choice[1][1]) ]['COST']" % (player)
                exec "temp_hp = player%i.buildings[ (choice[1][0], choice[1][1]) ]['HP']" % (player)
                exec "temp_maxhp = player%i.buildings[ (choice[1][0], choice[1][1]) ]['MAXHP']" % (player)
                mana_gain = int((float(temp_hp) / temp_maxhp) * temp_cost) - 1
                exec "player%i.gold += mana_gain" % (player)
                exec "player%i.dest_building( choice[1][0], choice[1][1] )" % (player)
                field.setcell(choice[1][0], choice[1][1], "")
                print "Sold For: " + str(mana_gain) + " MP"
                raw_input("\nPress Enter to Continue: ")
                mana_gain = 0
                choice = ""
                continue_option = False
                exec "temp_alive = player%i.isalive()" % (player)
                if not temp_alive:
                    set_color(012)
                    print "\nGAME OVER\nYou Have No More Buildings, you have lost the game."
                    raw_input("Press Enter to Continue: ")
                    set_color(COLOR)
                    choice = "done"
                
            # BUILD CONTINUE
            #if one of the menu's need the map shown, all must end with "continue_option = False" and "choice = ''"
            ####################################################################
            elif continue_option == "build":
                choice = ""
                exec "allies = player%i.allies[:]" %(player)
                for ally in allies:
                    exec "other_ally_list = player%i.allies[:]" % (ally)
                    if player not in other_ally_list:
                        allies.remove(ally)
                if player not in allies:
                    allies.append(player)
                allies.sort()
                while 1:
                    
                    print ""
                    print "%s  - " % (name),
                    print BUILDING[ name ]["COST"],
                    print "MP"
                    
                    choice = raw_input("(Type 'cancel' to quit)\n(format: 'x,y')\nSelect Place to Build: ").lower()
                    if choice == "cancel" or choice == "quit" or choice == "q" or choice == "exit":
                        continue_option = False
                        continue_building_till_stop = False
                        break
                    
                    choice = choice.split(",")
                    # check if input was correct
                    can_build = False
                    if len(choice) == 2 and choice[0].isdigit() and choice[1].isdigit():
                        if field.cell(int(choice[0]), int(choice[1])) == "":
                            x = int(choice[0])
                            y = int(choice[1])
                            # if it is a building check only adjacent spots
                            if "B" in BUILDING[name]["TYPE"] and x % 2 == 0 and y % 2 == 0:
                                if field.cell(x+1,y) in allies or field.cell(x-1,y) in allies or field.cell(x,y+1) in allies or field.cell(x,y-1) in allies:
                                    can_build = True
                            # if it is an AL check adjacent, and spots connected by other AL's
                            if "AL" in BUILDING[name]["TYPE"] and not can_build:
                                if field.cell(x+1,y) in allies or field.cell(x-1,y) in allies or field.cell(x,y+1) in allies or field.cell(x,y-1) in allies:
                                    can_build = True
                                elif field.cell(x+1,y+1) in allies or field.cell(x-1,y-1) in allies or field.cell(x-1,y+1) in allies or field.cell(x+1,y-1) in allies:
                                    can_build = True
                                elif (x % 2 == 0 and y % 2 != 0) and (field.cell(x,y+2) in allies or field.cell(x,y-2) in allies):
                                    can_build = True
                                elif (x % 2 != 0 and y % 2 == 0) and (field.cell(x+2,y) in allies or field.cell(x-2,y) in allies):
                                    can_build = True
                                if x % 2 == 0 and y % 2 == 0:
                                    can_build = False
                            if x % 2 != 0 and y % 2 != 0:
                                can_build = False
                            if x < 0 or x >= field.sizex() or y < 0 or y >= field.sizex():
                                can_build = False
                            
                        if not can_build:
                            set_color(12)
                            print "Square Not Possible"
                            raw_input("Press Enter to Continue: ")
                            set_color(COLOR)
                            break
                        
                        else:
                            exec "player%i.gold -= BUILDING[name]['COST']" % (player)
                            exec "player%i.add_building(BUILDING[name].copy(), x, y)" % (player)
                            field.setcell(x, y, player)
                            exec "cur_gold = player%i.gold" % (player)
                            if not continue_building_till_stop or cur_gold < BUILDING[name]['COST']:
                                continue_option = False
                                continue_building_till_stop = False
                            break
                            
                    elif choice == ["continue"]:
                        continue_building_till_stop = True
                        break
                    
                    else:
                        set_color(12)
                        print "\nWrong Format"
                        raw_input("Press Enter to Continue: ")
                        set_color(COLOR)
                        break
                    
                choice = ""
            #SURRENDER CONTINUE
            ####################################################################
            elif continue_option == "done":
                choice = "done"
                continue_option = False
            
            # HELP
            ####################################################################
            if len(choice) >= 4 and choice[:4].lower() == "help":
                help_menu(choice)
            
            #BUILD
            ####################################################################
            elif choice.lower() == "build":
                exec "temp = player%i.poss_building()" % (player)
                build_choice = ""
                name = ""
                clear()
                while build_choice != "0":
                    exec "cur_gold = player%i.gold" % (player)
                    exec "player_color = player%i.color" % (player)
                    # if a buildings was not chosen
                    if len(name) == 0:
                        print "--> Build Menu <--"
                        length = 0
                        for item in temp:
                            if len(item) > length:
                                length = len(item)
                        for item in range(len(temp)):
                            if BUILDING[ temp[item] ]["COST"] > cur_gold:
                                set_color(12)
                                #red
                            print "%i) %s" % (item + 1, temp[item]),
                            print " " * (length - len(temp[item])) + "-",
                            print BUILDING[ temp[item] ]["COST"],
                            print "MP"
                            set_color(COLOR)
                        print "\n0) QUIT"
                            
                        build_choice = raw_input("\n: ").lower()
                        if build_choice.isdigit() and int(build_choice) > 0 and int(build_choice) <= len(temp):
                            name = temp[int(build_choice) - 1]
                    
                    # if a building was chosen
                    elif len(name) > 0:
                        
                        clear()
                        print "--> %s <--" % (name)
                        # the place it can be built on
                        print "Type:"
                        if "AL" in BUILDING[name]["TYPE"]:
                            print "    Astral Line"
                        if "B" in BUILDING[name]["TYPE"]:
                            print "    Building"

                        if len(BUILDING[name]["PRE"]) > 0:
                            print "\nPre-requisites:"
                            for item in BUILDING[name]["PRE"]:
                                print " -> " + item
                            print ""
                        print "Cost :              ",
                        print BUILDING[name]["COST"],
                        print "MP"
                        # for astral lines to show the two symbol types
                        if "AL" in BUILDING[name]["TYPE"] and "B" not in BUILDING[name]["TYPE"]:
                            print "Symbol - Horizontal:",
                            set_color(color_num(player_color))
                            print BUILDING[name]["SYMB"][0]
                            set_color(COLOR)
                            print "Symbol - Vertical:  ",
                            set_color(color_num(player_color))
                            print BUILDING[name]["SYMB"][1]
                            set_color(COLOR)
                        # to show the type of symbol if it is a building
                        else:
                            print "Symbol :            ",
                            set_color(color_num(player_color))
                            print BUILDING[name]["SYMB"]
                            set_color(COLOR)
                        #print "",
                        #print BUILDING[name]["IMAGE"]
                        # for when images are implemented
                        print "HP:                 ",
                        print BUILDING[name]["HP"],
                        print "/",
                        print BUILDING[name]["MAXHP"]
                        if BUILDING[name]["MP"] > 0:
                            print "MP Per Turn:       +",
                            print BUILDING[name]["MP"],
                            print "MP"
                        if BUILDING[name]["RES"] > 0:
                            print "Resistance:         ",
                            print BUILDING[name]["RES"],
                            print "DMG"
                        print "Cost to Fix 1 HP:   ",
                        print BUILDING[name]["FIX"]
                        print ""
                        print BUILDING[name]["DESC"]
                        
                        
                        print ""
                        if BUILDING[ temp[int(build_choice) - 1] ]["COST"] <= cur_gold:
                            print "1) Build"
                        else:
                            set_color(12)
                            print "--> NOT ENOUGH MANA <--"
                            set_color(COLOR)
                        print "0) Cancel"
                        build_choice = raw_input("\n: ").lower()
                        if build_choice == "1" and BUILDING[name]["COST"] <= cur_gold:
                            continue_option = "build"
                            build_choice = "0"
                            
            # BUILD PART 2
            # for the build menu if no long list of options is needed
            ####################################################################
            elif len(choice) >= 5 and choice[:5].lower() == "build":
                #splits off the name part, and capitalizes it
                choice = choice[6:]
                choice = choice.split(" ")
                name = ""
                for line in range(len(choice)):
                    name += choice[line].capitalize()
                    name += " "
                name = name[:-1]
                # Finds possible buildings, then checks if there is such a building, and if it is possible to build it
                exec "temp = player%i.poss_building()" % (player)
                exec "cur_gold = player%i.gold" % (player)
                
                # Syntax Error Messages
                if name not in BUILDING:
                    set_color(12)
                    raw_input("Not Possible Building\n\nPress Enter to Continue: ")
                    set_color(COLOR)
                
                elif name not in temp:
                    set_color(12)
                    raw_input("Pre-requisites not met\n\nPress Enter to Continue: ")
                    set_color(COLOR)
                
                elif cur_gold < BUILDING[name]["COST"]:
                    set_color(12)
                    raw_input("Not Enough Mana\n\nPress Enter to Continue: ")
                    set_color(COLOR)
                    
                else:
                    continue_option = "build"
                    choice = ""   
            
            # SELL
            ####################################################################
            elif len(choice) >= 4 and choice[:4].lower() == "sell" and not did_player_attack:
                choice = choice.split(" ")
                if len(choice) == 3 or len(choice) == 2:
                    choice[1] = choice[1].split(",")
                    if len(choice[1]) == 2 and choice[1][0].isdigit() and choice[1][1].isdigit():
                        choice[1][0] = int(choice[1][0])
                        choice[1][1] = int(choice[1][1])
                        if field.cell( choice[1][0], choice[1][1]) == player:
                            continue_option = "sell"
                        else:
                            choice = ""
            
                    
            # STATS
            # Shows stats of buildings
            ####################################################################
            elif len(choice) >= 5 and choice[:5].lower() == "stats":
                choice = choice.split(" ")
                if len(choice) == 2:
                    choice[1] = choice[1].split(",")
                    if len(choice[1]) == 2 and choice[1][0].isdigit() and choice[1][1].isdigit():
                        choice[1][0] = int(choice[1][0])
                        choice[1][1] = int(choice[1][1])
                        loc_player = field.cell(choice[1][0], choice[1][1])
                        if loc_player != "":
                            exec "people = player%i.allies" % (loc_player)
                            exec "loc_building = player%i.buildings[ (choice[1][0], choice[1][1]) ].copy()" % (loc_player)
                            if player in people or player == loc_player:
                                #Displays stats
                                clear()
                                print "--> %s <--" % (loc_building["NAME"])
                                # the place it can be built on
                                print "Type:"
                                if "AL" in loc_building["TYPE"]:
                                    print "    Astral Line"
                                if "B" in loc_building["TYPE"]:
                                    print "    Building"
        
                                if len(loc_building["PRE"]) > 0:
                                    print "\nPre-requisites:"
                                    for item in loc_building["PRE"]:
                                        print " -> " + item
                                    print ""
                                # for astral lines to show the two symbol types
                                if "AL" in loc_building["TYPE"] and "B" not in loc_building["TYPE"]:
                                    print "Symbol - Horizontal:",
                                    set_color(color_num(player_color))
                                    print loc_building["SYMB"][0]
                                    set_color(COLOR)
                                    print "Symbol - Vertical:  ",
                                    set_color(color_num(player_color))
                                    print loc_building["SYMB"][1]
                                    set_color(COLOR)
                                # to show the type of symbol if it is a building
                                else:
                                    print "Symbol :            ",
                                    set_color(color_num(player_color))
                                    print loc_building["SYMB"][-1]
                                    set_color(COLOR)
                                #print "",
                                #print loc_building["IMAGE"]
                                # for when images are implemented
                                print "HP:                 ",
                                print loc_building["HP"],
                                print "/",
                                print loc_building["MAXHP"]
                                if loc_building["MP"] > 0:
                                    print "MP Per Turn:       +",
                                    print loc_building["MP"],
                                    print "MP"
                                if loc_building["RES"] > 0:
                                    print "Resistance:         ",
                                    print loc_building["RES"],
                                    print "DMG"
                                print "Cost to Fix 1 HP:   ",
                                print loc_building["FIX"]
                                print ""
                                print loc_building["DESC"]
                                
                                
                                print ""
                                if not did_player_attack:
                                    print "1) Sell"
                                    exec "temp_cost = player%i.buildings[ (choice[1][0], choice[1][1]) ]['COST']" % (player)
                                    exec "temp_hp = player%i.buildings[ (choice[1][0], choice[1][1]) ]['HP']" % (player)
                                    exec "temp_maxhp = player%i.buildings[ (choice[1][0], choice[1][1]) ]['MAXHP']" % (player)
                                    mana_gain = int((float(temp_hp) / temp_maxhp) * temp_cost) - 1
                                    print "    FOR: " + str(mana_gain) + " MP"
                                    mana_gain = 0
                                if loc_building["FIX"] < cur_gold and loc_building["HP"] != loc_building["MAXHP"]:
                                    print "2) Fix"
                                    print "3) Max Possible Fix"
                                
                                exec "cur_pos_research = player%i.poss_research(include_special = True)" % (player)
                                for item in range(len(loc_building["OPT"])):
                                    if loc_building["OPT"][item] not in loc_building["OPT-DONE"] and loc_building["OPT"][item] in cur_pos_research:
                                        print "%i) %s" % (item + 4, loc_building["OPT"][item]),
                                        print ": COST " + str(RESEARCH[loc_building["OPT"][item]]["COST"]) + " MP"
                                        print ""
                                        print RESEARCH[loc_building["OPT"][item]]["DESC"]
                                    else:print ""
                                
                                print "\n0) Cancel"
                                stats_choice = raw_input("\n: ").lower()
                                if stats_choice.isdigit():
                                    stats_choice = int(stats_choice)
                                else:
                                    stats_choice = 0
                                if stats_choice == 1 and not did_player_attack:
                                    if raw_input("Are You Sure You Wish to Sell? (Y/N)\n: ").lower() == "y":
                                        choice[0] = "sell"
                                        continue_option = "sell"
                                elif stats_choice == 2 and loc_building["HP"] != loc_building["MAXHP"]:
                                    continue_option = "fix" 
                                    max_heal = 0
                                            
                                elif stats_choice == 3 and loc_building["HP"] != loc_building["MAXHP"]:
                                    continue_option = "fix"
                                    max_heal = "max"
                                    
                                elif stats_choice > 3 and stats_choice <= len(loc_building["OPT"]) + 3:
                                    if loc_building["OPT"][stats_choice - 4] not in loc_building["OPT-DONE"] and RESEARCH[ loc_building["OPT"][stats_choice - 4] ]["COST"] <= cur_gold and loc_building["OPT"][item] in cur_pos_research:
                                        name = loc_building["OPT"][stats_choice - 4]
                                        # Research for options for these buildings
                                        if "EXEC" in RESEARCH[name].keys():
                                            lines = RESEARCH[name]["EXEC"].split("\n")
                                            for line in lines:
                                                exec line % (player)
                                        
                else:fail = True

            # ALLY-MENU
            # changes of alliances menu
            ####################################################################
            elif len(choice) >= 4 and choice[:4].lower() == "ally":
                people = {}
                for person in Player.live_players[:]:
                    exec "people[player%s.name] = person" % (person)
                choice = choice.split(" ")
                if len(choice[0]) >= 5:
                    choice.append( choice[0][4] )
                name = ""
                exec "allies = player%i.allies[:]" % (player)
                while len(choice) < 2 and name != "q" and name != "quit" and name != "cancel" and name != "exit":
                    clear()
                    exec "allies = player%i.allies[:]" % (player)
                    # shows the current players
                    for person in range(1, options[3] + 1):
                        print ""
                        exec "print player%s.name"  % (person)
                        exec "set_color(color_num(player%s.color))"  % (person)
                        print "    COLOR"
                        set_color(COLOR)
                        if person not in Player.live_players:
                            set_color(012)
                            print "    DEAD"
                            set_color(COLOR)
                        elif person in allies:
                            print "    ALLY"
                        else:
                            print "    ENEMY"
                    
                    name = raw_input("(EXACT name is required)\n(Type cancel to quit)\nChange Which Player: ")
                    if name not in people.keys():
                        set_color(012)
                        print "Not a Player"
                        set_color(COLOR)
                    else:
                        choice.append(name)
                        name = ""
                if len(choice) < 2 or choice[1] not in people.keys():
                    set_color(012)
                    print "Not a Player"
                    set_color(COLOR)
                else:                
                    if len(choice) < 3:
                        print ""
                        print choice[1]
                        exec "set_color(color_num(player%s.color))" % (people[choice[1]])
                        print "    COLOR"
                        set_color(COLOR)
                        if people[choice[1]] in allies:
                            print "    ALLY"
                            name = raw_input("Do you wish to remove(-) him as an ally?\n:")
                        else:
                            print "    ENEMY"
                            name = raw_input("Do you wish to add(+) him as an ally?\n:")
                        if name in "+-":
                            choice.append(name)
                        else: name = ""
                    if len(choice) >= 3 and choice[2] in "+-":
                        if choice[2] == "+" and people[choice[1]] not in allies:
                            if player * -1 in ally_invite[people[choice[1]]]:
                                ally_invite[people[choice[1]]].remove(player * -1)
                            ally_invite[people[choice[1]]].append(player)
                            exec "player%i.add_ally(people[choice[1]])" % (player)
                        elif choice[2] == "-" and people[choice[1]] in allies:
                            if people[choice[1]] != player:
                                ally_invite[people[choice[1]]].append(-1 * player)
                                if player in ally_invite[people[choice[1]]]:
                                    ally_invite[people[choice[1]]].remove(player)
                            exec "player%i.remove_ally(people[choice[1]])" % (player)
                    else:
                        set_color(012)
                        print "Format Error Try Again"
                        set_color(COLOR)
                choice = ""

            # TRIBUTE
            ####################################################################
            elif len(choice) >= 7 and choice.lower()[:7] == "tribute":
                people = {}
                for person in Player.live_players[:]:
                    exec "people[player%s.name] = person" % (person)
                choice = choice.split(" ")
                if len(choice) < 2:
                    choice.append("")
                name = ""
                while choice[1] not in people.keys():
                    for person in people.keys():
                        print ""
                        exec "print player%s.name"  % (people[person])
                        exec "set_color(color_num(player%s.color))"  % (people[person])
                        print "    COLOR"
                        set_color(COLOR)
                    print "\nMake sure to check name spelling."
                    name = raw_input("(EXACT name)\n('Cancel to quit')\nTribute Which Player: ")
                    if name == "cancel" or name == "q":
                        break
                    choice[1] = name
                if len(choice) < 3:
                    choice.append(cur_gold + 1)
                elif type(choice[2]) == type("") and choice[2].isdigit():
                    choice[2] = int(choice[2])
                elif type(choice[2]) != type(0):
                    choice[2] = cur_gold + 1
                while int(choice[2]) > cur_gold and name != "cancel" and name != "q":
                    print "(Type cancel to quit)"
                    exec "cur_gold = player%i.gold" % (player)
                    print "MANA: " + str(cur_gold)
                    choice[2] = raw_input("How Much: ")
                    if choice[2] == "cancel" or choice[2] == "q":break
                    if not choice[2].isdigit():
                        choice[2] = cur_gold + 1
                if name != "cancel" and name != "q" and choice[2] != "cancel" and choice[2] != "q":
                    exec "player%i.gold += int(choice[2])" % (people[choice[1]])
                    exec "player%i.gold -= int(choice[2])" % (player)
            
            # RESEARCH
            ####################################################################
            elif len(choice) >= 5 and choice[:5].lower() == "learn":
                #splits off the name part, and capitalizes it
                name = ""
                if choice != "learn":
                    choice = choice[6:]
                    choice = choice.split(" ")
                    name = ""
                    for line in range(len(choice)):
                        if line == 0:
                            name += choice[line].upper()
                            name += " "
                        else:
                            name += choice[line].capitalize()
                            name += " "
                    name = name[:-1]
                    # if a buildings was not chosen
                exec "cur_gold = player%i.gold" % (player)
                exec "cur_pos_research = player%i.poss_research()[:]" % (player)
                if len(name) == 0:
                    exec "cur_research = player%i.research.copy()" % (player)
                    print "--> Completed Research <--"
                    for item in cur_research:
                        print item
                    
                    print "\n--> Research Menu <--"
                    length = 0
                    for item in cur_pos_research:
                        if len(item) > length:
                            length = len(item)
                    for item in range(len(cur_pos_research)):
                        if RESEARCH[ cur_pos_research[item] ]["COST"] > cur_gold:
                            set_color(12)
                            #red
                        print "%i) %s" % (item + 1, cur_pos_research[item]),
                        print " " * (length - len(cur_pos_research[item])) + "-",
                        print RESEARCH[ cur_pos_research[item] ]["COST"],
                        print "MP"
                        print "" + RESEARCH[ cur_pos_research[item] ]["DESC"]
                        set_color(COLOR)
                    print "\n0) QUIT"
                        
                    build_choice = raw_input("\n: ").lower()
                    if build_choice.isdigit() and int(build_choice) > 0 and int(build_choice) <= len(cur_pos_research):
                        name = cur_pos_research[int(build_choice) - 1]
                
                # if a building was chosen
                if len(name) > 0:
                    if name in cur_pos_research and RESEARCH[name]["COST"] <= cur_gold:
                        exec "player%i.research[RESEARCH[name]['NAME']] = RESEARCH[name].copy()" % (player)
                        exec "player%i.gold -= RESEARCH[name]['COST']" % (player)
                        if name[:6] == "ATTACK":
                            exec "player%i.attacks[RESEARCH[name]['NAME']]= RESEARCH[name].copy()" % (player)
                        #adds item etc.
            
            # FIX
            ####################################################################
            elif len(choice) >= 3 and choice[:3].lower() == "fix":
                choice = choice.split(" ")
                if len(choice) == 3 or len(choice) == 2:
                    choice[1] = choice[1].split(",")
                    if len(choice[1]) == 2 and choice[1][0].isdigit() and choice[1][1].isdigit():
                        choice[1][0] = int(choice[1][0])
                        choice[1][1] = int(choice[1][1])
                        
                        if len(choice) == 3 and choice[2].isdigit():
                            choice[2] = int(choice[2])
                            continue_option = "fix"
                            max_heal = choice[2]
                        elif len(choice) == 3 and choice[2] == "max":
                            max_heal = "max"
                            continue_option = "fix"
                        elif len(choice) == 2:
                            continue_option = "fix"
                            max_heal = 0
            
            # INCOME
            ####################################################################     
            elif choice.lower() == "income":
                clear(num = 20)
                print "--> INCOME <--"
                # adds mana to the next player
                exec "items = player%i.buildings.copy()" % (player)
                mana_gain = 0
                num = 1
                for item in items:
                    exec 'next_mana = player%i.gold + mana_gain' % (player)
                    if num % 5 == 0:
                        print "--------------------"
                        print mana_gain
                        print ""
                        num += 1
                        
                    if type(items[item]["MP"]) == type("str"):
                        print items[item]["NAME"]
                        print "    + " + items[item]["MP"]
                        print "    + " + str(next_mana / int(items[item]["MP"][:-1])) + " MP"
                        num += 1
                        mana_gain += next_mana / int(items[item]["MP"][:-1])
                    else:
                        if items[item]["MP"] != 0:
                            mana_gain += items[item]["MP"]
                            print items[item]["NAME"]
                            print "    + " + str(items[item]["MP"]) + " MP"
                            num += 1
                exec 'next_mana = player%i.gold + mana_gain' % (player)
                print "\n--------------------"
                print "TOTAL: " + str(mana_gain) + " " * (10 - len(str(mana_gain))) + " MP"
                print "\nMana Next Turn:"
                print str(next_mana) + " " * (17 - len(str(next_mana))) + " MP"
                raw_input("\n\nPress Enter to Continue: ")
            
            # CONSOLE
            ####################################################################
            elif choice.lower() == "~" and raw_input("There is NO console in this game\n:Press Enter to Continue:") == "~":
                clear()
                console_choice = "start"
                while console_choice != "" or console_choice != (" " * len(console_choice)):
                    console_choice = raw_input("\n     (Type '#<--' to decrease indent)\n     (Type '' to quit)\n>>> ")
                    if len(console_choice) > 0 and console_choice[-1] == ":":
                        temp = raw_input("...... ")
                        loop_num = 1
                        while temp != ""  or temp != (" "  * len(temp)):
                            if temp == "#<--":
                                loop_num -= 1
                            console_choice += "\n" + "    " * loop_num + temp
                            if console_choice[-1] == ":":
                                loop_num += 1
                            if loop_num < 0:
                                break
                            temp = raw_input("..." * (loop_num + 1) + " ")
                    try:
                        exec console_choice
                    except:
                        print "Error!\n"
                clear(100)
                    
            #END TURN
            ####################################################################
            elif choice.lower() == "end turn" or choice.lower() == "done":
                # changes to next player
                attack_field = Maze("#")
                attack_field.clear(field.sizex(), field.sizey(), "")
                
                
                player += 1
                while player not in Player.live_players:
                    player += 1
                    if player > int(options[3]):
                        player = 1

                # adds mana to the next player
                exec "items = player%i.buildings.copy()" % (player)
                mana_gain = 0
                for item in items:
                    if type(items[item]["MP"]) == type("str"):
                        exec 'next_mana = player%i.gold + mana_gain' % (player)
                        mana_gain += next_mana / int(items[item]["MP"][:-1])
                    else:
                        mana_gain += items[item]["MP"]
                exec "player%i.gold += mana_gain" % (player)
                
                # shows any alliance cancellations and invitations
                for person in ally_invite[player]:
                    if person >= 0:exec "name = player%i.name" % (person)
                    else: exec "name = player%i.name" % (person * -1)
                    # player information, gold, color, whose turn it is
                    print "\n\n\n\n\n"
                    exec "player_color = player%i.color" % (player)
                    exec "player_name = player%i.name" % (player)
                    print "    %s  - " % (player_name),
                    set_color(color_num(player_color))
                    print "COLOR"
                    set_color(COLOR)
            
                    if person >= 0:
                        print '%s wants to invite you to an alliance.' % (name)
                        exec "set_color(color_num(player%s.color))" % (person)
                        print "COLOR"
                        set_color(COLOR)
                        yn_choice = raw_input("Do you wish to ally with him? (Y/N)\n: ").lower()
                        if yn_choice == "y":
                            exec "player%i.add_ally(person)" % (player)
                    elif person < 0:
                        person = person * -1
                        print '%s has cancelled your allience.' % (name)
                        exec "set_color(color_num(player%s.color))" % (person)
                        print "COLOR"
                        set_color(COLOR)
                        yn_choice = raw_input("Do you wish to remain an ally to him? (Y/N)\n: ").lower()
                        if yn_choice == "n":
                            exec "player%i.remove_ally(person)" % (player)
                ally_invite[player] = []
                
                # adds 1 turn to next player
                exec "player%i.turn += 1" % (player)
                # shows the player did not attack yet
                did_player_attack = False
                #adds score
                # UPDATE

            # SURRENDER
            ####################################################################
            elif choice.lower() == "surrender":
                exec "temp = player%i.buildings.keys()" % (player)
                for key in temp:
                    field.setcell(key[0], key[1], "")
                exec "player%i.buildings = {}" % (player)
                exec "player%i.build_list = {}" % (player)
                print Player.live_players
                exec "player%i.isalive()" % (player)
                continue_option = "done"
                
            # SAVE
            ####################################################################
            elif len(choice) >= 4 and choice.lower()[:4].lower() == "save":
                choice = choice.split(" ")
                if len(choice) == 2:
                    choice = choice[1]
                else:
                    choice = "Auto Save" #+ strftime("%Y%m%d%H%M%S")
                save_data = ""
                
                save_data += "options = %s\n" % (str(options[:]))
                save_data += "field = Maze('#')\n"
                save_data += 'field.clear(options[0], options[1], value = "")\n'
                save_data += "effect_field = Maze('#')\n"
                save_data += 'effect_field.clear(options[0], options[1], value = "")\n'
                save_data += "attack_field = Maze('#')\n"
                save_data += 'attack_field.clear(options[0], options[1], value = "")\n'
                for x in range(field.sizex()):
                    for y in range(field.sizey()):
                        if field.cell(x,y) != "":
                            save_data += "field.setcell(%i, %i, %s)\n" % (x, y, field.cell(x,y))
                        if effect_field.cell(x,y) != "":
                            save_data += "effect_field.setcell(%i, %i, %s)\n" % (x, y, effect_field.cell(x,y))
                        if attack_field.cell(x,y) != "":
                            save_data += "attack_field.setcell(%i, %i, %s)\n" % (x, y, attack_field.cell(x,y))            
                for person in Player.live_players[:]:
                    exec "save_color = player%i.color" % (person)
                    exec "save_name = player%i.name" % (person)
                    exec "save_gold = player%i.gold" % (person)
                    exec "save_allies = str(player%i.allies[:])" % (person)
                    exec "save_research = str(player%i.research.copy())" % (person)
                    exec "save_attacks = str(player%i.attacks.copy())" % (person)
                    exec "save_buildings = str(player%i.buildings.copy())" % (person)
                    exec "save_build_list = str(player%i.build_list.copy())" % (person)
                    exec "save_turn = player%i.turn" % (person)
                    exec "save_score = player%i.score" % (person)
                    save_data += "player%i = Player(%i, '%s', '%s', gold = %i, allies = %s, research = %s, attacks = %s, buildings = %s, build_list = %s, turn = %i, score = %i)\n" % (person, person, save_color, save_name, save_gold, save_allies, save_research, save_attacks, save_buildings, save_build_list, save_turn, save_score)
                
                save_data += "player = %i\n" % (player)
                save_data += "ally_invite = %s\n" %(str(ally_invite))
                save_data += "did_player_attack = %s" % (str(did_player_attack))
                savegame(choice, save_data, loc = getcwd() + "\\Save Games" ,ext = ".sav")
                
            # LOAD
            ####################################################################
            # if game is loaded
            elif len(choice) >= 4 and choice.lower()[:4].lower() == "load":
                if raw_input("Are you sure you wish to abandon this game? (Y/N)\n: ").lower() == "y":
                    choice = choice.split(" ")
                    if len(choice) >= 2:
                        choice = " ".join(choice[1:])
                    else:
                        choice = "Auto Save" #+ strftime("%Y%m%d%H%M%S")
                    directory = getcwd()
                    name = choice
                    try:
                        save_data = loadgame(name, loc = getcwd() + "\\Save Games", ext = ".sav")
                        exec save_data
                        game = True
                    except:
                        print "Game could not load..."
                        raw_input("Press Enter to Continue: ")
                    chdir(directory)
                choice = ""
                        
            # checks if the player truly wants to exit
            ####################################################################
            elif choice.lower() == "quit" or choice.lower() == "q" or choice.lower() == "exit":  
                set_color(12)
                if raw_input("\nAre You Sure You Wish to Exit? (Y/N)\n:").lower() != "y":
                    choice = ""
                set_color(COLOR)
                
            # if the person misspelled somethin, not a known combination
            ####################################################################
            elif choice.lower() == "":pass
            
            # ATTACK
            ####################################################################
            elif len(choice) >= 6 and choice[:6].lower() == "attack":
                
                name = choice.split(" ")
                # choosing of the attack
                if len(name) > 2:
                    name[0] = name[0].upper()
                    for times in range(len(name) - 1):
                        name[times+1] = name[times+1].capitalize()
                    temp = ""
                    for item in name:
                        temp += item + " "
                    temp = temp[:-1]
                    name = temp
                else:
                    # choosing name, becomes "" if cancelled
                    name = ""
                    exec "cur_gold = player%i.gold" % (player)
                    exec "cur_attacks = player%i.attacks.keys()" % (player)
                    if len(name) == 0:
                        print "\n--> Attack Menu <--"
                        length = 0
                        for item in cur_attacks:
                            if len(item) > length:
                                length = len(item)
                        for item in range(len(cur_attacks)):
                            if RESEARCH[ cur_attacks[item] ]["COST"] > cur_gold:
                                set_color(12)
                                #red
                            print "%i) %s" % (item + 1, cur_attacks[item]),
                            print " " * (length - len(cur_attacks[item])) + "-",
                            print RESEARCH[ cur_attacks[item] ]["COST"],
                            print "MP"
                            print "" + RESEARCH[ cur_attacks[item] ]["DESC"]
                            set_color(COLOR)
                        print "\n0) QUIT"
                            
                        name = raw_input("\n: ").lower()
                        if name.isdigit() and int(name) > 0 and int(name) <= len(cur_attacks):
                            name = cur_attacks[int(name) - 1]
                    
                exec "cur_attacks = player%i.attacks.copy()" % (player)
                if name in cur_attacks and continue_option != "attack2" and (x_loc == "" or y_loc == "" or direction == ""):
                    player_did_attack = True
                    continue_option = "attack"
                    choice = name
                    x_loc = ""
                    y_loc = ""
                    name = ""
                elif name in cur_attacks and continue_option == "attack2":
                    choice = name
                    name = ""
                if name not in cur_attacks:
                    name = ""
                    
                #choose power
                if name != "":
                    exec "cur_power_max = player%i.attacks[name]['MAX']" % (player)
                    while 1:
                        print "Max Power: " + str(cur_power_max) + " MP"
                        print "How Much Power Do You Want To Use?"
                        power = raw_input(": ")
                        if power == "cancel" or power == "q" or power == "quit":
                            power = ""
                            name = ""
                            break
                        if power.isdigit() and int(power) <= cur_power_max and int(power) > 0 :
                            power = int(power)
                            break
                    
                if name != "":
                    attack_field.setcell(x_loc, y_loc, 1)
                    power_field = Maze("#")
                    power_field.clear(field.sizex(), field.sizey(), 0)
                
                ################################################################
                if name == "ATTACK: Basic Magics":
                    exec "cur_allies = player%i.allies[:]" % (player)
                    while power > 0:
                        temp = direction
                        temp = replace(temp, "+","!")
                        temp = replace(temp, "-","+")
                        temp = replace(temp, "!","-")
                        exec direction
                        possible = pos_dir(x_loc, y_loc)
                        if temp in possible:
                            possible.remove( temp )
                        power_field.setcell(x_loc, y_loc, power)
                        if field.cell(x_loc, y_loc) != "" and field.cell(x_loc, y_loc) not in cur_allies:
                            exec "temp_build = player%i.buildings[ (x_loc, y_loc) ].copy()"% (field.cell(x_loc, y_loc))
                            power -= temp_build["RES"]
                            power -= temp_build["HP"]
                        elif field.cell(x_loc, y_loc) in cur_allies:
                            if x_loc % 2 == 0 and y_loc % 2 == 0:
                                power = 0
                        if len(possible) >= 1:
                            direction = randint(0,len(possible) - 1)
                            direction = possible[direction]
                        else:
                            power = 0
                
                if name != "":
                    # Distributes power
                    ###############################################################
                    exec "cur_allies = player%i.allies[:]" % (player)
                    for x in range(field.sizex()):
                        for y in range(field.sizey()):
                            if field.cell(x,y) != "" and power_field.cell(x,y) != 0:
                                power = power_field.cell(x,y)
                                person = field.cell(x,y)
                                if person not in cur_allies:
                                    exec "cur_hp = player%i.buildings[ (x,y) ]['HP']" % (person)
                                    exec "cur_res = player%i.buildings[ (x,y) ]['RES']" % (person)
                                    if power - (cur_res + cur_hp) >= 0:
                                        exec "player%i.capt_building( x, y, player%i )" % (player, person)
                                        exec "player%i.buildings[ (x,y) ]['HP'] = (player%i.buildings[ (x,y) ]['HP'] / 10) + 1" % (player, player)
                                        field.setcell(x,y,player)
                                    elif power - cur_res >= 0:
                                        exec "player%i.buildings[ (x,y) ]['HP'] = player%i.buildings[ (x,y) ]['HP'] - (power - cur_res)" % (person, person)
            
                    direction = ""
                    x_loc = ""
                    y_loc = ""
            ####################################################################
            else:
                fail = True
        
        game = False