# Entrance sector-parity repair

## Bounded question

Is there a minimal source symmetry that removes WP628's entrance kinetic Gram
without deleting the messenger routes or the even cross-invariants supporting
the noncollinear entrance vacuum?

## Declared extension

Add one \(Z_2\) sector parity. Take the common quark entrance, the up entrance,
the up messenger chain, \(u_R\), the connector, and the exit flavon to be even.
Take the down entrance, the complete down messenger chain, and \(d_R\) to be
odd. The exact parity equations for all route vertices and vectorlike masses
then have one solution under these frozen source assignments:

\[
p(H^u)=p(A^u)=p(B^u)=p(u_R)=0,
\]

\[
p(H^d)=p(A^d)=p(B^d)=p(d_R)=1.
\]

Here left and right members of each vectorlike pair carry the same parity.

## What the symmetry repairs

The off-diagonal kinetic term

\[
(D_\mu H^u)^\dagger D^\mu H^d+\mathrm{h.c.}
\]

is odd and forbidden. The wrong-sector entrance vertices are also odd. Every
declared same-sector messenger vertex and mass remains even.

The positive entrance potential is not destroyed. Radial norms, row Grams,
\(|H^{u\dagger}H^d|^2\), the real part of
\((H^{u\dagger}H^d)^2\), and weak-antisymmetric alignment norms all contain
an even number of down fields. They survive the parity and can retain the
noncollinear vacuum construction.

## Authority boundary

This is the smallest algebraically sufficient repair of WP628, but the new
parity is a declared source extension. It is not derived from the existing
gauge group, and it changes the admitted theory by adding a discrete charge
grading. It rigidifies the up/down presentation and makes diagonal kinetic
normalization radiatively stable so long as the parity is exact.

The parity selects neither its own existence nor any numerical `physical16`
point. If both entrance vevs are nonzero, the parity is spontaneously broken;
the associated domain-wall history and possible soft breaking must be typed
before cosmological or detector claims. Complete RG closure and finite
threshold matching remain open.

## Reproduction

Run:

    python research/flavor/checkers/wp629_entrance_sector_parity_repair.py

The generated result is
`research/flavor/results/wp629_entrance_sector_parity_repair.json`.

