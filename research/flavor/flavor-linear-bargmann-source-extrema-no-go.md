# The linear CP-even Bargmann source selects only rank-deficient CP-blind extrema: WP961

## Question

Does the lowest ternary weak-basis invariant repair WP960 and derive a
spanning CP-bearing ordered triple without fitted overlap targets?

## Frozen source term

For normalized rank-one projectors define the Bargmann invariant

\[
\mathcal B(P,Q,R)=\operatorname{Tr}(PQR).
\]

The lowest real CP-even ternary source term is

\[
V_{\rm cyc}=\kappa\operatorname{Re}\mathcal B.
\]

It is invariant under simultaneous weak-basis conjugation and independent
rescaling of the three source triplets.  Complex conjugation preserves it, so
it cannot explicitly choose a CP orientation.

## Exact global bounds

Write the three pairwise overlap magnitudes as `a`, `b`, and `c`.  Positivity
of their Gram matrix gives

\[
1-a^2-b^2-c^2+2\operatorname{Re}\mathcal B\geq0.
\]

The upper bound is immediate:

\[
\operatorname{Re}\mathcal B\leq |\mathcal B|=abc\leq1,
\]

with equality for three coincident rays.  For a negative real Bargmann value,
the Gram inequality and arithmetic-geometric mean imply

\[
1-3(abc)^{2/3}-2abc\geq0,
\]

so `abc` is at most `1/8` and

\[
-\frac18\leq\operatorname{Re}\mathcal B.
\]

The lower bound is attained by the real trine: three coplanar unit rays with
all signed inner products equal to `-1/2`.  Its Gram determinant is zero and
its span has rank two.

## Source classification

- Positive `kappa` selects the trine lower endpoint with
  `Bargmann=-1/8`, zero imaginary part, and span rank two.
- Negative `kappa` selects the collinear upper endpoint with `Bargmann=1`,
  zero imaginary part, and span rank one.
- Zero `kappa` leaves the relational triple flat.

Thus the linear CP-even ternary invariant reaches only CP-blind,
rank-deficient boundary strata.  It is ternary but orientation-even; taking a
real part removes precisely the conjugation-odd datum needed by WP959.

## Disposition

WP961 closes the unfitted linear Bargmann branch.  A spanning spontaneous-CP
source must contain nonlinear phase frustration that can favor nonzero
`(Im B)^2` while retaining conjugate minima, or an independently authorized
CP-odd term proportional to `Im B`.  The latter cannot be inserted merely to
choose the observed sign.  Completion stability and calibrated instrument
transport remain open.  No composition is assigned physical time or
causality.

## Smallest exact falsifiers

The real trine realizes the exact minimum `-1/8` at span rank two; the
coincident triple realizes the maximum `1` at span rank one.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp961_linear_bargmann_source_extrema_no_go.py

Generated result:
`research/flavor/results/wp961_linear_bargmann_source_extrema_no_go.json`.
