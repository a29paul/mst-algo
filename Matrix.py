from Haversine import Haversine
class Matrix:
    def createMemoryMatrix(self, n):
        memoryMatrix = []
        for i in range(n):
            rowList = []
            for j in range(n):
                rowList.append(0)
            memoryMatrix.append(rowList)
        return memoryMatrix
    def createWeightsAndEdges(self, coordinateDict):
        haversine = Haversine()
        memoryMatrix = self.createMemoryMatrix(len(coordinateDict))
        edges = []
        weights = []
        edgesAndWeights = []
        for i in range(len(coordinateDict)):
            for j in range(len(coordinateDict)):
                firstPointer = len(coordinateDict)-(i+1)
                secondPointer =  len(coordinateDict)-(j+2)
                listOfCoordinates = list(coordinateDict.items())
                vertex1 = listOfCoordinates[firstPointer][0]
                vertex2 = listOfCoordinates[secondPointer][0]
                lat1 = listOfCoordinates[firstPointer][1][0]
                lng1 = listOfCoordinates[firstPointer][1][1]
                lat2 = listOfCoordinates[secondPointer][1][0]
                lng2 = listOfCoordinates[secondPointer][1][1]
                if vertex1 != vertex2:
                    if memoryMatrix[secondPointer][firstPointer] != 1 and  memoryMatrix[firstPointer][secondPointer] != 1:
                        edges.append(vertex1+vertex2) 
                        weights.append(haversine.distanceInKm(lat1,lng1, lat2, lng2))
                        memoryMatrix[secondPointer][firstPointer] = 1
                        memoryMatrix[firstPointer][secondPointer] = 1
        edgesAndWeights.append(edges)
        edgesAndWeights.append(weights)
        return edgesAndWeights