class Crawler:
    
    def __init__(self, position): #Initializes crawler by making its starting position as current position and adding that position to a visited set
        self.position = position
        self.visited = {position}
    
    def updatePosition(self,newPosition): #Replaced current position with new position and new position to visited set
        self.position = newPosition
        self.visited.add(newPosition)
 
    def getXPosition(self): #Returns x value of current position in array
        return self.position[0]
    
    def getYPosition(self): #Returns y value of current position in array
        return self.position[1]
    
    def getPossibleDirections(self,environment): #Returns array of possible directions crawler can move. Crawlers cannot move out of bounds or into spaces that they already visited
        directions = []
        #North Check
        if self.position[1] != 0 and (self.position[0], self.position[1] - 1) not in self.visited:
            directions.append(0)
        #East Check
        if self.getXPosition() != 100 and (self.position[0] + 1 , self.position[1]) not in self.visited:
            directions.append(1)
        #South Check
        if self.position[1] != 100 and (self.position[0], self.position[1] + 1) not in self.visited:
            directions.append(2)
        #West Check
        if self.getYPosition() != 0 and (self.position[0] - 1 , self.position[1]) not in self.visited:
            directions.append(3)
        return directions
