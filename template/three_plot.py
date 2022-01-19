import numpy as np
import matplotlib.pyplot as plt
from mplconfig import get_acsparameter
from _config import plot_format

filename = "three_plot"
filename += plot_format

x = np.arange(100,800, 25)
kappa = 5 + 2000 / x
seebeck = 200 - x / 40 - x**3 / 64000000
zt = 0.3 + x**2 / 640000

with plt.rc_context(get_acsparameter(width = "double", n = 1, color = "line")):
    fig = plt.figure()
    axes = fig.subplots(1,3)

    fig.subplots_adjust(left = 0.075, right = 0.95)
    axes[0].text(0.03,0.96, "a)", size = 10, ha = "left", va = "top", transform = axes[0].transAxes)
    axes[1].text(0.03,0.96, "b)", size = 10, ha = "left", va = "top", transform = axes[1].transAxes)
    axes[2].text(0.03,0.96, "c)", size = 10, ha = "left", va = "top", transform = axes[2].transAxes)
    
    axes[0].set_ylabel("Thermal conductivity (W/mK)")
    axes[1].set_ylabel("Seebeck ($\mu$V/K)")
    axes[2].set_ylabel("ZT")
    axes[0].set_xlabel("Tempature (K)")
    axes[1].set_xlabel("Tempature (K)")
    axes[2].set_xlabel("Tempature (K)")
    
    axes[0].plot(x, kappa, label = "sample1")
    axes[1].plot(x, seebeck, label = "sample2")
    axes[2].plot(x, zt, label = "sample3")
        
    
    axes[1].yaxis.set_major_formatter(plt.FormatStrFormatter('%.0f'))
    axes[0].legend()
    axes[1].legend()
    axes[2].legend()

    fig.savefig(filename)
