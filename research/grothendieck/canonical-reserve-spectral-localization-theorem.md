# Canonical reserve minimizers localize leading spectral atoms

Status: finite-dimensional theorem; asymptotic application requires explicit
Vandermonde and tail estimates

Let

\[
\mu=\sum_{j\ge1}w_j\delta_{x_j},
\qquad
1>x_1>x_2>\cdots>0,
\qquad w_j>0,
\]

and use the canonical `x dx` reference norm

\[
\|p\|_R^2=\int_0^1x|p(x)|^2dx.
\]

For degree at most `n`, let `p_n` attain

\[
\varepsilon_n^{(x)}
=\min_{0\ne p\in\mathcal P_n}
\frac{\sum_{j\ge1}w_jx_j|p(x_j)|^2}{\|p\|_R^2},
\qquad \|p_n\|_R=1.
\]

## Explicit annihilator upper bound

Put

\[
P_n(x)=\prod_{j=1}^n(x-x_j).
\]

Testing the Rayleigh quotient with `P_n` gives

\[
\boxed{
\varepsilon_n^{(x)}
\le
\frac{\sum_{j>n}w_jx_j|P_n(x_j)|^2}
{\int_0^1x|P_n(x)|^2dx}.}
\]

This separates the two sources of reserve decay: the tail weights and the
products of spectral gaps.

## Weighted Vandermonde stability

Every `p in P_n` has a unique decomposition

\[
p=aP_n+r,
\qquad r\in\mathcal P_{n-1}.
\]

Since `P_n(x_j)=0` for `j<=n`, the leading-atom energy sees exactly `r`.
Define the finite evaluation stability constant

\[
\sigma_n
=\inf_{0\ne r\in\mathcal P_{n-1}}
\frac{\left(\sum_{j=1}^nw_jx_j|r(x_j)|^2\right)^{1/2}}
{\|r\|_R}>0.
\]

It is the smallest generalized singular value of the weighted Vandermonde
map against the `x dx` Gram.  For the reserve minimizer,

\[
\sigma_n^2\|r_n\|_R^2
\le\sum_{j=1}^nw_jx_j|p_n(x_j)|^2
\le\varepsilon_n^{(x)},
\]

and hence

\[
\boxed{\|r_n\|_R\le\frac{\sqrt{\varepsilon_n^{(x)}}}{\sigma_n}.}
\]

Because `||p_n||_R=1`, the reverse triangle inequality also gives

\[
|a_n|\,\|P_n\|_R
\ge1-\frac{\sqrt{\varepsilon_n^{(x)}}}{\sigma_n}.
\]

Thus whenever `sqrt(epsilon_n)<sigma_n`, the minimizing polynomial has full
degree and is quantitatively close, after scale, to the leading-atom
annihilator.

## Root localization

Fix pairwise disjoint complex disks

\[
D_j=\{z:|z-x_j|<\rho_j\},
\qquad 1\le j\le n.
\]

Let `C_n(rho)` be any bound satisfying

\[
\sup_{z\in\partial D_j}|r(z)|
\le C_{n,j}(\rho_j)\|r\|_R
\]

for `r in P_(n-1)`; it is explicit from the inverse Hilbert Gram or the
Christoffel function.  On the same circle,

\[
|P_n(z)|
\ge\rho_j\prod_{k\ne j}(|x_j-x_k|-\rho_j).
\]

Therefore Rouché's theorem gives one root of `p_n` in every `D_j` whenever

\[
\boxed{
C_{n,j}(\rho_j)
\frac{\sqrt{\varepsilon_n^{(x)}}}{\sigma_n}
<
\frac{1-\sqrt{\varepsilon_n^{(x)}}/\sigma_n}{\|P_n\|_R}
\rho_j\prod_{k\ne j}(|x_j-x_k|-\rho_j).}
\]

This is a finite, explicit spectral-localization certificate.  It proves the
observed root locking without assuming that small point values alone force
real roots.

## Interpretation

The mechanism is

\[
\text{small canonical reserve}
+\text{stable leading-atom evaluation}
\Longrightarrow
\text{annihilator proximity}
\Longrightarrow
\text{root localization}.
\]

Weights enter the stability and tail terms, but support gaps enter
multiplicatively through both `sigma_n` and `P_n(x_j)`.  This explains why
the comparison census is substantially more sensitive to support changes
than to moderate weight changes.

## Riemann-support comparison

For the comparison model formed from the first 80 reciprocal squared Riemann
zero energies with normalized source weights, the dimensionless remainder
ratio

\[
\eta_n=\frac{\sqrt{\varepsilon_n^{(x)}}}{\sigma_n}
\]

is

\[
\begin{array}{c|cccccccc}
n&1&2&3&4&5&6&7&8\\ \hline
\eta_n
&7.19\!\times10^{-4}
&4.84\!\times10^{-4}
&5.72\!\times10^{-4}
&5.51\!\times10^{-4}
&1.05\!\times10^{-3}
&1.07\!\times10^{-3}
&1.07\!\times10^{-3}
&1.96\!\times10^{-3}.
\end{array}
\]

Thus `eta_n<1` holds with roughly three decimal orders of reserve throughout
the census.  The finite theorem already forces annihilator dominance in the
canonical norm; the observed locking of polynomial roots is not merely a
visual coincidence.  Turning this into certified root disks requires only
the explicit Christoffel/Rouche constants displayed above.

## Scope

This theorem is measure-theoretic and does not prove that the completed
source has the RH spectral measure.  Using known Riemann zeros to evaluate
its constants is a comparison experiment only.  A source-only application
would first require the all-order Hausdorff positivity theorem and would then
recover atoms from moment data rather than assume them.

Comparison implementation:

- `checkers/quarter_point_reserve_rate_census.py`
