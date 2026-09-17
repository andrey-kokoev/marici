# The pi-over-L terminal normalization is not source-faithful on the fixed observer core

For `f` in a fixed Paley--Wiener source packet and every larger window,

\[
\langle P_{\gamma,L}f,f\rangle
=A_\gamma(f)
=|f(\gamma)|^2+|f(-\gamma)|^2.
\]

Hence

\[
\left\langle {\pi\over L}P_{\gamma,L}f,f\right\rangle
={\pi\over L}A_\gamma(f)\longrightarrow0.
\]

For any fixed observer with nonzero point readout, the original terminal
source form remains nonzero while the normalized form vanishes.  Therefore
the trace-two normalization `(pi/L)P_{gamma,L}` is not a source-faithful
realization on the established fixed observer core.  Rescaling the source
norm simultaneously would change the declared source realization and cannot
be used as an internal filler without a new comparison theorem.

The exact identity is independent of the numerical fixture; the checker
`check_normalized_terminal_rotor_loses_fixed_source_readout.py` supplies one
explicit `PW_1` observer.

Together with the nonproportionality of atomic and bulk functionals, this
eliminates both scalar remedies inside the current source-faithful category:

1. adding a scalar multiple of the bulk Plancherel row cannot cancel the
   atomic functional for every observer;
2. multiplying the atomic row by `pi/L` destroys its fixed-source readout.

Thus a resolution of the terminal pro-horn now specifically requires a
crossing-dependent geometric/index row with the same atomic source functional
and compatible shared-face, dagger, successor, and translation laws.  Its
existence remains open.
