# Lagrangian seam 3+4+3 tomograph

## Purpose

Grothendieck's present theta frontier predicts that two reciprocal bulk
presentations lie on one two-dimensional Lagrangian graph. A genuine seam
extension contributes a transverse two-dimensional state. Quadratic controls
then split as

`3 bulk + 4 bulk--seam comparisons + 3 seam = 10`.

The optical apparatus can test this architecture directly at finite cutoff.
It is not the completed rigged instrument: the augmentation seam direction
becomes a covector in the limit.

## Extension

Add four phase-sensitive quadratures:

`bulk_q, bulk_p, seam_q, seam_p`.

For each quadrature, measure its direct power. For every unordered pair,
measure both plus and minus coherent combinations. There are four direct
settings and twelve paired settings, for sixteen power records.

The signed pair difference reconstructs the cross term. Together the records
recover the complete symmetric four-by-four quadratic form and its canonical
blocks:

- a symmetric two-by-two bulk block with three coordinates;
- a general two-by-two mixed block with four coordinates;
- a symmetric two-by-two seam block with three coordinates.

## Lagrangian graph gate

Before interpreting the seam extension, coherently tomograph the two-by-two
Fourier--Tate process `R`. Test its symplectic residual and pull back the
difference symplectic form to the graph `(x,Rx)`.

For a valid reciprocal graph, that pullback vanishes. Restricting all ten
ambient quadratic controls to this bare graph has rank three. Therefore the
apparatus rejects the false interpretation that the two reciprocal bulk
charts already supply ten independent controls.

## Seam-rank decision

Activate the source-derived seam waveforms only after the graph gate passes.
The normal block must have rank two within its preregistered uncertainty, and
the four mixed comparisons must be independently reconstructible. A rank-one
normal block, or mixed signals without a resolved normal state, falsifies the
proposed completed seam architecture.

## Value to Grothendieck

This instrument separates three questions that scalar theta readout merges:

1. Are the reciprocal bulk sectors genuinely one Lagrangian state?
2. Does completion add a two-dimensional transverse seam state?
3. Do the four comparison controls appear only after that state is present?

It therefore tests the finite analytic premise required before the endpoint
`sp4` interpretation is allowed. Passing the finite tomograph does not prove
that the seam extension persists in the restricted-product completion; it
produces the exact finite packet whose completion stability Grothendieck must
then prove.

The flat-comb completion hostile sharpens this: the four mixed comparisons
survive as state--dual evaluations, but the three pure-seam quadratic controls
require a separate continuous dual--dual pairing. Until that pairing is
derived, the completed `3+4+3` tower is conditional.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_lagrangian_seam_343_tomograph.py
```
