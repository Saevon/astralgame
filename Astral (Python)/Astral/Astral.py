#Maze is the class that creates a matrix like field
from Maze import Maze
from Player import *
from SaveLoad import *
from ConsoleColors import set_color
from Help import *
from INFO import *

# savegame()  options :  (name, info, tocipher = True, loc = getcwd(), ext = ".txt")
# loadgame()  options :  (name, tocipher = True, loc = getcwd(), ext = ".txt")
# loadgame returns the read file, deciphered
################################################################################
def clear(num = 15):
    for i in range(num):
        print "\n"

game = False       # should the gameplay start?
MAX_NAME_LEN = 10  # max possible name for a player
MAX_COLOR_LEN = 10 # max possible name for a color
COLOR = 15         # the standart Menu coloring
RESET_OPTIONS = ["15", "15", "0", "4", [["Red", "012"], ["Blue", "009"], ["Green", "010"], ["Yellow", "014"], ["Cyan", "011"], ["Purple", "005"]], [["Player 1", "Red"], ["Player 2", "Blue"], ["Player 3", "Green"], ["Player 4", "Yellow"]]]
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
    #first write the options file
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
    global choice
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
            print "\n\n(Max Number is 12)"
            choice = raw_input("Set New Number of Players\n:")
            if choice.isdigit() and int(choice) <= 12 and int(choice) > 1:
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
            RESET_OPTIONS = write_options(RESET_OPTIONS)
            options = RESET_OPTIONS[:]
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
        elif choice != "0" and choice.isdigit():
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
            
# Main Menu, loops until quit
################################################################################
choice = ""
set_color(COLOR)
while choice != "5" or choice.lower() == "quit":
    clear()
    print """
    --> Astral <--
    
    1) New Game
    2) Load Game
    3) Options
    4) Instructions
    5) Quit
    """
    choice = raw_input(":")
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
        for player in range(options[3]):
            exec "player%i = Player(options[5][player][1], options[5][player][0], gold = options[2])" % (player + 1)
            
        game = True
        clear()
################################################################################
    elif choice == "2":
        print "Under construction!" # if game is loaded 
################################################################################
    elif choice == "3":
        options_menu()
################################################################################   
    elif choice == "4":
        #instructions for the game
        help_menu("help")
################################################################################
    elif choice == "5" or choice.lower() == "quit":
        if raw_input("Are you sure you wish to quit?\n(Y/N)\n:").lower() == "n":
            choice = ""
        game = False
