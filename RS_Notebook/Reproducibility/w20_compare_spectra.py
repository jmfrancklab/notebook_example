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
# compare all RM spectra of w0=20 before cooling
## 250324: Control experiment maintaining same time interval
# d['250324: Old TSO4 + Old AOT'] = find_file("250324_OldAOT_OldTSO4.DSC", exp_type = "francklab_esr/romana")
# d['250324: New TSO4 + New AOT'] = find_file("250324_NewAOT_NewTSO4.DSC", exp_type = "francklab_esr/romana")
# d['250324: Old TSO4 (NaOH) + Old AOT'] = find_file("250324_OldAOT_OldTSO4_NaOH.DSC", exp_type = "francklab_esr/romana")
# d['250324: Old TSO4 (HCl) + Old AOT'] = find_file("250324_OldAOT_OldTSO4_HCl.DSC", exp_type = "francklab_esr/romana")
# d['250324: New TSO4 + Old AOT'] = find_file("250324_OldAOT_NewTSO4.DSC", exp_type = "francklab_esr/romana")
# d['250324: Old TSO4 + New AOT'] = find_file("250324_NewAOT_OldTSO4.DSC", exp_type = "francklab_esr/romana")
## 250321: Reproduce old materials and new materials
# d['250321: Old SL + Old AOT'] = find_file("250321_OldSL_Old_AOT_MoreHeating.DSC", exp_type = "francklab_esr/romana")
# d['250321: New SL + New AOT'] = find_file("250321_NewSL_New_AOT_MoreHeating.DSC", exp_type = "francklab_esr/romana")
## 250320: combination of old and new materials
# d['250320: Old SL+ Old AOT before centrifuge'] = find_file("250320_OldSL_Old_AOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
# d['250320: Old SL+ Old AOT After centrifuge'] = find_file("250320_OldSL_Old_AOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")
# d['250320: New SL + New AOT before centrifuge'] = find_file("250320_NewSL_NewAOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
# d['250320: New SL + New AOT After centrifuge'] = find_file("250320_NewSL_NewAOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")
# d['250320: Old SL + New AOT before centrifuge'] = find_file("250320_OldSL_NewAOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
# d['250320: Old SL + New AOT After centrifuge'] = find_file("250320_OldSL_NewAOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")
# d['250320: New SL + Old AOT before centrifuge'] = find_file("250320_NewSL_OldAOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
# d['250320: New SL + Old AOT After centrifuge'] = find_file("250320_NewSL_OldAOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")
## 250318: Reproduce reasonable spectra with new materials
# d['250318: new materials UP water'] = find_file("250318_20mM_TSO4_C8_w20_UPwater_12ms.DSC", exp_type = "francklab_esr/romana")
# d['250318: new materials DI water'] = find_file("250318_20mM_TSO4_C8_w20_DIwater_12ms.DSC", exp_type = "francklab_esr/romana")
# d['250318: with HCl'] = find_file("250318_20mM_TSO4_C8_w20_HCl_12ms.DSC", exp_type = "francklab_esr/romana")
# ## 250314: effect of NaOH
# d['250314: with NaOH'] = find_file("250314_20mM_TSO4_C8_w20_oldSL_oldAOT_NaOH_convTime12ms.DSC", exp_type = "francklab_esr/romana")
## 250313: effect of heat (old SL + old AOT)
# d['250313: with heat 1 hr'] = find_file("250313_20mM_TSO4_C8_w20_oldSL_oldAOT_heat_1hr_convTime12ms", exp_type = "francklab_esr/romana")
# d['250313: with heat 1 day'] = find_file("250314_20mM_TSO4_C8_w20_oldSL_oldAOT_heat_1day_convTime12ms", exp_type = "francklab_esr/romana")
## 250307: RM prep with old SL & old AOT solution
# d['250310: old AOT & SL, 3 day convTime 12 ms'] = find_file("250310_20mM_TSO4_C8_w20_oldSL_oldAOT_3day_equilibrate_convTime12ms.DSC", exp_type = "francklab_esr/romana")
# d['250310: old AOT & SL, 3 day convTime 5 ms'] = find_file("250310_20mM_TSO4_C8_w20_oldSL_oldAOT_3day_equilibrate_convTime5ms.DSC", exp_type = "francklab_esr/romana")
# d['250307: old AOT & SL, 1 hr convTime 12 ms'] = find_file("250307_20mM_TSO4_C8_w20_oldSL_oldAOT_convTime12ms.DSC", exp_type = "francklab_esr/romana")
# d['250307: old AOT & SL, 1 hr convTime 5 ms'] = find_file("250307_20mM_TSO4_C8_w20_oldSL_oldAOT_convTime5ms.DSC", exp_type = "francklab_esr/romana")
# ## 250304: AOT Latest and less dust
# d['250305: ctrl 1 day'] = find_file("250305_20mM_TSO4_C8_w20_ThinID_1day_Equilibrate_beforeCooling.DSC", exp_type = "francklab_esr/romana")
# d['250304: ctrl 3 hr'] = find_file("250304_20mM_TSO4_C8_w20_ThinID_beforeCooling.DSC", exp_type = "francklab_esr/romana")
# d['250304: ctrl 5.5 hr'] = find_file("250304_20mM_TSO4_C8_w20_ThinID_5hrEquilibrate.DSC", exp_type = "francklab_esr/romana")
# d['250304: ctrl centrifuge'] = find_file("250304_20mM_TSO4_C8_w20_centrifuge_beforeCooling.DSC", exp_type = "francklab_esr/romana")
## 250225 latest ordered AOT and Isooctane and UP water
# d['250225: latest AOT & isooctane'] = find_file("250225_TSO4_20mM_C8_W20_BeforeCooling.DSC", exp_type = "francklab_esr/romana")
# ## 250210 New PChem AOT
# d['250210: PChem AOT'] = find_file("250210_20mM_TSO4_C8_W20.DSC", exp_type = "francklab_esr/romana")
# ## 250206: old AOT solution + new SL
# d['250206: old AOT + new SL'] = find_file("250206_20mM_TSO4_W20_C8.DSC", exp_type = "francklab_esr/romana")
# ## 250130: bad data Medium AOT
# d['250131: Medium AOT 1 day'] = find_file("250131_20mM_TSO4_Isooct_w20_prep250130.DSC", exp_type = "francklab_esr/romana")
# # d['250130 VTU: Medium AOT 1 hr'] = find_file("250130_20mM_TSO4_W20_Isooct_run1.DSC", exp_type = "francklab_esr/romana")
# ## 241219: Non-equilibrated
# d['241219 VTU: Non-equilibrated'] = find_file("241219_TS_C8_W20_20mM_NonEqui_run1.DSC", exp_type = "francklab_esr/romana")
# ## 241218: Reproducibility coarse T-step
# d['241218 VTU: Reproducibility coarse-T'] = find_file("241218_TS_C8_W20_20mM_run1.DSC", exp_type = "francklab_esr/romana")
# ## 241213: 11 mM TEMPO-SO4
# d['241213 VTU: 11 mM TSO4'] = find_file("241213_TS_isooct_W20_11mM_run1.DSC", exp_type = "francklab_esr/romana")
# ## 241210: Reproducibility fine T-step
# d['241210 VTU: Reproducibility fine T-step'] = find_file("241210_TS_isooct_W20_20mM_run1.DSC", exp_type = "francklab_esr/romana")
# ## 241206: Reproducibility fine T-step
# d['241206 VTU: Reproducibility fine T-step'] = find_file("241206_TS_Isooctane_W20_20mM_run1.DSC", exp_type = "francklab_esr/romana")
# ## 240808: HE samples w0=20
# d['240808: 10 mM TSO4'] = find_file("240809_10mM_TS_W20_C8.DSC", exp_type = "francklab_esr/romana")
# d['240808: 31.6 mM TSO4'] = find_file("240808_31.6mM_TS_W20_C8.DSC", exp_type = "francklab_esr/romana")
## 240220: Manuscript data
# d['240220 VTU: manuscript data at 293 K'] = find_file("240220_TempoSO4_W20_run1.DSC", exp_type="francklab_esr/romana") #cooling

