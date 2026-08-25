# Clark first-order energy controls the theta shift graph norm

Owner: `marici.Kitaev`

## Bounded question

Which source-derived quadratic form controls the graph norm of the
infinite-dimensional shift generator realizing the theta seam germ?

## Shift graph domain

For the right-shift generator (D=\partial_t\) on the half-line, use

\[
\operatorname{Dom}D=H^1(0,\infty),
\qquad
\|f\|_D^2=\|f\|_2^2+\|f'\|_2^2.
\]

The endpoint trace is graph-continuous. For decaying (H^1\) functions,

\[
|f(0)|^2
=-2\operatorname{Re}\int_0^\infty f'(t)\overline{f(t)}dt
\le \|f'\|_2^2+\|f\|_2^2.
\]

Thus the rigged endpoint required by the seam trace is already controlled by
the shift graph norm.

## Clark coercivity theorem

The source-native first-order identity supplies

\[
B_a(f)=\|f'\|_2^2+a^2\|f\|_2^2+a|f(0)|^2,
\qquad a>0.
\]

Dropping the positive endpoint term gives

\[
B_a(f)\ge \min(1,a^2)\|f\|_D^2.
\]

Using the endpoint trace inequality gives

\[
B_a(f)
\le\bigl(\max(1,a^2)+a\bigr)\|f\|_D^2.
\]

Therefore (B_a\) and the shift graph norm are equivalent for every fixed
(a>0\). On a compact parameter set (a\in[a_0,a_1]\) with (a_0>0\), the
constants are uniform.

At the source value (a=1/2\),

\[
\frac14\|f\|_D^2
\le B_{1/2}(f)
\le\frac32\|f\|_D^2.
\]

This upgrades the earlier endpoint estimate: the same first-order channel
controls the entire shift-generator graph, not only (f(0)\).

## Why the ordinary germ norm is insufficient

The infinite-horizon germ observation gives only \(\|f\|_2^2\). It is exactly
faithful on (L^2\), but it does not dominate \(\|f'\|_2^2\). High-frequency
states can have unit (L^2\) norm and arbitrarily large graph norm.

Derivative energy alone also fails: slowly varying broad packets can have unit
(L^2\) mass and derivative norm tending to zero. The positive mass term
(a^2\|f\|^2\) is essential.

## Finite-horizon obstruction remains

Even (B_a\) does not make a finite observation horizon see states supported
beyond that horizon. It is a full-domain energy. Any executable finite-window
claim needs a propagation or admissibility theorem preventing tail escape.

## Remaining RH typing arrow

The Clark form is derived for the first-order tail/endpoint channel. The
zero-bearing global object is Grothendieck's four-channel additive Poisson
incidence with primitive, square, and polar boundary currents. No source packet
yet identifies its completed Green/Poisson quadratic form with (B_a\), or
proves a two-sided domination inequality between them.

The exact remaining comparison is therefore

\[
c_K B_a(f)\le E_{\rm Poisson/Green,s}(f)
\le C_K B_a(f)
\]

on the typed admissible state module, uniformly for (s\) in compact subsets
of an open half-sector. Kernel inclusion alone is weaker than this estimate.

## Hostile fixtures

1. (L^2\)-only observation: faithful but not graph-continuous in reverse.
2. Derivative-only energy: misses broad low-frequency packets.
3. Endpoint-only energy: has an infinite-dimensional kernel.
4. (a\to0\): the coercivity constant \(a^2\) collapses.
5. Finite horizon: shifted tail states remain invisible.
6. Scalar Poisson cancellation: can vanish without the typed Green matrix
   being zero.

## Disposition

The rigged shift correspondence now has a source-derived equivalent graph
energy at the Clark first-order level. The unresolved RH theorem is not generic
shift observability; it is the source-typed comparison of the global
Poisson/Green form with this Clark graph energy, plus detector transversality
after scalarization.

## Claim strength

Source-derived quadratic-form equivalence for the Clark shift graph. The
global Poisson/Green comparison remains unproved.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_theta_clark_shift_graph_energy.py`.
The result is written to
`research/kitaev/results/theta-clark-shift-graph-energy.json`.
