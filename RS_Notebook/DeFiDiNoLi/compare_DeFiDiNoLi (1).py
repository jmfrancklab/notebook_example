from pyspecdata import *
import numpy as np
from pyspecProcScripts import *
from pyspecProcScripts import QESR_scalefactor
fieldaxis = '$B_0$'
exp_type = "francklab_esr/alex"
calibration_name = "220720"
with figlist_var() as fl:
    for filenum, (thisfile, wetlab_conc, thislabel,pushout,background) in enumerate(
            [
              ('230222_3p8mM_TEMPOL_3.DSC',3.8, '3.8 mM',0.5,
                  find_file('230110_water.DSC',exp_type=exp_type)['harmonic',0]),
              ('230222_9p4mM_TEMPOL_4.DSC',9.4, '9.4 mM',0.5,
                  find_file('230105_water.DSC',exp_type=exp_type)['harmonic',0]),
              ('230222_200uM_TEMPOL_4.DSC',0.2, '200 uM',0.5,
                  find_file('230105_water.DSC',exp_type=exp_type)['harmonic',0]),
              ('230410_6p5mM_TEMPOL.DSC',6.5, '6.5 mM',0.5,
                  find_file('230105_water.DSC',exp_type=exp_type)['harmonic',0]),
              ('230411_27mM_TEMPOL.DSC',27.0, '27 mM',0.5,
                  find_file('230105_water.DSC',exp_type=exp_type)['harmonic',0]),
              ('230413_35mM_TEMPOL.DSC',35.0, '35 mM',0.5,
                  find_file('230105_water.DSC',exp_type=exp_type)['harmonic',0]),
             ]):
        d = find_file(thisfile,exp_type = exp_type)
        if "harmonic" in d.dimlabels:
            d = d['harmonic',0]
        fl.next("Raw QESR")
        fl.plot(d,label=thislabel)
        # {{{ Calculate linewidths
        thismax = d.C.argmax().item()
        thismin = d.C.argmin()[fieldaxis]
        lw = thismax-thismin
        print("%d linewidth = %0.3f"%(wetlab_conc,lw))
        # }}}
        fl.next("Rescaled")
        d /= QESR_scalefactor(d, calibration_name = calibration_name,
                diameter_name = calibration_name)
        # {{{ Align 
        s = d.C
        peak = s.C.argmax().item()
        s.setaxis(fieldaxis,lambda x: x-peak)
        fl.plot(s,label=thislabel)
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
        fl.plot(norm_d[fieldaxis:(-20,60)], label=thislabel)
        # }}}
        DeFiDiNoLi = norm_d[fieldaxis:(0,10)].min()
        fl.next("norm'd first min depth vs. wetlab conc")
        fl.plot(wetlab_conc,DeFiDiNoLi,'o', label = f'{thislabel} - %0.4f'%DeFiDiNoLi)
