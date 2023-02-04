class Crawler:
    
    def __init__(self, position):
        self.position = position
        self.visited = {position}
    
    def updatePosition(self,newPosition):
        self.position = newPosition
        self.visited.add(newPosition)

    def getXPosition(self):
        return self.position[0]
    
    def getYPosition(self):
        return self.position[1]
    
    def getPossibleDirections(self,environment):
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
