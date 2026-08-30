---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2236 — The Gaussian Quadrupole Resolves the Homogeneous Contact Kernel

## Response matrix

Pair the isotropic and quadrupole source components with the three contact
directions. Up to the source-fixed contact factors, the response matrix is

\[
R=-8\operatorname{diag}(C_{12},C_{23},C_{31})
\begin{pmatrix}
1&2&0\\
1&-1&-1\\
1&-1&1
\end{pmatrix}.
\]

At generic finite contact kinematics,

\[
\det R
=(-8)^3C_{12}C_{23}C_{31}(-6)\neq0.
\]

Thus the homogeneous contact kernel is fully observable after adjoining the
quadrupole port.

Under cyclic rotation, the two quadrupole components transform as the
rational cyclotomic plane. They match, rather than merely equal in rank, the
blind representation isolated in Entry 2233.

## Status

This is an independently defined anisotropic boundary-state lens. It does
not alter the Carrier and does not claim that the original isotropic
Bunch–Davies state already contains the missing readout.

## Evidence

- Entries 2233–2235
- `research/benincasa/checkers/equilateral_quadrupole_contact_response.rs`

