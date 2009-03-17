from SaveLoad import *
# use this line to uncipher a file, then edit it and use the other line to cipher it again
savegame("G" ,loadgame(raw_input(":"), tocipher = True), tocipher = False)
# use the this line to cipher it again
#savegame(raw_input(":") , loadgame("G", tocipher = False), tocipher = True, ext = ".sav")