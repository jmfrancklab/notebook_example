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
# d['240220 VTU: manuscript data'] = find_file("240220_TempoSO4_W20_run1.DSC", exp_type="francklab_esr/romana") #cooling
# d['240220 VTU: manuscript data reheating at 293K'] = find_file("240220_TempoSO4_W20_run2.DSC", exp_type="francklab_esr/romana") #reheating

# # # Compare previous capillaries
# d['250501: same capillary tube room temp'] = find_file("250501_20mM_TSO4_C8_W20_previous_240220.DSC", exp_type = "francklab_esr/romana")
# # d['250501: capillary for w0=3'] = find_file("250501_20mM_TSO4_C8_W3_previous_240220.DSC", exp_type = "francklab_esr/romana")

# 250130: bad data VTU Medium AOT
# d['250130 VTU: RM prepared using AOT aged 1 year'] = find_file("250130_20mM_TSO4_W20_Isooct_run1.DSC", exp_type="francklab_esr/romana") #cooling
# d['250130 VTU: after cooling and reheating at 293K'] = find_file("250130_20mM_TSO4_W20_Isooct_run3.DSC", exp_type="francklab_esr/romana") #reheating

# 250206 using same AOT solution from 240217
# d['250206: RM prepared using the same AOT solution as 240220'] = find_file("250206_20mM_TSO4_W20_C8.DSC", exp_type="francklab_esr/romana")
# d['250206: After cooling bath'] = find_file("250206_20mM_TSO4_W20_C8_cooled.DSC", exp_type="francklab_esr/romana")

# 250210 New PChem AOT
# d['250210: RM prepared using new AOT and new UP water'] = find_file("250210_20mM_TSO4_C8_W20.DSC", exp_type="francklab_esr/romana")
# d['250210: New AOT after cooling bath'] = find_file("250210_20mM_TSO4_C8_W20_Cooled.DSC", exp_type="francklab_esr/romana")

# 250225 latest ordered AOT and Isooctane and UP water
# d['250225: RM with latest AOT and isooctane before cooling']= find_file("250225_TSO4_20mM_C8_W20_BeforeCooling.DSC", exp_type = "francklab_esr/romana")
# d['250225: RM with latest AOT and isooctane after cooling']= find_file("250225_TSO4_20mM_C8_W20_AfterCooling.DSC", exp_type = "francklab_esr/romana")
# d['250225: RM with latest AOT and isooctane after cooling EPR tube']= find_file("250225_TSO4_20mM_C8_W20_AfterCooling_EPRtube.DSC", exp_type = "francklab_esr/romana")

# {{ control experiments 
# Exp 1: NMR tube experiment
# d['Capillary tube before cooling'] = find_file("250304_20mM_TSO4_C8_w20_ThinID_beforeCooling.DSC", exp_type = "francklab_esr/romana")
# d['Capillary tube after cooling'] = find_file("250304_20mM_TSO4_C8_w20_ThinID_afterCooling.DSC", exp_type = "francklab_esr/romana")
# d['NMR tube top layer after water shedding'] = find_file("250304_20mM_TSO4_C8_w20_NMRTubeTopLayer_afterCooling.DSC", exp_type = "francklab_esr/romana")

# Exp 2: Thick (ID 1.6 mm) vs Thin (ID 0.704 mm) capillary tube
# d["Thin capillary tube (ID 0.704 mm)"] = find_file("250304_20mM_TSO4_C8_w20_ThinID_beforeCooling.DSC", exp_type = "francklab_esr/romana")
# d["Thicker capillary tube (ID 1.6256 mm)"] = find_file("250304_20mM_TSO4_C8_w20_ThickID_beforeCooling.DSC", exp_type ="francklab_esr/romana")

# Exp 3: Equilibration time
# d["Equilibration time 3 hr"] = find_file("250304_20mM_TSO4_C8_w20_ThinID_beforeCooling.DSC", exp_type = "francklab_esr/romana")
# d["Equilibration time 5.5 hr"] = find_file("250304_20mM_TSO4_C8_w20_ThinID_5hrEquilibrate.DSC", exp_type = "francklab_esr/romana")
# d["Equilibration time 1 day"] = find_file("250305_20mM_TSO4_C8_w20_ThinID_1day_Equilibrate_beforeCooling.DSC", exp_type = "francklab_esr/romana")

