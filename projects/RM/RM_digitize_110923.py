# moved to paper repo
from PIL import Image
import numpy as np
from numpy import r_, newaxis
from scipy import interpolate
from lmfit import Minimizer, Parameters
import matplotlib.pylab as plt
from pyspecdata import *
import scipy
k_B = scipy.constants.k
print("k_B is",k_B)

data = {}
data["britton"] = dict(
    figure="Radius Britton fig9.png",
    origin=r_[46, 1],
    topright=r_[442, 216],
    newtopright=r_[30, 10],
    digitized={
        "R": [
            (35, 7.6),
            (30, 6.18),
            (25, 5.25),
            (20, 4.393),
            (10, 3.427),
            (35, 6.96),
            (30, 5.932),
            (25, 4.9),
            (20.02, 4.197),
            (20.02, 4.417),
            (15.082, 3.951),
            (15.064, 4),
            (9.99, 4.18),
            (5.3, 2.777),
        ]
    },
)
data["yoshioka"] = dict(
    figure="Yoshioka fig4.png",
    origin=r_[-744, 1755],
    topright=r_[310, 306],
    newtopright=r_[4.2, 9],
    digitized={
        "$w_0=0$": [
            (4.0792, 9.5267),
            (3.9345, 9.5253),
            (3.8, 9.5339),
            (3.662, 9.564),
            (3.54, 9.625),
            (3.423, 9.767),
            (3.324, 9.9),
        ],
        "$w_0=2.5$": [
            (4.1038, 9.4194),
            (3.9432, 9.4466),
            (3.8, 9.4351),
            (3.662, 9.523),
            (3.52, 9.704),
            (3.401, 9.978),
            (3.2873, 10.277),
        ],
    },
)
for thiskey, thisdata in data.items():
    plt.figure()
    # 1. Load the grayscale image
    img = Image.open(thisdata["figure"])
    gray_img = np.array(img.convert("L"))[::-1, ::]

    if "origin" in thisdata.keys():
        # W0=12
        origin = thisdata[
            "origin"
        ]  # this is 0,0 on the graph, in the original coordinates (find by moving the cursor and looking in the top right)
        topright = thisdata[
            "topright"
        ]  # this is the top right on the graph, in the original coordinates
        topright_newcoords = thisdata[
            "newtopright"
        ]  # this is the top right corner of the graph, as labeled
        corners = np.array([[0, 0], list(gray_img.shape)[::-1]])
        corners -= origin[newaxis, :]
        corners = np.double(corners)
        plot_coord_diff = topright - origin
        for j in range(2):
            corners[:, j] *= np.double(topright_newcoords[j]) / np.double(
                plot_coord_diff[j]
            )
        plt.imshow(
            gray_img,
            origin="lower",
            extent=corners.T.ravel(),
            aspect="auto",
            cmap="gray",
        )
        for thiskey, datapoints in thisdata["digitized"].items():
            x, y = map(np.array, zip(*datapoints))
            plt.plot(x, y, "o", label=thiskey, alpha=0.5)
        plt.legend()
    else:
        # assume you have not measured the corners yet
        plt.imshow(gray_img, origin="lower", aspect="auto", cmap="gray")
# {{{ plot the processed yoshioka data
plt.figure()
for thiskey, thisval in data["yoshioka"]["digitized"].items():
    x, y = map(np.array, zip(*thisval))
    # here x is -log τ_c
    tau = 10 ** (-y)
    T = 1000 / x
    plt.plot(1000 / T, np.log10(tau * T), "o-", label=thiskey)
    plt.ylabel(r"$\log(\tau_c T / \mathrm{s} \cdot \mathrm{K})$")
    plt.xlabel(r"1000 K / $T$")
plt.legend()
# }}}
# {{{ literature viscosity for heptane
# RS note references here
visc_data = [(254.1619011,6.8300E-04),
(273.0748225,5.1800E-04),
(292.1413964,4.1000E-04),
(300.8423586,3.7600E-04)]
viscT,visc = map(np.array,zip(*visc_data))
plt.figure()
c_visc = nddata(np.log10(visc/viscT),[-1],['invT']).setaxis('invT',1000/viscT).polyfit('invT')
def visc_vs_T(T):
    invT = 1000/T
    log_visc_times_T = c_visc[0]+c_visc[1]*invT
    return T*10**(log_visc_times_T)
