from matplotlib.pyplot import axvline, axhline, gca
from pint import UnitRegistry
from pyspecdata import *
from itertools import cycle
from pyspecProcScripts import *
from pyspecProcScripts import QESR_scalefactor
colors = plt.rcParams["axes.prop_cycle"]() # this is the default matplotlib cycler for line styles
init_logging(level='debug')
fieldaxis = '$B_0$'
exp_type = "francklab_esr/romana" #Change to your folder or the folder with the files you want to look at
plot_rescaled = False #Run with False for double integral to get conc, change to True to compare to relative concentration with another sample  
all_conc = []
with figlist_var() as fl:
    for filenum, (thisfile, that_exp_type, thislabel, thiscolor, pushout, concscale, calibration, diameter,
            background) in enumerate(
            [
              ('230511_CAT16QESR.DSC', exp_type, 'L118 2-28-24', 'darkmagenta', 0.5, 300, 'AGs', 'QESR caps',
                  find_file('230511_water.DSC', exp_type=exp_type)['harmonic',0]),
              #('230628_TEMPOL_dil1.DSC', exp_type,'230628 TEMPOL 1:3 dilution','blue', 0.2,210,'AGs','QESR caps',
              #      None), #If you don't use a background scan, just use 'None'
              #('230628_TEMPOL_dil1-2.DSC', exp_type,'230628 TEMPOL 1:2 dilution','darkorchid',0.2, 330,'AGs','QESR caps',
              #      None), #I think these samples are in AGs folder if you want to run them, not certain thou
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
        if plot_rescaled:
            new_d = d.C
            new_d /= concscale
            fl.next('Rescaled and divided by estimated QESR')
            fl.plot(new_d,label = '%s - divided by %0.4f'%(thislabel,concscale))
        norm_d = d.C
        center_field = norm_d.C.argmax().item()#norm_d.getaxis(fieldaxis)[r_[0,-1]].mean()
        norm_d.setaxis(fieldaxis, lambda x:x-center_field)
        dmax = norm_d.C.max()
        dmin = norm_d.C.min()
        delta_d = dmax-dmin
        norm_d /= delta_d
        fl.next('Normalized')
        fl.plot(norm_d, color=color,label=thislabel)
        if plot_rescaled:
            pass
        else:
            c = protein_QESR(thisfile, label=thislabel, pushout=pushout,
                    exp_type = that_exp_type,
                    color = color,
                    calibration_name = calibration,
                    diameter_name = diameter,
                    background =  background,
                    which_plot = 'compare',
                    pickle_file = "240228_L118_Rasbatch240220_probe.pickle", #Don't forget to change if for a new sample, does write over old pickle file if reran without saving
                    fl = fl)
        #all_conc.append(c)
    #allconcs = np.array(all_conc)
    #ax = gca()
    #text(0.5,0.5,'$%0.2f\\pm%0.2f$'%(np.mean(allconcs), np.std(allconcs, ddof=1)/sqrt(len(allconcs))), transform = ax.transAxes)


