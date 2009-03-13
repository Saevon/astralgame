from INFO import *

class Player():
    def __init__(self, color, name, gold = 0, allies = [], research = [], attacks = {}, buildings = {}, build_list = {}):
        self.gold = gold
        self.color = color
        self.name = name
        self.allies = allies
        self.research = research[:]
        self.attacks = attacks.copy()
        self.buildings = buildings.copy()
        self.build_list = build_list.copy()
        
    def add_ally(self, player):
        self.allies.append(player)
        self.allies.sort()

    def remove_ally(self,player):
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
            build = enemy.buildings[ (x_loc, y_loc) ]
            self.add_building(build, x_loc, y_loc)
            enemy.dest_building(x_loc, y_loc)
            
    def poss_research(self):
        """poss_research(...) --> list
        Returns all possible research items whoses pre-requisites have been met"""
        possible = []
        for item in RESEARCH:
            for prequisite in RESEARCH[item]["PRE"]:
                if prequisite in self.build_list.keys() or prequisite in self.research:
                    possible.append(item.strip('"').strip("'"))
                    break
            if len(RESEARCH[item]["PRE"]) == 0:
                possible.append(item.strip('"').strip("'"))
        return possible
    
    def poss_building(self):
        """poss_building(...) --> list
        Returns all possible research items whoses pre-requisites have been met"""
        possible = []
        for item in BUILDING:
            for prequisite in BUILDING[item]["PRE"]:
                if prequisite in self.build_list.keys() or prequisite in self.research:
                    possible.append(item.strip('"').strip("'"))
                    break
            if len(BUILDING[item]["PRE"]) == 0:
                possible.append(item.strip('"').strip("'"))
        return possible
    
    
    
if __name__ == "__main__":
    player1 = Player("Red", "SirJ", research = ['RESEARCH: Gem Mining'])
    player1.add_building({"NAME" : "House", "RES" : 10, "PRE" : []}, 10, 10)
    player1.add_building({"NAME" : "Village", "RES" : 10, "PRE" : []}, 9, 10)
    player1.dest_building(10,10)
    player2 = Player("Blue", "Dim")
    player2.add_building({"NAME" : "House", "RES" : 10, "PRE" : []}, 9, 10)
    player2.add_building({"NAME" : "House", "RES" : 10, "PRE" : []}, 6, 7)
    player2.add_building({"NAME" : "House", "RES" : 10, "PRE" : []}, 4, 9)
    player2.add_building({"NAME" : "Mining Camp", "RES" : 10, "PRE" : []}, 1, 2)
    player1.capt_building(4, 7, player2)
    
    print player1.build_list
    print player1.buildings
    print ""
    print player2.build_list
    print player2.buildings
    print "----------"
    
    print player2.poss_research()
    print player1.poss_building()