# Exp 4: Centrfugation effect
# d["Without centrifuge before cooling"] = find_file("250304_20mM_TSO4_C8_w20_ThinID_beforeCooling.DSC", exp_type = "francklab_esr/romana")
# d["Without centrifuge after cooling"] = find_file("250304_20mM_TSO4_C8_w20_ThinID_afterCooling.DSC", exp_type = "francklab_esr/romana")
# d["With centrifuge before cooling"] = find_file("250304_20mM_TSO4_C8_w20_centrifuge_beforeCooling.DSC", exp_type = "francklab_esr/romana")
# d["With centrifuge after cooling"] = find_file("250304_20mM_TSO4_C8_w20_centrifuge_afterCooling.DSC", exp_type = "francklab_esr/romana")

# # Exp 5: Cooling bath at -28 C
# d["Equilibration time 1 day before cooling"] = find_file("250305_20mM_TSO4_C8_w20_ThinID_1day_Equilibrate_beforeCooling.DSC", exp_type = "francklab_esr/romana")
# d["Equilibration time 1 day after cooling"] = find_file("250305_20mM_TSO4_C8_w20_ThinID_1day_Equilibrate_afterCooling.DSC", exp_type = "francklab_esr/romana")

# Exp 6: Stock solution 20 mM 250303 vs 231121
# d["(Broad) QESR of 20 mM TEMPO-SO4 prepared 250303"] = find_file("250305_20mM_TSO4_water.DSC", exp_type = "francklab_esr/romana")
# d["(Control) QESR of old 20 mM TEMPO-SO4 prepared 231121"] = find_file("250305_20mM_TSO4_water_lastYears.DSC", exp_type = "francklab_esr/romana")

# Exp 7: Compare coversion time
# d["Conversion time 4 ms"] = find_file("250122_TEMPOSO4_100uM_2ndSynthesis_sameParameter250112.DSC", exp_type = "francklab_esr/romana")
# d["Conversion time 12 ms"] = find_file("test250122_small_app_A_cc.DSC", exp_type = "francklab_esr/romana")
# 250307
# d["Conversion time 4 ms"] = find_file("250307_100uM_TSO4_ConvTime4ms_CapillaryFrom_250122.DSC", exp_type = "francklab_esr/romana")
# d["Conversion time 12 ms"] = find_file("250307_100uM_TSO4_CapillaryFrom_250122.DSC", exp_type = "francklab_esr/romana")

# Exp 8: prep RM with old SL & old AOT solution --with varying conversion time
# d['250307: RM with old SL+AOT solution, convTime 5 ms'] = find_file("250307_20mM_TSO4_C8_w20_oldSL_oldAOT_convTime5ms.DSC", exp_type = "francklab_esr/romana")
# d['250307: RM with old SL+AOT solution, convTime 12 ms'] = find_file("250307_20mM_TSO4_C8_w20_oldSL_oldAOT_convTime12ms.DSC", exp_type = "francklab_esr/romana")

# Exp 9: prep RM with old SL & old AOT solution --with varying number of scan
# d['250307: scan 5'] = find_file("250307_20mM_TSO4_C8_w20_oldSL_oldAOT_convTime12ms.DSC", exp_type = "francklab_esr/romana")
# d['250307: scan 25'] = find_file("250307_20mM_TSO4_C8_w20_oldSL_oldAOT_convTime12ms_scan25.DSC", exp_type = "francklab_esr/romana")

