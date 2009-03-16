from SaveLoad import *
# use this line to uncipher a file, then edit it and use the other line to cipher it again
savegame("Auto Save-2" ,loadgame("Auto Save.sav", tocipher = True), tocipher = False)
# use the this line to cipher it again
#savegame("Auto Save-3" , loadgame("Auto Save-2", tocipher = False), tocipher = True, ext = ".sav")