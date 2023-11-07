from matplotlib.pyplot import axvline, axhline, gca
from pint import UnitRegistry
from pyspecdata import *
from itertools import cycle
from pyspecProcScripts import *
from pyspecProcScripts import QESR_scalefactor
colors = plt.rcParams["axes.prop_cycle"]() # this is the default matplotlib cycler for line styles
fieldaxis = '$B_0$'
exp_type = "francklab_esr/alex"
with figlist_var() as fl:
    for filenum, (thisfile, thislabel, pushout, calibration, diameter, background) in enumerate(
            [
              ('230929_100mM_tempo_so4.DSC','CAT16', 0.3, '230202','QESR caps',
                  find_file('230511_water.DSC',exp_type=exp_type)['harmonic',0]),
             ]):
        d = find_file(thisfile,exp_type = exp_type)
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
        fl.plot(d,color=color,label=thislabel)
        norm_d = d.C
        center_field = norm_d.C.argmax().item()
        norm_d.setaxis(fieldaxis, lambda x:x-center_field)
        dmax = norm_d.C.max()
        dmin = norm_d.C.min()
        delta_d = dmax-dmin
        norm_d /= delta_d
        fl.next('Normalized')
        fl.plot(norm_d, color=color,label=thislabel)
        c = protein_QESR(thisfile, label=thislabel,pushout=pushout,
                exp_type = exp_type,
                color=color,
                calibration_name = calibration,
                diameter_name = diameter,
                background =  background,
                which_plot = 'compare',
                pickle_file = "TEMPOL_rerun_conc.pickle",
                fl = fl)