# Exp 10: prep RM with old SL & old AOT solution --after cooling bath
# 5 ms
# d['250307: convTime 5ms before cooling'] = find_file("250307_20mM_TSO4_C8_w20_oldSL_oldAOT_convTime5ms.DSC", exp_type = "francklab_esr/romana")
# d['250307: convTime 5ms after cooling'] = find_file("250307_20mM_TSO4_C8_w20_oldSL_oldAOT_convTime5ms_afterCoolingBath.DSC", exp_type = "francklab_esr/romana")
# # 12 ms
# d['250307: convTime 12ms before cooling'] = find_file("250307_20mM_TSO4_C8_w20_oldSL_oldAOT_convTime12ms.DSC", exp_type = "francklab_esr/romana")
# d['250307: convTime 12ms after cooling'] = find_file("250307_20mM_TSO4_C8_w20_oldSL_oldAOT_convTime12ms_afterCoolingBath.DSC", exp_type = "francklab_esr/romana")

# Exp 11: prep RM with old SL & old AOT solution -- 3 day equilibrate 
# 5 ms
# d['250310: 3day equilibrate convTime 5ms before cooling'] = find_file("250310_20mM_TSO4_C8_w20_oldSL_oldAOT_3day_equilibrate_convTime5ms.DSC", exp_type = "francklab_esr/romana")
# d['250310: 3day equilibrate convTime 5ms after cooling'] = find_file("250310_20mM_TSO4_C8_w20_oldSL_oldAOT_3day_equilibrate_convTime5ms_afterCooling.DSC", exp_type = "francklab_esr/romana")
# # 12 ms
# d['250310: 3day equilibrate convTime 12ms before cooling'] = find_file("250310_20mM_TSO4_C8_w20_oldSL_oldAOT_3day_equilibrate_convTime12ms.DSC", exp_type = "francklab_esr/romana")
# d['250310: 3day equilibrate convTime 12ms after cooling'] = find_file("250310_20mM_TSO4_C8_w20_oldSL_oldAOT_3day_equilibrate_convTime12ms_afterCooling.DSC", exp_type = "francklab_esr/romana")

# Exp 12: effect of heat: old SL & old AOT solution
# # 5 ms
# d['250313: with heat 1 hr'] = find_file("250313_20mM_TSO4_C8_w20_oldSL_oldAOT_heat_1hr_convTime5ms", exp_type = "francklab_esr/romana")
# d['250313: with heat 1 day'] = find_file("250314_20mM_TSO4_C8_w20_oldSL_oldAOT_heat_1day_convTime5ms", exp_type = "francklab_esr/romana")
# d['250307: without heat 1hr'] = find_file("250307_20mM_TSO4_C8_w20_oldSL_oldAOT_convTime5ms.DSC", exp_type = "francklab_esr/romana")
# # 12 ms
# d['250313: with heat 1 hr'] = find_file("250313_20mM_TSO4_C8_w20_oldSL_oldAOT_heat_1hr_convTime12ms", exp_type = "francklab_esr/romana")
# d['250313: with heat 1 day'] = find_file("250314_20mM_TSO4_C8_w20_oldSL_oldAOT_heat_1day_convTime12ms", exp_type = "francklab_esr/romana")
# d['250307: Without heat 1hr'] = find_file("250307_20mM_TSO4_C8_w20_oldSL_oldAOT_convTime12ms.DSC", exp_type = "francklab_esr/romana")

# Exp 13: effect of NaOH
# d['250314: with NaOH'] = find_file("250314_20mM_TSO4_C8_w20_oldSL_oldAOT_NaOH_convTime12ms.DSC", exp_type = "francklab_esr/romana")
# d['250313: without NaOH'] = find_file("250313_20mM_TSO4_C8_w20_oldSL_oldAOT_heat_1hr_convTime12ms.DSC", exp_type = "francklab_esr/romana")
# spin label only (not RM)
# d['250314: QESR of TEMPO-SO4 with NaOH'] = find_file("250314_20mM_TSO4_water_old_NaOH.DSC", exp_type = "francklab_esr/romana")
# d['250313: QESR of TEMPO-SO4 without NaOH'] = find_file("250314_20mM_TSO4_water_convTime12ms.DSC", exp_type = "francklab_esr/romana")

