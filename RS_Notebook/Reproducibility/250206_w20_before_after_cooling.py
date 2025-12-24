from pyspecdata import find_file, figlist_var
from pyspecProcScripts import align_esr
from itertools import cycle
import matplotlib.pyplot as plt
import numpy as np
d = {}
d['250206: initial sample w0=20'] = find_file("250206_20mM_TSO4_W20_C8.DSC", exp_type="francklab_esr/romana") #cooling
d['250206: After cooling bath w0=20'] = find_file("250206_20mM_TSO4_W20_C8_cooled.DSC", exp_type="francklab_esr/romana") #cooling
for k,v in d.items():
    d[k] = v.chunk_auto('harmonic','harmonic')['harmonic', 0]['phase',0]
with figlist_var() as fl:
    aligned_d = align_esr(d, fl=fl)
