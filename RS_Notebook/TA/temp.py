from pyspecdata import *
def my_residual_transform(d):
    d.ft("B")
    return d.real
with figlist_var() as fl:
    B = sp.symbols("B", real=True) # this ends up being not field, but the inverse Fourier domain for field
    data = nddata(r_[3000:3600:500j],'B') # normally this would be the spectrum
    data.ift('B', shift=True) # don't shift
    data = lmfitdata(data)
    npeaks = 3
    # {{{ set up arrays of symbols that we use below.  I start with an array of empty strings, just b/c that's easier for me to replace.
    A = list(['']*npeaks)
    R = list(['']*npeaks)
    nu = list(['']*npeaks)
    the_guesses = {}
    # }}}
    thefunction = 0
    for j in range(npeaks):
        # generate a unique amplitude, linewidth, and center frequency for each peak
        A[j], R[j], nu[j] = sp.symbols(f"A{j} R{j} nu{j}", real=True)
        # {{{ this is the ift of the derivative of a Lorentzian
        thefunction += (
                A[j]
                * (-1j * 2 * pi * B)
                * sp.exp(1j * 2 * pi * nu[j] * B)
                * sp.exp(-R[j] * sp.pi * abs(B))
                )
        # {{{ start out with all guesses the same
        the_guesses.update(
                {
                    str(A[j]): 1,
                    str(R[j]): 20.,
                    str(nu[j]): 3300,
                    })
        # }}}
        # }}}
    data.functional_form = thefunction
    data.residual_transform = my_residual_transform
    # {{{ change only the fields
    the_guesses['nu0'] = 3100.
    the_guesses['nu1'] = 3300.
    the_guesses['nu2'] = 3500.
    # }}}
    data.set_guess(the_guesses)
    # eval returns in the frequency domain, b/c residual transform transforms it
    plot(data.settoguess().eval())
