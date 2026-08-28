# Squared Bargmann orientation creates a conjugate pair only on the rank-two boundary: WP962

## Question

Can the least adjustable nonlinear CP-even orientation source,
`-(Im B)^2`, force a spanning conjugate pair with nonzero Bargmann magnitude?

## Source term and exact bound

For three normalized rays let

\[
\mathcal B=\operatorname{Tr}(PQR)=r+iq
\]

and let `x`, `y`, and `z` be the three squared pairwise overlap magnitudes.
Their Gram determinant obeys

\[
D=1-x-y-z+2r\geq0,
\qquad q^2=xyz-r^2.
\]

Put `s=x+y+z`.  If `s` is at most one, arithmetic-geometric mean gives
`q^2 <= (s/3)^3 <= 1/27`.  If `s` is at least one, Gram positivity gives
`r >= (s-1)/2`, hence

\[
q^2\leq\left(\frac{s}{3}\right)^3-rac{(s-1)^2}{4}leq\frac1{16}.
\]

The second bound is sharp at `s=3/2`.  Equality requires

\[
x=y=z=\frac12,
\qquad r=\frac14,
\qquad q=\pm\frac14,
\qquad D=0.
\]

Thus the global maximizers of `(Im B)^2` are a conjugate pair, but their Gram
rank is two.  An exact representative is supplied by the rays proportional to
`(1,0,0)`, `(1,1,0)`, and `(1,i,0)`.

## Pairwise-factorization hostile

The modulus factors through pairwise data:

\[
|\mathcal B|^2=xyz.
\]

But pairwise overlaps do not determine the orientation magnitude.  Two exact
positive-definite Gram matrices with `x=y=z=1/4` have respectively
`B=1/8` and `B=i/8`.  They are identical to every pairwise-modulus probe but
have different `|Im B|`.  Therefore the successful term is genuinely ternary;
it cannot be explained as an aggregation of the WP960 tester family.

## Disposition

The squared-orientation term proves that a CP-even source can select a
conjugate pair with nonzero absolute orientation, but not on the faithful
three-family interior.  Its unconstrained optimum collapses to a rank-two
boundary.  A viable source must independently supply a positive volume or
completion term that keeps `D>0`; the relative normalization between volume
and orientation may not be fitted from flavor readout.  Exact conjugation
symmetry still cannot select one handedness.  Instrument transport remains
open.  No composition is assigned physical time or causality.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp962_squared_bargmann_orientation_boundary_no_go.py

Generated result:
`research/flavor/results/wp962_squared_bargmann_orientation_boundary_no_go.json`.
