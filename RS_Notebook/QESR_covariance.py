from pylab import *
from pyspecdata import *
from pyspecProcScripts import *
fieldaxis = "$B_0$"
fl = figlist_var()
data = find_file('250123_TEMPOL_100uM_AG_Covariance_2D.DSC', exp_type = "francklab_esr/romana")
if "harmonic" in data.dimlabels:
    data = data['harmonic',0]
data.set_units(fieldaxis, 'T').setaxis(fieldaxis, lambda x: x*1e-4)
data.rename("Time", "observations")
print(ndshape(data))
quit()
data.reorder(["observations",fieldaxis])
fl.next("Covariance in B domain",figsize = (6,4))
fl.image(data.C.cov_mat('observations'))
plt.title('')
# savefig("QESR_Bdom_cov.pdf", bbox_inches="tight", pad_inches=0.1)
data.ift(fieldaxis,shift = True)
fl.next("Covariance in U domain", figsize = (6,4))
fl.image(data.cov_mat("observations"))
plt.title("")
# savefig("QESR_Udom_cov.pdf", bbox_inches="tight", pad_inches=0.1)
fl.show()
