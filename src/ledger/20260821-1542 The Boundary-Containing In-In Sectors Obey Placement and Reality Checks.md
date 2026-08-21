# 1542 — The Boundary-Containing In-In Sectors Obey Placement and Reality Checks

## Hard-to-vary claim

Using the source-derived cubic kernel

\[
C_K=\frac1K\left(\frac1{K\eta_0}-i\right)
\]

and the exponent-normalized insertion of Entry 1539, the branch-labelled
bulk--boundary, boundary--bulk, and boundary--boundary sectors form a
consistent real Schwinger--Keldysh contribution.

## Frozen branch weights

For a bulk vertex on branch \(a\in\{+,-\}\), use

\[
w_a^{\rm bulk}(t)=\frac{a}{t^2}.
\]

For the integrated boundary vertex, the plus and minus weights are

\[
w_+^{\partial}=-a_0^2C_K,
\qquad
w_-^{\partial}=a_0^2C_K^*,
\qquad
a_0^2=\frac1{H^2\eta_0^2}.
\]

No endpoint delta is numerically integrated; its source-authoritative
integrated value is used directly.

## Finite tests

At generic unequal momenta, independently compute

\[
M_{B\partial}
=
\sum_{a,b}\int dt\,
w_a^{\rm bulk}(t)w_b^\partial
G_p^{+a}(\eta,t)G_p^{+b}(\eta,\eta_0)
G_q^{ab}(t,\eta_0)G_k^{ab}(t,\eta_0),
\]

and the placement-reversed \(M_{\partial B}\).  The checker finds

The corrected numerical values are recorded in the machine-readable packet.

with relative placement defect

\[
\text{below }10^{-14}.
\]

Their sum is real.  The independently assembled boundary--boundary sector is
also real.

## Artifacts

- `research/benincasa/checkers/finite_time_sk_boundary_sectors.rs`
- `research/benincasa/results/finite-time-sk-boundary-sectors.json`

## Narrow conclusion

Together with Entry 1541, every cubic-vertex placement in Eq. (18) now has a
branch-labelled computational representation satisfying its first structural
checks.  This does not yet reproduce Eq. (19), because the momentum integral,
bulk counterterm insertion, and \(\eta_0\)-graded asymptotic reduction remain.

## Next falsifier

Assemble the four cubic placement sectors with the corrected bulk
counterterms, extract the \(\eta_0^2\) asymptotic coefficient, and require exact
reproduction of Eq. (19) before calculating the omitted grades.
