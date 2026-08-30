---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2162 — The Literal Positive Cycle Misses the Generic Component--Soft Tor Support

## Physical incidence equations

For the grade-two sector isolating vertex \(i\), let \(jk\) be the retained
edge. Its connected complementary component has energy pole

\[
q_{jk}=X_j+X_k+y_{ij}+y_{ik}.
\]

The Tor support of Entry 2160 is

\[
Z_{jk}=\{q_{jk}=0,\ y_{jk}=0\}.
\]

On the literal Bunch--Davies positive chamber all displayed energies are
positive. Therefore \(q_{jk}>0\), including on the retained-edge soft face
\(y_{jk}=0\). Hence

\[
\boxed{
\overline\Gamma_{\rm BD}^{\,\rm generic}\cap Z_{jk}=\varnothing.
}
\]

## Boundary closure

For nonnegative energies,

\[
q_{jk}=0
\quad\Longleftrightarrow\quad
X_j=X_k=y_{ij}=y_{ik}=0.
\]

Together with \(y_{jk}=0\), physical incidence is confined to the deeper
boundary

\[
X_j=X_k=y_{12}=y_{23}=y_{31}=0.
\]

The remaining isolated-site energy \(X_i\) need not vanish. Thus each cyclic
Tor packet reaches the physical closure only on a labelled two-site
all-soft stratum, not on its generic codimension-two support.

## Consequence

The generic \((3,6,3)\) Tor family of Entry 2161 has zero literal physical
pairing by support disjointness. It remains a valid coefficient object but
is not selected by the positive contour.

Only two routes remain admissible:

1. compute specialization on the deeper labelled two-site all-soft strata;
2. derive an analytically continued relative cycle independently from the
source prescription.

No continuation may be inferred merely from the existence of the Tor packet.

## Classification

- generic coefficient Tor packet: nonzero;
- literal positive-cycle incidence: empty;
- physical closure incidence: deeper existing soft support only;
- generic physical null syndrome: absent;
- new Carrier support: none.

## Evidence

- Entries 2135 and 2160--2161
- research/benincasa/checkers/component_soft_positive_incidence.rs
- allocator claim seqclaim-e685f5eeaee39b32f88862f4
