#This script generates 50 different levels, of class type Level, which are 101 x 101 grids of blocks that either have terrain or do not.
#The terrain needs to be generated according to a certain algorithm.

from level import Level
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
    currentLevel.array = [[randint(0, 1) for x in range(101)] for y in range(101)]

if __name__ == "__main__":
    pickle50Levels();