from .acs_sty import get_acsparameter
from .color_cycler import set1_cycler, tableau_cycler

# to use the parameters, use
#    rcparam = get_parameter(width = "single", n = 1, color_cycler = set1_cycler)
#    with plt.rc_context(rcparam):
#        fig = plt.figure()