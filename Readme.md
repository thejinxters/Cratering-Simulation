# Cratering Simulations

## Project Description

**Author:**
    Brandon Mikulka

**Project:** To carry out a numerical simulation of the cratering process on a planetary surface and then visualize the data.

**Extended Idea:** Considering a 500km square planetary surface, and that one 50km diameter crater is formed on the surface every 1000 years, this project determines when saturation is achieved. Saturation is reached when the test area changes by less than 5% when the time is doubled. This simulation provides a plot visualization and a graphical visualization.


## Installation

### 1. Install the pip requirements
```bash
pip install -r requirements.txt
```

### 2. Usage:

```bash
run_simulation <command> [<args>]

If you want to run plotted trials:
    python run_simulation plot <number-of-trials>

If you want to run a visualization:
    python run_simulation viz
```
