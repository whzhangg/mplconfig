# mplconfig

- provide suitable matplotlib's rcParam for scientific journals  

- matplotlib styles can be controlled using the rc parameters and context management: https://matplotlib.org/stable/tutorials/introductory/customizing.html

- the scripts in this packages provide functions that generate the parameter dictionary to be used as:

```
import matplotlib.pyplot as plt

param = get_acsparam()
with plt.rc_context(param):
```
To use, simply put the folder to where python can find it.
