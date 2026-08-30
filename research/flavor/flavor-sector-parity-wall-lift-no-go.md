# Sector-parity wall-lift no-go

## Bounded question

Can the WP629 sector parity both protect exact up/down kinetic alignment and be
explicitly softened to remove the degenerate vacua created by the odd down
entrance expectation value?

## Exact incompatibility

Let \(P\) denote the sector parity, with \(H^u\) even and \(H^d\) odd. Exact
kinetic protection requires every admitted source operator to be even under
\(P\). Therefore the full source action obeys

\[
S[H^u,H^d]=S[H^u,-H^d].
\]

Whenever the odd field has a nonzero vacuum expectation value, the two vacua
related by \(P\) are exactly degenerate. An operator that assigns them
different energies must be parity odd. Admitting it removes the exact symmetry
argument that forbids both the off-diagonal kinetic Gram and wrong-sector
entrance tensors. Exact alignment protection and explicit wall lifting cannot
be obtained from the same global \(Z_2\).

## Smallest soft term

The lowest-dimensional gauge-invariant parity-odd candidate is the real
bilinear

\[
\mu_{ud}^2\operatorname{Re}(H^{u\dagger}H^d).
\]

At the declared noncollinear representative the two row-triplet vacuum vectors
are orthogonal, so this bilinear vanishes on both sign-related vacua and does
not split their energies there. Its first derivative in the overlap direction
is \(\mu_{ud}^2\), however, so every nonzero coefficient destroys exact
orthogonal stationarity. The smallest soft repair therefore fails before any
loop calculation: it neither preserves the declared vacuum nor retains the
exact selection rule.

## Remaining branches

Three honest branches remain:

1. keep the global parity exact and supply a cosmological history that avoids
   populated disconnected domains;
2. gauge the discrete parity, explicitly changing the physical groupoid and
   auditing discrete anomalies and gauge defects;
3. add a source-derived parity-odd reference operator, recompute the complete
   vacuum and kinetic/Yukawa system, and accept that alignment becomes a
   quantitative rather than exact statement.

None is already present in the connector source. In particular, a soft term
cannot be treated as a harmless wall eraser while canonical alignment and the
old noncollinear vacuum are retained unchanged.

## Disposition

WP629 is a valid conditional rigidifier but not a closed physical completion.
The wall gate cannot be removed by the minimal bilinear without reopening the
kinetic/Yukawa gate. No numerical selector or physical instrument results.

## Reproduction

Run:

    python research/flavor/checkers/wp630_sector_parity_wall_lift_no_go.py

The generated result is
`research/flavor/results/wp630_sector_parity_wall_lift_no_go.json`.

