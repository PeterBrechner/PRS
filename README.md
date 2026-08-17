# PRS
PRS.py: Construct probabilistic ranges of solutions (PRSs) following the methodology in Brechner et al. (2026).

PRSgamma.py: Fit particle size distributions to gamma distributions following the methodology in Brechner et al. (2026).

PRSplot.py: Plot representations of a PRS.

PRSplotSix.py: Plot representations of 6 PRSs (3 quantitative regimes for 2 categorical regimes).
#
Recommended use:

Step 1 - Construct a PRSgamma.fitting() object.

Step 2 - Call get_params() on your fitting() object, which outputs the parameters needed for PRS.PRS() to a .MAT file.

Step 3 - Construct PRS.PRS() objects.

Step 4 - Construct PRSplot.PlotPRS() and PRSplotSix.PlotPRS() objects using your PRS.PRS() objects.

Step 5 - Call functions on your PlotPRS() objects to plot representations of PRSs.
