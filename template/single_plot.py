import numpy as np
import matplotlib.pyplot as plt
from mplconfig import get_acsparameter
from _config import plot_format

filename = "single_plot" 
filename += plot_format
x = np.arange(0.1,10, 0.25)
y = np.sin(x)
yerr = np.log10(x) * 0.5

label = "$\sin x$"   # latex math format

with plt.rc_context(get_acsparameter(width = "single", n = 1, color = "line")):
    fig = plt.figure()
    axes = fig.subplots()

    axes.text(0.03,0.03, "single plot", ha = "left", va = "bottom", transform = axes.transAxes)

            
    axes.set_xlabel("input x")
    axes.set_ylabel("output y")
    
    axes.set_xlim(1, 9)
    axes.errorbar(x, y, yerr, fmt='-o', label = label, elinewidth=0.8, capsize=2)
    axes.legend()

    fig.savefig(filename)