#This script generates 50 different levels, of class type Level, which are 101 x 101 grids of blocks that either have terrain or do not.
#The terrain needs to be generated according to a certain algorithm.
#This code will theoretically be ran only one time.
from level import Level
from crawler import Crawler
import pickle
from random import *

def pickle50Levels():
    print("TODO: This function will Generate 50 levels and then pickle them.")
    with open('levels.pickle', 'wb') as file:
            for x in range(50):
                print(x)
                currentLevel: Level = Level(x)
                generateLevelTerrain(currentLevel); #Generate Random Terrain.
                currentLevel.describe_level()   #Makeshift print
                pickle.dump(currentLevel, file)

def generateLevelTerrain(currentLevel): #TODO: Rewrite this function according to the project specsheet. @Owen
    print("TODO: Generate Terrain for each level in this function. Terrain should be indicated with a 1.")
    currentLevel.array = [[1 for x in range(101)] for y in range(101)]
    crawlers = []
    for twohundred in range(200):  #Adding 200 crawlers
        xValue = randint(0,100)
        yValue = randint(0,100)
        while Crawler((xValue,yValue)) in crawlers: #Check if starting position is occupied by other crawler
            xValue = randint(0,100)
            yValue = randint(0,100)
        currCrawler = Crawler((xValue,yValue))
        crawlers.append(currCrawler)
        currentLevel.array[xValue][yValue] = 0 #Set starting position equal to terrain
    while crawlers: #While there are still crawlers
        crawlerIndex = randint(0,len(crawlers) -1) #Randomly choose a crawler to move
        directions = crawlers[crawlerIndex].getPossibleDirections(currentLevel.array) #Check possible directions current crawler can make
        if not directions:
            crawlers.pop(crawlerIndex) #If crawler cannot move remove it
        else:
            randDirection = directions[randint(0, len(directions) - 1)] #If crawler can move choose a random direction where it will move
            match randDirection:
                #North
                case 0:
                    crawlers[crawlerIndex].updatePosition((crawlers[crawlerIndex].getXPosition(), crawlers[crawlerIndex].getYPosition() - 1))
                    
                #East
                case 1:
                    crawlers[crawlerIndex].updatePosition((crawlers[crawlerIndex].getXPosition() + 1, crawlers[crawlerIndex].getYPosition()))
                    
                #South
                case 2:
                    crawlers[crawlerIndex].updatePosition((crawlers[crawlerIndex].getXPosition(), crawlers[crawlerIndex].getYPosition() + 1))
                    
                #West
                case 3:
                    crawlers[crawlerIndex].updatePosition((crawlers[crawlerIndex].getXPosition() - 1, crawlers[crawlerIndex].getYPosition()))
                    
            if currentLevel.array[crawlers[crawlerIndex].getXPosition()][crawlers[crawlerIndex].getYPosition()] == 0: #Delete crawler if its moves into another crawler's path
                crawlers.pop(crawlerIndex)
            else:
                currentLevel.array[crawlers[crawlerIndex].getXPosition()][crawlers[crawlerIndex].getYPosition()] = 0 #Set crawler's current location to terrain










if __name__ == "__main__":
    pickle50Levels();