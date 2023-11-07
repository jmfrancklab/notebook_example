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
    for filenum, (thisfile, that_exp_type, thislabel, thiscolor, pushout, concscale, calibration, diameter, const) in enumerate(
            [
              
               
              # ('230621_A_ISOOCTANE_CAT16.DSC', exp_type, '(A) in pure isooctane', 'black', 0.2, 200, '230202', 'QESR caps',
              #      50),
               ('230621_w0_0.DSC', exp_type, '(A) W0=0', 'red', 0.2, 200, '230202', 'QESR caps',
                    35),
               ('230621_w0_2.DSC', exp_type, '(B) W0=2', 'orange', 0.2, 200, '230202', 'QESR caps',
                    30),
               ('230621_w0_10.DSC', exp_type, '(C) W0=10', 'black', 0.2, 200, '230202', 'QESR caps',
                    20),
               ('230621_w0_25.DSC', exp_type, '(D) W0=25', 'green', 0.2, 200, '230202', 'QESR caps',
                    10), 
               ('230621_w0_50.DSC', exp_type, '(E) W0=50', 'blue', 0.2, 200, '230202', 'QESR caps',
                    0)
            
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
        d += const
        fl.plot(d,color=color,label=thislabel,alpha = 1)#ROMANA, IF YOU DON'T WANT THE LABELS CHANGE THIS TO BE label =None
        
        norm_d = d.C
        center_field = norm_d.C.argmax().item()#norm_d.getaxis(fieldaxis)[r_[0,-1]].mean()
        norm_d.setaxis(fieldaxis, lambda x:x-center_field)
        dmax = norm_d.C.max()
        dmin = norm_d.C.min()
        delta_d = dmax-dmin
        norm_d /= delta_d
        fl.next('Normalized')
        fl.plot(norm_d, color=color,label=thislabel,alpha = 1)#ROMANA, SAME THING HERE IF YOU DON'T WANT LABELS
        
    fl.show()
