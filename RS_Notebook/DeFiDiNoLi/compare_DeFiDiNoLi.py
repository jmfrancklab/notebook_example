from pyspecdata import *
import numpy as np
from pyspecProcScripts import *
from pyspecProcScripts import QESR_scalefactor
fieldaxis = '$B_0$'
exp_type = "francklab_esr/alex"
# calibration_name = "220720"
T_MW = 172.24 # g/mol
# {{{ calculate error for wet lab concentrations
# A1
ep_weight0 = (
        nddata(r_[859.4,859.4,859.3,859.3]*1e-3).set_units("g").mean(stderr = True)
        )
ep_T_weight0 = (
        nddata(r_[868.1,868,867.9,868.1,868]*1e-3).set_units("g").mean(stderr=True)
        )
ep_w_T_weight0 = (
        nddata(r_[1561.6,1561.8,1561.6,1561.7,1561.7]*1e-3).set_units("g").mean(stderr=True)
        )
#A2
ep_weight1=(
        nddata(r_[830.4,830.2,830.4,830.2]*1e-3).set_units("g").mean(stderr=True)
        )
ep_T_weight1 = (
        nddata(r_[840.2,840.1,840,839.9,840]*1e-3).set_units("g").mean(stderr=True)
        )
ep_w_T_weight1 = (
    nddata(r_[1617.5,1617.4,1617.4,1617.3]*1e-3).set_units("g").mean(stderr=True)
    )
# A3    
ep_weight2 = (
    nddata(r_[856.7,856.7,856.7,856.8]*1e-3).set_units("g").mean(stderr=True)
    )
ep_T_weight2 = (
        nddata(r_[868.1,868.1,868,868.1]*1e-3).set_units("g").mean(stderr=True)
        )
ep_w_T_weight2 = (
        nddata(r_[1832.5,1832.6,1832.8,1832.8,1832.7,1832.7,1832.6]*1e-3).set_units("g").mean(stderr=True)
        )
#A4
ep_weight3 = (
        nddata(r_[830.2,830.3,830.3,830.2]*1e-3).set_units("g").mean(stderr=True)
        )
ep_T_weight3 = (
        nddata(r_[841.9,841.8,841.8,841.8]*1e-3).set_units("g").mean(stderr=True)
        )
ep_w_T_weight3 = (
        nddata(r_[1832.5,1832.6,1832.8,1832.8,1832.7,1832.7,1832.6]*1e-3).set_units("g").mean(stderr=True)
        )
#A5
ep_weight4 = (
        nddata(r_[860.7,860.8,860.7,860.8]*1e-3).set_units("g").mean(stderr=True)
        )
ep_T_weight4 = (
        nddata(r_[871.5,871.4,871.5,871.5]*1e-3).set_units("g").mean(stderr=True)
        )
ep_w_T_weight4 = (
        nddata(r_[1731.7,1731.8,1731.8,1731.8,1731.7,1731.7]*1e-3).set_units("g").mean(stderr=True)
        )
#S1
ep_weight5 = (
        nddata(r_[853.6,853.6,853.5,853.5,853.5]*1e-3).set_units("g").mean(stderr=True)
        )
print(ep_weight5.get_error())
ep_T_weight5 = (
        nddata(r_[868.6,868.6,868.6,868.6,868.7,868.5]*1e-3).set_units("g").mean(stderr=True)
        )
print(ep_T_weight5.get_error())
ep_w_T_weight5 = (
        nddata(r_[2078.6,2078.6,2078.7,2078.8]*1e-3).set_units("g").mean(stderr=True)
        )
print(ep_w_T_weight5.get_error())
#S2
ep_weight6 = (
        # nddata(r_[830.2,830.2,830.2,830.2]*1e-3).set_units("g").mean()
        # ).set_error(1e-16)
        nddata(r_[830.2,830.2,830.2,830.2]*1e-3).set_units("g").mean(stderr=True)
        )
print(ep_weight6.get_error())
ep_T_weight6 = (
        nddata(r_[844.6,844.4,844.4,844.4]*1e-3).set_units("g").mean(stderr=True)
        )
print(ep_T_weight6.get_error())
ep_w_T_weight6 = (
        nddata(r_[1980.8,1980.9,1980.9,1980.8]*1e-3).set_units("g").mean(stderr=True)
        )
print(ep_w_T_weight6.get_error())

