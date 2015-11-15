import sys
from utils import *
from simulated_objects import *
from Tkinter import Tk, Canvas, Frame, BOTH

def main(argv):

    # RUN PLOT SIMULATION:
    if len(argv) >= 1 and argv[0] == "plot":
        if len(argv) > 1:
            number_of_trials = int(argv[1])
        else:
            number_of_trials = 1

        # Repeat Simulations for # of trials
        for trial in range(number_of_trials):
            # Run Simulation
            year, saturation, saturation_per_year, _ = simulation()

            # Render Plot
            plot = TimeDensityPlot(saturation_per_year, trial)
            plot.show()
            plot.close()

    # RUN VIZUALIZATION:
    elif len(argv) == 1 and argv[0] == "viz":
        # Run Simulation
        year, saturation, _, surface = simulation()

        #Render Visualization
        tkinter = CraterViz(surface)
        tkinter.mainloop()

    # IMPROPER INPUT
    else:
        usage()

def simulation():
    #Create some uniformly random locations
    x_locations = UniformRandomNumbers(0, 500, 5000)
    y_locations = UniformRandomNumbers(0, 500, 5000)

    surface = PlanetarySurface()
    year = 0 #years in thousands
    saturation_per_year = {} #keep track of saturation
    saturation_per_year[year] = 0 #add 0th year

    not_saturated = True
    while not_saturated:
        year += 1

        # Randomly Generate Crater and add it to surface
        crater = Crater(x_locations.get_next(), y_locations.get_next())
        surface.add_crater(crater)

        # Determine Saturation (changes by less than 5%)
        new_saturation = surface.crater_density()
        old_saturation = saturation_per_year[year/2]
        if old_saturation != 0:
            change_percent = new_saturation / (old_saturation  * 1.0) - 1
            if (change_percent < 0.05):
                saturation_per_year[year] = new_saturation
                break

        saturation_per_year[year] = new_saturation

    # Return all values needed for plots and viz
    return (year, new_saturation, saturation_per_year, surface)

def usage():
    print """usage: run_simulation <command> [<args>]

If you want to run plotted trials:
    python run_simulation plot <number-of-trials>

If you want to run a visualization:
    python run_simulation viz
    """


# Run Main function
if __name__ == "__main__":
    main(sys.argv[1:])
