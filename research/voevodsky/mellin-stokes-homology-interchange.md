# Mellin–Stokes homology interchange

## Question

Does the fixed-cycle theorem close the two-locus interchange at the relative-class and period level?

## Claim boundary

The result concerns relative classes, period vectors, and their dual coefficient pairing. It does not construct thimble-chain representatives or cutoff transitions.

## Basis mutation

For an integral cycle-basis mutation \(T\), period vectors and dual coefficients transform as

\[
p\mapsto Tp,
\qquad
c\mapsto T^{-T}c.
\]

Therefore

\[
(T^{-T}c)^T(Tp)=c^Tp.
\]

An exact two-dimensional fixture verifies the pairing identity.

## Interchange

Reciprocal transport acts on the spectral factor, while Stokes mutation acts on the relative-cycle factor. On period classes their actions commute. The theta source supplies the two required class-level statements:

- covariance of Mellin jets under basis mutation;
- endpoint incidence determines the completed relative class.

Thus the homology/period-level interchange is verified.

## Remaining boundary

This does not supply:

- a Stokes map on chosen thimble chains;
- a chain homotopy comparing representative choices;
- cutoff transition maps;
- completed cutoff interchange.

These are unnecessary for a class-valued claim but mandatory for strict chain selection or completed filler descent.

## Disposition

The two-locus obstruction is now closed at relative-class level and remains open only at chain and cutoff levels. No chain representative is promoted from basis-independent period data.

## Verification

- `research/voevodsky/mellin-stokes-homology-interchange-v1.json`
- `research/voevodsky/checkers/check_mellin_stokes_homology_interchange.py`
- `research/voevodsky/results/mellin_stokes_homology_interchange.json`
