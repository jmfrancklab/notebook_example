from matplotlib.pyplot import axvline, axhline, gca
from pint import UnitRegistry
from pyspecdata import *
from itertools import cycle
from pyspecProcScripts import *
from pyspecProcScripts import QESR_scalefactor
import pickle


# {{{ all basic info
colors = plt.rcParams[
    "axes.prop_cycle"
]()  # this is the default matplotlib cycler for line styles
fieldaxis = "$B_0$"
#pushout = 1
myconcs = []
# }}}
#for RS presentation we are editing this function here instead of in proc_scripts
def present_nddata_QESR(thisnddata, label, pushout=0.5,
        threshold=0.05, pickle_file=None, background=None,
        fl=None, exp_type="francklab_esr/Farhana",
        which_plot=None, calibration_name=None,
        diameter_name=None, color=None):
    if which_plot is None:
        which_plot = file_name
    if fl is None:
        raise ValueError("for now, you just have to pass a figure list")
    if pickle_file is not None:
        # {{{ make a pickle file, all_concs.pickle that has a
        #     dictionary of the concentrations of all samples
        #     that we are looking at
        #     the label should have the batch date and
        #     residue, so should be good identifier
        if os.path.exists(pickle_file):
            with open(pickle_file, "rb") as fp:
                pickle_vars = pickle.load(fp)
        else:
            pickle_vars = {}
        # }}}
    # {{{ load the file of interest, and get set up
    d = thisnddata
    d.setaxis(fieldaxis,
            lambda x: x-d.get_prop('MWFQ')/gammabar_e*1e4)
    # }}}
    if background is None:
        background = ndshape(d).alloc() # zeros -- keep life easy!
        background.copy_axes(d)
    else:
        # {{{ set up the background
        background = background.C
        background -= background[fieldaxis, -100:].data.mean()
        background.setaxis(fieldaxis,
                lambda x: x-background.get_prop('MWFQ')/gammabar_e*1e4)
        # }}}
    background = background.interp(fieldaxis, d.getaxis(fieldaxis))
    # {{{ configure all the plots -- I like to do this in one place so I
    #     can easily control placement in the PDF
    fl.text(r"\textbf{\texttt{%s}}\par"%label)
    fl.next(f"{which_plot} show background subtraction in abs mode")
    gca().set_title("abs mode:\nspectrum and background")
    fl.text(r'\par')
    fl.next(f"{which_plot} absorption, bg. no bl.")
    gca().set_title("abs mode:\nbackground subtracted, show baseline")
    fl.text(r'\par')
    fl.next(f"{which_plot} baseline diagnostic")
    gca().set_title("zoomed-in baseline diagnostic\nshowing only baseline\n(data and fit)")
    # }}}
    if color is None:
        color = next(colors)["color"]
    d.set_plot_color(color)
    fl.next(f"{which_plot} show background subtraction in abs mode")
    forplot = background.C.integrate(fieldaxis, cumulative=True)
    forplot.set_plot_color(d.get_plot_color())
    fl.plot(forplot, alpha=0.2)
    forplot = d.C.integrate(fieldaxis, cumulative=True)
    fl.plot(forplot, alpha=0.5, label=label)
    fl.next(f"{which_plot} absorption, bg. no bl.")
    # show the same thing on the main plot as a faint line
    fl.plot(forplot, alpha=0.2)#, label=None)
    d -= background # subtract background in derivative mode
    d_abs = d.C.integrate(fieldaxis, cumulative=True)
    fl.plot(d_abs, alpha=0.5, label=label)
    # for a protein, we assume we have 1 broad peak that's always over threshold*max
    right_side = abs(d_abs.data)[-1]
    # define a peak as anything that rises above threshold*max
    peaklist = d_abs.contiguous(
        lambda x: abs(x) > right_side + (abs(x).data.max() - right_side) * threshold
    )
    # pull the furthest left and furthest right boundaries of any peaks that we find
    specrange = (peaklist.ravel().min(), peaklist.ravel().max())
    fl.next(f"{which_plot} absorption, bg. no bl.")
    generous_limits = specrange + np.diff(specrange).item() * r_[-pushout, +pushout]
    #for j in r_[np.array(specrange)]:
        # show where the peaks were identified
        #axvline(x=j, alpha=0.5, color=d.get_plot_color(), ls=":")
    for j in r_[generous_limits]:
        # show the actual limits
        axvline(x=j, alpha=0.5, color=d.get_plot_color(), ls="-")
    d_baseline = d_abs[
        fieldaxis,
        lambda x: np.logical_or(x < generous_limits[0], x > generous_limits[1]),
    ]
    fl.next(f"{which_plot} baseline diagnostic")
    fl.plot(d_baseline, ".", alpha=0.3, label=label, human_units=False)
    # {{{ we don't have a spline in pyspecdata yet, so just hack it
    spl = UnivariateSpline(d_baseline.getaxis(fieldaxis), d_baseline.data)
    polybaseline = d.copy(data=False)
    polybaseline.data = spl(d.getaxis(fieldaxis))
    # }}}
    fl.plot(polybaseline, alpha=0.5, human_units=False)
    fl.next(f"{which_plot} absorption, bg. no bl.")
    fl.plot(polybaseline, alpha=0.5)
    d_abs -= polybaseline
    d_abs.integrate(fieldaxis, cumulative=True)
    thisgca = plt.gca()
    thisgca.set_ylabel('Intensity')
    fl.next("dblint ÷ denom * conversion")
    d_abs /= QESR_scalefactor(d, calibration_name=calibration_name,
            diameter_name=diameter_name)
    final_conc = (
        d_abs[fieldaxis : (generous_limits[-1], None)].mean(fieldaxis).item()
    ).real
    #print("AVerage concentration:", final_conc)
    d_abs.name("conc").set_units("μM")
    ### RS- to not printing concentration
    # fl.plot(d_abs, alpha=0.5, label=f"{label}"), # %0.4f μM" % final_conc) ###RS - not to show SL cncentration
    fl.plot(d_abs, alpha=0.5, label=f"{label}, %0.4f μM" % final_conc) ###RS - to show SL cncentration
    fl.grid()
    if pickle_file is not None:
        pickle_vars[label] = final_conc
        with open(pickle_file, "wb") as fp:
            pickle_vars = pickle.dump(pickle_vars, fp)
    return final_conc


