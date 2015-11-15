import numpy as np
import matplotlib.pyplot as plt

class TimeDensityPlot:
    def __init__(self, craters_per_year, trial):

        #Format data
        trial += 1
        years = len(craters_per_year)-1
        data = craters_per_year.values()
        saturation = craters_per_year[years]

        #Generate Plot Options
        plt.plot(data, 'bo')
        plt.xlabel('Thousands of Years', fontsize=20)
        plt.ylabel('Number of Craters', fontsize=20)
        plt.title(
            'Crater Density Per Thousand Years in 500km Square Region | Trial: '+str(trial),
            fontsize=25)
        plt.axis([0, years+1, 0, 120])
        plt.text(years-5, 10,
            "Saturation Density is " + str(saturation) + " after " + str(years) + "000 years",
            verticalalignment='bottom',
            horizontalalignment='right',
            fontsize=15)


    def show(self):
        plt.show()


    def close(self):
        plt.close()

