# 1800 — Base Transversality Does Not Prove Coefficient Product Structure

## Correction

The first version of Entry 1799 inferred a product decomposition of the
integrated coefficient object from the unimodular external-energy Jacobian.
That inference is invalid and is withdrawn.

## Type distinction

For a further singleton wall \(g_j\), the map

\[
(E_T,X_i,X_j)\longmapsto(q_e,g_i,g_j)
\]

has determinant one at fixed loop variables. This proves that the equations
are transverse in the external-energy base.

It does not make \(g_j\) constant on the integration fiber. Its local
expansion at the threshold critical point is

\[
g_j=h+\lambda_1u+\lambda_2v+\cdots.
\]

Consequently the coefficient germ has the three-wall form

\[
\int
\frac{du\,dv}
{(\tau+H_1u^2+H_2v^2)(h+\lambda_1u+\lambda_2v)}.
\]

Its nearby cycles cannot be inferred from the base Jacobian.

## Surviving narrow statement

\[
\boxed{
\text{The twenty singleton intersections are existing, base-transverse
carrier incidences in four free }C_5\text{-orbits.}
}
\]

No statement about coefficient splitting, nilpotent rank, or supported excess
survives without the loop-gradient calculation.

## Epistemic consequence

This is another instance of the governing warning

\[
\text{carrier incidence}
\not\Rightarrow
\text{integrated period system}.
\]

The corrected Entry 1799 now records only the carrier-level result.

## Next falsifier

Compute the four representative loop-gradient vectors
\((\lambda_1,\lambda_2)\), then derive the complete source-weighted
two-parameter local periods before taking cyclic assembly.

## Evidence

- corrected Entry 1799
- research/benincasa/checkers/five_site_g5_spectator_singleton_intersections.py
- allocator claim: seqclaim-3b9feb751f8eae363fccd035