# Exp 14: reproduce reasonable spectra with new materials UP water
# d['250318: new materials 5 ms'] = find_file("250318_20mM_TSO4_C8_w20_UPwater_5ms.DSC", exp_type = "francklab_esr/romana")
# d['250318: new materials 12 ms'] = find_file("250318_20mM_TSO4_C8_w20_UPwater_12ms.DSC", exp_type = "francklab_esr/romana")
# d['250318 VT: new materials 293K'] = find_file("250318_20mM_TSO4_C8_w20_UPwater_12ms_293K.DSC", exp_type = "francklab_esr/romana")

# # Exp 15: reproduce reasonable spectra with new materials
# d['250318: new materials UP water'] = find_file("250318_20mM_TSO4_C8_w20_UPwater_12ms.DSC", exp_type = "francklab_esr/romana")
# d['250318: new materials DI water'] = find_file("250318_20mM_TSO4_C8_w20_DIwater_12ms.DSC", exp_type = "francklab_esr/romana")

# # Exp 16: effect of HCl
# d['250318: without HCl'] = find_file("250318_20mM_TSO4_C8_w20_UPwater_12ms.DSC", exp_type = "francklab_esr/romana")
# d['250318: with HCl'] = find_file("250318_20mM_TSO4_C8_w20_HCl_12ms.DSC", exp_type = "francklab_esr/romana")

# # Exp 17: Old SL + Old AOT 
# d['250320: Old SL+ Old AOT before centrifuge'] = find_file("250320_OldSL_Old_AOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
# # d['250320: Old SL+ Old AOT After centrifuge'] = find_file("250320_OldSL_Old_AOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")

# # # Exp 18: New SL + New AOT 
# d['250320: New SL + New AOT before centrifuge'] = find_file("250320_NewSL_NewAOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
# # d['250320: New SL + New AOT After centrifuge'] = find_file("250320_NewSL_NewAOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")

# # # Exp 19: Old SL + New AOT 
# d['250320: Old SL + New AOT before centrifuge'] = find_file("250320_OldSL_NewAOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
# # d['250320: Old SL + New AOT After centrifuge'] = find_file("250320_OldSL_NewAOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")

# # # Exp 20: New SL + Old AOT 
# d['250320: New SL + Old AOT before centrifuge'] = find_file("250320_NewSL_OldAOT_beforeCentrifuge.DSC", exp_type = "francklab_esr/romana")
# # d['250320: New SL + Old AOT After centrifuge'] = find_file("250320_NewSL_OldAOT_AfterCentrifuge.DSC", exp_type = "francklab_esr/romana")

# # # Exp 21: More Heating 
# d['250321: Old SL + Old AOT'] = find_file("250321_OldSL_Old_AOT_MoreHeating.DSC", exp_type = "francklab_esr/romana")
# d['250321: New SL + New AOT'] = find_file("250321_NewSL_New_AOT_MoreHeating.DSC", exp_type = "francklab_esr/romana")
# # d['250321: Old SL + Old AOT another capillary'] = find_file("250321_OldSL_Old_AOT_MoreHeating_2.DSC", exp_type = "francklab_esr/romana")
# # d['250321: New SL + New AOT another capillary'] = find_file("250321_NewSL_New_AOT_MoreHeating_2.DSC", exp_type = "francklab_esr/romana")

# ## Exp 22: 6 RM (Old + New combination)
# d['250324: Old TSO4 + Old AOT'] = find_file("250324_OldAOT_OldTSO4.DSC", exp_type = "francklab_esr/romana")
# d['250324: New TSO4 + New AOT'] = find_file("250324_NewAOT_NewTSO4.DSC", exp_type = "francklab_esr/romana")
# d['250324: New TSO4 + Old AOT'] = find_file("250324_OldAOT_NewTSO4.DSC", exp_type = "francklab_esr/romana")
# d['250324: Old TSO4 + New AOT'] = find_file("250324_NewAOT_OldTSO4.DSC", exp_type = "francklab_esr/romana")
# # d['250324: Old TSO4 (NaOH) + Old AOT'] = find_file("250324_OldAOT_OldTSO4_NaOH.DSC", exp_type = "francklab_esr/romana")
# d['250324: Old TSO4 (HCl) + Old AOT'] = find_file("250324_OldAOT_OldTSO4_HCl.DSC", exp_type = "francklab_esr/romana")

