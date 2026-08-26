# Signed-J physical16 kernel (WP295)

## Complementary magnitude probe

WP294 leaves open an obvious repair: supplement the binary branch with an
exact magnitude measurement. Together these give the full signed Jarlskog
invariant $J$, which descends under the full weak-basis groupoid.

This complementary CP-odd probe repairs the magnitude erased by
`physical16 -> sign(J)`. It does not repair the CP-even kernel.

## Exact hostile pair

Fix the six ordered masses and the remaining two CKM mixing angles. Compare
the exact angle packets

\[
(s_{12},c_{12})=(3/5,4/5)
\]

and

\[
(s_{12},c_{12})=(4/5,3/5).
\]

Their product $s_{12}c_{12}$, and hence signed $J$, is identical. Their CKM
moduli differ. Both CKM matrices are exactly unitary, so they are physically
inequivalent `physical16` points collapsed by the full signed-$J$ readout.

The first nonfaithful arrow after adding the magnitude probe is therefore
`physical16 -> signed J`.

## Classification

Signed $J$ is a valid weak-basis-invariant readout and may be the target of a
conditional orientation-and-magnitude selector. It is neither a faithful
separator nor a point selector on `physical16`. CP-even masses and moduli need
independent source-derived operations; they cannot be inferred from CP-odd
branch preparation.

Run `uv run --with sympy python
research/flavor/checkers/wp295_signed_j_physical16_kernel.py` to regenerate the
exact hostile-pair audit.
