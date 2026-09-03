# The completed Weil form is not globally continuous in the L2 norm

## Question

Can the exact `L2` tail fraction of a truncated inverse Gaussian be multiplied by a fixed constant to control the corresponding Weil-form error?

## Claim

No global estimate

\[
|Q(f)|\le C\|f\|_2^2
\]

holds on the full test space with one finite constant `C`. Consequently the exact `L2` tail calculation does not by itself compare Gaussian truncation error with a compact-window positivity margin.

## High-frequency obstruction

Choose a nonzero compactly supported smooth function `phi` and define

\[
f_N(x)=e^{iNx}\phi(x).
\]

Its Fourier transform is a translate,

\[
F_N(u)=\widehat\phi(u-N),
\]

while

\[
\|f_N\|_2=\|\phi\|_2.
\]

On any fixed compact support window, the geometric Weil form has an archimedean multiplier containing

\[
\operatorname{Re}\psi\!\left(\frac14+\frac{iu}{2}\right)-\log\pi
=\log|u|-\log(2\pi)+O(u^{-2}).
\]

Therefore

\[
\int_{\mathbb R}|F_N(u)|^2
\left[\operatorname{Re}\psi\!\left(\frac14+\frac{iu}{2}\right)-\log\pi\right]du
=\log N\,\|\phi\|_2^2+O_\phi(1).
\]

The finite prime comb associated with the fixed support has bounded multiplier, and the endpoint evaluation contributes only a bounded term for this family. Hence `Q(f_N)/||f_N||_2^2` is unbounded as `N` tends to infinity.

This obstruction is source-side and does not depend on RH.

## Correct topology for truncation error

A valid comparison must control at least three distinct seminorms:

1. an archimedean logarithmic Fourier norm such as
   \[
   \int_{\mathbb R}\log(2+|u|)|F(u)|^2\,du;
   \]
2. the endpoint functional `F(i/2)`, equivalently an exponential moment of `f`;
3. the arithmetic translation correlations sampled at logarithms of prime powers.

For the decomposition `f=f_L+r_L`, the required object is a direct bound on

\[
Q(f)-Q(f_L)=2\operatorname{Re}B(f_L,r_L)+Q(r_L),
\]

where `B` is the polarized completed Weil form. Applying Cauchy--Schwarz in `Q` would assume positivity and is circular. Each endpoint, gamma, and prime block must instead be bounded from its explicit source formula.

## Consequence for the fixed-window proposal

The identity

\[
\frac{\|r_L\|_2^2}{\|f\|_2^2}
=\operatorname{erfc}\!\left(\frac{2\pi L}{\sqrt t}\right)
\]

remains an exact scale diagnostic, but it is not a form-error estimate. The next calculation must use the explicit Gaussian tail to bound:

- the endpoint cross and tail terms;
- the digamma-weighted Fourier cross and tail terms;
- every prime-power translation cross and tail term, with a convergent common majorant.

A smooth cutoff may reduce high-frequency leakage in the gamma term; a sharp cutoff is admissible only if the selected localized form theorem genuinely extends to `L2` factors and the global difference terms remain defined.

## Disposition

The proposed unit-scale `L2` continuity shortcut is rejected. The compact-window route remains live only through a blockwise explicit-formula error estimate in a stronger declared topology. This is a smaller and executable target, but no such bound has yet been proved.
