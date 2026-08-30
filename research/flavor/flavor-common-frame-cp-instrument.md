# Common-frame CP instrument (WP331)

## Instrument contract

WP331 replaces the abstract complementary coordinates of WP330 by three
co-located channels in one freeze-out cell:

\[
A=e^{-\beta\Delta},
\qquad
C=\kappa c_0,
\qquad
L=2\beta\epsilon c_0.
\]

Here (Delta) is an independently calibrated two-level thermometer gap and
(kappa) is an independently calibrated CP-amplitude gain. The three channels
must share the same support, time window, normalization record, and freeze-out
history.

With frozen (Delta) and (kappa), the response determinant is

\[
2\beta c_0\Delta\kappa e^{-\beta\Delta},
\]

which is nonzero on the positive domain. The exact inverse is

\[
\beta=-\frac{\log A}{\Delta},
\qquad
c_0=\frac{C}{\kappa},
\qquad
\epsilon=\frac{L\Delta\kappa}{-2C\log A}.
\]

## Calibration kernel

If (Delta) and (kappa) are allowed to float with the source parameters,
the three-channel response has a two-dimensional rescaling kernel. Algebraic
compatibility therefore does not replace independent calibration.

## Status

This is an executable algebraic instrument contract, not an established
laboratory or cosmological instrument. It identifies the prepared source
packet conditional on frozen calibrations; it does not select that packet's
values.

Physical admission requires a real co-located transition and CP transducer,
uncertainty and drift bounds, freeze-out simultaneity, repeated domain samples,
and the nonzero detector-contrast gate from WP329.

Run `uv run --with sympy python
research/flavor/checkers/wp331_common_frame_cp_instrument.py` to regenerate the
exact contract audit.
