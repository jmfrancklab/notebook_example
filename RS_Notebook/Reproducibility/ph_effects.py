from cycler import cycler
import matplotlib.pyplot as plt
plt.rcParams['axes.prop_cycle'] = (
        cycler(linestyle=['-','--'])
        *
        cycler(color='bgrcmyk')
        )
from pyspecdata import find_file, figlist_var, plot
from pyspecProcScripts import align_esr
from itertools import cycle
import numpy as np

d = {}
d['240220 VTU: manuscript data before cooling at 293 K'] = find_file("240220_TempoSO4_W20_run1.DSC", exp_type="francklab_esr/romana") #cooling
d['250318: without HCl'] = find_file("250318_20mM_TSO4_C8_w20_UPwater_12ms.DSC", exp_type = "francklab_esr/romana")
d['250314: TEMPO-SO4 without NaOH\nequil 1 day'] = find_file("250314_20mM_TSO4_water_convTime12ms.DSC", exp_type = "francklab_esr/romana")
d['250313: without NaOH'] = find_file("250313_20mM_TSO4_C8_w20_oldSL_oldAOT_heat_1hr_convTime12ms.DSC", exp_type = "francklab_esr/romana")

d['250318: with HCl'] = find_file("250318_20mM_TSO4_C8_w20_HCl_12ms.DSC", exp_type = "francklab_esr/romana")
d['250314: with NaOH'] = find_file("250314_20mM_TSO4_C8_w20_oldSL_oldAOT_NaOH_convTime12ms.DSC", exp_type = "francklab_esr/romana")
# spin label

for k, v in d.items():
    d[k] = v.chunk_auto("harmonic", "harmonic")["harmonic", 0]["phase", 0]
    if 'VTU' in k or '240220' in k or '250130' in k or '240226' in k:
        d[k].reorder("Temperature").sort("Temperature")
        d[k] = d[k]["Temperature":293]
with figlist_var() as fl:
    d = align_esr(d, fl=fl)
    fl.next("normalized after alignment", legend=True)
    for k, v in d.items():
        extra_norm = abs(d[k].data.max() - d[k].data.min())
        d[k] /= extra_norm
        d[k].set_prop("scaling", d[k].get_prop("scaling") * extra_norm)
        fl.plot(
            d[k],
            alpha=0.5,
            label=f"{k}\n÷ {d[k].get_prop('scaling'):#0.3g}",
        )
    fl.adjust_spines("bottom")
    plt.ylabel("")
    plt.gca().set_yticks([])    
    plt.xlim([-1,4.5])
