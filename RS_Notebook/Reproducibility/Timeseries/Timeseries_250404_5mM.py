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
import dateutil
# JF runs the following to copy files locally
# rclone copy -v --include '250404*' jmf_teams:General/exp_data/francklab_es\
#   r/romana ~/exp_data/francklab_esr/romana/
def hhmmss_to_seconds(time_str, date_str, ref_datetime):
    full_time = dateutil.parser.parse(f"{date_str} {time_str}")
    return (full_time - ref_time).total_seconds()
pathsep = re.escape(os.path.sep)
# we need to modify the following search pattern, which determines
# how it finds the temperatures + run numbers for sorting
tempsearch_re = re.compile(r"5mM_(.*)\.")
all_files = sorted(
    [
        re.sub(".*" + pathsep + "([^" + pathsep + r"]+)\.YGF", "\\1.DSC", j)
        for j in search_filename(
            r"250404_.*\.YGF", exp_type="francklab_esr/Romana"
        )
    ],
    key=lambda x: tempsearch_re.search(x).groups()[0],
)
# all_files.sort()
all_spectra = []
all_norm = []
n_max, n_min, R, t = sp.symbols("n_max n_min R Time", positive=True)
with figlist_var() as fl:
    for j, thisfile in enumerate(all_files):
        T_string = tempsearch_re.search(thisfile).groups()[0]
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
        if j == 0:
            ref_time = dateutil.parser.parse(
                d.get_prop("DATE") + " " + d.get_prop("TIME")
            )
        d["Time"] -= d["Time"][-1]
        d["Time"] += hhmmss_to_seconds(
            d.get_prop("TIME"), d.get_prop("DATE"), ref_time
        )
        d["Time"] /= 60
        d.set_units("Time", "min")
        normalization = d.C.run(np.amax, "$B_0$")
        normalization -= d.C.run(np.amin, "$B_0$")
        fl.next("normalized spectra")
        fl.plot(d, human_units=False)
        fl.next("normalization")
        fl.plot(normalization, "o-", label=T_string)
        all_norm.append(normalization)
        all_spectra.append(d)
    all_spectra = concat(all_spectra, dimname="Time").sort("Time")
    all_norm = concat(all_norm, dimname="Time").sort("Time")
    fl.next("all spectra!")
    all_spectra.pcolor(cmap="RdBu")
    gca().set_title(fl.current)
    fl.next("all spectra, normalized!")
    (all_spectra/all_norm).pcolor(cmap="RdBu")
    gca().set_title(fl.current)
    # {{{ here we use the normalization curve to fit a time constant for
    #     the shedding process
    fl.next("normalization")
    all_norm = lmfitdata(all_norm["Time":(63.8, 111.1)]) # for 250404
    t_start = all_norm["Time"][0]
    all_norm["Time"] -= t_start  # make fitting easier
    all_norm.functional_form = n_min + sp.exp(-R * t) * (n_max - n_min)
    all_norm.set_guess(
        n_max=all_norm["Time", 0].item(),
        n_min=all_norm["Time", -1].item(),
        R=0.054,  # rate per minute
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
