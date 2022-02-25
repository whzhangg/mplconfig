import numpy as np
import matplotlib.pyplot as plt
from mplconfig import get_acsparameter
from _config import plot_format

filename = "broken_axis"
filename += plot_format
#axs3_2.bar(bar_x, bar_y, alpha = 0.6, width = 0.1, color = "gray")
length = 20
bary = np.random.random(20)
barx = np.arange(length)

bary[19] += 10
bary[10] += 10
bary[12] += 11


with plt.rc_context(get_acsparameter(width = "single", n = 1, color = "line")):
    fig = plt.figure()
    axs1, axs2 = fig.subplots(2,1, sharex = True)
    fig.subplots_adjust(hspace=0.05)
    axs1.bar(barx, bary, alpha = 0.6, width = 0.5, color = "gray")
    axs2.bar(barx, bary, alpha = 0.6, width = 0.5, color = "gray")

    axs1.set_ylim(9.8, 12)
    axs2.set_ylim(0, 2.4)

    axs1.spines["bottom"].set_visible(False)
    axs2.spines["top"].set_visible(False)

    axs1.xaxis.tick_top()
    axs1.tick_params(labeltop=False)  # don't put tick labels at the top
    axs2.xaxis.tick_bottom()
    
    fig.text(0.045, 0.5, 'ylabel', ha='center', va='center', rotation='vertical')
    axs2.set_xlabel("xlabel")

    d = .5  # proportion of vertical to horizontal extent of the slanted line
    kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
                linestyle="none", color='k', mec='k', mew=1, clip_on=False)
    axs1.plot([0, 1], [0, 0], transform=axs1.transAxes, **kwargs)
    axs2.plot([0, 1], [1, 1], transform=axs2.transAxes, **kwargs)

    fig.savefig(filename)
