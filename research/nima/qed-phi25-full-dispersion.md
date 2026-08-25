# The crossing-even channels need one boundary value each

Owner: marici.Nima

At fixed \(T=-1/4\), the Bose-reduced amplitudes \(\Phi_2\) and \(\Phi_5\)
are crossing-even. Their coupled right/left cuts therefore coincide, and the
twice-subtracted dispersive part is

\[
D_i(\nu,T)=
\frac{\nu^2}{\pi}\int_{\nu_0}^{\infty}
\frac{\rho_i(\nu',T)}{\nu'^2}
\left(
\frac1{\nu'-\nu}+\frac1{\nu'+\nu}
\right)d\nu'.
\]

Crossing forbids a linear subtraction. We fitted one constant

\[
c_i(T)=\Phi_i(0,T)
\]

from the first real point and retained it unchanged at every other point.

For \(\Phi_2\), four held-out real points and two hostile complex points have
relative residuals

\[
1.31\times10^{-7},
\qquad
9.10\times10^{-8}.
\]

For \(\Phi_5\), the corresponding residuals are

\[
2.35\times10^{-5},
\qquad
1.63\times10^{-5}.
\]

The latter are below the independently measured coarse/fine quadrature change
\(1.43\times10^{-4}\).

## Vector result

Together with the \(\Phi_1\) crossing pair, the complete three-function
one-loop helicity packet is reconstructed on the tested domain by:

- the source-labelled electron cuts;
- the tensor crossing action;
- the crossing-fixed first boundary jet.

No additional polynomial direction, missing cut, or inner/CDD residual is
detected. The surviving boundary data are finite-dimensional:

\[
\Phi_1(0,T),\quad
\partial_\nu\Phi_1(0,T),\quad
\Phi_2(0,T),\quad
\Phi_5(0,T).
\]

Their transfer dependence remains source data and must not be replaced by
arbitrary constants across \(T\).

Reproduce with
uv run --with numpy --with mpmath python
research/nima/checkers/check_qed_phi25_full_dispersion.py.

