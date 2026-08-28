# 3840 — The Two Active Conductor Logarithms Do Not Cancel Wall to Wall

## Hard claim tested

A minimal candidate for the physical rank-26 readout was that the two source-prescribed conductor logarithms cancel directly after assigning their relative wall orientation.

This candidate has only two possible signed combinations. It can therefore be falsified at one exact generic source point.

## Exact test

At ((x,y,z)=(2,3,4)), Entry 3832 gives the source-oriented conductor coefficients

\[
c_1=\frac{16}{99225}-\frac{\sqrt{46}}{101430},
\qquad
c_2=\frac1{2025}-\frac{\sqrt{94}}{28200}.
\]

The two possible relative-orientation combinations are

\[
c_1+c_2
=
\frac{13}{19845}-\frac{\sqrt{46}}{101430}-\frac{\sqrt{94}}{28200},
\]

\[
c_1-c_2
=
-\frac{11}{33075}-\frac{\sqrt{46}}{101430}+\frac{\sqrt{94}}{28200}.
\]

Both are nonzero. Exact degree-four minimal polynomials with nonzero constant terms certify this without numerical fitting.

## Result

The two active conductor logarithms do not cancel directly for either relative wall sign. Hence no universal physical covector can be obtained by separately regularizing the two wall forms and summing them.

This does not show that the complete source period diverges. It proves that any cancellation or lift independence must involve additional terms already present in the source-defined relative object—such as its bulk current, endpoint faces, or their chain homotopy. Such a term must be derived from the frozen source; it cannot be appended to repair the failed wall-only model.

## Classification

- Existing Carrier: unchanged.
- Wall-only readout: falsified.
- Full source-relative readout: still viable.
- New Carrier datum: unsupported.

## Durable artifacts

- `research/benincasa/checkers/check_rank26_wall_only_conductor_cancellation.py`
- `research/benincasa/results/rank26-wall-only-conductor-cancellation.json`

The checker passes six exact gates.

## Next falsifier

Derive the boundary identity for the complete (q_{\mathcal G_{12}})-residue current restricted to the two active wall neighborhoods. Test whether its source bulk term supplies the missing conductor coefficient with no adjustable finite part. If no such source-derived term exists, the direct literal-chain construction does not define the sought rank-26 physical covector.
