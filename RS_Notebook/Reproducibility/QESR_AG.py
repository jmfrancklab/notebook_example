from matplotlib.pyplot import axvline, axhline, gca
from pint import UnitRegistry
from pyspecdata import *
from itertools import cycle
from pyspecProcScripts import *
from pyspecProcScripts import QESR_scalefactor, QESR
colors = plt.rcParams["axes.prop_cycle"]() # this is the default matplotlib cycler for line styles
fieldaxis = '$B_0$'
exp_type = "francklab_esr/romana"
plot_rescaled = False
all_conc = []
with figlist_var() as fl:
    for filenum, (thisfile, that_exp_type, thislabel, pushout, concscale, calibration, diameter,
            background) in enumerate(
            [
                #{{{
              ('250305_20mM_TSO4_water.DSC',exp_type,'250303: New 20 mM TEMPO-SO4', 0.4, 20.0, 'ags','QESR caps', #conc is in milimolar # ags q = 4600, ags propfactor = 8.637e-5
                  find_file('230511_water.DSC',exp_type=exp_type)['harmonic',0]),
              ('250305_20mM_TSO4_water_lastYears.DSC',exp_type,'231121: Old 20 mM TEMPO-SO4', 0.4, 20.0, 'ags','QESR caps',
                  find_file('230511_water.DSC',exp_type=exp_type)['harmonic',0]),            
              #}}}
              
             ]):
        d = find_file(thisfile,exp_type = that_exp_type)
        d -= d[fieldaxis, -100:].data.mean()
        if "harmonic" in d.dimlabels:
            d = d['harmonic',0]
        color = d.get_plot_color()
        fl.next("Raw QESR")
        fl.plot(d,color=color, label=thislabel,alpha = 0.5)
        rescaled = d.C
        fl.next("Rescaled")
        d /= QESR_scalefactor(d, calibration_name = calibration,
                diameter_name = diameter)
        d -= d[fieldaxis, -100:].data.mean()
        fl.plot(d,color=color,label=thislabel)
        if plot_rescaled:
            center_field = d.C.argmax().item()#norm_d.getaxis(fieldaxis)[r_[0,-1]].mean()
            d.setaxis(fieldaxis,lambda x:x-center_field)
            new_d = d.C
            new_d /= concscale
            fl.next('Rescaled and divided by estimated QESR')
            fl.plot(new_d,label = '%s - divided by %0.4f'%(thislabel,concscale))
        if plot_rescaled:
            pass
        else:        
            norm_d = d.C
            center_field = norm_d.C.argmax().item()#norm_d.getaxis(fieldaxis)[r_[0,-1]].mean()
            norm_d.setaxis(fieldaxis, lambda x:x-center_field)
            dmax = norm_d.C.max()
            dmin = norm_d.C.min()
            delta_d = dmax-dmin
            norm_d /= delta_d
            fl.next('Normalized')
            fl.plot(norm_d, color=color,label=thislabel)
            c = QESR(thisfile, label=thislabel,pushout=pushout,
                    exp_type = that_exp_type,
                    color=color,
                    calibration_name = calibration,
                    diameter_name = diameter,
                    background =  background,
                    which_plot = 'compare',
                    pickle_file = "TEMPOL_rerun_conc.pickle",
                    fl = fl)
            print(thislabel, c)
        all_conc.append(c)
    allconcs = np.array(all_conc)
    ax = gca()
    # ax.text(0.5,0.5,'$%0.2f\\pm%0.2f$'%(np.mean(allconcs), np.std(allconcs, ddof=1)/sqrt(len(allconcs))), transform = ax.transAxes)
