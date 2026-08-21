# 1549 — The Mixed Second Grade Has Only External Frequency Support

## Hard-to-vary claim

In the one-cubic-operator finite-time truncation, the exact sum of the two
mixed bulk--boundary placements at order \(\eta_0^2\) has frequency support

\[
\boxed{\{-2p,0,2p\}}.
\]

All terms carrying an internal \(q\)- or \(k\)-frequency cancel in the
Schwinger--Keldysh branch sum.

## Frozen construction

The calculation retains separately:

- the bulk integration-time frequency;
- the boundary-time frequency;
- the Laurent powers in both times;
- all four Schwinger--Keldysh branch assignments;
- the source scale factors in both the bulk and boundary insertions.

The \(\eta_0^2\) coefficient is extracted only after evaluating the lower
endpoint of the bulk primitive.  The two equal mixed placements and their
common perturbative factor are then combined.

At

\[
(p,q,k,\eta)=(1.1,0.8,0.9,-0.15),
\]

the surviving coefficients are

\[
c_{-2p}=-4.104067068163046+0.01209374535622313i,
\]

\[
c_0=-1.758893522945457,
\]

\[
c_{2p}=-4.104067068163046-0.01209374535622313i.
\]

Hence

\[
c_{-2p}=c_{2p}^*,
\qquad c_0\in\mathbb R.
\]

These signs retain the relative contour phase of the source boundary
insertion \(+iS_0^{(3)}\) in Eq. (17). The original checker treated the
boundary insertion as a second bulk Hamiltonian insertion and therefore
reversed the complete mixed packet. That error changed the displayed signs,
but not frequency support or reality.

## Artifacts

- `research/benincasa/checkers/finite_time_mixed_grade.rs`
- `research/benincasa/results/finite-time-mixed-grade.json`

## Narrow conclusion

The mixed sector satisfies the same external-frequency constraint as the
boundary--boundary sector in Entry 1548.  This removes internal oscillatory
support as a possible obstruction at second normal order in these two
sectors.

This is not yet the complete Eq. (19) coefficient.  The bulk--bulk lower
endpoint can generate the same three external frequencies and must be
computed before comparison with the source \(J_i\) combination.

## Next falsifier

Construct the exact bulk--bulk lower-endpoint Laurent--exponential packet.
Test first whether its \(\eta_0^2\) grade is supported on
\(\{0,\pm2p\}\); only after that support test combine all three sectors and
compare the resulting coefficients with Eq. (19).
