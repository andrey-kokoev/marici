---
title: "The Physical Radial Boundary Is the Equator of the Four-Site Vanishing Sphere"
date: 2026-08-20
entry: 1169
status: active
sector: cosmology
---

# 1169 — The Physical Radial Boundary Is the Equator of the Four-Site Vanishing Sphere

Sequence claim: `seqclaim-01fc77398fcce38f937559bb`.

## Why the lower Gram term returns

Entry 1168 computes the node from the degree-four infinity branch. For the
radial strict transform, the lower edge-degree term discarded at fixed
projective infinity returns at the same Rees order as the node quadratic.

The full block-Gram form is

\[
K=\det(G)\,\ell^2-v^T\operatorname{adj}(G)v,
\qquad
v_i=\ell\cdot p_i.
\]

With \(\ell=Rn\), divide by \(R^2\) and retain the radial normal
\(s=R^{-1}\). In normalized exceptional coordinates the leading equation is

\[
\boxed{
\omega^2
=\det(G)-\widehat v^T\operatorname{adj}(G)\widehat v.
}
\]

For positive-definite real external Gram data this is the real \(S^3\)
model of the rank-one \(A_1\) vanishing cycle.

## Physical three-dimensional specialization

In three spatial dimensions, three generic external momenta span the full
loop-momentum space. Therefore

\[
\ell=\ell_\parallel,
\qquad
\ell_\perp=0.
\]

The Schur-complement identity gives

\[
K=\det(G)\,\ell_\perp^2=0.
\]

Hence the literal physical radial chain reaches the exceptional smoothing
on

\[
\boxed{\omega=0.}
\]

Inside the real vanishing \(S^3\), this is its equatorial \(S^2\).

## Integral consequence

The source therefore supplies a canonical oriented equatorial boundary, but
not yet an oriented generator of the full vanishing \(S^3\). Constructing
that generator requires choosing or deriving how the two transverse
\(\omega\)-hemispheres are glued.

Thus

\[
\boxed{
\text{physical equator }S^2
\not\Rightarrow
\text{canonically normalized vanishing }S^3.
}
\]

The local vanishing coefficient exists, and the physical chain reaches its
boundary, but its integral activation remains unselected. It is neither
proved zero nor canonically primitive.

## Classification

- carrier: existing total-energy, radial-normal, and Gram support;
- coefficient: rank-one threefold-node vanishing cycle;
- literal physical datum: the equatorial \(S^2\);
- missing datum: a source-derived transverse/dimensional continuation or
  sheet-gluing chain;
- new carrier stratum: none.

## Next falsifier

Audit the dimensional-continuation prescription in the primary loop measure.
Determine whether continuation from generic spatial \(d\) to \(d=3\)
canonically glues the two \(\omega\)-hemispheres with a fixed orientation and
multiplicity. If it does not, close integral activation of this local
vanishing line under the frozen source.

## Evidence

- `research/benincasa/checkers/four_site_qg_radial_rees_boundary.py`
- `research/benincasa/results/four-site-qg-radial-rees-boundary.json`
- Entries 1167--1168.
