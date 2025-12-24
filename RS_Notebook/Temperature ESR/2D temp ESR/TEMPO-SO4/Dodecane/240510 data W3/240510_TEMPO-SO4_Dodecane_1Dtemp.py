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
            #    ('230929_100mM_TEMPOSO4.DSC', exp_type, 'Room temperature', 'black', 0.2, 200, '230202', 'QESR caps',
            #          None),

               #21 Dec 20mM TEMPO-SO4 Spin label W0=30 
               #('old_temposo4_rt_231221.DSC', exp_type, 'Room temperature', 'black', 0.2, 200, '230202', 'QESR caps',
               #      None),
               # ('231221_TEMP_Tempo_295K.DSC', exp_type, '295K', 'Red', 0.2, 200, '230202', 'QESR caps',
               #      None),
               # ('231221_TEMP_Tempo_285K.DSC', exp_type, '285K', 'orange', 0.2, 200, '230202', 'QESR caps',
               #      None),
               # ('231221_TEMP_Tempo_255K.DSC', exp_type, '255K', 'blue', 0.2, 200, '230202', 'QESR caps',
               #      None),

               
               # 240510_TEMPO-SO4_Dodecane_W3S2 
                ('240510_TS_C10_W3S2_223_1D_1.DSC', exp_type, '223K', 'blue', 0.2, 200, '230202', 'QESR caps',
                    None),
                ('240510_TS_C10_W3S2_223_1D_2.DSC', exp_type, '223K', '#61CBF4', 0.2, 200, '230202', 'QESR caps',
                    None),
                
                ('240510_TS_C10_W3S2_243_1D_1.DSC', exp_type, '243K', 'red', 0.2, 200, '230202', 'QESR caps',
                    None),
                ('240510_TS_C10_W3S2_243_1D_2.DSC', exp_type, '243K', 'pink', 0.2, 200, '230202', 'QESR caps',
                    None),
                
                ('240510_TS_C10_W3S2_250_1D_1.DSC', exp_type, '250K', 'black', 0.2, 200, '230202', 'QESR caps',
                    None),
                ('240510_TS_C10_W3S2_250_1D_2.DSC', exp_type, '250K', 'grey', 0.2, 200, '230202', 'QESR caps',
                    None),

                ('240510_TS_C10_W3S2_260_1D_1.DSC', exp_type, '260K', 'orange', 0.2, 200, '230202', 'QESR caps',
                    None),
                ('240510_TS_C10_W3S2_260_1D_2.DSC', exp_type, '260K', 'green', 0.2, 200, '230202', 'QESR caps',
                    None),
                ('240510_TS_C10_W3S2_260_1D_3.DSC', exp_type, '260K', 'magenta', 0.2, 200, '230202', 'QESR caps',
                    None),

                ('240510_TS_C10_W3S2_270_1D_1.DSC', exp_type, '270K', '#5B2076', 0.2, 200, '230202', 'QESR caps',
                    None),
                ('240510_TS_C10_W3S2_270_1D_2.DSC', exp_type, '270K', '#BD7BDB', 0.2, 200, '230202', 'QESR caps',
                    None),

                ('240510_TS_C10_W3S2_283_1D_1.DSC', exp_type, '283K', '#4A682E', 0.2, 200, '230202', 'QESR caps',
                    None),
                ('240510_TS_C10_W3S2_283_1D_2.DSC', exp_type, '283K', '#90E2E4', 0.2, 200, '230202', 'QESR caps',
                    None),

                ('240510_TS_C10_W3S2_293_1D_1.DSC', exp_type, '293K', '#43C220', 0.2, 200, '230202', 'QESR caps',
                    None),
                ('240510_TS_C10_W3S2_293_1D_1.DSC', exp_type, '293K', '#E05702', 0.2, 200, '230202', 'QESR caps',
                    None),
                
                ('240510_TS_C10_W3S2_run4.DSC', exp_type, 'after cooling and heating', 'red', 0.2, 200, '230202', 'QESR caps',
                    None)


                # ('240510_TS_C10_W3S2_270_1D_1.DSC', exp_type, '255K', 'blue', 0.2, 200, '230202', 'QESR caps',
                #     None),
                # ('240510_TS_C10_W3S2_270_1D_1.DSC', exp_type, '255K', 'blue', 0.2, 200, '230202', 'QESR caps',
                #     None),
                # ('240510_TS_C10_W3S2_270_1D_1.DSC', exp_type, '255K', 'blue', 0.2, 200, '230202', 'QESR caps',
                #     None),                          
             ]):
        d = find_file(thisfile,exp_type = that_exp_type)
        if thislabel == 'after cooling and heating':
              d = d["Temperature":283] ##RS
       # d = d["Temperature":293] ##RS
        d -= d[fieldaxis, -100:].data.mean()
        if "harmonic" in d.dimlabels:
            d = d['harmonic',0]
       # d = d["Temperature":293] ##RS
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