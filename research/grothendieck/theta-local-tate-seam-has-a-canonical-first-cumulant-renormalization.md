# The local Tate seam has a canonical first-cumulant renormalization

## Bounded question

Nima proved that the raw critical-line local transitions fail the canonical
infinite-tensor implementability criterion. Is the divergent part structurally
isolated, and does removing it leave an implementable projective family?

## Exact local phase expansion

On the critical line put

\[
 r_p=p^{-1/2},
 \qquad
 \theta_p=t\log p.
\]

Then

\[
 \gamma_p
 =\frac{1-r_pe^{-i\theta_p}}{1-r_pe^{i\theta_p}}.
\]

Using the power series for the logarithm,

\[
 \boxed{
 \log\gamma_p
 =2i\sum_{k\ge1}
 \frac{r_p^k\sin(k\theta_p)}{k}.}
\]

The leading term is

\[
 2ip^{-1/2}\sin(t\log p).
\]

Its squared magnitude is of order `1/p`, producing precisely the logarithmic
prime divergence found by Nima. Every higher local term starts at order
`1/p`.

## First connected-cluster subtraction

Define the locally renormalized transition

\[
 \boxed{
 \widetilde\gamma_p(t)
 =\gamma_p(1/2+it)
 \exp\left[-2ip^{-1/2}\sin(t\log p)\right].}
\]

Then

\[
 \log\widetilde\gamma_p
 =2i\sum_{k\ge2}
 \frac{p^{-k/2}\sin(kt\log p)}{k}
 =O(p^{-1}),
\]

uniformly for real `t`. Consequently

\[
 |1-\widetilde\gamma_p(t)|^2=O(p^{-2})
\]

and

\[
 \boxed{
 \sum_p|1-\widetilde\gamma_p(t)|^2<\infty.}
\]

Thus the first-cumulant-renormalized local seams satisfy the raw square-
summability requirement for a projective/infinite-tensor implementer.

## Interpretation of the removed channel

The removed term is not an arbitrary counterphase. It is exactly the
primitive-prime contribution `k=1` in the logarithm of the local Euler/Tate
transition. The retained terms are the prime-power tower `k>=2`.

The term “first cumulant” here means first connected coefficient in the
fugacity/plethystic logarithm. It is not probabilistic centering by the mean
occupation number.

This matches the source grammar found earlier:

\[
 \boxed{
 \text{primitive prime current}
 +\text{square-summable prime-power dressing}.}
\]

At `t=0`, the primitive current vanishes and no subtraction occurs, agreeing
with Nima's exact raw implementability there.

Formally, before continuation,

\[
 \sum_p\log\gamma_p(s)
 =\log\frac{\zeta(1-s)}{\zeta(s)}.
\]

On the critical line this is `-2i Im log zeta(s)` with the corresponding
branch convention, and the removed term is exactly its `k=1` Euler-logarithm
component. Thus the identity of the divergent channel is independently fixed
by the prime source grammar. This does not yet authorize deleting it.

## Scope boundary

Square summability of the renormalized local deviations establishes a
candidate projective implementer. It does **not** prove convergence of a
canonically phased scalar product

\[
 \prod_p\widetilde\gamma_p(t),
\]

because the residual phase begins at order `1/p` and may require conditional
summation or a determinant prescription. Nor has the source yet authorized
discarding the primitive current.

The candidate global object is therefore a projectively phased family:

\[
 \text{implementable renormalized local family}
 +\text{explicit primitive-prime phase defect}.
\]

## Next gate and falsifier

Derive the first-cumulant subtraction from a source operation—normal ordering
of the positive prime Fock current, a relative determinant, or the global
product formula—rather than adopting it because it converges.

Analytic continuation through `log zeta` is not by itself an acceptable
derivation: its branches and singularities already know the global divisor.
The renormalization must be constructed before that scalar continuation if it
is to carry independent RH force.

The parameter `t` does not make `gamma_p(t)` a group character, so an additive
cocycle law is not imposed. The falsifier is instead a mismatch between the
subtracted primitive current and the independently derived logarithmic Euler
source, or failure of one uniform normal-ordering/relative-determinant rule to
produce the same subtraction at every prime. Either would make the
renormalization an inadmissible fitted counterterm.
