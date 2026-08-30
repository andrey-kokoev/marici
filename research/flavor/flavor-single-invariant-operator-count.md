# Single-invariant operator-count theorem (WP262)

## Bounded theorem

Let \(x\) be one normalized weak-basis-invariant mixing coordinate with
\(0<x<1\). For a single nonconstant monomial source operator

\[
V_n(x)=c x^n,
\qquad c\neq0,
\qquad n\geq1,
\]

the derivative is

\[
V_n'(x)=ncx^{n-1},
\]

which never vanishes in the interior. A single homogeneous operator can prefer
a boundary, but it cannot select a nonzero, nonmaximal mixing point.

The minimal polynomial repair uses two degrees. For

\[
V(x)=-ax+bx^2,
\]

the interior stationary point is \(x_*=a/(2b)\). The location is therefore a
relative-coefficient datum, not a consequence of weak-basis invariance alone.

## Exact hostile relation

Selecting \(x_*=3/10\) requires

\[
a=\frac35 b.
\]

The coefficient packet \((a,b)=(3,5)\) realizes that point, while the equally
descending packet \((1,1)\) selects \(x_*=1/2\). The checker also verifies the
mixing coordinate under an exact nontrivial weak-basis rotation.

## Consequence

An interior selector requires more than an invariant operator grammar. At
least one relative coefficient must be derived by an independent symmetry,
radiative matching calculation, or microscopic source construction. Fitting
that relation from flavor readout is not selection.

This is a bounded single-coordinate polynomial theorem. It does not exclude a
symmetry that independently fixes coefficient ratios, multiple invariant
coordinates, nonpolynomial source geometry, or boundary-selected stationary
points. Those are the precise reopening classes.

Run `uv run --with sympy python
research/flavor/checkers/wp262_single_invariant_operator_count.py` for the
exact derivative family, target relation, hostile coefficient pair, and
weak-basis invariance test.