wet_lab_concs = []
wet_error = []
DeFiDiNoLi = []
DeFiDiNoLi_v_c = nddata(r_[0:5:1],[-1],["wet_lab"])
c_v_DeFiDiNoLi = nddata(r_[0:5:1],[-1],["DeFiDiNoLi"])
for j,(ep_weight,ep_T_weight, ep_w_T_weight) in enumerate(
        [
            (ep_weight0,ep_T_weight0,ep_w_T_weight0),
            (ep_weight1,ep_T_weight1,ep_w_T_weight1),
        #     (ep_weight2,ep_T_weight2,ep_w_T_weight2),
        #     (ep_weight3,ep_T_weight3,ep_w_T_weight3),
            (ep_weight4,ep_T_weight4,ep_w_T_weight4),
            (ep_weight5,ep_T_weight5,ep_w_T_weight5),
            (ep_weight6,ep_T_weight6,ep_w_T_weight6),
        ]
        ):
    w_vol = (ep_w_T_weight-ep_T_weight)/nddata(0.997).set_units("g/ml").set_units("g/mL")
    T_mol = (ep_T_weight-ep_weight)/nddata(T_MW).set_units("g/mol")
    T_conc = T_mol/w_vol
    T_conc = (T_conc.C.set_units(None)*T_conc.div_units("mM")).set_units("mM")
    wet_lab_concs.append(T_conc.data[0])
    wet_error.append(T_conc.get_error()[0])
DeFiDiNoLi_v_c.setaxis("wet_lab",wet_lab_concs).set_error("wet_lab",np.array(wet_error))
print("wet_lab_concs are:",wet_lab_concs)
c_v_DeFiDiNoLi.data[:] = wet_lab_concs#.set_error("wet_lab",np.array(wet_error))
print("But the nddata I added the wet_lab_concs to is:",c_v_DeFiDiNoLi)
# quit()

with figlist_var() as fl:
    for filenum, (thisfile,thislabel) in enumerate(
            [
              ('250325_72mM_A1_modamp1.DSC',"A1, modamp = 1"),
              ('250325_72mM_TEMPOL_A2_modamp1.DSC',"A2, modamp = 1"),
              #('250325_72mM_TEMPOL_A3_modamp1.DSC'),
              #('250325_72mM_TEMPOL_A4_modamp1.DSC',"A4, modamp = 1"),
              ('250325_72mM_TEMPOL_A5_modamp1.DSC',"A5, modamp = 1"),
              ('250325_72mM_TEMPOL_S1_modamp1.DSC',"S1, modamp = 1"),
              ('250325_72mM_TEMPOL_S2_modamp1.DSC',"S2, modamp = 1"),
             ]):
        d = find_file(thisfile,exp_type = exp_type)
        if "harmonic" in d.dimlabels:
            d = d['harmonic',0]
        fl.next("Raw QESR")
        fl.plot(d,label='%f mM'%(DeFiDiNoLi_v_c["wet_lab"][filenum]*1e3))
        # {{{ Calculate linewidths
        thismax = d.C.argmax().item()
        thismin = d.C.argmin()[fieldaxis]
        lw = thismax-thismin
        print("%0.3f mM linewidth = %0.3f"%(DeFiDiNoLi_v_c["wet_lab"][filenum]*1e3,lw))
        # }}}
        fl.next("Rescaled")
        d = QESR_apply_scalefactor(d)#,
                #diameter_name = calibration_name)
        # {{{ Align 
        s = d.C
        peak = s.C.argmax().item()
        s.setaxis(fieldaxis,lambda x: x-peak)
        fl.plot(s,label='%f mM'%(DeFiDiNoLi_v_c["wet_lab"][filenum]*1e3))
        # }}}
        # {{{ Plot Normalized and align
        d_max = d.C.argmax(fieldaxis)
        d_min = d.C.argmin(fieldaxis)
        pph = d_min - d_max
        fl.next('Normalized')
        norm_d = d.C
        peak = norm_d.C.argmax().item()
        norm_d.setaxis(fieldaxis, lambda x:x-peak)
        # {{{ amplitude norm
        dmax = norm_d.max()
        dmin = norm_d.min()
        delta_d = dmax-dmin
        norm_d /= delta_d
        # }}}
        if "modamp = 1" in thislabel:
            thiscolor = "red"
        else:
            thiscolor = "blue"
        fl.plot(norm_d[fieldaxis:(-20,60)], color = thiscolor,label=thislabel)
        # }}}
        DeFiDiNoLi.append(norm_d[fieldaxis:(0,10)].min())
    DeFiDiNoLi_v_c.data[:] = DeFiDiNoLi
    thisdata = nddata(DeFiDiNoLi,[-1],["wet_lab_c"]).setaxis("wet_lab_c",DeFiDiNoLi_v_c["wet_lab"])
    fl.next("norm'd first min depth vs. wetlab conc")
    fl.plot(thisdata,'o')
    new_data = nddata(DeFiDiNoLi_v_c["wet_lab"],[-1],["DeFiDiNoLi"]).setaxis("DeFiDiNoLi",thisdata.data)
    new_data.set_error(np.array(wet_error))
    fl.next("Wet Lab conc v DeFiDiNoLi, red = modamp of 1, blue = modamp of2")
    fl.plot(new_data,'o',capsize=6)
