# Source-normalized Breit-Wheeler tree kernel

The nonforward Cutkosky calculation now has an independently normalized tree
kernel for

\[
\gamma\gamma\longrightarrow e^+e^-.
\]

Using metric \((+---)\), \(m_e=1\), and \(e=1\), the two QED diagrams were
implemented as a Dirac matrix between the electron and positron completeness
numerators. Two gates were applied before admitting the kernel:

1. replacing either photon polarization by its momentum annihilates the
   spin-summed matrix element to double-precision roundoff;
2. after averaging over the four incoming linear-polarization states and
   integrating the two-body phase space, the result reproduces

\[
\sigma_{\rm BW}
=\frac{\pi\alpha^2}{2m_e^2}(1-\beta^2)
\left[
(3-\beta^4)\log\frac{1+\beta}{1-\beta}
-2\beta(2-\beta^2)
\right]
\]

at \(\beta=0.2,0.6,0.9\), with relative error below \(2\times10^{-12}\).

This fixes the diagram ordering, flux, polarization average, phase-space
normalization, and coupling convention needed by the nonforward cut.

Reproduce with
`research/nima/check_breit_wheeler_tree_normalization.py`.
