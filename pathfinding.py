import pickle 
from level import Level

def unpickle50Levels(levels):    
    with open('levels.pickle', 'rb') as file:
        for x in range(50):
            currentLevel: Level = pickle.load(file)
            levels.append(currentLevel)


def loadSpecificLevel(levels, levelSelectNum):
    print('Loading level ', levelSelectNum, "...", sep='')
    return levels[levelSelectNum]

def displayLevel():
    #This function displays a single enviroment in a GUI.
    #Obviously loadSpecificLevel must work before display level does.
    print("This does nothing right now but it will print the current, working level eventually.")
    
def main():
    levels = []
    unpickle50Levels(levels)
    
    levelSelectNum = input("What level from 0-49 should be loaded? ")
    levelSelect = loadSpecificLevel(levels, int(levelSelectNum))

    levelSelect.describe_level()






if __name__ == "__main__":
    main()