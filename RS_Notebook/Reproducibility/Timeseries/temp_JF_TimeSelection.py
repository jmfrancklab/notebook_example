from pyspecdata import find_file, plot
from matplotlib.pyplot import show, figure

fieldname = "$B_0$"  # this name looks nice, which is why we use it, but
#                      I get tired of typing is, so I define a variable
d = find_file("250320_OldSL_OldAOT_Reheat.DSC", exp_type="francklab_esr/Romana")
if "harmonic" in d.dimlabels:
    d = d.chunk_auto("harmonic")["phase", 0]["harmonic", 0]
d.pcolor()  # show what this data looks like -- note that later times are
#             filled with zeros because we stopped the time series early
if "Time" in d.dimlabels:  # this is how you  tell if it's a time series.
    #                       Do not use the file name, etc, which is less
    #                       reliable
    # {{{ The next two lines throw out the "empty" block at the end of the data
    #     that comes from stopping early.
    # 
    #     These two lines were more complicated than I expected, and in
    #     particular, we don't usually want to directly access the .data
    #     element of an nddata.  Therefore, typically I would make a PR
    #     for pyspecdata to make this easier, but I want  to just send
    #     an answer now
    mask = abs(d).sum(fieldname) > 0 ## 
    d = d["Time", mask.data]
    # }}}
figure()
d.pcolor()
figure()
plot(d["Time", -1])  # now, we can show the last time slice
show()
