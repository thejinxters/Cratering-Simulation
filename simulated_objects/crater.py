class Crater:
    """ Crater Object with measurements stored in km """
    def __init__(self, location_x, location_y):
        # diameter of every crater is 50km
        self.diameter = 50
        self.radius = self.diameter/2
        self._calculate_ejecta()
        self._set_location(location_x, location_y)

    def __str__(self):
        x, y = self.get_location()
        return "Crater: \n\tx:" + str(x) + "\n\ty:" + str(y)

    #Calculate ejecta
    def _calculate_ejecta(self):
        # ejecta 20% larger than diameter
        self.ejecta_diameter = self.diameter*1.2
        self.ejecta_radius = self.ejecta_diameter/2


    #Set the location of the crater
    def _set_location(self, location_x, location_y):
        self.x = location_x
        self.y = location_y


    #Get the location of the crater
    def get_location(self):
        return (self.x, self.y)


    #Get covered radius
    def get_covering_radius(self):
        return self.ejecta_radius