# # separate unique spectra plot
# # type 1: broad peak
# d['250305: ctrl 1 day'] = find_file("250305_20mM_TSO4_C8_w20_ThinID_1day_Equilibrate_beforeCooling.DSC", exp_type = "francklab_esr/romana")
# d['250304: ctrl 3 hr'] = find_file("250304_20mM_TSO4_C8_w20_ThinID_beforeCooling.DSC", exp_type = "francklab_esr/romana")
# d['250304: ctrl 5.5 hr'] = find_file("250304_20mM_TSO4_C8_w20_ThinID_5hrEquilibrate.DSC", exp_type = "francklab_esr/romana")
# d['250304: ctrl centrifuge'] = find_file("250304_20mM_TSO4_C8_w20_centrifuge_beforeCooling.DSC", exp_type = "francklab_esr/romana")

# # type 2: separate by right peak hyperfine
# lowest hyperfine <3.40
# d['250130 VTU: Medium AOT 1 hr'] = find_file("250130_20mM_TSO4_W20_Isooct_run1.DSC", exp_type = "francklab_esr/romana")
# d['250320: New SL + Old AOT After centrifuge'] = find_file("250320_NewSL_OldAOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")
# d['250321: Old SL + Old AOT'] = find_file("250321_OldSL_Old_AOT_MoreHeating.DSC", exp_type = "francklab_esr/romana")
# d['250314: with NaOH'] = find_file("250314_20mM_TSO4_C8_w20_oldSL_oldAOT_NaOH_convTime12ms.DSC", exp_type = "francklab_esr/romana")
# d['250310: old AOT & SL, 3 day convTime 12 ms'] = find_file("250310_20mM_TSO4_C8_w20_oldSL_oldAOT_3day_equilibrate_convTime12ms.DSC", exp_type = "francklab_esr/romana")
# d['250320: New SL + Old AOT before centrifuge'] = find_file("250320_NewSL_OldAOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
# d['250321: Old SL + Old AOT'] = find_file("250321_OldSL_Old_AOT_MoreHeating.DSC", exp_type = "francklab_esr/romana")
# d['250320: Old SL+ Old AOT After centrifuge'] = find_file("250320_OldSL_Old_AOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")
# d['250324: Old TSO4 (NaOH) + Old AOT'] = find_file("250324_OldAOT_OldTSO4_NaOH.DSC", exp_type = "francklab_esr/romana")
# d['250324: Old TSO4 (HCl) + Old AOT'] = find_file("250324_OldAOT_OldTSO4_HCl.DSC", exp_type = "francklab_esr/romana")

