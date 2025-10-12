from pyspecdata import find_file, figlist_var
from pyspecProcScripts import align_esr
from itertools import cycle
import matplotlib.pyplot as plt
import numpy as np
d = {}
d['cooling 25'] = find_file("250130_20mM_TSO4_W20_Isooct_run1.DSC", exp_type="francklab_esr/romana") #cooling
d['cooling 25 aged'] = find_file("250131_20mM_TSO4_Isooct_w20_prep250130.DSC", exp_type="francklab_esr/romana") #cooling
for k,v in d.items():
    d[k] = v.chunk_auto('harmonic','harmonic')['harmonic', 0]['phase',0]
d['cooling 25'].reorder('Temperature').sort('Temperature')
d['cooling 25'] = d['cooling 25']['Temperature':293] 
with figlist_var() as fl:
    aligned_d = align_esr(d, fl=fl)
