%load_ext pyspecdata.ipy
from itertools import cycle
import matplotlib.pyplot as plt
import numpy as np
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = cycle(prop_cycle.by_key()['color'])

# load 250130 data: 20 mM TEMPO-SO4 in isooctane $w_0 = 20$
d_cooling_25 = find_file("250130_20mM_TSO4_W20_Isooct_run1.DSC", exp_type="francklab_esr/romana") #cooling
d_cooling_25= d_cooling_25.chunk_auto('harmonic','harmonic')['harmonic', 0]['phase',0]
d_cooling_25.reorder('Temperature').sort('Temperature')
d_cooling_25.pcolor()
title("20 mM TEMPO-SO4 in isooctane $w_0=20$ for cooling 250130")
show()

# load 250131 data: 20 mM TEMPO-SO4 in isooctane $w_0 = 20$
d_cooling_25_aged = find_file("250131_20mM_TSO4_Isooct_w20_prep250130.DSC", exp_type="francklab_esr/romana") #cooling
d_cooling_25_aged= d_cooling_25_aged.chunk_auto('harmonic','harmonic')['harmonic', 0]['phase',0]
plot(d_cooling_25_aged, label="aged 1 day equilibrate room temp ESR")
title("250131 aged data: 20 mM TEMPO-SO4 in isooctane $w_0=20$ prepared 250130")
legend()
show()

# plot comparison aligned
## 250131 data
thismax_aged1day= d_cooling_25_aged["$B_0$":(3482, 3494)].C.argmax().item()
print(thismax_aged1day)
d_cooling_25_aged["$B_0$"]-=thismax_aged1day
plot(d_cooling_25_aged/d_cooling_25_aged.max(), label="1 day equilibrate room temp ESR")
## 250130 data
thismax_aged1hr= d_cooling_25["$B_0$":(3324, 3340)]["Temperature":293].C.argmax().item()
print(thismax_aged1hr)
d_cooling_25["$B_0$"]-=thismax_aged1hr
plot(d_cooling_25["Temperature":293]/d_cooling_25["Temperature":293].max(), label="1 hour equilibrate VT ESR at 293 K")
title("250130 data vs 250131 data of 20 mM TEMPO-SO4 in isooctane $w_0=20$")
legend()
show()