# 1824 — All Mixed Edge–Region Pair Orbits Fail the Physical Pullback Gate

## Frozen family

Among the 49 source-compatible two-wall orbits, consider the fourteen mixed
profiles consisting of one edge wall \(G^-_e\) and one connected-region wall
\(g_A\).  Six have disjoint cut supports and eight share the edge \(e\).

Entry 1823 already closes the six disjoint representatives

\[
g_3, g_4, g_5, g_{34}, g_{45}, g_{345}
\]

after the physical \(d^3\ell\) pullback gate.

## Shared-edge theorem

For a shared-edge profile, write \(j\) for the other boundary edge of the
region and \(u_e,u_j\) for the corresponding unit vectors.  At a smooth,
nonsoft point,

\[
\nabla_\ell G^-_e=2u_e,
\qquad
\nabla_\ell g_A=u_e+u_j.
\]

Linear dependence forces \(u_j=\pm u_e\).

- If \(u_j=u_e\), the two gradients point in the same direction, so no
  positive nonzero Landau multipliers can cancel them.
- If \(u_j=-u_e\), then \(\nabla_\ell g_A=0\), while
  \(\nabla_\ell G^-_e\ne0\); positive nonzero multipliers again cannot solve
  the Landau equation.

Hence all eight shared-edge orbits fail before elimination, Hessian, or
residue calculations.

## Result

Combining the direct shared-edge theorem with Entry 1823 gives

\[
\boxed{
\text{smooth physical survivors among all 14 mixed edge--region pair orbits}
=0.
}
\]

Zero-distance endpoints are outside the unit-gradient argument and remain
classified as already existing soft support.  This result neither removes
that support nor addresses total-energy or region--region pair profiles.

## Consequence

The physical-gradient gate closes an entire source-compatible orbit class
without constructing ambient resultants.  The remaining pair audit should
therefore classify total-energy and region--region profiles directly in
physical loop space before any period interpretation.

## Evidence

- `research/benincasa/checkers/five_site_mixed_edge_region_physical_no_go.py`
- `research/benincasa/results/five-site-mixed-edge-region-physical-no-go.json`
- Entries 1822--1823
- allocator claim: `seqclaim-e23ef346cba8fdeaf1c2f2ca`
