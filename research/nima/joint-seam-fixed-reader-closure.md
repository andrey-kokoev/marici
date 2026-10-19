# Fixed seam prediction closes in three readings, with one retained hidden coordinate

## Result

**44 exact checks pass**, after freshly rebuilding the preceding source-rotation
comparison for all four deleted-edge cases.

The four-dimensional conditional state has a smaller fixed-seam predictive
readout: three independent scalar linear forms suffice for every continuation.
One further conserved coordinate remains invisible to that reader but is
retained for complete state recovery.

## Construction

Let T be the exact four-coordinate update and C the fixed seam-defect reader.
Define present-state functions

    y0=Cx,    y1=CTx,    y2=CT^2x.

These predict future readings; they do not presume that future measurements
have already been acquired. The prior source test establishes T^3=I. Therefore

    (y0,y1,y2) -> (y1,y2,y0).

The three rows have rank three. Any invariant linear observation space containing
C must contain CT and CT^2; these rows already form a closed space. This proves
minimality within linear readout spaces on the declared four-dimensional carrier.
It is not a claim about every nonlinear encoding or every possible preparation.

A concrete vector with Cx=0 but CTx nonzero is exported for each case. Thus the
present scalar alone is insufficient even though its complete future response
is periodic.

## No provenance or hidden state is erased

The common kernel of C, CT and CT^2 is one-dimensional and fixed by T. Choose
an independent conserved covector H and retain h=Hx. Then

    Q = [C; CT; CT^2; H]

is invertible and

    Q T Q^-1 = diag(cyclic_shift_3, 1).

The receipt contains Q's observer rows, H, the exact inverse and the transported
metric. Hence the full state reconstructs from (y0,y1,y2,h), although the first
three entries already predict every future fixed-seam reading. H's normalization
is a coordinate choice, not a source-selected physical unit.

The original word and construction provenance remain separate from this linear
state representation. No unique history is recovered from the final state.

## Scope

All preceding assumptions remain explicit: the edge-matching completion is
conditional, and the orphan spatial record is transported by a declared
covariant extension of the surviving source rotation. Neither the interface
nor that extension has become a physically selected operation by acquiring a
closed observer.

The result consolidates that candidate's information requirements: one current
scalar is too coarse, three linear readings predict its future, and one retained
hidden coordinate completes recovery. It supplies no preparation, measurement
instrument, interaction energy or physical clock.

## Reproduction

    uv run --with sympy python research/nima/checkers/check_joint_seam_fixed_reader_closure.py

Receipt: `results/joint-seam-fixed-reader-closure.json`.
The preceding constructor/transport checks are freshly rerun. No source or
physical law is changed.
