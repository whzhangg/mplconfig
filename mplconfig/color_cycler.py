import numpy as np
from palettable.colorbrewer.qualitative import Set1_9
from palettable.tableau import Tableau_10, Tableau_20
from cycler import cycler

# two color theme. 
# The first  works well for line plots
# the second works well for scatter plots 
almost_black = '#262626'
light_grey = np.array([float(248) / float(255)] * 3)

# https://jiffyclub.github.io/palettable/colorbrewer
brewer_set1 = Set1_9.mpl_colors                #https://bl.ocks.org/mbostock/5577023
brewer_set1.pop(5) # bright yellow
brewer_set1[0], brewer_set1[1] = brewer_set1[1], brewer_set1[0] # switch red and blue
brewer_set1[2], brewer_set1[3] = brewer_set1[3], brewer_set1[2] # switch purple and green
brewer_set1.append(almost_black)
set1_cycler = cycler('color', brewer_set1)   

tableau_10 = Tableau_10.mpl_colors
tableau_10.append(almost_black)
tableau_cycler = cycler('color', tableau_10)