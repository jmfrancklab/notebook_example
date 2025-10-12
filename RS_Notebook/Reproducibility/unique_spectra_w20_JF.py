import matplotlib.pyplot as plt
from cycler import cycler
plt.rcParams['axes.prop_cycle'] = (
        cycler(linestyle=['-',(0,(1,0.5)),(0,(2,0.5))])
        *
        cycler(color='bgrcmyk')
        )
from pyspecdata import find_file, figlist_var, plot
import pyspecdata
from itertools import cycle
pyspecdata.core.default_cycler = cycle('bgrcmyk')
from pyspecProcScripts import align_esr
from itertools import cycle
import numpy as np

# RS had organized things into a dicts, and I think was commented out.  Here, I
# throw all those dicts into another dict (a dict of dicts) to help me organize
# all the data.
d = {}
# compare all RM spectra of w0=20 before cooling
# # separate unique spectra plot
# # type 1: broad peak
d['broad and weird'] = {}
thisd = d['broad and weird']
thisd['250130 VTU: Medium AOT 1 hr'] = find_file("250130_20mM_TSO4_W20_Isooct_run1.DSC", exp_type = "francklab_esr/romana")
thisd['250305: ctrl 1 day'] = find_file("250305_20mM_TSO4_C8_w20_ThinID_1day_Equilibrate_beforeCooling.DSC", exp_type = "francklab_esr/romana")
thisd['250304: ctrl 3 hr'] = find_file("250304_20mM_TSO4_C8_w20_ThinID_beforeCooling.DSC", exp_type = "francklab_esr/romana")
thisd['250304: ctrl 5.5 hr'] = find_file("250304_20mM_TSO4_C8_w20_ThinID_5hrEquilibrate.DSC", exp_type = "francklab_esr/romana")
thisd['250304: ctrl centrifuge'] = find_file("250304_20mM_TSO4_C8_w20_centrifuge_beforeCooling.DSC", exp_type = "francklab_esr/romana")
# water loading series
thisd['230726: 0.5mM TSO4 w0 = 0'] = find_file("230726_TEMPO_SO4_W0.DSC", exp_type = "francklab_esr/romana") # water loading series
thisd['230726: 0.5mM TSO4 w0 = 2'] = find_file("230726_TEMPO_SO4_W2.DSC", exp_type = "francklab_esr/romana") # water loading series
thisd['250113: 20mM TSO4 w0 = 1'] = find_file("250113_20mM_TSO4_W1_Syn2.DSC", exp_type = "francklab_esr/romana") # water loading series
thisd['250113: 20mM TSO4 w0 = 3'] = find_file("250113_20mM_TSO4_W3_Syn2.DSC", exp_type = "francklab_esr/romana") # water loading series
thisd['231221 VT: 20mM TSO4 w0 = 30 at 295K'] = find_file("231221_TEMP_Tempo_295K.DSC", exp_type = "francklab_esr/romana") # water loading series

