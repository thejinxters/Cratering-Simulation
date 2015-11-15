from Tkinter import Tk, Canvas, Frame, BOTH
import math

class CraterViz(Tk):
    """
    Visualization class using Tkinter to build objects
    and track them on a canvas
    """

    def __init__(self, surface):
        Tk.__init__(self)
        self.title("Crater Density Visualization")
        self.surface = surface
        self.craters = {}
        fr = Frame(self)
        fr.pack()
        self.canvas = Canvas(fr, height = 580, width = 500)
        self.canvas.pack()
        self.init_ui()
        self.counter = 0;
        self.text_year = None
        self.text_craters = None


    #Builds canvas and adds the craters to it
    def init_ui(self):
        self._create_grid(self.canvas)
        self.canvas.pack()
        counter = 1
        for crater in self.surface.get_all_craters():
            self.after(counter * 100, self._add_crater, crater)
            counter += 1


    #Creates the grid on the canvas
    def _create_grid(self, canvas):
        """ Create 10km Grid """
        for i in range(50):
            canvas.create_line(10 * i, 0, 10 * i, 500, fill="#eee")
            canvas.create_line(0, 10 * i, 500, 10 * i, fill="#eee")


    #Adds a single crater to the map
    def _add_crater(self, crater):
        x, y = crater.get_location()
        outer_left = x - (25 * 1.2)
        outer_right = x + (25 * 1.2)
        outer_top = y - (25 * 1.2)
        outer_bottom = y + (25 * 1.2)
        outer = self.canvas.create_oval(
            outer_left, outer_top,
            outer_right,
            outer_bottom,
            outline="#f11",
            fill="#1f1",
            width=2)
        inner_left = x - 25
        inner_right = x + 25
        inner_top = y - 25
        inner_bottom = y + 25
        inner = self.canvas.create_oval(
            inner_left,
            inner_top,
            inner_right,
            inner_bottom,
            outline="#ccc",
            fill="green",
            width=2)
        craters_to_obliterate = self._find_obliterated_craters(crater)
        for obliterated in craters_to_obliterate:
            self._obliterate_crater(obliterated)

        self.craters[crater] = (x, y, inner, outer)
        self.counter += 1
        self._update_hud(self.counter, len(self.craters))


    #Removes crater from surface
    def _obliterate_crater(self, crater):
        x, y, inner, outer = self.craters[crater]
        del self.craters[crater]
        self.canvas.delete(inner)
        self.canvas.delete(outer)


    #Finds all Craters that need to be removed
    def _find_obliterated_craters(self, new_crater):
        obliterated_craters = []

        #Check if other craters are within cover radius
        cover_radius = new_crater.get_covering_radius()
        for crater in self.craters:
            if cover_radius > self._get_distance(crater, new_crater):
                obliterated_craters.append(crater)

        return obliterated_craters


    #Gets the distance between crater centers
    def _get_distance(self, crater1, crater2):
        x1, y1 = crater1.get_location()
        x2, y2 = crater2.get_location()
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


    #Updates the heads up display on the bottom of the canvas
    def _update_hud(self, year, craters):
        if self.text_year:
            self.canvas.delete(self.text_year)
        self.text_year = self.canvas.create_text(480, 560, anchor="e", text="Year: "+str(year)+"000")
        if self.text_craters:
            self.canvas.delete(self.text_craters)
        self.text_craters = self.canvas.create_text(20, 560, anchor="w", text="Craters: "+str(craters))