# ##low-middle 3.4-3.45
# d['250321: New SL + New AOT'] = find_file("250321_NewSL_New_AOT_MoreHeating.DSC", exp_type = "francklab_esr/romana")
# d['250320: Old SL+ Old AOT before centrifuge'] = find_file("250320_OldSL_Old_AOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
# d['250320: New SL + New AOT before centrifuge'] = find_file("250320_NewSL_NewAOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
# d['250320: New SL + New AOT After centrifuge'] = find_file("250320_NewSL_NewAOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")
# d['250320: Old SL + New AOT before centrifuge'] = find_file("250320_OldSL_NewAOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
# d['250320: Old SL + New AOT After centrifuge'] = find_file("250320_OldSL_NewAOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")
# d['250318: new materials UP water'] = find_file("250318_20mM_TSO4_C8_w20_UPwater_12ms.DSC", exp_type = "francklab_esr/romana")
# d['250318: new materials DI water'] = find_file("250318_20mM_TSO4_C8_w20_DIwater_12ms.DSC", exp_type = "francklab_esr/romana")
# d['250318: with HCl'] = find_file("250318_20mM_TSO4_C8_w20_HCl_12ms.DSC", exp_type = "francklab_esr/romana")
# d['250313: with heat 1 day'] = find_file("250314_20mM_TSO4_C8_w20_oldSL_oldAOT_heat_1day_convTime12ms", exp_type = "francklab_esr/romana")
# d['250310: old AOT & SL, 3 day convTime 5 ms'] = find_file("250310_20mM_TSO4_C8_w20_oldSL_oldAOT_3day_equilibrate_convTime5ms.DSC", exp_type = "francklab_esr/romana")
# d['250307: old AOT & SL, 1 hr convTime 12 ms'] = find_file("250307_20mM_TSO4_C8_w20_oldSL_oldAOT_convTime12ms.DSC", exp_type = "francklab_esr/romana")
# d['250307: old AOT & SL, 1 hr convTime 5 ms'] = find_file("250307_20mM_TSO4_C8_w20_oldSL_oldAOT_convTime5ms.DSC", exp_type = "francklab_esr/romana")
# d['250313: with heat 1 hr'] = find_file("250313_20mM_TSO4_C8_w20_oldSL_oldAOT_heat_1hr_convTime12ms", exp_type = "francklab_esr/romana")
# d['250324: Old TSO4 + Old AOT'] = find_file("250324_OldAOT_OldTSO4.DSC", exp_type = "francklab_esr/romana")
# d['250324: New TSO4 + New AOT'] = find_file("250324_NewAOT_NewTSO4.DSC", exp_type = "francklab_esr/romana")
# d['250324: New TSO4 + Old AOT'] = find_file("250324_OldAOT_NewTSO4.DSC", exp_type = "francklab_esr/romana")
# d['250324: Old TSO4 + New AOT'] = find_file("250324_NewAOT_OldTSO4.DSC", exp_type = "francklab_esr/romana")

