# notebook_example
Example lab notebook using tools embedded in pyspecdata

pySpecData comes with embedded with the capability to run and update python environments that are embedded into latex (we haven't done a detailed comparison of this to pythontex, which might also be an alternate option -- this is based on code we've been using for a long time, and just works for us).

*Also* for convenience, the repo includes a tarball of the texmf directory that you need -- unpack the .tgz file into a registered texmf directory, or else unpack and then register the directory to be able to `\usepackage{mynotebook}` which defined the `\begin{python}` environment and other things you need.
