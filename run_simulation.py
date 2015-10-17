from utils import *
from simulated_objects import *
import time


def main():
    year, saturation, saturation_per_year = simulation()

    print "Years: " + str(year) + "000"
    print "Crater Saturation: " + str(saturation)
    print saturation_per_year


def simulation():
    #Create some uniformly random locations
    x_locations = UniformRandomNumbers(0, 500, 5000)
    y_locations = UniformRandomNumbers(0, 500, 5000)

    surface = PlanetarySurface()
    year = 0 #years in thousands
    saturation_per_year = {} #keep track of saturation
    saturation_per_year[year] = 0
    not_saturated = True
    while not_saturated:
        year += 1
        #time.sleep(.1) #enable to slow simulation
        crater = Crater(x_locations.get_next(), y_locations.get_next())
        surface.add_crater(crater)


        new_saturation = surface.crater_density()
        old_saturation = saturation_per_year[year/2]
        if old_saturation != 0:
            change_percent = new_saturation / (old_saturation  * 1.0) - 1
            if (change_percent < 0.05):
                saturation_per_year[year] = new_saturation
                break

        saturation_per_year[year] = new_saturation

    return (year, new_saturation, saturation_per_year)



# Run Main function
if __name__ == "__main__":
    main()