colors = plt.rcParams["axes.prop_cycle"]() # this is the default matplotlib cycler for line styles
init_logging(level='debug')
fieldaxis = '$B_0$'
exp_type = "francklab_esr/romana" #Change to your folder or the folder with the files you want to look at
plot_rescaled = False #Run with False for double integral to get conc, change to True to compare to relative concentration with another sample  
all_conc = []
with figlist_var() as fl:
    for filenum, (thisfile, that_exp_type, thislabel, thisT, thiscolor, pushout, concscale, calibration, diameter,
            background) in enumerate(
            [
        ### Isooctane
            ###TEMPO-SO4
            # ('240220_TempoSO4_W3.DSC', exp_type, 'TEMPO-SO$_4$ W$_0=3$: Initial sample', 293, 'blue', 0.2, 200, 'RS', 'QESR caps',
            #       None), 
            # ('240220_TempoSO4_W3_run2.DSC', exp_type, 'TEMPO-SO$_4$ W$_0=3$: After cooling and heating', 293, 'red', 0.25, 200, 'RS', 'QESR caps',
            #       None),
            # ('240220_TempoSO4_W20_run1.DSC', exp_type, 'TEMPO-SO$_4$ W$_0=20$: Initial sample', 293, 'blue', 0.2, 200, 'RS', 'QESR caps',
            #       None),
            # ('240220_TempoSO4_W20_run2.DSC', exp_type, 'TEMPO-SO$_4$ W$_0=20$: After cooling and heating', 293, 'red', 0.15, 200, 'RS', 'QESR caps',
            #       None),
             
            ### CAT16 
            # ('240226_CAT16_C8_W3_run1.DSC', exp_type, 'Initial sample', 293, 'blue', 0.2, 200, 'RS', 'QESR caps',
            #       None), # cooling
            # ('240226_CAT16_C8_W3_run2.DSC', exp_type, 'After cooling and heating', 293, 'red', 0.25, 200, 'RS', 'QESR caps',
            #      None), #heating subsequently
            # ('240226_CAT16_C8_W20_run1.DSC', exp_type, 'Initial sample', 293, 'blue', 0.2, 200, 'RS', 'QESR caps',
            #       None),
            # ('240226_CAT16_C8_W20_run2.DSC', exp_type, 'After cooling and heating', 293, 'red', 0.15, 200, 'RS', 'QESR caps',
            #        None),
            
        ### Dodecane
            ###TEMPO-SO4
            # ('240226_TEMPOSO4_C10_W3_run1.DSC', exp_type, 'TEMPO-SO$_4$ W$_0=3$: Initial sample', 293, 'blue', 0.1, 200, 'RS', 'QESR caps',
            #       None), 
            # ('240226_TEMPOSO4_C10_W3_run2.DSC', exp_type, 'TEMPO-SO$_4$ W$_0=3$: After cooling and heating', 293, 'red', 0.11, 200, 'RS', 'QESR caps',
            #       None),
            ('240226_TEMPOSO4_C10_W20_run1.DSC', exp_type, 'TEMPO-SO$_4$ W$_0=20$: Initial sample', 293, 'blue', 0.2, 200, 'RS', 'QESR caps',
                  None),
            ('240226_TEMPOSO4_C10_W20_run2.DSC', exp_type, 'TEMPO-SO$_4$ W$_0=20$: After cooling and heating', 293, 'red', 0.2, 200, 'RS', 'QESR caps',
                  None),
            
            ### CAT16 
            # ('240226_CAT16_C10_W3_run1.DSC', exp_type, 'CAT16 W$_0=3$: Initial sample', 293, 'blue', 0.13, 200, 'RS', 'QESR caps',
            #       None), # cooling
            # ('240226_CAT16_C10_W3_run2.DSC', exp_type, 'CAT16 W$_0=3$: After cooling and heating', 293, 'red', 0.13, 200, 'RS', 'QESR caps',
            #      None), #heating subsequently
            # ('240226_CAT16_C10_W20_run1.DSC', exp_type, 'CAT16 W$_0=20$: Initial sample', 293, 'blue', 0.2, 200, 'RS', 'QESR caps',
            #       None),
            # ('240226_CAT16_C10_W20_run2.DSC', exp_type, 'CAT16 W$_0=20$: After cooling and heating', 293, 'red', 0.2, 200, 'RS', 'QESR caps',
            #        None),


            #('230628_TEMPOL_dil1.DSC', exp_type,'230628 TEMPOL 1:3 dilution','blue', 0.2,210,'AGs','QESR caps',
            #      None), #If you don't use a background scan, just use 'None'
            #('230628_TEMPOL_dil1-2.DSC', exp_type,'230628 TEMPOL 1:2 dilution','darkorchid',0.2, 330,'AGs','QESR caps',
            #      None), #I think these samples are in AGs folder if you want to run them, not certain thou
            ]):
        d = find_file(thisfile,exp_type = that_exp_type)
        d = d["Temperature":thisT] ##RS
        d -= d[fieldaxis, -100:].data.mean()
        if "harmonic" in d.dimlabels:
            d = d['harmonic',0]
        color = thiscolor
        print(d['$B_0$']) ##RS
        fl.next("Raw QESR")
        fl.plot(d,color=color, label=thislabel,alpha = 0.5)
        rescaled = d.C
        this_d = d.C
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
        center_field = norm_d.C.argmax(fieldaxis).item()#norm_d.getaxis(fieldaxis)[r_[0,-1]].mean()
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

            #c = present_nddata_QESR(thisnddata = this_d, label=thislabel, pushout=pushout, ### RS- not to show temp
            c = present_nddata_QESR(thisnddata = this_d, label=thislabel + ' - %d K'%thisT, pushout=pushout, ### RS- to show temp
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


