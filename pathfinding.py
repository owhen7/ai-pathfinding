import pickle 
from level import Level
from matplotlib import pyplot as plt

def unpickle50Levels(levels):    
    with open('levels.pickle', 'rb') as file:
        for x in range(50):
            currentLevel: Level = pickle.load(file)
            levels.append(currentLevel)

def loadSpecificLevel(levels, levelSelectNum):
    print('Loading level ', levelSelectNum, "...", sep='')
    return levels[levelSelectNum]

def displayLevel(incomingLevel):
    #There is probably a better way to print the map and the player out. This will do for now.
    plt.imshow(incomingLevel.array)
    plt.show()

def main():
    levels = []
    unpickle50Levels(levels)
    
    levelSelectNum = input("What level from 0-49 should be loaded? ")
    currentLevelSelect = loadSpecificLevel(levels, int(levelSelectNum))

    displayLevel(currentLevelSelect)

if __name__ == "__main__":
    main()