# Exp: effect of pH
# d['250324: Control (old materials'] = find_file("250324_OldAOT_OldTSO4.DSC", exp_type = "francklab_esr/romana")
# d['250314: NaOH (old materials)'] = find_file("250314_20mM_TSO4_C8_w20_oldSL_oldAOT_NaOH_convTime12ms.DSC", exp_type = "francklab_esr/romana")
# d['250318: HCl (new materials)'] = find_file("250318_20mM_TSO4_C8_w20_HCl_12ms.DSC", exp_type = "francklab_esr/romana")
# d['250324: NaOH (old materials)'] = find_file("250324_OldAOT_OldTSO4_NaOH.DSC", exp_type = "francklab_esr/romana")
# d['250324: HCl (old materials)'] = find_file("250324_OldAOT_OldTSO4_HCl.DSC", exp_type = "francklab_esr/romana")
# #d['250324: HCl (old materials) rerun'] = find_file("250324_OldAOT_OldTSO4_HCl_2.DSC", exp_type = "francklab_esr/romana")

# # Exp: 250328
# d['250328: Freshly prepared old AOT (purchased 2023)'] = find_file("250328_20mMTSO4_C8_W20_OldAOTbottle23.DSC", exp_type = "francklab_esr/romana")
# d['250328: Freshly prepared New AOT RM1 (purchased 2025)'] = find_file("250328_20mMTSO4_C8_W20_NewAOTbottle25_RM1.DSC", exp_type = "francklab_esr/romana")
# d['250328: Freshly prepared New AOT RM2 (purchased 2025)'] = find_file("250328_20mMTSO4_C8_W20_NewAOTbottle25_RM2.DSC", exp_type = "francklab_esr/romana")
# ### # to compare
# d['250324: RM prepared with Old AOT solution (prepared 2023)'] = find_file("250324_OldAOT_OldTSO4.DSC", exp_type = "francklab_esr/romana")
# d['250324: RM prepared with New AOT solution (prepared 2025)'] = find_file("250324_NewAOT_NewTSO4.DSC", exp_type = "francklab_esr/romana")

# # # Exp: 250402
# d['250328: Friday data'] = find_file("250328_20mMTSO4_C8_W20_OldAOTbottle23.DSC", exp_type = "francklab_esr/romana")
# d['250402: rerun same capillary from 200328'] = find_file("250402_20mM_TSO4_C8_W20.DSC", exp_type = "francklab_esr/romana")
# d['250402: rerun thick capillary'] = find_file("250402_20mM_TSO4_C8_W20_ThickID.DSC", exp_type = "francklab_esr/romana")

# # Exp: Timeseries 5 mM
# d['250404: 5mM shedding temp 232K'] = find_file("250404_5mM_TSO4_C8_W20_RT.DSC", exp_type = "francklab_esr/romana")
# d['250425: 5mM shedding temp 254K'] = find_file("250425_5mM_TSO4_C8_W20_RT.DSC", exp_type = "francklab_esr/romana")
# d['250428: 5mM shedding temp 260K'] = find_file("250428_5mM_TSO4_C8_W20_RT.DSC", exp_type = "francklab_esr/romana")
# d['250501: 5mM'] = find_file("250501_5mM_TSO4_C8_W20_RT.DSC", exp_type = "francklab_esr/romana")

# 240220 manuscript data VTU
d['240220 VTU: manuscript data cooling at 293K'] = find_file("240220_TempoSO4_W20_run1.DSC", exp_type="francklab_esr/romana") #cooling
d['240220 VTU: manuscript data reheating at 293K'] = find_file("240220_TempoSO4_W20_run2.DSC", exp_type="francklab_esr/romana") #reheating

# # Compare previous capillaries
d['250501: same capillary tube acquired today in RT'] = find_file("250501_20mM_TSO4_C8_W20_previous_240220.DSC", exp_type = "francklab_esr/romana")
# d['250501: capillary for w0=3'] = find_file("250501_20mM_TSO4_C8_W3_previous_240220.DSC", exp_type = "francklab_esr/romana")





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
 
