from pyspecdata import (
    figlist_var,
    find_file,
    search_filename,
    concat,
    lmfitdata,
    gridandtick,
)
from matplotlib.pyplot import text, gca, xlabel, ylabel, subplots
import numpy as np
import pandas as pd
import re
import os
import sympy as sp
import dateutil
from pathlib import Path

df = pd.read_excel("temperature_log_clean_250425_5mM.xlsx")
df.columns

unique_filenames = df['Filename'].unique()
df['Time'] = pd.to_datetime(df['Time'])
start_time = {
    fname: df[df["Filename"] == fname]["Time"].min()
    for fname in unique_filenames
}

tempsearch_re = re.compile(r"5mM_(.*)\.")
all_files_sorted = sorted(unique_filenames, key=lambda x: tempsearch_re.search(x).groups()[0])

all_files = {}
for fname in unique_filenames:
    all_files[fname] = find_file(fname, exp_type="francklab_esr/romana")
    all_files[fname] = all_files[fname].chunk_auto("harmonic", "harmonic")["harmonic", 0]["phase", 0]

all_spectra = []
all_norm = []

n_max, n_min, R, t = sp.symbols("n_max n_min R Time", positive=True)
def hhmmss_to_seconds(time_str, date_str, ref_datetime):
    full_time = dateutil.parser.parse(f"{date_str} {time_str}")
    return (full_time - ref_time).total_seconds()

with figlist_var() as fl:
    for j, thisfile in enumerate(all_files_sorted):
        T_string = tempsearch_re.search(thisfile).groups()[0]
        d = all_files[thisfile]
        
        # {{{ to remove empty zeros when we ESR stopped early
        mask = abs(d).sum("$B_0$") > 0
        d = d["Time", mask.data]
        # }}}

        # Get earliest start time from Excel 
        if j == 0:
            ref_time = start_time[thisfile]  
        
        # Time axis: align to reference 
        d["Time"] -= d["Time"][-1]
        d["Time"] += hhmmss_to_seconds(
            d.get_prop("TIME"), d.get_prop("DATE"), ref_time
        )
        d["Time"] /= 60
        d.set_units("Time", "min")

        # Normalize
        normalization = d.C.run(np.amax, "$B_0$")
        normalization -= d.C.run(np.amin, "$B_0$")
        fl.next("normalization")
        fl.plot(normalization, "o-", label=T_string)

        # store
        all_norm.append(normalization)
        all_spectra.append(d)

        # Plot temperature vs. time from Excel
        excel_subset = df[df["Filename"] == thisfile].copy()
        excel_subset = excel_subset.sort_values(by="Time")
        temp_time = (excel_subset["Time"] - ref_time).dt.total_seconds() / 60  # in minutes
        temp_vals = excel_subset["Temperature"]
        fl.next("Temperature")
        fl.plot(temp_time, temp_vals, "o-", label=f"{T_string}")

    # concatanate all data
    all_spectra = concat(all_spectra, dimname="Time").sort("Time")
    all_norm = concat(all_norm, dimname="Time").sort("Time")

    # plot
    fl.next("all spectra!")
    all_spectra.pcolor(cmap="RdBu")

    # {{{ here we use the normalization curve to fit a time constant for
    #     the shedding process
    fl.next("normalization")
    all_norm = lmfitdata(all_norm["Time":(144, 189)])
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

# Here I'm trying to plot both Normalize and Temperature in subplot.
# I tried multiple times to do this in above for loop. But it didn't let me do correctly
all_spectra = []
all_norm = []

with figlist_var() as fl:
    fig, (ax1, ax2) = subplots(2,1, sharex = True, figsize=(10,10))
    for j, thisfile in enumerate(all_files_sorted):
        T_string = tempsearch_re.search(thisfile).groups()[0]
        d = all_files[thisfile]
        
        # {{{ to remove empty zeros when we ESR stopped early
        mask = abs(d).sum("$B_0$") > 0
        d = d["Time", mask.data]
        # }}}

        # Get earliest start time from Excel 
        if j == 0:
            ref_time = start_time[thisfile]  
        
        # Time axis: align to reference 
        d["Time"] -= d["Time"][-1]
        d["Time"] += hhmmss_to_seconds(
            d.get_prop("TIME"), d.get_prop("DATE"), ref_time
        )
        d["Time"] /= 60
        d.set_units("Time", "min")

        # Normalize
        normalization = d.C.run(np.amax, "$B_0$")
        normalization -= d.C.run(np.amin, "$B_0$")

        # store
        all_norm.append(normalization)
        # all_spectra.append(d)

        # temperature vs. time from Excel
        excel_subset = df[df["Filename"] == thisfile].copy()
        excel_subset = excel_subset.sort_values(by="Time")
        temp_time = (excel_subset["Time"] - ref_time).dt.total_seconds() / 60  # in minutes
        temp_vals = excel_subset["Temperature"]

        # subplot
        fl.next("Normalization & Temperature vs Time")
        fl.plot(normalization, "o-", ax=ax1, label=f"{T_string}")        
        fl.plot(temp_time, temp_vals, "o-", ax=ax2, label=f"{T_string}")
        ax1.legend()
        ax2.legend()
        ax1.set_ylabel("Normalized ESR Signal")
        ax2.set_ylabel("Temperature (K)")
        ax2.set_xlabel("Time (min)")
        gridandtick(ax1)
        gridandtick(ax2)
        ax1.sharex(ax2)
        ax1.tick_params(labelbottom=True)
