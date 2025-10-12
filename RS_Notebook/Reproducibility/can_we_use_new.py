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
import matplotlib.pyplot as plt
import numpy as np
d = {}
d['240220 VTU: manuscript data before cooling at 293 K'] = find_file("240220_TempoSO4_W20_run1.DSC", exp_type="francklab_esr/romana") #cooling
d['250320: Old SL+ Old AOT before centrifuge'] = find_file("250320_OldSL_Old_AOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
d['250320: Old SL+ Old AOT After centrifuge'] = find_file("250320_OldSL_Old_AOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")
d['250320: Old SL + New AOT before centrifuge'] = find_file("250320_OldSL_NewAOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
d['250320: New SL + Old AOT before centrifuge'] = find_file("250320_NewSL_OldAOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
d['250320: New SL + New AOT After centrifuge\nexample of lopsided'] = find_file("250320_NewSL_NewAOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")

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
