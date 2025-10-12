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
                          
               ('230726_TEMPO_SO4_W0.DSC', exp_type, '(A) W0=0', 'cyan', 0.2, 200, '230202', 'QESR caps',
                    None),
               ('230726_TEMPO_SO4_W2.DSC', exp_type, '(B) W0=2', 'green', 0.2, 200, '230202', 'QESR caps',
                    None),
               ('230726_TEMPO_SO4_W10.DSC', exp_type, '(C) W0=10', 'violet', 0.2, 200, '230202', 'QESR caps',
                    None),
               ('230726_TEMPO_SO4_W25.DSC', exp_type, '(D) W0=25', 'red', 0.2, 200, '230202', 'QESR caps',
                    None), 
               ('230726_TEMPO_SO4_W50.DSC', exp_type, '(E) W0=50', 'blue', 0.2, 200, '230202', 'QESR caps',
                    None),
               
               ### for 2D temperature data
               ('240220_TempoSO4_W20_run2.DSC', exp_type, 'after cooling and heating', 'black', 0.2, 200, '230202', 'QESR caps',
                    None)           
             ]):
        d = find_file(thisfile,exp_type = that_exp_type)
        
        ### RS: for 2D Temperatutre data [
        if thislabel == 'after cooling and heating':
              d = d["Temperature":293] ## RS ]
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

        ### RS: 2D Temperature
        if (thislabel == '(A) W0=0') or (thislabel == '(B) W0=2'):
             print("HASDKFASPIUHFSAEUG")
             print(norm_d.getaxis(fieldaxis))
             center_field = norm_d[fieldaxis:(3424.55,3574.50605)].C.argmax().item()
        else:
          center_field = norm_d.C.argmax().item()#norm_d.getaxis(fieldaxis)[r_[0,-1]].mean()
        
     #    center_field = norm_d.C.argmax().item()#norm_d.getaxis(fieldaxis)[r_[0,-1]].mean() ### RS: hide it for running 2D Temperature
        norm_d.setaxis(fieldaxis, lambda x:x-center_field)
        dmax = norm_d.C.max()
        dmin = norm_d.C.min()
        delta_d = dmax-dmin
        norm_d /= delta_d
        fl.next('Normalized')
        fl.plot(norm_d, color=color,label=thislabel,alpha = 1)
        
    fl.show()