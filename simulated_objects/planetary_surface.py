import math
class PlanetarySurface:
    """ Planetary Surface of 500km x 500km """
    def __init__(self):
        self.craters = {}
        self.total_craters = {}


    #Removes crater from surface
    def _obliterate_crater(self, crater):
        del self.craters[crater]


    #Returns list of craters that should be obliterated
    def _find_obliterated_craters(self, new_crater):
        obliterated_craters = []

        #Check if other craters are within cover radius
        cover_radius = new_crater.get_covering_radius()
        for crater in self.craters:
            if cover_radius > self._get_distance(crater, new_crater):
                obliterated_craters.append(crater)

        return obliterated_craters


    #Calculate Distance between crater centers
    def _get_distance(self, crater1, crater2):
        x1, y1 = crater1.get_location()
        x2, y2 = crater2.get_location()
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


    #Adds a crater to the surface
    def add_crater(self, crater):
        craters_to_obliterate = self._find_obliterated_craters(crater)

        #Remove all craters
        for obliterated in craters_to_obliterate:
            self._obliterate_crater(obliterated)

        #Add new crater to dictionary
        self.craters[crater] = crater.get_location()
        self.total_craters[crater] = crater.get_location()


    #Gives a list of all craters and locations
    def get_current_craters(self):
        return self.craters


    #Get Number of craters on surface
    def crater_density(self):
        return len(self.craters)


    #Gets all craters
    def get_all_craters(self):
        return self.total_craters
