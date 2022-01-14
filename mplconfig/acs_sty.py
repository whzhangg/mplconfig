from .color_cycler import set1_cycler, tableau_cycler

width_single_column = 3.25
width_double_column = 7.00
height_width_ratio = 0.68

_width = width_single_column
_height = width_single_column * height_width_ratio

_default_params = { 'font.family': 'arial',
                    'font.size': 7,
                    'axes.prop_cycle': set1_cycler,
                    'axes.labelsize': 7,
                    'axes.labelpad' : 2,
                    'axes.linewidth': 0.8,
                    'figure.figsize': (_width, _height),
                    'figure.subplot.left': 0.135,
                    'figure.subplot.right': 0.925,
                    'figure.subplot.bottom': 0.135,
                    'figure.subplot.top': 0.95,
                    'savefig.dpi': 300,
                    'savefig.format': 'eps',
                    'legend.fontsize': 7,
                    'legend.frameon': False,
                    'legend.numpoints': 1,
                    'legend.handlelength': 2,
                    'legend.scatterpoints': 1,
                    'legend.labelspacing': 0.4,
                    'legend.markerscale': 0.9,
                    'legend.handletextpad': 0.5,   # pad between handle and text
                    'legend.borderaxespad': 0.5,   # pad between legend and axes
                    'legend.borderpad': 0.5,       # pad between legend and legend content
                    'legend.columnspacing': 0.25,  # pad between each legend column
                    'xtick.labelsize': 7,
                    'ytick.labelsize': 7,
                    'xtick.major.size' : 3,
                    'xtick.minor.size' : 2,
                    'ytick.major.size' : 3,
                    'ytick.minor.size' : 2,
                    'lines.linewidth': 0.8,
                    'lines.markersize': 3,
                    # 'lines.markeredgewidth': 0,
                    # 0 will make line-type markers, such as '+', 'x', invisible
                    #'axes.autolimit_mode': 'round_numbers',
                    'axes.xmargin': 0,
                    'axes.ymargin': 0,
                    'xtick.direction': 'in',
                    'xtick.top': True,
                    'ytick.direction' : 'in',
                    'ytick.right': True,
                    'xtick.major.width': 0.8,
                    'ytick.major.width': 0.8,
                    'xtick.minor.width': 0.6,
                    'xtick.minor.width': 0.6,
                    }


available_width = { "single" : width_single_column,
                    "double" : width_double_column}

def get_acsparameter(width:str = "single", n:int = 1, color_cycler = set1_cycler, square:bool = False, ratio: float = None) -> dict:
    """this function return rcParam with suitable setting for plots"""
    param = _default_params
    w = available_width[width]
    h = _height * n - (n - 1) * _height * (1.0 - param['figure.subplot.top'])

    if square:
        assert n == 1
        h = w
    
    if ratio:
        h = w * ratio
    
    param['axes.prop_cycle'] = color_cycler
    param['figure.subplot.bottom'] = param['figure.subplot.left']
    param['figure.subplot.top'] = param['figure.subplot.right']

    param['figure.figsize'] = (w, h)

    return param



