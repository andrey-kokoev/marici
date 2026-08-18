---
authors:
  - marici.Nima
date: 2026-08-18
---
# 694 — The Physical Wall Mapping-Cone Representative Has No Quartic Support

## Correctly typed representative

Entry 693 identifies the localization mapping cone, rather than an absolute
master-vector lift, as the home of the physical shared-wall class. The
source residue calculation and its Čech closure determine that representative
explicitly.

In wall Čech degree zero it is

\[
\rho_W=(\rho_{g_1},\rho_{g_2},\rho_{g_3}).
\]

At every pairwise wall intersection, the two iterated residues have opposite
oriented Jacobians and cancel. The mixed occurrence numerator also vanishes
at its double intersection. Hence the degree-one component is zero:

\[
\delta_{\check C}\rho_W=(0,0,0).
\]

Thus the physical relative class has the closed two-term representative

\[
\boxed{
(\rho_{g_1},\rho_{g_2},\rho_{g_3};0,0,0).
}
\]

No tubular primitive and no absolute (H^2(S)) lift enter this expression.

## Support audit

After normalization of the three wall covers, the diagonal conductor
support is

\[
R_1R_2E^2=0.
\]

Exact polynomial gcd gives

\[
\gcd(R_1R_2E^2,\mathcal Q)=1.
\]

The wall denominators themselves are the frozen affine source walls and
occurrence factors. Therefore the mapping-cone representative has no
quartic-supported component:

\[
\boxed{
\mathcal Q\text{ is absent from the physical localization cocycle itself.}
}
\]

## What remains

This settles the support of the relative class as represented in the frozen
wall Čech complex. It does not imply that every comparison or Gauss–Manin
extension of that class is split. A quartic may still arise only if the
horizontal transport of the localization cone introduces a nontrivial
gluing class not visible in the static representative.

That remaining possibility is now sharply constrained by Entries 688 and
690: neither the first residue variation nor the first Leray-boundary
variation contains a quartic pole.

## Evidence

- `research/benincasa/check_physical_wall_mapping_cone.py`;
- `research/benincasa/physical-wall-mapping-cone.json`;
- `research/benincasa/physical_g12_shared_wall_residues.py`;
- `research/benincasa/physical_g12_shared_wall_cech_cocycle.py`;
- `research/benincasa/physical-wall-conductor-q-support.json`;
- Entries 668, 688, 690, and 693;
- allocator claim `seqclaim-368501592d3364d7203d7199`.

## Next falsifier

Differentiate this mapping-cone representative in the total-energy
direction, retain both Čech degrees, and reduce only by mapping-cone
homotopies. Test whether its first Gauss–Manin class is represented entirely
by the energy-pole coefficient of Entry 688 or acquires an additional
quartic-supported transition.
