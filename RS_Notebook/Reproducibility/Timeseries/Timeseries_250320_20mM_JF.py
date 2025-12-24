from pyspecdata import figlist_var, find_file, search_filename, concat
import numpy as np
import re
import os
# JF runs the following to copy files locally
# rclone copy -v --include '250320*2*' jmf_teams:General/exp_data/francklab_es\
#   r/Romana ~/exp_data/francklab_esr/Romana/
def hhmmss_to_seconds(time_str):
    h, m, s = map(int, time_str.split(":"))
    h -= 15  # use 3pm as reference time
    return h * 3600 + m * 60 + s
pathsep = re.escape(os.path.sep)
all_files = [
    re.sub(".*" + pathsep + "([^" + pathsep + r"]+)\.YGF", "\\1.DSC", j)
    for j in search_filename(
        r"250320_.*\.YGF", exp_type="francklab_esr/Romana"
    )
]
# all_files.sort()
all_spectra = []
with figlist_var() as fl:
    for thisfile in all_files:
        m = re.search("([0-9]{3})(_([0-9]))?K", thisfile)
        d = find_file(re.escape(thisfile), exp_type="francklab_esr/Romana")
        # {{{ only use the first harmonic
        d.chunk_auto("harmonic")
        d = d["harmonic", 0]["phase", 0]
        # }}}
        # {{{ when we stop early, the end is filled with zeros, and we
        #     want to just throw it out
        mask = abs(d).sum("$B_0$") > 0
        d = d["Time", mask.data]
        # }}}
        # pretty sure it uses the time when you save the file, so
        # following is only an approximation
        d["Time"] += hhmmss_to_seconds(d.get_prop("TIME")) - d["Time"][-1]
        d["Time"] /= 60
        d.set_units("Time", "min")
        normalization = d.C.run(np.amax, "$B_0$")
        normalization -= d.C.run(np.amin, "$B_0$")
        fl.next("normalization")
        fl.plot(normalization, "o-")
        all_spectra.append(d)
    all_spectra = concat(all_spectra, dimname="Time").sort("Time")
    fl.next("all spectra!")
    all_spectra.pcolor(cmap="RdBu")
