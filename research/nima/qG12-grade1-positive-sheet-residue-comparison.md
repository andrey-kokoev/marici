# Grade `-1` sewn class versus the positive-sheet bulk residue

## Question

Is the nonzero `q_g1`–`q_g3` sewn class source-typed by the positive-sheet exceptional bulk form, and does existing evidence establish a nonzero positive-cut period?

## Exact comparison

The exceptional bulk rational factor is

\[
\frac{a+p}{2p(a-p)^2(a+3p)(\xi+1)}.
\]

The strict-transform certificate gives unit leading measure ratio on the chosen positive square-root sheet. Since

\[
da\wedge d\xi=-d\xi\wedge da,
\]

the Poincaré residue at `xi=-1` is

\[
-\frac{a+p}{2p(a-p)^2(a+3p)
\left(a^2+(4\kappa-5)p^2\right)}\,da.
\]

Execution `structured_command_execution:e_30844_1788300707526657600_9` verifies exact equality with the oriented grade `-1` `q_g1` form. Its residue at the `q_g1`–`q_g3` node remains

\[
\frac{1}{64p^4(\kappa+1)},
\]

which the `q_g3` occurrence cancels with the opposite sign. Therefore the sewn class is the exact oriented boundary residue of the positive-sheet bulk strict transform.

## Pairing boundary

This constructs a source-typed cohomology comparison and fixes its sign. It does not compute a period. The strict-transform certificate explicitly limits itself to algebraic strict transform and numerator independence and states no claim that resulting periods are physically nonzero.

The first missing object is an explicit positive-cut relative chain on the exceptional surface, including orientation, endpoints, and avoidance or regulation of the branch and conductor divisors. Without that chain, nonzero cohomology and positive-sheet provenance do not imply nonzero pairing.

## Acceptance test

1. specify the positive-cut relative chain in `(a,xi)` coordinates;
2. verify its boundary lies in the declared relative divisor;
3. fix orientation against the unit positive-sheet measure ratio;
4. evaluate the bulk period or, equivalently, the induced boundary pairing;
5. show the value is nonzero on one generic admissible chamber;
6. track sign changes under square-root-sheet reversal;
7. test degeneration at `kappa=±1` or `xi=±1` separately.

## Disposition

The grade `-1` sewn class agrees exactly, including orientation, with the Poincaré boundary residue of the positive-sheet bulk strict transform. A nonzero physical positive-cut period is not established because the source packet supplies no explicit relative chain.

## Evidence

- `research/nima/checkers/check_grade1_sewn_bulk_residue_orientation.py`
- `research/benincasa/x1-soft-physical-strict-transform.json`
- `research/benincasa/check_x1_soft_physical_strict_transform.py`
- `research/nima/qG12-grade-minus-one-sewn-cech-class.md`
