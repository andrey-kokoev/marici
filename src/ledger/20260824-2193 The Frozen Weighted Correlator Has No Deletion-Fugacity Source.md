---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2193 — The Frozen Weighted Correlator Has No Deletion-Fugacity Source

## Primary-source audit

Freeze Benincasa–Dian, *The Geometry of Cosmological Correlators*,
arXiv:2401.05207:

- equations (2.13)–(2.14) define the edge-erasure sum;
- equations (2.27)–(2.30) fix the dashed-edge adapter;
- equations (4.66)–(4.71) realize the same correlator through a weighted-
  polytope subdivision.

For deletion grade (j), the coefficient is fixed as

\[
\boxed{(-2)^j.}
\]

The construction does not declare a continuous parameter (z), an
edge-erasure chemical potential, or a source coupled to deletion count.
The weighted polytope is presented as the geometry of the correlator, and
its weights encode the orientation-changing construction.

## Consequence for Entry 2192

The replacement

\[
(-2)^j\longmapsto(-2z)^j
\]

is a canonical Rees deformation of the *filtration*, but it is not a family
of physical correlators supplied by the frozen source.

Therefore

\[
\boxed{
F'(1)=-8C
\text{ is not presently a source derivative of a physical coupling.}
}

It remains an exact filtered coefficient selector.

## Narrow closure

The search for a physical deletion fugacity is negative within the declared
primary construction. This does not prove that no enlarged theory can
supply one. Any enlargement must independently define:

1. the deformed probability or contour object;
2. why its weights remain compatible with unitarity and normalization;
3. the observable conjugate to deletion count;
4. specialization back to (z=1).

Adding (z) solely because its derivative exposes the known hidden packet
would be a prohibited fitted repair.

## Evidence

- Benincasa–Dian, arXiv:2401.05207, equations listed above
- Entries 2112–2115 and 2192
- `research/benincasa/checkers/deletion_weight_source_audit.rs`
- allocator claim `seqclaim-fa32e4bfdea43fbf74d62d1b`
