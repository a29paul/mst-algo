from Graph import Graph
from Matrix import Matrix
from Graph import Vertex
from Prims import Prims
class Client:
    def createMSTWithCoordinates(self, coordinateDict):
        matrix = Matrix()
        graph = Graph()
        prims = Prims()
        weightsAndEdges = matrix.createWeightsAndEdges(coordinateDict)
        weights = weightsAndEdges[1]
        edges = weightsAndEdges[0]
        for i in range(ord('A'), ord('A') + len(coordinateDict) ):
            graph.add_vertex(Vertex(chr(i)))
        i = 0
        for edge in edges:
            graph.add_edge(edge[:1], edge[1:], weights[i])
            i+=1
        adjacencyMatrix = graph.returnAdjacencyMatrix()
        MST = prims.primsAlgo(len(coordinateDict), adjacencyMatrix)
        return MST
    def arrayOrdering(self, MST):
        orderArray = []
        firstInSequence = ''
        while(len(orderArray)<len(MST)):
            if len(orderArray) == 0:
                orderArray.append(min(MST))
                firstInSequence = min(MST)[1:]
            else: 
                for x in MST:
                    if x[:1] == firstInSequence:
                        orderArray.append(x)
                        firstInSequence = x[1:]
        return orderArray
    def returnFinalOrderedArray(self, MST):
        orderedArray = self.arrayOrdering(MST)
        newArray = []
        for x in orderedArray:
            newArray.append(x[:1])
            newArray.append(x[1:])

        finalArray = []
        for x in range(len(newArray)):
            if x==0 or x==len(newArray)-1:
                finalArray.append(newArray[x])
            elif x%2==0:
                finalArray.append(newArray[x])
        return finalArray