################################################################################
    if game:
        
        #only for testing
        player1.add_building(BUILDING["Wizards Cottage"], 2, 2)
        player1.add_building(BUILDING["Village"], 4, 4)
        field.setcell(2, 2, "1")
        field.setcell(4, 4, "1")
        player2.add_building(BUILDING["Astral Line"], 2, 3)
        field.setcell(2, 3, "2")
        player1.gold = 500
        player2.add_building(BUILDING["Astral Line"], 3, 2)
        field.setcell(3, 2, "2")
        #only for testing
        
        #gameplay, options file is in this format:
            # [0] field size, (x)
            # [1] field size, (y)
            # [2] starting gold
            # [3] # of players
            # [4] possible colors, each divided by " - " and in the form "COLOR NAME<>Code"
            # [5] previously used players, each divided by " - " and in the form "PLAYER NAME<>COLOR NAME"
    
        choice = ""
        player = 1
        # Loop for all players
        
        continue_option = False
        
        while choice != "quit" and choice != "q" and choice != "exit":         
            # First Show Field
            ####################################################################
            clear()
            
            for y_value in range(field.sizex()):
                #changes numbers to be with 0 at the bottom
                print "\n%i" % (field.sizex() - y_value - 1),
                print " " * ( 2 - len(str(int(options[0]) - y_value - 1))),
                for x_value in range(field.sizey()):
                    # iff there is a building add its symbol
                    if field.cell(x_value,y_value) != "":
                        play = int(field.cell(x_value,y_value))
                        # for Astral Lines
                        exec "build_type =player%i.buildings[(%i,%i)]['TYPE']" % (play, x_value, y_value)
                        sym = " "
                        if "AL" in build_type and ((x_value % 2 == 0 and y_value % 2 != 0) or (x_value % 2 != 0 and y_value % 2 == 0)):
                            exec "sym = player%i.buildings[(%i,%i)]['SYMB']" % (play, x_value, y_value)
                            exec "set_color(color_num(player%i.color))" % (play)
                            if (x_value % 2 == 0 and y_value % 2 != 0):
                                sym = sym[0]
                            elif (x_value % 2 != 0 and y_value % 2 == 0):
                                sym = sym[1]
                        # for buildings
                        elif "B" in build_type and x_value % 2 == 0 and y_value % 2 == 0:
                            exec "sym = player%i.buildings[(%i,%i)]['SYMB']" % (play, x_value, y_value)
                            exec "set_color(color_num(player%i.color))" % (play)
                        print sym,
                        print "",
                        set_color(COLOR)
                    #if there is no building add 'empty' symbols for each square
                    elif x_value % 2 == 0 and y_value % 2 == 0:
                        # location for buildings
                        print "#",
                        print "",
                    elif x_value % 2 != 0 and y_value % 2 != 0:
                        # location for nothing...
                        print " ",
                        print "",
                    else:
                        # location for empty astral lines
                        print ".",
                        print "",
            
            # adds bottom numbers
            print "\n\n   ",
            for x_value in range(field.sizey()):
                print str(x_value) + " " * (2 - len(str(x_value))),

            # player information, gold, color, whose turn it is
            print "\n"
            exec "player_color = player%i.color" % (player)
            exec "cur_gold = player%i.gold" % (player)
            exec "player_name = player%i.name" % (player)
                
            print "    %s  -  MP: %i  - " % (player_name, cur_gold),
            
            set_color(color_num(player_color))
            print "COLOR"
            set_color(COLOR)
            
            # possible choice for player input
            ####################################################################
            if not continue_option:
                print "\n"
                print "\nType 'help' for general help with the game"
                choice = raw_input(": ").lower()
              
            # if one of the menu's need the map shown, all must end with "continue_option = False" and "choice = ''"
            ####################################################################
            elif continue_option == "build":
                choice = ""
                print "got here"
                while choice != "cancel":
                    
                    print "%i) %s  - " % (item + 1, name),
                    print BUILDING[ name ]["COST"],
                    print "MP"
                    
                    choice = raw_input("(Type 'cancel' to quit)\n(format: 'x,y')\nSelect Place to Build: ").lower()
                    choice = choice.split(",")
                    # check if input was correct
                    can_build = False
                    if len(choice) == 2 and choice[0].isdigit() and choice[1].isdigit():
                        if field.cell(int(choice[0]), int(choice[1])) == "":
                            if "B" in BUILDING[temp]["TYPE"] and choice[0] % 2 == 0 and choice[1] % 2 == 0:
                                can_build = True
                            if "AL" in BUILDING[temp]["TYPE"] and ((choice[0] % 2 != 0 and choice[1] % 2 == 0) or (choice[0] % 2 == 0 and choice[1] % 2 != 0)):
                                can_build = True
                            # it needs to check for where you can actually build
                            # currently only checks if the square is occupied and if it is the same type of building

                        if not can_build:
                            set_color(12)
                            print "Square Not Possible"
                            set_color(COLOR)
                        
                        if can_build:
                            exec "player%i.gold -= BUILDING[name]['COST']" % (player)
                            exec "player%i.add_building(BUILDING[name], choice[0], choice[1])"
                            field.setcell(choice[0], choice[1], player)
                        
                    else:
                        set_color(12)
                        print "Wrong Format"
                        set_color(COLOR)
                    
                choice = ""
                continue_option = False
            
            ####################################################################
            if choice[:4] == "help":
                help_menu(choice)
            
            #Build Menu
            ####################################################################
            elif choice == "build":
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
                        if BUILDING[ temp[int(build_choice) - 1] ]["COST"] < cur_gold:
                            print "1) Build"
                        else:
                            set_color(12)
                            print "--> NOT ENOUGH MANA <--"
                            set_color(COLOR)
                        print "0) Cancel"
                        build_choice = raw_input("\n: ").lower()
                        if build_choice == "1" and BUILDING[name]["COST"] < cur_gold:
                            continue_option = "build"
                            build_choice = "0"
            
            #Console
            ####################################################################
            elif choice == "~" and raw_input("There is NO console in this game\n:Press Enter to Continue:") == "~":
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
                    try:exec console_choice
                    except:print "Error!\n"
                clear(100)
                    
            #End Turn
            ####################################################################
            elif choice == "end turn":
                player += 1
                if player > int(options[3]):
                    player = 1
                exec "items = player%i.building.copy()" % (player)
                mana_gain = 0
                for item in items:
                    if items[item]["MP"].isdigit():
                        mana_gain += items[item]["MP"]
                    else:
                        try:exec items[item]["MP"]
                        except:pass
                exec "player%i.gold += mana_gain" % (player)
                # add next players Mana, end of turn effects etc.
        
        