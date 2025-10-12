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
               #Trial 1= 16-17 Nov
               # ('231116_TEMPOSO4_W30.DSC', exp_type, '100 mM TEMPOSO4 W0=30', 'black', 0.2, 200, '230202', 'QESR caps',
               #      None),
               # ('231116_Empty_W30.DSC', exp_type, 'Empty RM W0=30', 'red', 0.2, 200, '230202', 'QESR caps',
               #      None),
               # ('231116_Mix_Empty_TEMPOSO4_W30.DSC', exp_type, 'Empty RM+Tempo-SO4 trial 1', 'green', 0.2, 200, '230202', 'QESR caps',
               #      None),
               # ('231117_Mix_Empty_TEMPO_day2.DSC', exp_type, 'Empty RM+Tempo-SO4 trial 1 day2', 'violet', 0.2, 200, '230202', 'QESR caps',
               #      None),
               
               #Trial 2= 18 Nov
               # ('231116_TEMPOSO4_W30.DSC', exp_type, '100 mM TEMPOSO4 W0=30', 'black', 0.2, 200, '230202', 'QESR caps',
               #      None),
               # ('231118_Empty_W30.DSC', exp_type, 'Empty RM W0=30', 'red', 0.2, 200, '230202', 'QESR caps',
               #      None),
               # ('231118_Mix_Empty_TEMPO_100mins.DSC', exp_type, 'Empty RM+Tempo-SO4 trial 2 100 mins', 'teal', 0.2, 200, '230202', 'QESR caps',
               #      None),
               # ('231118_Mix_Empty_TEMPO_120mins.DSC', exp_type, 'Empty RM+Tempo-SO4 trial 2 120mins', 'purple', 0.2, 200, '230202', 'QESR caps',
               #      None),

               #Trial 3= 19 Nov
               # ('231119_TEMPOSO4_W30.DSC', exp_type, '100 mM TEMPOSO4 W0=30', 'black', 0.2, 200, '230202', 'QESR caps',
               #      None),
               # ('231118_Empty_W30.DSC', exp_type, 'Empty RM W0=30', 'red', 0.2, 200, '230202', 'QESR caps',
               #      None),
               # ('231119_Mix_Empty_TEMPO_5mins.DSC', exp_type, 'Empty RM+Tempo-SO4  5mins', 'green', 0.2, 200, '230202', 'QESR caps',
               #      None),
               # ('231119_Mix_Empty_TEMPO_25mins.DSC', exp_type, 'Empty RM+Tempo-SO4 25mins', 'blue', 0.2, 200, '230202', 'QESR caps',
               #      None),
               # ('231119_Mix_Empty_TEMPO_45mins.DSC', exp_type, 'Empty RM+Tempo-SO4 45mins', 'yellow', 0.2, 200, '230202', 'QESR caps',
               #      None),
               # ('231119_Mix_Empty_TEMPO_60mins.DSC', exp_type, 'Empty RM+Tempo-SO4 60mins', 'purple', 0.2, 200, '230202', 'QESR caps',
               #      None),               
               # ('231119_Mix_Empty_TEMPO_90mins.DSC', exp_type, 'Empty RM+Tempo-SO4 90mins', 'orange', 0.2, 200, '230202', 'QESR caps',
               #      None),
               # ('231119_Mix_Empty_TEMPO_105mins.DSC', exp_type, 'Empty RM+Tempo-SO4 105mins', 'brown', 0.2, 200, '230202', 'QESR caps',
               #      None),   

               #Trial 4= 21 Nov 20mM TEMPO-SO4 Spin label
               ('231121_Empty_W30.DSC', exp_type, 'Empty RM W0=30', 'red', 0.2, 200, '230202', 'QESR caps',
                    None),
               ('231121_20mMTEMPOSO4_W30.DSC', exp_type, '20 mM TEMPOSO4 RM W0=30', 'black', 0.2, 200, '230202', 'QESR caps',
                    None),
               ('231121_Mix_Empty_20mMTEMPO_30mins.DSC', exp_type, 'Mix RMs 30 mins', 'green', 0.2, 200, '230202', 'QESR caps',
                    None),
               ('231121_Mix_Empty_20mMTEMPO_45mins.DSC', exp_type, 'Mix RMs 45 mins', 'blue', 0.2, 200, '230202', 'QESR caps',
                    None),
               ('231121_Mix_Empty_20mMTEMPO_65mins.DSC', exp_type, 'Mix RMs 65 mins', 'cyan', 0.2, 200, '230202', 'QESR caps',
                    None),
               ('231121_Mix_Empty_20mMTEMPO_75mins.DSC', exp_type, 'Mix RMs 75 mins', 'purple', 0.2, 200, '230202', 'QESR caps',
                    None),               
               ('231121_Mix_Empty_20mMTEMPO_100mins.DSC', exp_type, 'Mix RMs 100 mins', 'orange', 0.2, 200, '230202', 'QESR caps',
                    None),
               ('231121_Mix_Empty_20mMTEMPO_120mins.DSC', exp_type, 'Mix RMs 120 mins', 'brown', 0.2, 200, '230202', 'QESR caps',
                    None),        

              
                          
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