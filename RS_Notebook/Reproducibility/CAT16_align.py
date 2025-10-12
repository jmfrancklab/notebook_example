from pyspecdata import find_file, figlist_var, plot
from pyspecProcScripts import align_esr
from itertools import cycle
from cycler import cycler
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['axes.prop_cycle'] = (
        cycler(linestyle=['-','--'])
        *
        cycler(color='bgrcmyk')
        )

d = {}
# # 240226 previous CAT16 RT vs VT
# d['240226: CAT-16 w20 RT'] = find_file("240226_CAT16_C8_W20.DSC", exp_type = "francklab_esr/romana")
# d["240226: CAT-16 w20 VT"] = find_file("240226_CAT16_C8_W20_run1.DSC", exp_type="francklab_esr/romana")

# ## CAT 16 water loading series
d['230621: CAT-16 w0=0'] = find_file("230621_w0_0.DSC", exp_type = "francklab_esr/romana")
d['230621: CAT-16 w0=2'] = find_file("230621_w0_2.DSC", exp_type = "francklab_esr/romana")
d['230621: CAT-16 w0=10'] = find_file("230621_w0_10.DSC", exp_type = "francklab_esr/romana")
d['230621: CAT-16 w0=25'] = find_file("230621_w0_25.DSC", exp_type = "francklab_esr/romana")
d['230621: CAT-16 w0=50'] = find_file("230621_w0_50.DSC", exp_type = "francklab_esr/romana")
# after 1 month in fridge
d['230726: CAT-16 w0=0'] = find_file("230726_CAT16_W0.DSC", exp_type = "francklab_esr/romana")
d['230726: CAT-16 w0=2'] = find_file("230726_CAT16_W2.DSC", exp_type = "francklab_esr/romana")
d['230726: CAT-16 w0=10'] = find_file("230726_CAT16_W10.DSC", exp_type = "francklab_esr/romana")
d['230726: CAT-16 w0=25'] = find_file("230726_CAT16_W25.DSC", exp_type = "francklab_esr/romana")
d['230726: CAT-16 w0=50'] = find_file("230726_CAT16_W50.DSC", exp_type = "francklab_esr/romana")



for k, v in d.items():
    d[k] = v.chunk_auto("harmonic", "harmonic")["harmonic", 0]["phase", 0]
    if 'VTU' in k:
        d[k].reorder("Temperature").sort("Temperature")
        d[k] = d[k]["Temperature":293]
        
with figlist_var() as fl:
    d = align_esr(d, fl=fl)
    fl.next("normalized after alignment")#, legend=True)
    # If the data very dissimilar, the least-squares scaling doesn't
    # work as well.  For these, it makes more sense to use a peak
    # normalization.
    for k, v in d.items():
        extra_norm = abs(d[k].data.max() - d[k].data.min())
        d[k] /= extra_norm
        d[k].set_prop("scaling", d[k].get_prop("scaling") * extra_norm)
        fl.plot(
            d[k],
            lw=0.8,
            alpha=0.5,
            label=f"{k}\n÷ {d[k].get_prop('scaling'):#0.3g}",
        )
    fl.adjust_spines("bottom")
    plt.ylabel("")
    plt.gca().set_yticks([])    
    # plt.xlim([-5,5])
 
