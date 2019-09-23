import sys

class Prims: 
    def printMST(self, MST, vertices, adjacencyMatrix):
        print ("Edge \tWeight")
        for i in range(1, vertices):
            print (chr(MST[i]+65) + chr(i+65))
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def getMinimumKey(self, weight, visited, vertices):
        # initialize the min by infinite number
        min = sys.maxsize

        for i in range(vertices):
            # Find the edge with minimum weight if it not visited
            if weight[i] < min and visited[i] == False:
                min = weight[i]
                minIndex = i

        # Return the index of the found edge with minimum weight
        return minIndex
  
    # Function to construct and print MST for a graph  
    # represented using adjacency matrix representation 
    def primsAlgo(self, vertices, adjacencyMatrix):
        weight = [sys.maxsize] * vertices     # This list will be used for storing the weights of all vertices
        MST = [None] * vertices        # This will contain our minimum spanning tree
        weight[0] = 0                       # Weight of the root node will be 0
        visited = [False] * vertices
        MST[0] = -1                         # Choosing first node as root vertex
        orderArray = []

        for _ in range(vertices):
            minIndex = self.getMinimumKey(weight, visited, vertices)
            # mark the index as visited
            visited[minIndex] = True
            for vertex in range(vertices):
                if adjacencyMatrix[minIndex][vertex] > 0 and visited[vertex] == False and \
                weight[vertex] > adjacencyMatrix[minIndex][vertex]:
                    weight[vertex] = adjacencyMatrix[minIndex][vertex]
                    MST[vertex] = minIndex 
        for i in range(1, vertices):
            edge = chr(MST[i]+65) + chr(i+65)
            orderArray.append(edge)
        return orderArray