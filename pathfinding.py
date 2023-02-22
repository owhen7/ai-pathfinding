import pickle 
from level import Level
from matplotlib import pyplot as plt
import heapq
import time
import statistics

#TODO: Optimize Forward A to make it run faster.
#TODO: Write forwardA with different tie breaking
#TODO: Write 

#Node Tiebreak value to check. Can be either 1 or 2
TIEBREAK = 2

#1: Breaks ties in favor of nodes with smaller G values.
#2: Breaks ties in favor of nodes with larger G values.
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

    if TIEBREAK == 1:
        def __lt__(self, other):
            if(self.f == other.f):
                return self.g > other.g
            return self.f < other.f
    
        #for heap queue sorting. Tie breaking too.
        def __gt__(self, other):
            if(self.f == other.f):
                return self.g < other.g
            return self.f > other.f
        
    if TIEBREAK == 2:
        def __lt__(self, other):
                    if(self.f == other.f):
                        return self.g < other.g
                    return self.f < other.f
        def __gt__(self, other):
                if(self.f == other.f):
                    return self.g > other.g
                return self.f > other.f

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

def forwardA(array, start, goal, averageNodes):

    startNode = Node(None, start)
    #startNode.g = startNode.heuristic = startNode.f = 0
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
            averageNodes.append(len(closedList))
            return computePath(currentNode)
        
        neighbors = []  
        for x in directions: 
            node_position = (currentNode.position[0] + x[0], currentNode.position[1] + x[1])
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
    averageNodes.append(len(closedList))
    return None

def backwardA(array, start, goal, averageNodes):

    startNode = Node(None, goal)
    #startNode.g = startNode.heuristic = startNode.f = 0
    goalNode = Node(None, start)

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
            averageNodes.append(len(closedList))
            return computePath(currentNode)
        
        neighbors = []  
        for x in directions: 
            node_position = (currentNode.position[0] + x[0], currentNode.position[1] + x[1])
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
    averageNodes.append(len(closedList))
    return None
def adaptiveA(array, start, goal, averageNodes, mode, closedL):
    startNode = Node(None,start)
    goalNode = Node(None,goal)
    directions = (0, -1), (0, 1), (-1, 0), (1, 0) #Directions we can move in.
    openList = []
    heapq.heapify(openList) 
    heapq.heappush(openList, startNode)
    closedList = []
    while len(openList) > 0:  
        currentNode = heapq.heappop(openList)
        closedList.append(currentNode)
        if currentNode.position == goalNode.position:
            match mode:
                case 2:
                    averageNodes.append(len(closedList))
                    return computePath(currentNode)
                case 1:
                    for lNodes in closedList:
                        closedL.append(copy.copy(lNodes))
                    for cNodes in closedL:
                        cNodes.heuristic = currentNode.g - cNodes.g
                        cNodes.f = cNodes.g + cNodes.heuristic
                    return adaptiveA(array, start, goal, averageNodes, 2, closedL)
        
        neighbors = []  
        for x in directions: 
            node_position = (currentNode.position[0] + x[0], currentNode.position[1] + x[1])
            if node_position[0] < 101 and node_position[0] > -1 and node_position[1] < 101 and node_position[1] > -1 and array[node_position[0]][node_position[1]] == 0: #if open square
                newNode = Node(currentNode, node_position)
                neighbors.append(newNode)
        
        for node in neighbors:
            if len([closed_child for closed_child in closedList if closed_child == node]) > 0:
                continue
            
            if node in closedL:
                for n in closedL:
                    if node.position[0] == n.position[0] and node.position[1] == n.position[1]:
                        node.g = n.g
                        node.heuristic = n.heuristic
                        node.f = n.f
                        
            
            if node not in closedL:
                node.g = currentNode.g + 1
                node.heuristic = abs(node.position[0] - goalNode.position[0]) + abs(node.position[1] - goalNode.position[1])
                node.f = node.g + node.heuristic

            if node in openList: 
                idx = openList.index(node) 
                if node.g < openList[idx].g:
                    openList[idx].g = node.g
                    openList[idx].f = node.f
                    openList[idx].h = node.heuristic
            
            if node not in openList:
                heapq.heappush(openList, node)

    print("No path between start and end seen.")
    averageNodes.append(len(closedList))
    return None


def main():
    levels = []
    averageNodes = []
    unpickle50Levels(levels)
    
    levelSelectNum = input("What level from 0-49 should be loaded? ")
    currentLevelSelection = loadSpecificLevel(levels, int(levelSelectNum))

    #TERRAIN IS YELLOW, ITS THE 1s. IT IS LIKE A LINE, OPEN SPACES TEND TO BE MORE ROUND. DOUBLE CHECK THE DISPLAY.
    displayLevel(currentLevelSelection)

    #COORDINATES ARE FLIPPED FROM WHAT IT LOOKS LIKE ON THE PLOT DISPLAY. ENTER AS Y,X !!!!!!!!!!!!!!!!!!
    start = (0, 0)
    goal = (100, 100)
    #path = forwardA(currentLevelSelection.array, start, goal, averageNodes)
    
    #level 5:1: closed list was 936
    #level 5:2: closed list was 1967
    #level 31 for method 2: 6153
    
    times = []
    for i in range(50):
        x = loadSpecificLevel(levels, i)
        start_time = time.time()
        path = forwardA(x.array, start, goal,  averageNodes)
        end_time = time.time()
        times.append(end_time - start_time)
        

    average_time = statistics.mean(times)
    average_nodes = statistics.mean(averageNodes)
    standard_deviation = statistics.stdev(times)
    print(f"Average time taken: {average_time:.4f} seconds")
    print(f"Standard deviation: {standard_deviation:.4f} seconds")
    print(f"Average amount of nodes visited: {average_nodes:.4f}")
    
    

    averageNodesA = []
    timesA = []
    mode = 1
    for j in range(50):
        x = loadSpecificLevel(levels,j)
        start_timeA = time.time()
        path = adaptiveA(x.array, start, goal, averageNodesA, mode, [])
        end_timeA = time.time()
        timesA.append(end_timeA - start_timeA)
    average_timeA = statistics.mean(timesA)
    average_nodesA = statistics.mean(averageNodesA)
    standard_deviationA = statistics.stdev(timesA)
    print(f"Average time taken: {average_timeA:.4f} seconds")
    print(f"Standard deviation: {standard_deviationA:.4f} seconds")
    print(f"Average amount of nodes visited: {average_nodesA:.4f}")
    
    # Draw the path onto the array.
    # arrayWithPath = currentLevelSelection.array
    # if path is not None:
    #     for i in path:
    #         x = i[0]
    #         y = i[1]
    #         arrayWithPath[x][y] = 0.5
    
    # displayLevel(currentLevelSelection)
    #print(path) #print out tuples of the path

if __name__ == "__main__":
    main()