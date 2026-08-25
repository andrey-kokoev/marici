# The prime-Fock seam has an exact Schatten-three filtration

## Bounded question

Does the plethystic prime-power degree determine a canonical global
regularization class, rather than merely suggesting an ad hoc phase
subtraction?

## Exact connected expansion

On the critical line put

\[
 r_p=p^{-1/2},\qquad \theta_p=t\log p.
\]

The source-derived local Tate transition satisfies

\[
 \log\gamma_p
 =2i\sum_{k\ge1}\frac{r_p^k\sin(k\theta_p)}{k}.
\]

Its connected prime-power degrees fall into three different global summability
classes:

\[
 \begin{array}{c|c|c}
 k & \text{prime coefficient size} & \text{global type}\\
 \hline
 1 & p^{-1/2} & \ell^q\ (q>2),\ \text{not }\ell^2\\
 2 & p^{-1} & \ell^2,\ \text{not }\ell^1\\
 k\ge3 & O(p^{-3/2}) & \ell^1.
 \end{array}
\]

The qualifications are generic in `t`: special phases can annihilate
individual coefficients, but they do not change the source-level filtration.
The convergence statements follow from the prime subseries of the ordinary
`p`-series.

## Two distinct regularization thresholds

Removing only the primitive degree gives

\[
 \gamma_p^{[2]}
 =\gamma_p\exp\!\left(-2ir_p\sin\theta_p\right),
\]

with

\[
 \log\gamma_p^{[2]}=O(p^{-1}).
\]

Hence its local deviations are square summable across primes. This is the
threshold for a projective or Hilbert implementation candidate. It does **not**
make the scalar Euler product absolutely convergent, because the connected
prime-square term is generally only `ell^2`, not `ell^1`.

Removing the first two connected degrees gives

\[
 \boxed{
 \gamma_p^{[3]}
 =\gamma_p\exp\!\left[-2i\left(
 r_p\sin\theta_p+\frac{r_p^2}{2}\sin(2\theta_p)
 \right)\right].}
\]

Now

\[
 \log\gamma_p^{[3]}
 =2i\sum_{k\ge3}\frac{r_p^k\sin(k\theta_p)}{k}
 =O(p^{-3/2}),
\]

uniformly on real `t`. Therefore

\[
 \sum_p\left|\log\gamma_p^{[3]}\right|<\infty,
\]

so the degree-three-renormalized scalar prime product converges absolutely.

## Determinant interpretation

The primitive prime carrier has singular scale `p^(-1/2)`. Consequently its
global diagonal perturbation belongs to every Schatten class `S_q` for
`q>2`, in particular `S_3`, but not to `S_2`:

\[
 \sum_pp^{-q/2}<\infty\quad(q>2),
 \qquad
 \sum_pp^{-1}=\infty.
\]

The subtraction of connected logarithmic degrees one and two is exactly the
subtraction pattern of an order-three regularized determinant. Thus the first
integer determinant class authorized by the source asymptotics is `det_3`,
not `det_2`.

This statement concerns the regularization *order*. Identifying the scalar
product of the `gamma_p^[3]` with a Fredholm `det_3` still requires an explicit
source-derived global operator whose eigenvalue packet has these local
transitions. The summability calculation alone does not construct that
operator.

## Three-rigging architecture

The global seam therefore has three typed layers:

\[
 \boxed{
 \begin{aligned}
 k=1 &: \text{distributional primitive prime current},\\
 k=2 &: \text{Hilbert but non-trace-class prime-square current},\\
 k\ge3 &: \text{trace-class connected tail}.
 \end{aligned}}
\]

This is stronger than a two-rigging split. The prime-square channel is the
intermediate seam: it is already implementable at the quadratic level but
still contributes a non-absolutely-summable determinant phase.

## Claim boundary and falsifier

No term has been deleted from the completed arithmetic object. The exact
finite-cutoff identity is

\[
 \prod_{p\le X}\gamma_p
 =\exp\!\left(2i\sum_{p\le X}\left[
 r_p\sin\theta_p+\frac{r_p^2}{2}\sin(2\theta_p)
 \right]\right)
 \prod_{p\le X}\gamma_p^{[3]}.
\]

Any global relative determinant must retain the two displayed countercurrents
and reproduce this identity before taking a limit. The proposed architecture
is falsified if the eventual source-derived operator has a different Schatten
threshold, or if modular/archimedean sewing fails to absorb the degree-one and
degree-two currents without changing the completed divisor.

