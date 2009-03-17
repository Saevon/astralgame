from INFO import BUILDING
from INFO import RESEARCH

class Player():
    
    live_players = []

    def __init__(self, instance_name, color, name, gold = 0, allies = [], research = {}, attacks = {}, buildings = {}, build_list = {}, turn = 0, score = 0):
        Player.live_players.append(instance_name)
        self.instance = instance_name
        self.gold = gold
        self.color = color
        self.name = name
        self.allies = allies
        self.research = research.copy()
        self.attacks = attacks.copy()
        self.buildings = buildings.copy()
        self.build_list = build_list.copy()
        self.turn = turn
        self.score = score

    def add_ally(self, player):
        self.allies.append(player)
        self.allies.sort()

    def remove_ally(self,player):
        if player in self.allies:
            self.allies.remove(player)
        
    def dest_building(self, x_loc, y_loc):
        """dest_building(...) --> None
        The Building at (x_loc, y_loc) is removed from this players buildings
        x_loc, y_loc are int"""
        
        if (x_loc, y_loc) in self.buildings.keys():
            temp = self.buildings[ (x_loc, y_loc) ]["NAME"]
            if len(self.build_list[temp]) != 1:
                self.build_list[temp].remove( (x_loc, y_loc) )
            else:
                self.build_list.pop(temp)
            self.buildings.pop( (x_loc, y_loc) )
        
    def add_building(self, build, x_loc, y_loc):
        """add_building(...) --> None
        The Building at (x_loc, y_loc) is added to this players buildings
        x_loc, y_loc are int"""
        
        self.dest_building(x_loc, y_loc)
        self.buildings[ (x_loc, y_loc) ] = build
        try:
            self.build_list[ build["NAME"] ].append( (x_loc, y_loc) )
        except:
            self.build_list[ build["NAME"] ] = [ (x_loc, y_loc) ]
       
    def capt_building(self, x_loc, y_loc, enemy):
        """capt_building(...) --> None
        Your building at (x_loc, y_loc) is captured by enemy
        x_loc, y_loc are int
        enemy is a str"""
        
        if (x_loc, y_loc) in enemy.buildings.keys():
            build = enemy.buildings[ (x_loc, y_loc) ].copy()
            enemy.dest_building(x_loc, y_loc)
            self.add_building(build, x_loc, y_loc)
            
    def poss_research(self, include_special = False):
        """poss_research(...) --> list
        Returns all possible research items whoses pre-requisites have been met.
        Unless they have 'SPECIAL' in them"""
        possible = []
        for item in RESEARCH:
            if "SPECIAL" not in item or include_special:
                is_pos = True
                for prequisite in RESEARCH[item]["PRE"]:
                    if is_pos:
                        if " OR " in prequisite:
                            temp = prequisite.split(" OR " )
                            is_pos = False
                            for or_pre in temp:
                                if or_pre in self.build_list.keys() or or_pre in self.research:
                                    is_pos = True
                        elif (prequisite not in self.build_list.keys() and prequisite not in self.research) or item in self.research:
                            is_pos = False
                if is_pos:
                    possible.append(item.strip('"').strip("'"))
        return possible
    
    def poss_building(self):
        """poss_building(...) --> list
        Returns all possible buildings whose pre-requisites have been met"""
        possible = []
        for item in BUILDING:
            is_pos = True
            for prequisite in BUILDING[item]["PRE"]:
                for prequisite in BUILDING[item]["PRE"]:
                    if is_pos:
                        if " OR " in prequisite:
                            temp = prequisite.split(" OR " )
                            is_pos = False
                            for or_pre in temp:
                                if or_pre in self.build_list.keys() or or_pre in self.research:
                                    is_pos = True
                        elif (prequisite not in self.build_list.keys() and prequisite not in self.research) or item in self.research:
                            is_pos = False
            if is_pos:
                possible.append(item.strip('"').strip("'"))
        return possible
    
    def isalive(self):
        if len(self.build_list) < 1:
            for i in range(Player.live_players.count(self.instance)):
                Player.live_players.remove(self.instance)
            return False
        else:return True
    
    
    
if __name__ == "__main__":
    player1 = Player(1, "Red", "SirJ")
    player1.add_building({"NAME" : "House", "RES" : 10, "PRE" : []}, 10, 10)
    player1.add_building({"NAME" : "Village", "RES" : 10, "PRE" : []}, 9, 10)
    player1.add_building({"NAME" : "Wizard Tower", "RES" : 10, "PRE" : []}, 6, 7)
    player1.add_building({"NAME" : "Void Crystal", "RES" : 10, "PRE" : []}, 4, 7)
    player1.add_building({"NAME" : "Mining Camp", "RES" : 10, "PRE" : []}, 1, 2)
    player2 = Player(2, "Red", "SirJ")
    player2.capt_building( 10, 10, player1)
    
    print player1.build_list
    print player2.buildings
    print "----------"
    
    print player1.poss_research(include_special = True)
    print player1.poss_building()
    