# # type 2: separate by right peak hyperfine
# lowest hyperfine <3.40
d['low hyperfine'] = {}
thisd = d['low hyperfine']
thisd['250324: New TSO4 + Old AOT'] = find_file("250324_OldAOT_NewTSO4.DSC", exp_type = "francklab_esr/romana")
thisd['250320: New SL + Old AOT After centrifuge'] = find_file("250320_NewSL_OldAOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")
thisd['250321: Old SL + Old AOT'] = find_file("250321_OldSL_Old_AOT_MoreHeating.DSC", exp_type = "francklab_esr/romana")
thisd['250314: with NaOH'] = find_file("250314_20mM_TSO4_C8_w20_oldSL_oldAOT_NaOH_convTime12ms.DSC", exp_type = "francklab_esr/romana")
thisd['250310: old AOT & SL, 3 day convTime 12 ms'] = find_file("250310_20mM_TSO4_C8_w20_oldSL_oldAOT_3day_equilibrate_convTime12ms.DSC", exp_type = "francklab_esr/romana")
thisd['250320: New SL + Old AOT before centrifuge'] = find_file("250320_NewSL_OldAOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
thisd['250321: Old SL + Old AOT'] = find_file("250321_OldSL_Old_AOT_MoreHeating.DSC", exp_type = "francklab_esr/romana")
thisd['250320: Old SL+ Old AOT After centrifuge'] = find_file("250320_OldSL_Old_AOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")
thisd['250324: Old TSO4 (NaOH) + Old AOT'] = find_file("250324_OldAOT_OldTSO4_NaOH.DSC", exp_type = "francklab_esr/romana")
thisd['250324: Old TSO4 (HCl) + Old AOT'] = find_file("250324_OldAOT_OldTSO4_HCl.DSC", exp_type = "francklab_esr/romana")
# water loading series
# thisd['230726: 0.5mM TSO4 w0 = 0'] = find_file("230726_TEMPO_SO4_W0.DSC", exp_type = "francklab_esr/romana") # water loading series
# thisd['230726: 0.5mM TSO4 w0 = 2'] = find_file("230726_TEMPO_SO4_W2.DSC", exp_type = "francklab_esr/romana") # water loading series
# thisd['250113: 20mM TSO4 w0 = 1'] = find_file("250113_20mM_TSO4_W1_Syn2.DSC", exp_type = "francklab_esr/romana") # water loading series
# thisd['250113: 20mM TSO4 w0 = 3'] = find_file("250113_20mM_TSO4_W3_Syn2.DSC", exp_type = "francklab_esr/romana") # water loading series
# thisd['231221 VT: 20mM TSO4 w0 = 30 at 295K'] = find_file("231221_TEMP_Tempo_295K.DSC", exp_type = "francklab_esr/romana") # water loading series

# ## middle 3.4-3.45
d['middle hyperfine'] = {}
thisd = d['middle hyperfine']
thisd['250225: latest AOT & isooctane'] = find_file("250225_TSO4_20mM_C8_W20_BeforeCooling.DSC", exp_type = "francklab_esr/romana")
thisd['250310: old AOT & SL, 3 day convTime 5 ms'] = find_file("250310_20mM_TSO4_C8_w20_oldSL_oldAOT_3day_equilibrate_convTime5ms.DSC", exp_type = "francklab_esr/romana")
thisd['250131: Medium AOT 1 day'] = find_file("250131_20mM_TSO4_Isooct_w20_prep250130.DSC", exp_type = "francklab_esr/romana")
thisd['250313: with heat 1 day'] = find_file("250314_20mM_TSO4_C8_w20_oldSL_oldAOT_heat_1day_convTime12ms", exp_type = "francklab_esr/romana")
thisd['250318: new materials DI water'] = find_file("250318_20mM_TSO4_C8_w20_DIwater_12ms.DSC", exp_type = "francklab_esr/romana")
thisd['250321: New SL + New AOT'] = find_file("250321_NewSL_New_AOT_MoreHeating.DSC", exp_type = "francklab_esr/romana")
thisd['250320: Old SL+ Old AOT before centrifuge'] = find_file("250320_OldSL_Old_AOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
thisd['250320: New SL + New AOT before centrifuge'] = find_file("250320_NewSL_NewAOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
thisd['250320: New SL + New AOT After centrifuge'] = find_file("250320_NewSL_NewAOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")
thisd['250320: Old SL + New AOT before centrifuge'] = find_file("250320_OldSL_NewAOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
thisd['250320: Old SL + New AOT After centrifuge'] = find_file("250320_OldSL_NewAOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")
thisd['250318: new materials UP water'] = find_file("250318_20mM_TSO4_C8_w20_UPwater_12ms.DSC", exp_type = "francklab_esr/romana")
thisd['250318: with HCl'] = find_file("250318_20mM_TSO4_C8_w20_HCl_12ms.DSC", exp_type = "francklab_esr/romana")
thisd['250307: old AOT & SL, 1 hr convTime 12 ms'] = find_file("250307_20mM_TSO4_C8_w20_oldSL_oldAOT_convTime12ms.DSC", exp_type = "francklab_esr/romana")
thisd['250313: with heat 1 hr'] = find_file("250313_20mM_TSO4_C8_w20_oldSL_oldAOT_heat_1hr_convTime12ms", exp_type = "francklab_esr/romana")
thisd['250324: Old TSO4 + Old AOT'] = find_file("250324_OldAOT_OldTSO4.DSC", exp_type = "francklab_esr/romana")
thisd['250324: New TSO4 + New AOT'] = find_file("250324_NewAOT_NewTSO4.DSC", exp_type = "francklab_esr/romana")
thisd['250324: Old TSO4 + New AOT'] = find_file("250324_NewAOT_OldTSO4.DSC", exp_type = "francklab_esr/romana")
# water loading series
thisd['230726: 0.5mM TSO4 w0 = 10'] = find_file("230726_TEMPO_SO4_W10.DSC", exp_type = "francklab_esr/romana") 
thisd['230726: 0.5mM TSO4 w0 = 25'] = find_file("230726_TEMPO_SO4_W25.DSC", exp_type = "francklab_esr/romana") 
thisd['230726: 0.5mM TSO4 w0 = 50'] = find_file("230726_TEMPO_SO4_W50.DSC", exp_type = "francklab_esr/romana") 
thisd['231121 RT: 20mM TSO4 w0 = 30'] = find_file("231121_20mMTEMPOSO4_W30.DSC", exp_type = "francklab_esr/romana") 
thisd['231221 RT: 20mM TSO4 w0 = 30'] = find_file("old_temposo4_rt_231221.DSC", exp_type = "francklab_esr/romana")
thisd['240118 RT: 20mM TSO4 w0 = 30'] = find_file("240118_TempoSo4_W30_RT.DSC", exp_type = "francklab_esr/romana") 
thisd['240118 VTU: 20mM TSO4 w0 = 30 run1 heating'] = find_file("230118_VTU_run1.DSC", exp_type = "francklab_esr/romana")


# # # high >3.45 ← JF regrouped to make simpler
d['high hyperfine'] = {}
thisd = d['high hyperfine']
thisd['250307: old AOT & SL, 1 hr convTime 5 ms'] = find_file("250307_20mM_TSO4_C8_w20_oldSL_oldAOT_convTime5ms.DSC", exp_type = "francklab_esr/romana")
thisd['250206: old AOT + new SL'] = find_file("250206_20mM_TSO4_W20_C8.DSC", exp_type = "francklab_esr/romana")
thisd['241219 VTU: Non-equilibrated'] = find_file("241219_TS_C8_W20_20mM_NonEqui_run1.DSC", exp_type = "francklab_esr/romana")
thisd['241218 VTU: Reproducibility coarse-T'] = find_file("241218_TS_C8_W20_20mM_run1.DSC", exp_type = "francklab_esr/romana")
thisd['241213 VTU: 11 mM TSO4'] = find_file("241213_TS_isooct_W20_11mM_run1.DSC", exp_type = "francklab_esr/romana")
thisd['241210 VTU: Reproducibility fine T-step'] = find_file("241210_TS_isooct_W20_20mM_run1.DSC", exp_type = "francklab_esr/romana")
thisd['241206 VTU: Reproducibility fine T-step'] = find_file("241206_TS_Isooctane_W20_20mM_run1.DSC", exp_type = "francklab_esr/romana")
thisd['240808: 10 mM TSO4'] = find_file("240809_10mM_TS_W20_C8.DSC", exp_type = "francklab_esr/romana")
thisd['240808: 31.6 mM TSO4'] = find_file("240808_31.6mM_TS_W20_C8.DSC", exp_type = "francklab_esr/romana")
thisd['240220 VTU: manuscript data at 293 K'] = find_file("240220_TempoSO4_W20_run1.DSC", exp_type="francklab_esr/romana") #cooling

for kc, thisd in d.items():
    for k, v in thisd.items():
        if 'harmonic' in v.dimlabels:
            thisd[k] = v.chunk_auto("harmonic", "harmonic")["harmonic", 0]["phase", 0]
        if 'Temperature' in v.dimlabels:
            thisd[k].reorder("Temperature").sort("Temperature")
            thisd[k] = thisd[k]["Temperature":293]
        
# flatten so we can align
flattened_dict = { k1+k2:v for k1, thisd in d.items() for k2, v in thisd.items() }
with figlist_var() as fl:
    flattened_dict = align_esr(flattened_dict)
    # {{{ take the flattened data, and put back into the dict of dict.
    #     Realized I don't explicitly need to drop back into the original dict,
    #     but do it anyways.
    fl.next('collect all data', legend=True)
    for k1, thisd in d.items():
        for j, k2 in enumerate(thisd.keys()):
            extra_norm = abs(v.data.max() - v.data.min())
            flattened_dict[k1+k2].set_prop("scaling", flattened_dict[k1+k2].get_prop("scaling") * extra_norm)
            if j == 0:
                fieldname = flattened_dict[k1+k2].dimlabels[0]
            d[k1][k2] = flattened_dict[k1+k2][fieldname:(-1.8,5.4)] / extra_norm #['$B_0$':(-1.8,5.4)]
            if j==0:
                d[k1][k2].set_plot_color_next()
                color = d[k1][k2].get_plot_color()
                fl.plot(d[k1][k2], label=k1, alpha=0.2, ls='-')
            else:
                d[k1][k2].set_plot_color(color)
                fl.plot(d[k1][k2], alpha=0.2, ls='-')
    for k1, thisd in d.items():
        fl.next(k1, legend=True)
        for j, k2 in enumerate(thisd.keys()):
            d[k1][k2].set_plot_color(None) # go back to matplotlib default
            fl.plot(d[k1][k2], label=k2, alpha=0.5)
    # }}}
