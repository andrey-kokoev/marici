# Fixed versus transported seam: the residual needs a frame contract

## Result

**68 exact checks pass** for all four single-edge deletions.

Under the surviving source rotation, extended covariantly to the candidate
orphan spatial record:

- the fixed two-coordinate joint space is not invariant;
- its smallest invariant linear span has **four dimensions**;
- transporting the seam and its marking with the rotation preserves the original
  two coordinates, provided the three-stage frame is retained.

These are different observation contracts, not two normalizations of one fixed
reader. No source law selecting between them is claimed.

## Existing action and explicit extension

Each deleted source retains one directed triangle. Its supplied vertex cycle
induces an order-three proper spatial rotation R. The original three triangle
records transform by their existing permutation and R on each spatial block.
Their common assembled vector is invariant under this native action D.

The candidate orphan does not have a source-admitted update yet. This test makes
one explicit geometric extension:

    U = D direct-sum R.

Its endpoint marking is transported with R. U is unitary and U^3=I. This is a
covariance test of the conditional orphan completion, not a derivation of its
physical dynamics or an assertion that an orphan traversal was executed.

## Fixed-frame closure

Let E encode the previously constructed two coordinates (a,r) into twelve raw
coordinates and N=E(E*E)^-1 E*. The checker finds

    (I-N) U E != 0.

The fixed seam equality also fails on some evolved inputs even though it holds
on every initial vector in im(E). Thus the earlier static compatibility space
cannot simply be declared closed under this extension.

Compute the full orbit span

    W = span(E, U E, U^2 E).

It has exact rank four. Since U^3=I, this span is invariant and contains every
future iterate of the original subspace. Every invariant linear space containing
im(E) must contain these columns, so four is the minimal such dimension.

An exact basis, induced metric, decoder and reduced update T are constructed.
They satisfy UW=WT, T^3=I and metric preservation. Minimality concerns this
linear state-space closure, not arbitrary encodings or a scalar observer's
minimal realization.

## Moving-frame comparison

Alternatively transport the seam's edge covector, its incident surviving-mode
address and the orphan spatial record together. The edge equality then holds
at each of the three stages. Applying E's decoder after U^-k recovers the same
coordinates (a,r) at stage k.

This is a two-coordinate family with a retained frame/stage, not an autonomous
two-number state in the original fixed chart. The marking returns after three
rotations. A covariant reader changes alongside the state; it must not be
reported as conservation of the original fixed reader.

## Meaning of the result

The transverse record did solve the static parent-mode ambiguity. It did not
select a dynamic comparison frame. Once a concrete candidate source action is
tested, that distinction produces a measurable algebraic difference: a fixed
reader sees a seam defect, while a transported reader does not.

A preparation, a policy protecting a fixed relation, or a physical moving-frame
interpretation must still be supplied. The four-dimensional closure can retain
the candidate evolution without forcing the defect to vanish. No relaxation,
new energy functional, clock or particle identification is introduced.

## Reproduction

    uv run --with sympy python research/nima/checkers/check_joint_seam_residual_transport.py

Receipt: `results/joint-seam-residual-transport.json`.
It records each source cycle, fixed-seam defect, exact reduced update and metric.
The unchanged constructor is rerun for every deletion; owner files are not modified.
