import numpy as np
import matplotlib.pyplot as plt
from mplconfig import get_acsparameter, tableau_cycler
from _config import plot_format

filename = "scatter" 
filename += plot_format

npoints = 20
xset1 = np.random.random(npoints) * 5
yset1 = np.random.random(npoints) * 5
point_size1 = np.arange(3, 19, 16/npoints)

xset2 = np.random.random(npoints) * 5
yset2 = np.random.random(npoints) * 5
point_size2 = np.arange(3, 19, 16/npoints)

with plt.rc_context(get_acsparameter(width = "single", square = True, color = "point")):

    fig = plt.figure()
    axs = fig.subplots()
    axs.set_xlim(0, 5.1)
    axs.set_ylim(0, 5.1)
    axs.set_xlabel("Random variable 1 (color correspond to point size)")
    axs.set_ylabel("Random variable 2")
    axs.plot(np.arange(10), np.arange(10), linestyle = ":", color = "grey")

    axs.fill_between(np.arange(10), np.arange(10) - 0.3, np.arange(10) + 0.3, color = "grey", alpha = 0.4)
        
    color_tabluau = [ [c['color']] for c in tableau_cycler]
        
    counter = 0
    # > 6
    mask = point_size1 > 10
    axs.scatter(xset1[mask], yset1[mask],s=point_size1[mask], marker = 'o', c = color_tabluau[counter], label = "set1, >10")
    
    mask = point_size2 > 10
    axs.scatter(xset2[mask], yset2[mask],s=point_size2[mask], marker = 'd', c = color_tabluau[counter], label = "set2, >10")

    counter += 1
    # < 6
    mask = point_size1 < 10
    axs.scatter(xset1[mask], yset1[mask],s=point_size1[mask], marker = 'o', c = color_tabluau[counter], label = "set1, <10")
    
    mask = point_size2 < 10
    axs.scatter(xset2[mask], yset2[mask],s=point_size2[mask], marker = 'd', c = color_tabluau[counter], label = "set2, <10")

    axs.legend()
    fig.savefig(filename)
