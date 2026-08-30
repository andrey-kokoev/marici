# The universal coupled positivity object is a Loewner kernel

Put

\[
 F(t)=(4t-1)S(t).
\]

Under the fractional coordinates

\[
 x=\frac{1-z}{4},\qquad y=\frac1{4(1-w)},
\]

the bivariate Hausdorff generator collapses to

\[
 \boxed{G(z,w)=yK_F(x,y)},\qquad
 K_F(x,y)=\frac{F(y)-F(x)}{y-x}.
\]

Thus the universal coupled object is the Loewner divided-difference kernel of
one completed-source function.

Conditionally on nonnegative squared spectral coordinates,

\[
 S(t)=\sum_\lambda\frac{m_\lambda}{t+\lambda}
\]

gives the rank-one Gram decomposition

\[
 \boxed{K_F(x,y)=\sum_\lambda
 \frac{m_\lambda(1+4\lambda)}{(x+\lambda)(y+\lambda)}}.
\]

Every coefficient is positive for `lambda>=0`. A negative squared coordinate
with `lambda<-1/4` immediately contributes a negative rank-one weight; more
generally off-real poles obstruct a real positive Loewner kernel.

## Why this is the right universal theorem

Positive semidefiniteness of every matrix `K_F(x_i,x_j)` says that `F` is
matrix monotone on the positive axis. Loewner theory then supplies a canonical
positive resolvent representation. With the known meromorphic Xi pole set,
that representation forces the squared spectral poles onto the nonpositive
real source axis, hence nonnegative `lambda`.

Accordingly, subject to the already recorded analytic continuation and pole
identification clauses, RH is equivalent to source-side Loewner positivity of

\[
 F(t)=(4t-1)\frac{1}{2s-1}\frac{\Xi'}{\Xi}(s),
 \qquad t=(s-1/2)^2.
\]

This directly answers the self-adjointness question: a positive Loewner kernel
constructs the positive resolvent measure and hence the self-adjoint Jacobi
operator. Self-adjointness is not assumed from a boundary operator; it is
reconstructed from source divided-difference positivity.

## New attack

Derive `K_F` directly from the endpoint-reduced gamma--prime source and prove
it is a Gram kernel. This one theorem would imply every linear Hausdorff
inequality, every Hankel/localizer corner, the unique Weyl limit, and the
conditional Hilbert--Polya operator at once.

## Scope

The algebraic identity and conditional Gram formula are proved. Source-side
Loewner positivity is not proved, so RH is not proved. The physical
relative-chain pushforward remains unavailable and separate.

## Durable verification

- Checker: `checkers/loewner_divided_difference_gram.py`
- Result: `results/loewner-divided-difference-gram.json`

Loewner's theorem reduces this further to one upper-half-plane Pick inequality.
In source coordinates the endpoint poles cancel exactly to the constant four,
leaving a coupled gamma--prime imaginary-part target. See
`reduced-gamma-prime-pick-target.md`.
