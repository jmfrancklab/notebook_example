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
        # (
        #     "250314_20mM_TSO4_water_AG_Parameter.DSC",
        #     "AG's parameter",
        #     0.4,
        #     water_nddata,
        #     "francklab_esr/romana",
        # ),
        # (
        #     "250314_20mM_TSO4_water_convTime4ms.DSC",
        #     "convTime 4 ms",
        #     0.4,
        #     water_nddata,
        #     "francklab_esr/romana",
        # ),
        # (
        #     "250314_20mM_TSO4_water_convTime8ms.DSC",
        #     "convTime 8 ms",
        #     0.4,
        #     water_nddata,
        #     "francklab_esr/romana",
        # ),
        # (
        #     "250314_20mM_TSO4_water_convTime12ms.DSC",
        #     "convTime 12 ms",
        #     0.4,
        #     water_nddata,
        #     "francklab_esr/romana",
        # ),
        # (
        #     "250314_20mM_TSO4_water_convTime24ms.DSC",
        #     "convTime 24 ms",
        #     0.4,
        #     water_nddata,
        #     "francklab_esr/romana",
        # ),
        (
            "250317_20mM_TSO4_UPwater_AGParam.DSC",
            "UP water AG's parameter",
            0.4,
            water_nddata,
            "francklab_esr/romana",
        ),
        (
            "250317_20mM_TSO4_UPwater_12ms.DSC",
            "UP water",
            0.4,
            water_nddata,
            "francklab_esr/romana",
        ),
        (
            "250317_20mM_TSO4_DIwater_AGParam.DSC",
            "DI water AG's parameter",
            0.4,
            water_nddata,
            "francklab_esr/romana",
        ),
        (
            "250317_20mM_TSO4_DIwater_12ms.DSC",
            "DI water",
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
