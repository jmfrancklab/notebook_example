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
              #('220720_stock_2.DSC',70.0,'TGA stock 2',0.5, '220720','QESR caps',
              #    find_file('220720_background.DSC',exp_type=exp_type)['harmonic',0]),
              #('220720_stock_3.DSC',70.0,'TGA stock 3',0.5, '220720','QESR caps',
              #    find_file('220720_background.DSC',exp_type=exp_type)['harmonic',0]),
              #('220720_stock_4.DSC',70.0,'TGA stock 4',0.5, '220720','QESR caps',
              #    find_file('220720_background.DSC',exp_type=exp_type)['harmonic',0]),
              #('220720_stock_5.DSC',70.0,'TGA stock 5',0.5, '220720','QESR caps',
              #    find_file('220720_background.DSC',exp_type=exp_type)['harmonic',0]),
              #('230417_70mM_TEMPOL.DSC',70.0,'stock on 4-12',0.5, '220720','QESR caps',
              #    find_file('230417_water.DSC',exp_type=exp_type)['harmonic',0]),
              #('230202_stock_1d.DSC',70.0,'230202 stock 1d',0.5, '230202','QESR caps',
              #    find_file('230202_water.DSC',exp_type=exp_type)['harmonic',0]),
              #('230202_stock_2l.DSC',70.0,'230202 stock 2l',0.5, '230202','QESR caps',
              #    find_file('230202_water.DSC',exp_type=exp_type)['harmonic',0]),
               
               
              # ('230621_A_ISOOCTANE_CAT16.DSC', exp_type, '(A) in pure isooctane', 'black', 0.2, 200, '230202', 'QESR caps',
              #      None),
               ('230621_w0_0.DSC', exp_type, 'W0=0', 'cyan', 0.2, 200, '230202', 'QESR caps',
                    None),
               ('230726_CAT16_W0.DSC', exp_type, '(A) W0=0', 'red', 0.2, 200, '230202', 'QESR caps',
                    None), 
             # ('230621_w0_2.DSC', exp_type, 'W0=2', 'orange', 0.2, 200, '230202', 'QESR caps',
             #       None),
             #  ('230621_w0_10.DSC', exp_type, 'W0=10', 'red', 0.2, 200, '230202', 'QESR caps',
             #       None),
             #  ('230621_w0_25.DSC', exp_type, 'W0=25', 'green', 0.2, 200, '230202', 'QESR caps',
             #       None), 
             #  ('230621_w0_50.DSC', exp_type, 'W0=50', 'violet', 0.2, 200, '230202', 'QESR caps',
             #       None)
             

             #('230612_N187_pRbatch230605_pm.DSC', exp_type, 'N187 202 uM', 'orange',0.2, 200, 'AGs','QESR caps',
               #   find_file('230612_water.DSC',exp_type=exp_type)['harmonic',0]),
              #('230612_Q183_pRbatch230605_pm.DSC',exp_type,'Q183 135 uM','blue',0.2, 200,'AGs','QESR caps',
               #   find_file('230612_water.DSC',exp_type=exp_type)['harmonic',0]),
              #('230612_Q183_pRbatch230605.DSC',exp_type,'135 uM', 'blue',0.2, 1038.1508, 'AGs','QESR caps',
              #    find_file('230612_water.DSC',exp_type=exp_type)['harmonic',0]),
             ]):
        d = find_file(thisfile,exp_type = that_exp_type)
        d -= d[fieldaxis, -100:].data.mean()
        if "harmonic" in d.dimlabels:
            d = d['harmonic',0]
        color = thiscolor
        fl.next("Raw QESR")
        fl.plot(d,color=color, label=thislabel,alpha = 0.5)
        rescaled = d.C
        fl.next("Rescaled")
        d /= QESR_scalefactor(d, calibration_name = calibration,
                diameter_name = diameter)
        d -= d[fieldaxis, -100:].data.mean()
        fl.plot(d,color=color,label=thislabel)
        
        norm_d = d.C
        center_field = norm_d.C.argmax().item()#norm_d.getaxis(fieldaxis)[r_[0,-1]].mean()
        norm_d.setaxis(fieldaxis, lambda x:x-center_field)
        dmax = norm_d.C.max()
        dmin = norm_d.C.min()
        delta_d = dmax-dmin
        norm_d /= delta_d
        fl.next('Normalized')
        fl.plot(norm_d, color=color,label=thislabel)
        
    fl.show()