plt.plot(1000/viscT,np.log10(visc/viscT),'o')
T = r_[250:305:100j]
plt.plot(1000/T, np.log10(visc_vs_T(T)/T))
plt.ylabel(r'$\log_10(\eta/T)$ of heptane')
plt.xlabel('1000 / T')
plt.figure()
plt.plot(viscT,visc,'o')
plt.plot(T, visc_vs_T(T))
plt.ylabel(r'$\eta$ of heptane')
plt.xlabel('T')
# }}}
# {{{ fit the britton data
plt.figure()
x, y = map(np.array, zip(*data["britton"]["digitized"]["R"]))
d = nddata(y, [-1], ["w0"]).setaxis("w0", x)
c = d.polyfit("w0", order=1)
def r_vs_w0(w0):
    return 1e-9*(c[0]+w0*c[1])
plot(d, "o")
w0_extended = nddata(r_[0:d['w0'].max():100j],'w0').run(r_vs_w0).run(lambda x: x/1e-9)# last is to convert m to nm
plot(w0_extended)
plt.text(
    s=f"${c[1]:0.3f} w_0 + {c[0]:0.3f}$",
    x=0.5,
    y=0.5,
    transform=plt.gca().transAxes,
)
print("at w0=0, R_H is", r_vs_w0(0))
print("at w0=2.5, R_H is", r_vs_w0(2.5))
# }}}
#{{{tau,rm calculation
# T_w0_300K= 1000/3.324
# tau_W0_300K= 10 ** (-9.9)
# print(tau_W0_300K)
##viscosity at W0=0
# n=(3*scipy.constants.k*T_w0_300K*tau_W0_300K)/(4*np.pi*((R_H_0*10**-9)**3))
# print(n)
##tau rm for w0=2.5
# plt.figure()
# x=np.array([[4.0792], [3.9345], [3.8], [3.662], [3.54], [3.423], [3.324]])
# y=np.array([[9.5267], [9.5253], [9.5339], [9.564], [9.625], [9.767], [9.9]])
# tau_2p5 = 10 ** (-y)
# T_w2p5 = 1000 / x
# tau_RM=(4*np.pi*n*(R_H_2P5*10e-9)**3)/(3*scipy.constants.k*T_w2p5)
# plt.plot(1000/T, np.log10(tau_RM * T_w2p5), "o-", label="tau_rm")
##}}}
plt.figure()
for thiskey, thisval in data["yoshioka"]["digitized"].items():
    thisw0 = float(thiskey.split("=")[1][:-1])
    print("w0 is",thisw0)
    x, y = map(np.array, zip(*thisval))
    #here x is -log τ_c
    tau = 10 ** (-y)
    T = 1000 / x
    plt.plot(1000 / T, np.log10(tau), "o-", label=thiskey)
    fudge_factor = 1#0.316
    # on the next line, we calculated τT, because it's supposed to be
    # proportional to η
    tau_T_RM = 4*np.pi*visc_vs_T(T)*(r_vs_w0(thisw0)*fudge_factor)**3/3/k_B
    # but here, we note we want η/T, which is proportional to
    # 1/D (D = diffusivity), which is what should be arrhenius
    plt.plot(1000 / T, np.log10(tau_T_RM/T), label=r"$\tau_{RM}$ for "+thiskey)
    plt.ylabel(r"$\log(\tau_c / \mathrm{s} \cdot \mathrm{K})$")
    plt.xlabel(r"1000 K / $T$")
    # following above reasoning, we just want log of τ
    tau_aq = 1/(1/(tau)-1/(tau_T_RM*T))
    plt.plot(1000 / T, np.log10(tau_aq), label =r"$\tau_{aq}$ for"+thiskey)
plt.ylabel(r"$\log(\tau_c T / \mathrm{s} \cdot \mathrm{K})$")
plt.xlabel(r"1000 K / $T$")
plt.legend()

plt.show()
