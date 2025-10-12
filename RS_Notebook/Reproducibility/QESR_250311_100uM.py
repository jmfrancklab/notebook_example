from matplotlib.pyplot import axvline, axhline, gca
from pint import UnitRegistry
from pyspecdata import *
from itertools import cycle
from pyspecProcScripts import *
from pyspecProcScripts import QESR_scalefactor, QESR

init_logging(level='debug')

colors = plt.rcParams[
    "axes.prop_cycle"
]()  # this is the default matplotlib cycler for line styles
fieldaxis = "$B_0$"
plot_rescaled = False
water_nddata = find_file("230511_water.DSC", exp_type="francklab_esr/romana")["harmonic", 0]
with figlist_var() as fl:
    for file_searchstring, thislabel, pushout, background, exp_type in [
        (
            "250307_100uM_TSO4_ConvTime4ms_CapillaryFrom_250122.DSC",
            "4 ms conversion",
            0.4,
            water_nddata,
            "francklab_esr/romana",
        ),
        (
            "250307_100uM_TSO4_CapillaryFrom_250122.DSC",
            "12 ms conversion",
            0.4,
            water_nddata,
            "francklab_esr/romana",
        ),
    ]:
        c = QESR(
            file_searchstring,
            label=thislabel,
            exp_type=exp_type,
            #background=background,
            plot_derivative=True,
            fl=fl,
        )
        print(f"{c:~P}")
