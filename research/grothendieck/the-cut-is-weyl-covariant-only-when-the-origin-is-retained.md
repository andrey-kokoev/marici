# The Cut Is Weyl-Covariant Only When the Origin Is Retained

## The commutator audit

Let (C_L) be the exact (H^1) tail–seam cut and write (T_Lf(y)=f(y+L)). The two generators of the source Weyl algebra behave differently.

Differentiation is strictly covariant:

\[
T_L\partial_y=\partial_yT_L.
\]

Multiplication by the global wall coordinate is affine-covariant:

\[
T_L\,y=(y+L)T_L.
\]

Therefore the tail chart after cutting at (L) must remember that its local coordinate (y) represents the global coordinate (y+L).

## The hostile fixed-origin calculation

If the translated tail is incorrectly given the original multiplication operator (y), then

\[
T_L(yf)-yT_Lf=L\,T_Lf.
\]

This is a genuine bulk residual, not an interface distribution. It falsifies any construction that cuts the source but silently resets the wall origin to zero on every tail chart.

The remedy is not an added correction. It is to retain the source-derived affine origin (L) as part of the chart type. Then the commutator vanishes exactly.

## General first-order covariance

For a source differential expression

\[
D_a=\partial_y+a(y),
\]

the transported tail operator is

\[
D_{a,L}=\partial_y+a(y+L).
\]

It obeys

\[
T_LD_a=D_{a,L}T_L.
\]

On the seam interval, the operator remains the restriction of (D_a) in the global coordinate. Because the tail and seam traces match, reassembly introduces no delta distribution at the interface. A delta appears only if the incidence condition is violated.

## Prime coherence

Successive cuts add origins:

\[
(y+M)+L=y+(L+M).
\]

Thus the affine Weyl action is coherent over prime products. For (L=\log p) and (M=\log r), both orders produce the origin (log(pr)). The earlier prime-cocycle commutation is the scalar shadow of this affine chart law.

## Meaning

The cut correspondence now has three inseparable pieces:

- the translated tail state;
- the retained seam interval;
- the affine origin locating both inside the global wall coordinate.

Dropping the seam loses energy. Dropping the origin changes the operator and produces a bulk anomaly. The origin is comparison metadata, not another Hilbert-state channel, so it does not enlarge the six-dimensional linear carrier.

## Remaining Pearson gate

The formal Pearson differential expression is covariant when all coefficient functions are shifted with the chart. The next source-specific audit must include the Mellin pushforward and Clark parameter differentiation. Those operations can mix chart origin, exponent, and endpoint residue; their combined defect must still reduce to the declared seam current.

## Verification

The dependency-free exact-rational checker `research/grothendieck/checkers/weyl_cut_covariance.py` verifies derivative covariance, the affine (y+L) law, the hostile bulk residual from resetting the origin, additive two-cut coherence, and covariance of a general polynomial first-order operator.
