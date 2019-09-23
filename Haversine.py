import math
class Haversine:
    def distanceInKm(self, lat1, lng1, lat2, lng2):
        R = 6371000
        dLat = math.radians(lat2-lat1)
        dLon = math.radians(lng2-lng1)
        a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *  math.sin(dLon/2) * math.sin(dLon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)); 
        d = R * c
        return d