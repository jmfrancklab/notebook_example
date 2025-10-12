import nmrglue as ng
import matplotlib.pyplot as plt
import zipfile
import tempfile
import os
import pyspecdata as psd
from itertools import cycle

colorcyc_list = plt.rcParams["axes.prop_cycle"].by_key()["color"]


def process_titration(
    dataset_name,
    thismarker,
    display_range,
    aot_range,
    water_int_range,
    dry_water_peak_range,
    dry_water_int_range,
    baseline_left,
    baseline_right,
    crossover,
    file_list,
    fl,
):
    # {{{ first construct the AOT background
    baseline_for_int = load_pdata_as_nddata(
        baseline_left, (1, 1), "NMR_Data_AG"
    )
    baseline_for_int = baseline_for_int["t2":display_range]
    # define range for AOT integral (=1 proton)
    integral = baseline_for_int["t2":aot_range].integrate("t2")
    baseline_for_int /= integral.item()  # normalize baseline by this
    # Load dataset where water peak is outside of AOT peaks
    d = load_pdata_as_nddata(baseline_right, (1, 1), "NMR_Data_AG")
    # interpolate with the normalized baseline
    d = d.interp("t2", baseline_for_int["t2"].copy())
    aot_integral = d["t2":aot_range].integrate("t2")
    d /= aot_integral.item()  # again normalize by integral
    fl.next(f"{dataset_name} AOT NMR")
    # fill baseline region before the water and aot overlap with other dataset
    baseline_for_int["t2":(0, crossover)] = d["t2":(0, crossover)]
    fl.plot(baseline_for_int["t2":display_range], "k:", label="baseline")
    # }}}
    # {{{
    colorcyc = cycle(colorcyc_list)
    w0 = {}
    for filename, expno, thislabel in file_list:
        thisc = next(colorcyc)
        d = load_pdata_as_nddata(filename + ".zip", (expno, 1), "NMR_Data_AG")
        fl.next(f"{dataset_name}: check TMS")
        fl.plot(d["t2":(-0.05, 0.05)], label=thislabel, color=thisc)
        # interpolate baseline into actual data
        d = d.interp("t2", baseline_for_int["t2"].copy())
        # calculate integral under AOT peak
        d /= d["t2":aot_range].integrate("t2").item()
        fl.next(f"{dataset_name} AOT NMR")
        fl.plot(d["t2":display_range], color=thisc, label=thislabel)
        fl.next(f"{dataset_name}: check subtraction")
        # subtract the baseline in the region of the water peak
        thissubtraction = (d - baseline_for_int)["t2":water_int_range]
        fl.plot(thissubtraction, color=thisc, label=thislabel)
        # {{{ integrate, and note that the "dry" sample has H2O, not H2O:D2O
        #      mix, so there are 2 protons for every water.  We must divide by
        #      2 for the dry, and also subtract the extra protons from the
        #      other samples (because the H2O in the "dry" is double-counted)
        #      Also note that the peak we are normalized to represents 2
        #      protons, so we need to multiply by 2
        thisint = thissubtraction.C.integrate("t2").item() * 2
        w0[thislabel] = thisint
        # }}}
        cs = thissubtraction.argmax("t2").item()
        fl.next("chemical shift", legend=True)
        fl.plot(
            w0[thislabel],
            cs,
            thismarker,
            color=thisc,
            label=dataset_name + " " + thislabel,
        )
    fl.next(f"{dataset_name} AOT NMR")
    range_dict = {
        "AOT": (aot_range, "red"),
        "H2O_int": (water_int_range, "blue"),
    }
    for thisrange in range_dict:
        plt.gca().axvline(
            range_dict[thisrange][0][0],
            ls="--",
            alpha=0.5,
            color=range_dict[thisrange][1],
        )
        plt.gca().axvline(
            range_dict[thisrange][0][1],
            ls="--",
            alpha=0.5,
            color=range_dict[thisrange][1],
        )
    # }}}
    fl.next("chemical shift")
    plt.gca().set_ylabel("chemical shift")
    plt.gca().set_xlabel("$w_0$")


def read_pdata_from_zip(zip_path, pdata_path):
    "Function to read pdata from zip file using temporary directory"
    with zipfile.ZipFile(zip_path, "r") as z:
        with tempfile.TemporaryDirectory() as temp_dir:
            # Extract the pdata directory to the temporary directory
            for file in z.namelist():
                if file.startswith(pdata_path):
                    z.extract(file, temp_dir)
            # Construct the full path to the extracted pdata directory
            extracted_pdata_path = os.path.join(temp_dir, pdata_path)
            # Read in the processed Bruker data
            dic, data = ng.bruker.read_pdata(extracted_pdata_path)
    return dic, data


def load_pdata_as_nddata(zipfile, pdata, exp_type):
    # Path to the ZIP file
    zip_path = psd.search_filename(zipfile, exp_type=exp_type, unique=True)
    # Define the path to the pdata within the zip
    pdata_path = f"{zipfile.replace('.zip','')}/{pdata[0]}/pdata/{pdata[1]}"
    # Read in the processed Bruker data from the zip file
    # Convert the data to a universal dictionary (udic) format
    # and create the NMR spectrum object with ppm axis
    dic, data = read_pdata_from_zip(zip_path, pdata_path)
    uc = ng.fileiobase.uc_from_udic(ng.bruker.guess_udic(dic, data))
    # Plot the spectrum
    retval = (
        psd.nddata(data.real, [-1], ["t2"])
        .setaxis("t2", uc.ppm_scale())
        .set_units("t2", "ppm")
        .set_prop("x_inverted", True)["t2", ::-1]
    )
    return retval


with psd.figlist_var() as fl:
    process_titration(
        dataset_name="H2O",
        thismarker="o",
        display_range=(2.5, 4.75),
        aot_range=(3.88, 4.5),
        water_int_range=(3.9, 4.05),
        dry_water_peak_range=(3.63, 3.87),
        dry_water_int_range=(3.64, 3.86),
        baseline_left="240607_1_h2o_dry.zip",
        baseline_right="240607_1_4p28uL_H2O.zip",
        crossover=3.93,
        file_list=[
            ("240607_1_h2o_dry", 3, "initial dry"),
            ("240607_1_4p28uL_H2O", 1, "H2O added"),
        ],
        fl=fl,
    )
