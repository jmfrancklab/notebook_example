"""
Bruker cw ESR Data
==================

Load cw Bruker ESR data, both 1D and 2D.

Check out the
`Simple UV <Cary_simple.html>`_
example to understand how
pySpecData locates the file here.
"""
from numpy import *
import pylab as plt
from pyspecdata import *
# %%
# Load some 1D ESR data with harmonic + phase info.
# The data is initial organized into two dimensions -- `harmonic` and `$B_0$`.
# 

# d = find_file("230118_VTU_run2.DSC", #277K-295K
# d = find_file("230118_VTU_run3.DSC", #297K-279K
# d = find_file("230118_VTU_run4.DSC", #280K-260K
d = find_file("230118_VTU_run5.DSC", #295K-305K                                        
        exp_type='francklab_esr/romana')
print(ndshape(d))
print(d.shape)
print("here, we see the harmonic axis contains both harmonic and phase info",repr(d.getaxis('harmonic')))
d.chunk_auto('harmonic','phase')

# %%
# `chunk_auto` breaks the `harmonic` dimensions since it was labeled with an axis that had 2 fields.

print(ndshape(d))

figure(1)
plot(d['phase',0], alpha=0.5)
plot(d['phase',1], ':', alpha=0.5)
title("1D Data with Multiple Harmonics")

# %%
# Next, let's load some power-saturation data

# d = find_file("230118_VTU_run2.DSC", #277K-295K
# d = find_file("230118_VTU_run3.DSC", #297K-279K
# d = find_file("230118_VTU_run4.DSC", #280K-260K
d = find_file("230118_VTU_run5.DSC", #295K-305K               
        exp_type='francklab_esr/romana')
d.chunk_auto('harmonic','phase')
figure(2)
print(ndshape(d))

# image(d['harmonic',0]['phase',0].C.setaxis("'Temperature'",'#').set_units("'Temperature'",'scan #'))
plot(d['harmonic',0]['phase',0].C.setaxis("'Temperature'",'#').set_units("'Temperature'",'scan #'))
title("2D field temperature")
plt.gca().set_aspect('auto')
plt.show()
