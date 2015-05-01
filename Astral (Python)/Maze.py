class Maze():
    
    def __init__(self, maze):
        maze = maze.split("\n")
        self.maze = []
        self.max_line = 0
        for line in maze:
            if len(line) > self.max_line:
                self.max_line = len(line)
        for line in maze:
            if len(line) < max:
                line += " " * ( self.max_line - len(line) )
            self.maze.append(list(line))
        self.points = {}
            
    def show(self):
        print "\n\n"
        for y_val in range(len(self.maze)):
            print str(len(self.maze) - y_val - 1) + " " * (3 - len(str(len(self.maze) - y_val - 1))),
            for x_val in range(len(self.maze[y_val])):
                print str(self.maze[y_val][x_val]) + " " * (3 - len(str(self.maze[y_val][x_val]))+ (self.column_size(x_val)-1) ),
            print "\n",
        print "   ",
        for num in range(len(self.maze[0])):
            print str(num) + " " * (3 - len(str(num))+ (self.column_size(num)-1) ),
        print " "
    
    def cell(self, x_val, y_val):
        if x_val >= self.sizex() or x_val < 0:
            return ""
        if y_val >= self.sizey() or y_val < 0:
            return ""
        return self.maze[len(self.maze) - y_val - 1][x_val]
    
    def setcell(self, x_val, y_val, value):
        self.maze[len(self.maze) - y_val - 1][x_val] = value
        
    def __str__(self):
        string = ""
        for y_val in range(len(self.maze)):
            for x_val in range(len(self.maze[y_val])):
                string += str(self.maze[y_val][x_val])
            if y_val != len(self.maze) - 1:
                string += "\n"
        return string
    
    def sizey(self):
        return len(self.maze)
    
    def sizex(self):
        return len(self.maze[0])
    
    def area(self):
        return self.sizex() * self.sizey()
    
    """def __getslice__(self, start_y, end_y):
        temp = []
        self.maze.reverse()
        for line in range(start_y, end_y):
            temp += self.maze[line]
        self.maze.reverse() 
        def __getslice__(self, start_x, end_x):
            return temp[start_x:end_x]       
        return temp"""
    
    def newpoint(self, symbol):
        symbol = str(symbol)
        self.maze.reverse()
        for y_val in range(len(self.maze)):
            line = self.maze[y_val]
            if symbol in line:
                self.points[symbol] =(self.maze[y_val].index(symbol), y_val)
        self.maze.reverse()
            
    def point(self, symbol):
        symbol = str(symbol)
        return self.points[symbol]
    
    def addrow(self, y_val):
        pass
    
    def addcolumn(self, x_val):
        pass
    
    def column_size(self,x_val):
        max_size = 0
        for loc in range(self.sizey()):
            if len(str(self.maze[loc][x_val])) > max_size:
                max_size = len(str(self.maze[loc][x_val]))
        return max_size
    
    def row_size(self, y_val):
        return len(self.maze[y_val])
    
    def clear(self, x_val, y_val, value = "#"):
        """Maze.clear(...) --> None
        Changes every cell in the maze to value, the maze is changed to dimensions of x_val * y_val."""
        maze = ""
        for loop in range(y_val):
            maze += (str("#") * x_val) + "\n"
        self.__init__(maze[:-1])
        for y_val in range(self.sizey()):
            for x_val in range(self.sizex()):
                self.setcell(x_val,y_val,value)