# # # middle 3.45-3.5
d['250225: latest AOT & isooctane'] = find_file("250225_TSO4_20mM_C8_W20_BeforeCooling.DSC", exp_type = "francklab_esr/romana")
d['250210: PChem AOT'] = find_file("250210_20mM_TSO4_C8_W20.DSC", exp_type = "francklab_esr/romana")
d['250206: old AOT + new SL'] = find_file("250206_20mM_TSO4_W20_C8.DSC", exp_type = "francklab_esr/romana")
d['250131: Medium AOT 1 day'] = find_file("250131_20mM_TSO4_Isooct_w20_prep250130.DSC", exp_type = "francklab_esr/romana")
d['241219 VTU: Non-equilibrated'] = find_file("241219_TS_C8_W20_20mM_NonEqui_run1.DSC", exp_type = "francklab_esr/romana")
d['241218 VTU: Reproducibility coarse-T'] = find_file("241218_TS_C8_W20_20mM_run1.DSC", exp_type = "francklab_esr/romana")
d['241213 VTU: 11 mM TSO4'] = find_file("241213_TS_isooct_W20_11mM_run1.DSC", exp_type = "francklab_esr/romana")
d['241210 VTU: Reproducibility fine T-step'] = find_file("241210_TS_isooct_W20_20mM_run1.DSC", exp_type = "francklab_esr/romana")
d['241206 VTU: Reproducibility fine T-step'] = find_file("241206_TS_Isooctane_W20_20mM_run1.DSC", exp_type = "francklab_esr/romana")
d['240808: 10 mM TSO4'] = find_file("240809_10mM_TS_W20_C8.DSC", exp_type = "francklab_esr/romana")
d['240808: 31.6 mM TSO4'] = find_file("240808_31.6mM_TS_W20_C8.DSC", exp_type = "francklab_esr/romana")

# # high >3.5
# d['240220 VTU: manuscript data at 293 K'] = find_file("240220_TempoSO4_W20_run1.DSC", exp_type="francklab_esr/romana") #cooling





for k, v in d.items():
    d[k] = v.chunk_auto("harmonic", "harmonic")["harmonic", 0]["phase", 0]
    if 'VTU' in k or '240220' in k or '250130' in k or '240226' in k:
        d[k].reorder("Temperature").sort("Temperature")
        d[k] = d[k]["Temperature":293]
        
with figlist_var() as fl:
    d = align_esr(d, fl=fl)
    fl.next("normalized after alignment")
    # If the data very dissimilar, the least-squares scaling doesn't
    # work as well.  For these, it makes more sense to use a peak
    # normalization.
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

