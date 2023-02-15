import pickle 
from level import Level
from matplotlib import pyplot as plt
import heapq
import time
import statistics

#TODO: Optimize Forward A to make it run faster.
#TODO: Write forwardA with different tie breaking
#TODO: Write 


#Breaks ties in favor of nodes with larger G values
class Node:

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        
        self.f = 0
        self.g = 0
        self.heuristic = 0

    #So we can see if nodes are already in the list.
    def __eq__(self, other):
        return self.position == other.position

    #for heap queue sorting. Tie breaking too.
    def __lt__(self, other):
        if(self.f == other.f):
            return self.g > other.g
        return self.f < other.f
    
    #for heap queue sorting. Tie breaking too.
    def __gt__(self, other):
        if(self.f == other.f):
            return self.g < other.g
        return self.f > other.f
    

#Breaks ties in favor of nodes with larger G values.
#class Node2:

def unpickle50Levels(levels):    
    with open('levels.pickle', 'rb') as file:
        for x in range(50):
            currentLevel: Level = pickle.load(file)
            levels.append(currentLevel)

def loadSpecificLevel(levels, levelSelectNum):
    print('Loading level ', levelSelectNum, ".", sep='')
    return levels[levelSelectNum]

def displayLevel(incomingLevel):
    plt.imshow(incomingLevel.array)
    plt.show()

def computePath(currentNode):
    retrace = currentNode
    pathList = []
    while retrace is not None:
        pathList.insert(0, retrace.position) #Insert at start of the pathList list.
        retrace = retrace.parent
    return pathList

def forwardA(array, start, goal):

    startNode = Node(None, start)
    startNode.g = startNode.heuristic = startNode.f = 0
    goalNode = Node(None, goal)

    directions = (0, -1), (0, 1), (-1, 0), (1, 0) #Directions we can move in.
    openList = []
    heapq.heapify(openList) 
    heapq.heappush(openList, startNode)
    closedList = []

    while len(openList) > 0:  
    
        currentNode = heapq.heappop(openList)
        closedList.append(currentNode)
        #If we found the goal!
        if currentNode.position == goalNode.position:
            return computePath(currentNode)
        
        neighbors = []  
        for movement in directions: 
            node_position = (currentNode.position[0] + movement[0], currentNode.position[1] + movement[1])
            if node_position[0] < 101 and node_position[0] > -1 and node_position[1] < 101 and node_position[1] > -1 and array[node_position[0]][node_position[1]] == 0: #if open square
                newNode = Node(currentNode, node_position)
                neighbors.append(newNode)
            
        for node in neighbors:
            if len([closed_child for closed_child in closedList if closed_child == node]) > 0:
                continue

            node.g = currentNode.g + 1
            node.heuristic = abs(node.position[0] - goalNode.position[0]) + abs(node.position[1] - goalNode.position[1]) #manhattan is usually slower in diagonal map.
            #node.heuristic = ((node.position[0] - goalNode.position[0]) ** 2) + ((node.position[1] - goalNode.position[1]) ** 2)
            node.f = node.g + node.heuristic
            
            if node in openList: 
                idx = openList.index(node) 
                if node.g < openList[idx].g:
                    # update the node in the open list
                    openList[idx].g = node.g
                    openList[idx].f = node.f
                    openList[idx].h = node.heuristic
            else:
                # Add the node to the open list
                heapq.heappush(openList, node)

    print("No path between start and end seen.")
    return None

#def forwardA(array, start, goal):
    pass
def main():
    levels = []
    unpickle50Levels(levels)
    
    levelSelectNum = input("What level from 0-49 should be loaded? ")
    currentLevelSelection = loadSpecificLevel(levels, int(levelSelectNum))

    #TERRAIN IS YELLOW, ITS THE 1s. IT IS LIKE A LINE, OPEN SPACES TEND TO BE MORE ROUND. DOUBLE CHECK THE DISPLAY.
    displayLevel(currentLevelSelection)

    #COORDINATES ARE FLIPPED FROM WHAT IT LOOKS LIKE ON THE PLOT DISPLAY. ENTER AS Y,X !!!!!!!!!!!!!!!!!!
    start = (0, 0)
    goal = (100, 100)
    path = forwardA(currentLevelSelection.array, start, goal)


# call the function fifty times and record the time taken for each call
#     times = []
#     for i in range(2):
#         start_time = time.time()
#         x = loadSpecificLevel(levels, int(levelSelectNum))
#         path = forwardA(x.array, start, goal)
#         end_time = time.time()
#         times.append(end_time - start_time)
# #12.7111 seconds average


#     # calculate the average and standard deviation of the time taken
#     average_time = statistics.mean(times)
#     standard_deviation = statistics.stdev(times)

# print the results
    #print(f"Average time taken: {average_time:.4f} seconds")
    #print(f"Standard deviation: {standard_deviation:.4f} seconds")

    arrayWithPath = currentLevelSelection.array
    if path is not None:
        for i in path:
            x = i[0]
            y = i[1]
            arrayWithPath[x][y] = 0.5
    

    displayLevel(currentLevelSelection)
    #print(path)

if __name__ == "__main__":
    main()