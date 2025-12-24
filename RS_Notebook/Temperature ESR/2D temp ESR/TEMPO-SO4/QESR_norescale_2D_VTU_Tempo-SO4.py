from matplotlib.pyplot import axvline, axhline, gca
from pint import UnitRegistry
from pyspecdata import *
from itertools import cycle
from pyspecProcScripts import *
from pyspecProcScripts import QESR_scalefactor
colors = plt.rcParams["axes.prop_cycle"]() # this is the default matplotlib cycler for line styles
fieldaxis = '$B_0$'
exp_type = "francklab_esr/romana"
all_conc = []
with figlist_var() as fl:
    for filenum, (thisfile, that_exp_type, thislabel, thiscolor, pushout, concscale, calibration, diameter,
            background) in enumerate(
            [
               #21 Dec 20mM TEMPO-SO4 Spin label W0=30 
               ('230118_VTU_run2.DSC', exp_type, 'Room temperature', 'black', 0.2, 200, '230202', 'QESR caps',
                    None),
               # ('231221_TEMP_Tempo_295K.DSC', exp_type, '295K', 'Red', 0.2, 200, '230202', 'QESR caps',
               #      None),
               # ('231221_TEMP_Tempo_285K.DSC', exp_type, '285K', 'orange', 0.2, 200, '230202', 'QESR caps',
               #      None),
               # ('231221_TEMP_Tempo_255K.DSC', exp_type, '255K', 'blue', 0.2, 200, '230202', 'QESR caps',
               #      None),
              

            
                          
             ]):
        d = find_file(thisfile,exp_type = that_exp_type)
        d -= d[fieldaxis, -100:].data.mean()
        if "harmonic" in d.dimlabels:
            d = d['harmonic',0]
        color = thiscolor
        fl.next("Raw QESR")
        fl.plot(d,color=color, label=thislabel,alpha = 1)
        rescaled = d.C
        fl.next("Rescaled")
        d /= QESR_scalefactor(d, calibration_name = calibration,
                diameter_name = diameter)
        d -= d[fieldaxis, -100:].data.mean()
        fl.plot(d,color=color,label=thislabel,alpha = 1)
        
        norm_d = d.C
        center_field = norm_d.C.argmax().item()#norm_d.getaxis(fieldaxis)[r_[0,-1]].mean()
        norm_d.setaxis(fieldaxis, lambda x:x-center_field)
        dmax = norm_d.C.max()
        dmin = norm_d.C.min()
        delta_d = dmax-dmin
        norm_d /= delta_d
        fl.next('Normalized')
        fl.plot(norm_d, color=color,label=thislabel,alpha = 1)
        
    fl.show()