from pylab import *
from pyspecdata import *
#%load_ext pyspecdata.ipy
d = find_file("240220_TempoSO4_W20_run2",
              exp_type="francklab_esr/romana")
#print(d.shape) # this shows me what the dimensions are
d.chunk_auto('harmonic','harmonic') # the harmonic is typically stored so that we need to do this
#print(d.shape) # this shows me what the dimensions are
with figlist_var() as fl:
    fl.next('raw data as pcolor')
    d = d['harmonic',0]['phase',0]
    d.pcolor()
    # it's easiest to show the temperature above and below the transition
    for this_label,temp_range in [("below transition",(None,257.8)),
                       ("above transition",(258,None))]:
        fl.next(this_label)
        this_d = d['Temperature':temp_range]
        for temp_ithis_dx in range(this_d.shape['Temperature']):
            this_temp = this_d.getaxis('Temperature')[temp_ithis_dx]
            fl.plot(this_d['Temperature',temp_ithis_dx],
                    label=f"{this_temp} K")

