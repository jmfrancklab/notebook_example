from pyspecdata import find_file, figlist_var
from pyspecProcScripts import align_esr
import matplotlib.pyplot as plt

d = {}
d["new data"] = find_file(
    "250310_20mM_TSO4_C8_w20_oldSL_oldAOT_3day_equilibrate_convTime12ms.DSC", exp_type="francklab_esr/romana"
)
d["new data, fast conv"] = find_file(
    "250310_20mM_TSO4_C8_w20_oldSL_oldAOT_3day_equilibrate_convTime5ms.DSC", exp_type="francklab_esr/romana"
)
d["last year's"] = find_file(
    "240220_TempoSO4_W20_run1.DSC", exp_type="francklab_esr/romana"
)
for k, v in d.items():
    d[k] = v.chunk_auto("harmonic", "harmonic")["harmonic", 0]["phase", 0]
    if "last year" in k:
        d[k].reorder("Temperature").sort("Temperature")
        d[k] = d[k]["Temperature":293]
with figlist_var() as fl:
    d = align_esr(d, fl=fl)
    fl.next("normalized after alignment")
    # If the data very dissimilar, the least-squares scaling doesn't
    # work as well.  For these, it makes more sense to use a peak
    # normalization.
    for k, v in d.items():
        extra_norm = abs(d[k].data.max() - d[k].data.min())
        d[k] /= extra_norm
        d[k].set_prop("scaling", d[k].get_prop("scaling") * extra_norm)
        fl.plot(
            d[k],
            alpha=0.5,
            label=f"{k}\n÷ {d[k].get_prop('scaling'):#0.3g}",
        )
    fl.adjust_spines("bottom")
    plt.ylabel("")
    plt.gca().set_yticks([])
