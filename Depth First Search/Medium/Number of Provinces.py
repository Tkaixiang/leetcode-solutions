class Solution:
    def visitCity(self, city: int, isConnected, visitedCities):
        if city in visitedCities:
            return

        visitedCities[city] = True

        currentCity = isConnected[city]
        for cityIndex in range(0, len(currentCity), 1):
            connection = currentCity[cityIndex]
            if connection == 0 or cityIndex == city:
                continue  # Not connected to this city or is the city itself

            self.visitCity(cityIndex, isConnected, visitedCities)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        numProvinces = 0

        visitedCities = {}
        for city in range(0, len(isConnected), 1):
            if city not in visitedCities:
                numProvinces += 1
                self.visitCity(city, isConnected, visitedCities)

        return numProvinces
