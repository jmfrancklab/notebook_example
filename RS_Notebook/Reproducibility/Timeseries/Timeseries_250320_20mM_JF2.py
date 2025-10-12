from pyspecdata import (
    figlist_var,
    find_file,
    search_filename,
    concat,
    lmfitdata,
)
from matplotlib.pyplot import text, gca
import numpy as np
import re
import os
import sympy as sp
# JF runs the following to copy files locally
# rclone copy -v --include '250320*OldSL*' jmf_teams:General/exp_data/francklab_es\
#   r/Romana ~/exp_data/francklab_esr/Romana/
def hhmmss_to_seconds(time_str):
    h, m, s = map(int, time_str.split(":"))
    h -= 15  # use 3pm as reference time
    return h * 3600 + m * 60 + s
pathsep = re.escape(os.path.sep)
all_files = sorted(
    [
        re.sub(".*" + pathsep + "([^" + pathsep + r"]+)\.YGF", "\\1.DSC", j)
        for j in search_filename(
            r"250320_.*\.YGF", exp_type="francklab_esr/Romana"
        )
    ],
    key=lambda x: re.search(r"OldAOT_(.*)\.", x).groups()[0],
)
# all_files.sort()
all_spectra = []
all_norm = []
n_max, n_min, R, t = sp.symbols("n_max n_min R Time", positive=True)
with figlist_var() as fl:
    for thisfile in all_files:
        T_string = re.search(r"OldAOT_(.*)\.", thisfile).groups()[0]
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
        fl.plot(normalization, "o-", label=T_string)
        all_norm.append(normalization)
        all_spectra.append(d)
    all_spectra = concat(all_spectra, dimname="Time").sort("Time")
    all_norm = concat(all_norm, dimname="Time").sort("Time")
    fl.next("all spectra!")
    all_spectra.pcolor(cmap="RdBu")
    # {{{ here we use the normalization curve to fit a time constant for
    #     the shedding process
    fl.next("normalization")
    all_norm = lmfitdata(all_norm["Time":(14, 114)])
    t_start = all_norm["Time"][0]
    all_norm["Time"] -= t_start  # make fitting easier
    all_norm.functional_form = n_min + sp.exp(-R * t) * (n_max - n_min)
    all_norm.set_guess(
        n_max=all_norm["Time", 0].item(),
        n_min=all_norm["Time", -1].item(),
        R=0.03,  # rate per minute
    )
    do_fit = True  # set to False to check the guess
    if do_fit:
        all_norm.fit()
    else:
        all_norm.settoguess()  # do this first to see if guess is reasonable
    fit_curve = all_norm.eval()
    fit_curve["Time"] += t_start
    fl.plot(fit_curve, color="k", ls="--", alpha=1.0)
    text(
        0.5,
        0.5,
        f"time constant:\n{1/all_norm.output('R'):#0.3g} min",
        transform=gca().transAxes,
    )
    # }}}
