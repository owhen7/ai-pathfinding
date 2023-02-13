import pickle 
from level import Level
from matplotlib import pyplot as plt
import heapq

class Node:

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        
        self.f = 0
        self.g = 0
        self.heuristic = 0


    def __eq__(self, other):
        return self.position == other.position
    
    def __repr__(self):
        return f"{self.position} - g: {self.g} heuristic: {self.heuristic} f: {self.f}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
        return self.f < other.f
    
    # defining greater than for purposes of heap queue
    def __gt__(self, other):
        return self.f > other.f
    
#Courtesy of ChatGPT - can edit this. This would be extra points and isn't currently implemented.
#It actually would have to be from scratch so it wouldn't even be enough. But we can come back to it.
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

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
    goalNode.g = goalNode.heuristic = goalNode.f = 0

    openList = []
    closedList = []

    heapq.heapify(openList) 
    heapq.heappush(openList, startNode)

    outer_iterations = 0
    max_iterations = (101 * 101)
    #max_iterations = (101 * 101 // 2)

    while len(openList) > 0:
        outer_iterations += 1
        if outer_iterations > max_iterations:
            # if we hit this point return the path such as it is
            # it will not contain the destination
            print("giving up on pathfinding too many iterations")
            return computePath(currentNode)       
    
        #Move node from openList to closedList and begin work.
        currentNode = heapq.heappop(openList)
        closedList.append(currentNode)
        #If we found the goal!
        if currentNode.position == goalNode.position:
            return computePath(currentNode)
        
        neighbors = []  
        #Look to the four cardinal directions,
        for movement in ((0, -1), (0, 1), (-1, 0), (1, 0)): 
            node_position = (currentNode.position[0] + movement[0], currentNode.position[1] + movement[1])
            if not (node_position[0] > 100 or node_position[0] < 0 or node_position[1] > 100 or node_position[1] < 0):
                if array[node_position[0]][node_position[1]] == 0: #if not terrain
                    newNode = Node(currentNode, node_position)
                    neighbors.append(newNode)
            
        for node in neighbors:
            if len([closed_child for closed_child in closedList if closed_child == node]) > 0:
                continue

            node.g = currentNode.g + 1

            #This manhattan one is correwct and has a better path but its way way slower than the traditional formula.
            node.heuristic = abs(node.position[0] - goalNode.position[0]) + abs(node.position[1] - goalNode.position[1]) 
            #node.heuristic = ((node.position[0] - goalNode.position[0]) ** 2) + ((node.position[1] - goalNode.position[1]) ** 2)
            node.f = node.g + node.heuristic
            
            # Make sure the node isn't already in the openlist.
            if len([open_node for open_node in openList if node.position == open_node.position and node.g > open_node.g]) > 0:
                continue

            heapq.heappush(openList, node)

    print("There was no path between the two points.")
    return None

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

    arrayWithPath = currentLevelSelection.array
    if path is not None:
        for i in path:
            x = i[0]
            y = i[1]
            arrayWithPath[x][y] = 0.5 #Should be a number between 0 and 1 because of the way the plot software chooses colors. Otherwise the colors change.
    
    displayLevel(currentLevelSelection)
    #print(path)

if __name__ == "__main__":
    main()