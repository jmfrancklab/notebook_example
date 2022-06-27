# notebook_example
Example lab notebook using tools embedded in pyspecdata.

To make this work, clone this repo, unpack the zip/tgz file into your home directory, and register it as a texmf directory (or unpack into your existing registered texmf directory -- [for miktex see here](https://miktex.org/kb/texmf-roots) -- for linux/unix/mac use initexmf).  Then use `pdflatex_notebook_wrapper -synctex=1 notebook.tex` (in the main directory of this repo, the command `pdflatex_notebook_wrapper` is supplied by pySpecData)

pySpecData comes with embedded with the capability to run and update python environments that are embedded into latex (we haven't done a detailed comparison of this to pythontex, which might also be an alternate option -- this is based on code we've been using for a long time, and just works for us).

*Also* for convenience, the repo includes a tarball of the texmf directory that you need -- unpack the .tgz file into a registered texmf directory, or else unpack and then register the directory to be able to `\usepackage{mynotebook}` which defined the `\begin{python}` environment and other things you need.

## Organization

It's not required for you to organize your notebook in this way, but we show a recommended structure where actual notebook info lives inside a folder organized by project.
Then, to know what happened on a given day, you can have files that are organized by date -- these are like a manual “table of contents,” and you provide references to what happened on that date.
