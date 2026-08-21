# 1558 — Eq. (19) Requires a Nonmultiplicative Endpoint Normalization

## Hard-to-vary claim

With the source exponent

\[
\exp\left(-i\int H_I+iS_0^{(3)}\right)
\]

expanded directly, and with the common prefactor conversion fixed from the
printed Wightman normalization, the oscillatory second-grade sectors are

\[
\boxed{
\text{bulk--bulk}=J_1,
\qquad
\text{mixed}=-2J_2,
\qquad
\text{boundary--boundary}=-J_0.
}
\]

Equation (19) instead requires

\[
J_1-4J_2-2J_0.
\]

No multiplicative scalar normalization of the endpoint insertion relates the
two triples.

## Finite obstruction

Let one boundary insertion carry endpoint weight \(w\). Matching the mixed
sector requires

\[
w=2.
\]

Matching the boundary--boundary sector requires

\[
w^2=2.
\]

But the first equation implies \(w^2=4\). Therefore

\[
\boxed{
\text{no multiplicative endpoint weight reproduces Eq. (19).}
}
\]

The \(c_3\) counterterm cannot resolve this comparison: it contributes only
to the oscillatory \(I_4\) direction and cannot independently change the
\(J_0\) and \(J_2\) coefficients.

## Contraction audit

The discrepancy is not explained by ordinary Wick counting. Both the bulk
and boundary operators have the same labelled
\(\zeta(\partial\zeta)^2\) slots. The connected fish census is

\[
3\times3\times2=18
\]

for every choice of bulk or boundary location. The common momentum vertex is
the printed \((p^2+q^2+k^2)^2\).

## Artifacts

- `research/benincasa/checkers/finite_time_endpoint_multiplicativity_obstruction.rs`
- `research/benincasa/results/finite-time-endpoint-multiplicativity-obstruction.json`
- the three sector checkers, which now assert their individual
  \(J_1,J_2,J_0\) identifications at generic kinematics.

## Narrow conclusion

The frozen formulas do not support repairing Eq. (19) by choosing a different
scalar value for an endpoint delta function. At least one additional typed
datum is required:

1. a labelled coincidence/diagonal rule for two endpoint occurrences;
2. a nonmultiplicative endpoint distribution prescription independently
   derived from the contour;
3. or a correction to the primary-source normalization.

This is not evidence for a new cosmological carrier stratum. It is an
endpoint-comparison coherence obstruction.

## Next falsifier

Derive the endpoint coincidence rule directly from a regulated contour in
which the two boundary occurrences remain separated until the final limit.
Compute the mixed one-boundary and boundary--boundary two-occurrence limits
with the same regulator. If their weights are multiplicative, Eq. (19)'s
printed normalization is falsified within the toy truncation. If a canonical
diagonal excess survives, classify it as a coefficient/comparison cell before
proposing any carrier modification.
