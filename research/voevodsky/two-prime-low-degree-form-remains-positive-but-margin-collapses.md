# The two-prime low-degree form remains positive, but its margin collapses

A floating Legendre calculation was performed at `L=0.55`, immediately above
the `p=3` threshold. It uses the same source normalization as the directed
first-prime packet:

\[
s_L(u)=
\frac{\Re\psi(1/4+iu/2)-\log\pi}{2}
-\sum_{p\in\{2,3\}}\frac{\log p}{\sqrt p}\cos(u\log p),
\]

together with the polar endpoint half-sum. The multiplier was integrated on
positive panels through frequency `1000` with 240 Gauss nodes per panel.

For the first 60 normalized Legendre modes, the smallest eigenvalues are
approximately

\[
2.50\times10^{-8},\quad
6.76\times10^{-6},\quad
6.81\times10^{-4},\quad
3.60\times10^{-2}.
\]

No negative eigenvalue appears in this cutoff scout.

A parity error initially produced a large false negative: even Legendre modes
have real Fourier transforms while odd modes carry a factor `i`, so their
real multiplier cross block is exactly zero. Enforcing that source parity
removes the spurious negative direction. This is a useful implementation
falsifier for future interval code.

The positive margin is about five orders smaller than the corrected
first-prime pivot margin. Thus the second-prime window is not refuted, but a
directed certificate will require substantially tighter quadrature and tail
bounds. The large bad-set measure does not by itself imply a negative compact-
support form; time-frequency concentration and source parity remain decisive.

This result is reconnaissance only: the multiplier tail beyond `1000`,
interval rounding, and the full finite-complement Schur estimate are not yet
certified.
