"""
Processing the Captured Tuning Curve
====================================

Takes the npz file of the captured tuning curve at different
zoom levels and plots them on the same plot, allowing us to 
look at any drift or discrepancies of the tuning curve.
"""
from pyspecdata import *
import matplotlib.pyplot as plt
fl = figlist_var()
for filename,thislabel in [
    ("230612_water.npz","background"),
    #@("220808_10mM_TEMPOL.npz","10mM"),
    #("220808_70mM_TEMPOL.npz","70mM"),
    #("220720_stock_4.npz","4"),
    ("230612_Q183_pRbatch230605.npz","Q183_230612"),
    ("230612_N187_pRbatch230605.npz","N187_230612"),
    #("221221_T177_MSL_LC-CC.npz","T177_MSL"),
    #("221221_S175_MSL_LC-CC.npz","S175_MSL"),
       ]:
    if thislabel == "background": 
        thisfile = search_filename(filename,exp_type="francklab_esr/Warren",
                unique=True)
    else: 
        thisfile = search_filename(filename, exp_type="francklab_esr/Warren",
                unique=True)
    data = np.load(thisfile)
    nd_data = {}
    fl.next('Tuning curve comparison-zoom2')
    zoom_data = data['zoom2'].squeeze()
    zoom_data_nd = nddata(zoom_data[0],'frequency')
    zoom_data_nd.setaxis('frequency',zoom_data[1])
    nd_data['zoom2'] = zoom_data_nd
    shift_val = zoom_data_nd.argmin()
    zoom_data_nd.setaxis('frequency',lambda x:x- shift_val['frequency'])
    fl.plot(zoom_data_nd,label=thislabel,alpha=0.5)
fl.show()
