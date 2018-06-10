mapOfGTU = {
1 : set([2,3]),
2 : set([1,3,4]),
3 : set([1,2,4]),
4 : set([3,2]),
5 : set([6]),
6 : set([5])
} # graph is initialized as dictionary


#This function is my breaf first search algorithm
def myBfs(graph,key):
    visitVertexes=[] # to keep results
    visitVertexes.append(key) #get key
    keyEdges=graph[key]
    for x in keyEdges:
        visitVertexes.append(x) # get key's sets
    size=len(graph)
    for i in range(1,size+1): # search all vertexes of graph and append edges
        tempList=graph[i]
        for j in tempList:
            if visitVertexes.count(j)>0: # if a vertex has a same edge with key
                if i not in visitVertexes:
                    visitVertexes.append(i) # if edge is not in the result list
    visitVertexes.sort() #sort the list
    return visitVertexes

def findMinimumCostToLabifyGTU(x,y,mapOfGtu):
    # check that the graph is empty
    if(len(mapOfGTU) == 0): 
        print("Empty graph!")
        return -1
    # if cost of building a lab is less than repairing a road ; 
    # build a lab for every vertex
    if(y > x):
        return (len(mapOfGTU) * x) # total = num of vertexes * cost of building a lab
    
    size=len(mapOfGTU) # get num of vertexes
    numRoads=0 # to keep num of repairing roads
    numLabs=0 # to keep num of building labs
    
    vertexesList=list(mapOfGTU.keys()) # get list of all vertexes
    
    control=0
    while control<size:
        tempKey=vertexesList.pop(0) # get first vertex
        tempList=list(myBfs(mapOfGTU,tempKey)) # get edges with vertex
        if control < max(tempList): # check that last vertex
            numLabs+=1
            numRoads+=(len(tempList)-1)
        control=max(tempList) # get second vertex(! other component graph's first vertex)

    return (numLabs*x)+(numRoads*y) # calculete and return minimum cost

print ("Minimum Cost:",findMinimumCostToLabifyGTU(5,2,mapOfGTU));

















