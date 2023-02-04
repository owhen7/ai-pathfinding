#For now this method might only load one environment.
def unpickle50Levels():
    print("Unpickling all 50 Environments from the environemnts.pickle file and storing them.")
    
    #Code to unpickle stuff right here
    #with open('enviroments.pickle', 'rb') as file:
    #copy: Environment = pickle.load(file)

def loadSpecificLevel(levelSelect):
    print("TODO: This function will load a specific level into a different working array or something.")
    print('Loading level ', levelSelect, "...", sep='')

def displayLevel():
    #This function displays a single enviroment in a GUI.
    #Obviously loadSpecificLevel must work before display level does.
    print("This does nothing right now but it will print the current, working level eventually.")
    
def main():
    #unpickle50Levels()
    levelSelect = input("What level from 0-49 should be loaded? ")
    loadSpecificLevel(int(levelSelect))
    #displayLevel()

if __name__ == "__main__":
    main()