from pyspecdata import find_file, figlist_var, plot, ndshape
from pyspecProcScripts import align_esr
from itertools import cycle
from cycler import cycler
import matplotlib.pyplot as plt
from matplotlib.pyplot import show, figure
import numpy as np
plt.rcParams['axes.prop_cycle'] = (
        cycler(linestyle=['-','--'])
        *
        cycler(color='bgrcmyk')
        )

d = {}
# 240220 manuscript data VTU
d['240220 VTU: manuscript data w0=20'] = find_file("240220_TempoSO4_W20_run1.DSC", exp_type="francklab_esr/romana") #cooling
# d['240220 VTU: manuscript data after cooling at 293 K'] = find_file("240220_TempoSO4_W20_run2.DSC", exp_type="francklab_esr/romana") #reheating

## TEMPO_SO4 RM ancient times
# ## water loading series TEMPO-SO4 with CHCl3:CH3OH prep
d['230726: 0.5mM TSO4 w0 = 0'] = find_file("230726_TEMPO_SO4_W0.DSC", exp_type = "francklab_esr/romana")
d['230726: 0.5mM TSO4 w0 = 2'] = find_file("230726_TEMPO_SO4_W2.DSC", exp_type = "francklab_esr/romana")
d['230726: 0.5mM TSO4 w0 = 10'] = find_file("230726_TEMPO_SO4_W10.DSC", exp_type = "francklab_esr/romana")
d['230726: 0.5mM TSO4 w0 = 25'] = find_file("230726_TEMPO_SO4_W25.DSC", exp_type = "francklab_esr/romana")
# d['230726: 0.5mM TSO4 w0 = 50'] = find_file("230726_TEMPO_SO4_W50.DSC", exp_type = "francklab_esr/romana")
## 250113
d['250113: 20mM TSO4 w0 = 1'] = find_file("250113_20mM_TSO4_W1_Syn2.DSC", exp_type = "francklab_esr/romana")
d['250113: 20mM TSO4 w0 = 3'] = find_file("250113_20mM_TSO4_W3_Syn2.DSC", exp_type = "francklab_esr/romana")
## 100 mM w0 = 30 room temp
# d['231116: 100mM TSO4 w0 = 30'] = find_file("231116_TEMPOSO4_W30.DSC", exp_type = "francklab_esr/romana")
# d['231119: 100mM TSO4 w0 = 30'] = find_file("231119_TEMPOSO4_W30.DSC", exp_type = "francklab_esr/romana")
## 20 mM TEMPO-SO4 RM, w0 = 30 room temp
# 231121: 20 mM TEMPO-SO4 RM, w0 = 30 room temp
# d['231121 RT: 20mM TSO4 w0 = 30'] = find_file("231121_20mMTEMPOSO4_W30.DSC", exp_type = "francklab_esr/romana")
# 231221: Starting of VTU-- 20 mM TEMPO-SO4 RM, w0 = 30 (RT+VT)
# d['231221 RT: 20mM TSO4 w0 = 30'] = find_file("old_temposo4_rt_231221.DSC", exp_type = "francklab_esr/romana")
# d['231221 VT: 20mM TSO4 w0 = 30 at 295K'] = find_file("231221_TEMP_Tempo_295K.DSC", exp_type = "francklab_esr/romana")
# d['231221 VT: 20mM TSO4 w0 = 30 at 285K'] = find_file("231221_TEMP_Tempo_285K.DSC", exp_type = "francklab_esr/romana")
# d['231221 VT: 20mM TSO4 w0 = 30 at 255K'] = find_file("231221_Tempo_VTU.DSC", exp_type = "francklab_esr/romana")
# 240118: 20 mM TEMPO-SO4 RM, w0 = 30 (RT+VT)
# d['240118 RT: 20mM TSO4 w0 = 30'] = find_file("240118_TempoSo4_W30_RT.DSC", exp_type = "francklab_esr/romana")
# d['240118 VTU: 20mM TSO4 w0 = 30 run1 heating'] = find_file("230118_VTU_run1.DSC", exp_type = "francklab_esr/romana")
# d['240118 VTU: 20mM TSO4 w0 = 30 run2 heating'] = find_file("230118_VTU_run2.DSC", exp_type = "francklab_esr/romana")
# d['240118 VTU: 20mM TSO4 w0 = 30 run3 cooling'] = find_file("230118_VTU_run3.DSC", exp_type = "francklab_esr/romana")
# d['240118 VTU: 20mM TSO4 w0 = 30 run4 cooling'] = find_file("230118_VTU_run4.DSC", exp_type = "francklab_esr/romana")
# d['240118 VTU: 20mM TSO4 w0 = 30 run5 heating'] = find_file("230118_VTU_run5.DSC", exp_type = "francklab_esr/romana")


# control exp data
# # Exp: 250328
# d['250328: Freshly prepared old AOT (purchased 2023)'] = find_file("250328_20mMTSO4_C8_W20_OldAOTbottle23.DSC", exp_type = "francklab_esr/romana")
# d['250328: Freshly prepared New AOT (purchased 2025)'] = find_file("250328_20mMTSO4_C8_W20_NewAOTbottle25_RM1.DSC", exp_type = "francklab_esr/romana")
# # # to compare
# d['250324: RM prepared with Old AOT solution (prepared 2023)'] = find_file("250324_OldAOT_OldTSO4.DSC", exp_type = "francklab_esr/romana")
# d['250324: RM prepared with New AOT solution (prepared 2025)'] = find_file("250324_NewAOT_NewTSO4.DSC", exp_type = "francklab_esr/romana")

## Timeseries
d['250320: Before cooling RT'] = find_file("250320_OldSL_Old_AOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
# d['250320 initial_Timeseries: initial at 263K VT'] = find_file("250320_OldSL_OldAOT_263K.DSC", exp_type = "francklab_esr/romana")
d['250320 After_Timeseries: After reheating VT'] = find_file("250320_OldSL_OldAOT_Reheat.DSC", exp_type = "francklab_esr/romana")



for k, v in d.items():
    if "harmonic" in d[k].dimlabels:
        d[k] = v.chunk_auto("harmonic", "harmonic")["harmonic", 0]["phase", 0]
    if "Temperature" in d[k].dimlabels:
        d[k].reorder("Temperature").sort("Temperature")
        d[k] = d[k]["Temperature":293]
    if "Time" in d[k].dimlabels:
        fieldname = "$B_0$"
        mask = abs(d[k]).sum(fieldname) > 0
        d[k] = d[k]["Time", mask.data]
        figure()
        d[k].pcolor()
        if "initial_Timeseries" in k:
            d[k] = d[k]["Time", 0]
            figure()
            plot (d[k])
            show()
        if "After_Timeseries" in k:
            d[k] = d[k]["Time", -1]
            figure()
            plot (d[k])
            show()
        
with figlist_var() as fl:
    d = align_esr(d, fl=fl)
    fl.next("normalized after alignment", legend=True)
    # If the data very dissimilar, the least-squares scaling doesn't
    # work as well.  For these, it makes more sense to use a peak
    # normalization.
    for k, v in d.items():
        extra_norm = abs(d[k].data.max() - d[k].data.min())
        d[k] /= extra_norm
        d[k].set_prop("scaling", d[k].get_prop("scaling") * extra_norm)
        fl.plot(
            d[k],
            lw=1,
            alpha=0.5,
            label=f"{k}\n÷ {d[k].get_prop('scaling'):#0.3g}",
        )
    fl.adjust_spines("bottom")
    plt.ylabel("")
    plt.gca().set_yticks([])    
    plt.xlim([-1.5,5])
 
