import numpy as np
import matplotlib.pyplot as plt
from mplconfig import get_acsparameter
from _config import plot_format

filename = "double_plot"
filename += plot_format
x = np.arange(0.1,10, 0.1)
y1 = np.sin(x)
y2 = 1.0 / x
y3 = 2.0 / x + 1
label1 = "$\sin x$"   # latex math format
label2 = "1/x"
label2 = "2/x + 1"

with plt.rc_context(get_acsparameter(width = "single", n = 2, color = "line")):
    fig = plt.figure()
    axes = fig.subplots(2,1, sharex = False)

    fig.subplots_adjust(bottom = 0.1, top = 0.95)
    axes[0].text(0.03,0.96, "a)", size = 10, ha = "left", va = "top", transform = axes[0].transAxes)
    axes[1].text(0.03,0.96, "b)", size = 10, ha = "left", va = "top", transform = axes[1].transAxes)
    
    axes[0].set_ylabel("Mean Absolute Error")
    axes[1].set_ylabel("Mean Absolute Error")
    axes[1].set_xlabel("Number of x (eV)")

    axes[0].set_xlim(0.5, 8.5)
    axes[1].set_xlim(0.5, 8.5)
    axes[0].xaxis.set_major_locator(plt.FixedLocator([2,3,7,8]))
    axes[1].xaxis.set_major_locator(plt.FixedLocator([1,4,5,6]))

    axes[0].plot(x, y1, label = label1, alpha = 0.8)
    axes[1].plot(x, y2, label = label2, alpha = 0.8)
    axes[1].plot(x, y3, label = label2, alpha = 0.8)
        
    axes[0].legend()
    axes[1].legend()

    fig.savefig(filename)
