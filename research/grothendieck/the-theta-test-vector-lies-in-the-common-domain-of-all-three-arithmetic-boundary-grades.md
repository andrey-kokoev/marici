# The theta test vector lies in the common domain of all three arithmetic boundary grades

## Positive-chart theta decay

For one theta label, put

\[
X=\pi n^2e^{2q}.
\]

Up to fixed normalization, its forcing atom has the form

\[
X^{1/4}e^{-X}(4X^2-6X).
\]

On `q>=0`, summing the labels gives constants `C,c>0` such that the completed
forcing satisfies the convenient bound

\[
|f(q)|
\leq
C(1+e^{5q})e^{-c e^{2q}}.
\]

The exponent `5` is not sharp. Its role is only to dominate the polynomial
prefactor; the superexponential term is decisive.

## Three arithmetic distributions

On the logarithmic scale, retain the typed currents

\[
\nu_1=\sum_p p^{-1/2}\delta_{\log p},
\]

\[
\nu_2=\frac12\sum_p p^{-1}\delta_{2\log p},
\]

and

\[
\nu_{\geq3}
=\sum_p\sum_{k\geq3}
\frac{p^{-k/2}}{k}\delta_{k\log p}.
\]

The primitive measure is not tempered, the square measure is tempered, and
the connected tail has finite total variation. They must not be merged into
one Hilbert grade.

## Common evaluation domain

Nevertheless, all three act absolutely on the fixed theta vector. Indeed,

\[
|f(k\log p)|
\leq
C(1+p^{5k})e^{-cp^{2k}}.
\]

Therefore

\[
|\nu_1(f)|
\leq
C\sum_p p^{-1/2}(1+p^5)e^{-cp^2}
<\infty,
\]

and

\[
|\nu_2(f)|
\leq
\frac C2\sum_p p^{-1}(1+p^{10})e^{-cp^4}
<\infty.
\]

For the connected tail,

\[
|\nu_{\geq3}(f)|
\leq
C\sum_p\sum_{k\geq3}
\frac{p^{-k/2}}{k}(1+p^{5k})e^{-cp^{2k}}
<\infty.
\]

Each sum is dominated by the corresponding sum over all integers. The
super-Gaussian factor dominates every displayed polynomial uniformly in the
relevant indices.

## A concrete positive-chart test space

For fixed `0<c_0<c`, define the weighted seminorm

\[
p_{c_0}(g)
=
\sup_{q\geq0}
\frac{|g(q)|e^{c_0e^{2q}}}{1+e^{5q}}.
\]

Every current above is a continuous functional on the corresponding
positive-chart space after choosing `c_0` below the theta decay rate. The
theta forcing has finite seminorm there.

This is only the arithmetic positive-chart component of the eventual test
rigging. It is not claimed to be closed under the full additive Fourier
transform. Reciprocal sewing must join it to the reflected chart before a
global rigging is declared.

## Rigged-transpose consequence

For the source incidence `B_f(c)=cf`, the canonical transpose

\[
B_f^\times(\lambda)=\lambda(f)
\]

is defined on each of the primitive, square, and connected-tail boundary
grades. Thus the arithmetic part of the transpose-domain gate is solved:
different completion classes do not obstruct evaluation on the single fixed
theta test vector.

What remains is not convergence. It is incidence matching:

\[
B_{-,X}(\nu_{j,X})
\stackrel{?}{=}
B_{f,X}^\times(\nu_{j,X})
\]

for each grade `j=1,2,>=3`, with the independently constructed reciprocal map
on the left.

## Important limitation

Absolute evaluation of the currents on `f` does not identify their scalar
continuations, merge their topologies, prove completion strictness, or orient
the Evans divisor. It establishes only the common source-domain fact needed
to state the transpose comparison without a type error.
