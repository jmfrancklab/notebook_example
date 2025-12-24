from pylab import *
from pyspecdata import *
from scipy.optimize import root
import os
# init_logging(level='debug')

# rclone copy -v --include '250320*2*' jmf_teams:General/exp_data/francklab_esr/romana ~/exp_data/francklab_esr/romana/
def hhmmss_to_seconds(time_str):
    h, m, s = map(int, time_str.split(":"))
    h -= 15 # use 3pm as reference time
    return h * 3600 + m * 60 + s
pathsep = re.escape(os.path.sep)
all_files = [
    re.sub(".*"+pathsep+"([^"+pathsep+"]+)\.YGF", "\\1.DSC", j)
    for j in search_filename(
        "250320_.*\.YGF", exp_type="francklab_esr/romana"
    )
]
# all_files.sort()
with figlist_var() as fl:
    for thisfile in all_files:
        m = re.search("([0-9]{3})(_([0-9]))?K", thisfile)
        d = find_file(re.escape(thisfile), exp_type="francklab_esr/romana")
        d.chunk_auto("harmonic")
        d = d["harmonic", 0]["phase", 0]
        print(thisfile,"ends at",d.get_prop("TIME"))
        # really worried it stores the time when you saved the file
        d["Time"] += hhmmss_to_seconds(d.get_prop("TIME")) - d['Time'][-1]
        d['Time'] /= 60
        d.set_units('Time','min')
        normalization = d.C.run(np.amax, "$B_0$")
        normalization -= d.C.run(np.amin, "$B_0$")
        fl.next("normalized spectra")
        fl.plot(d, human_units=False)
        fl.next("normalization")
        fl.plot(normalization, "o-")
