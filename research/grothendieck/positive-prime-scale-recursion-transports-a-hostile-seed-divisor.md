# Positive prime-scale recursion transports a hostile seed divisor

## Result

An exact positive scale recursion does not constrain the divisor inherited
from its primitive remainder.

Let `w` denote the multiplicative spectral character, let `0 < c < 1`, and
let a positive primitive source have transform

\[
R(w)=\sum_{j=0}^d a_jw^j,
\qquad a_j\geq0.
\]

Complete it by repeated positive transport through one scale step:

\[
\Phi= A+cT_L\Phi.
\]

In the transform chart where `T_L` acts by multiplication by `w`, the unique
formal solution is

\[
F(w)=R(w)+cwF(w)=\frac{R(w)}{1-cw}.
\]

Every coefficient of `F` is nonnegative. Nevertheless, every zero of `R`
away from the positive pole `w=1/c` remains a zero of `F`. Positive recursive
transport supplies provenance and multiplicity, but it supplies no new
orientation of the primitive divisor.

## Smallest witness

Take

\[
R(w)=1+2w,
\qquad c=\frac13.
\]

Then

\[
F(w)=\frac{1+2w}{1-w/3}
\]

is the transform of a positive recursively generated source. Its series is

\[
F(w)=1+\sum_{n\geq1}\left(3^{-n}+2\,3^{-(n-1)}\right)w^n,
\]

so every source coefficient is strictly positive. But the hostile zero

\[
w=-\frac12
\]

survives, because the denominator there is `7/6`.

If `w=e^z`, this gives

\[
z=-\log2+(2k+1)i\pi,
\]

which is off the unitary seam `Re z = 0`.

## What this rules out

The recursion is an authorized transport grammar: it says which translated
copies exist and that their weights are positive. It does not select the
primitive remainder. Iterating several independent positive scale recursions
only multiplies `R` by further geometric factors in their common convergence
chamber, so it still preserves every primitive zero not coincident with a
pole.

Therefore neither one-prime recursion nor positive Fock closure by itself can
be the missing RH conservation law. A surviving theorem must constrain the
primitive seed through a relation that is not triangular in scale—most
plausibly the full archimedean/modular sewing relation or an equivalent
cross-scale boundary condition. That relation must reject the hostile seed
before its zeros are inspected.

## Mirroring the recursion does not repair it

The same obstruction survives the obvious two-sector completion. Take the
positive reciprocal primitive seed

\[
R_{\rm rec}(w)=(1+2w)(1+2w^{-1}).
\]

It has the reciprocal off-unit pair `w=-1/2,-2`. Apply equal positive
geometric transport in both directions:

\[
F_{\rm rec}(w)=
\frac{R_{\rm rec}(w)}{(1-cw)(1-cw^{-1})}.
\]

For `c=1/3`, both hostile zeros lie in the common annulus
`1/3 < |w| < 3`, and neither denominator vanishes there. The Laurent
expansion is coefficientwise positive and invariant under `w -> 1/w`, yet
the reciprocal off-seam zero pair survives exactly.

Thus reciprocal doubling of two independent triangular recursions is still
only an invertible localization of the primitive divisor. The missing sewing
law must be a genuine relation between the two scale directions, not the
product of their separately completed charts.

## Falsifier

Any claimed zero-confinement theorem derived solely from positivity and the
recursion `F = R + cwF` is falsified by `R=1+2w`, `c=1/3`. A stronger proposal
must name the additional source law and show exactly where this source violates
it.

Checker: `check_positive_recursion_transports_hostile_divisor.py`.
