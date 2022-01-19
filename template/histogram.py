import numpy as np
import matplotlib.pyplot as plt
from mplconfig import get_acsparameter
from _config import plot_format

filename = "histogram"
filename += plot_format

x = np.arange(0.1,10, 0.01)
y = np.sin(x)

with plt.rc_context(get_acsparameter(width = "single", n = 1, color = "line")):
    
    fig = plt.figure()
    axs = fig.subplots()

    n, bins, patches = axs.hist(y[y>0], bins = 25, density = True, alpha = 0.8, label = "Positive Part")
    n, bins, patches = axs.hist(y[y<0], bins = 25, density = True, alpha = 0.8, label = "Negative Part")
    axs.set_xlim(-1.1, 1.1)

    axs.set_xlabel("Spin Moments ($\mu B$)")
    axs.set_ylabel("Density")
    axs.legend()
    fig.savefig(filename)