# First certified Suzuki second-stage kernel minors

The canonical non-tautological second-stage candidate is the de Branges--Rovnyak kernel

\[
k_\Theta(z,w)=\frac{1-\Theta(z)\overline{\Theta(w)}}{-i(z-\bar w)},
\qquad
\Theta=E^\#/E,
\quad
E(z)=\xi(1/2-iz)+\xi'(1/2-iz).
\]

Unlike squaring the already positive Suzuki norm, positivity of this kernel tests the missing upper-half-plane contractivity directly.

`checkers/suzuki_debranges_kernel_scout.py` evaluates `xi` and `xi'` by Arb power series, forms `Theta` without zero data, and certifies diagonal values and every two-point principal minor on the four-point set

\[
0+0.4i,
\quad3+0.5i,
\quad7+0.75i,
\quad12+i.
\]

All four diagonal intervals are strictly positive. All six two-point determinants are strictly positive. The smallest certified determinant is approximately

\[
1.22201198121422\times10^{-4}.
\]

The executable result is stored in `results/suzuki-debranges-kernel-scout.json`.

This is a finite source-only certificate, not a continuum statement or an RH proof. It establishes that the correct second-stage kernel is computationally accessible with rigorous complex balls. The next step is adaptive point insertion followed by certified full-matrix positivity (LDL/Schur complements), then parameter boxes. This route tests the actual innerness gate rather than a quartic surrogate.
