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
# 240220 manuscript data VTU
d['240220 VTU: manuscript data cooling at 293K'] = find_file("240220_TempoSO4_W20_run1.DSC", exp_type="francklab_esr/romana") #cooling
d['240220 VTU: manuscript data reheating at 293K'] = find_file("240220_TempoSO4_W20_run2.DSC", exp_type="francklab_esr/romana") #reheating

# # Compare same year-old capillary
d['250501: same capillary tube acquired today in RT'] = find_file("250501_20mM_TSO4_C8_W20_previous_240220.DSC", exp_type = "francklab_esr/romana")

for k, v in d.items():
    d[k] = v.chunk_auto("harmonic", "harmonic")["harmonic", 0]["phase", 0]
    if 'VTU' in k or '240220' in k or '250130' in k or '240226' in k:
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
    plt.xlim([-1.5,5])
 
