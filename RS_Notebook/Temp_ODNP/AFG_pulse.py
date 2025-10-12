from Instruments import *
from pyspecdata import *
import time
from serial.tools.list_ports import comports
import serial
import numpy as np

# note that this requires the serial library!

# {{{ this section is just diagnostic, to check that it can see the
# instruments -- it's possible that with upgraded libraries, this will not work
print("These are the instruments available:")
SerialInstrument(None)
print("done printing available instruments")
with SerialInstrument("AFG-2225") as s:
    print(s.respond("*idn?"))
# }}}

def gen_pulse(freq=15.1e6, width=8e-6, ch1_only=True):
    with AFG() as a:
        a.reset()
        # {{{ here, we manually construct an ndarry that gives the
        #     square pulse waveform
        rate = freq * 4
        total_samples = width * rate
        total_samples = (
            int(total_samples / 4 + 0.5) * 4
        )  # convert to multiple of 4
        assert total_samples < 4097, (
            "Your pattern length (%d) exceeds the max (4096 samples at %g MHz)"
            % (total_samples, rate)
        )
        y = np.zeros(total_samples)
        y[0::4] = 0
        y[1::4] = 1
        y[2::4] = 0
        y[3::4] = -1
        y[-1] = 0
        # }}}
        this_ch = 0  # do everything on channel 1
        a[this_ch].digital_ndarray(y, rate=rate)
        print("now, output on")
        a[this_ch].output = True
        a[this_ch].burst = True
        a.set_burst(
            per=500e-6
        )  # this is how often the waveform (a square pulse) is played out
        a[this_ch].ampl = 0.1


gen_pulse()