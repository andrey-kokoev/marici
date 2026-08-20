---
title: "The Physical Five-Site Current Carries Only the External-Gram Kummer Density"
date: 2026-08-20
entry: 1216
status: active-supported-physical-measure
sector: cosmology
---

# 1216 — The Physical Five-Site Current Carries Only the External-Gram Kummer Density

Sequence claim: `seqclaim-ec15f849083267e0755287bd`.

## Physical coordinates

Continue on Entry 1215's labelled nonsingular external basis
\((q_1,q_2,q_3)\). Let \(Q_{\rm ext}\) be the matrix with these vectors as
columns and

\[
H=Q_{\rm ext}^TQ_{\rm ext}.
\]

Use the three physical loop coordinates

\[
u_i=\ell\cdot q_i.
\]

Then

\[
u=Q_{\rm ext}^T\ell,
\qquad
\det\frac{\partial u}{\partial\ell}=\det(Q_{\rm ext}),
\]

and

\[
\det(H)=\det(Q_{\rm ext})^2.
\]

Therefore the physical loop current is

\[
\boxed{
d^3\ell
=
\frac{du_1\wedge du_2\wedge du_3}{\sqrt{\det(H)}}.
}
\]

## Coefficient character

The only coefficient character introduced by this change of variables is

\[
\boxed{\mathcal K_{\det(H)^{-1/2}}.}
\]

Its branch support is the already declared external-Gram divisor
\(\det(H)=0\). Source denominator and soft supports remain separate and are
not altered by this calculation.

## Fate of the unrestricted radial Kummer line

On the physical rank-\(\le3\) locus, the unrestricted five-edge
Cayley--Menger determinant vanishes identically together with its required
higher minors. Its radial discriminant is therefore not a divisor of the
constrained three-dimensional current.

Consequently Entry 1212's endpoint Kummer line is a valid object of the
unrestricted \(d=5\) coefficient continuation, but it has no ordinary
pullback as a local system on the physical \(d=3\) current.

The correct classification is

\[
\boxed{
\text{physical activation of the }d=5\text{ endpoint line is not applicable,}
\text{ not zero}.
}
\]

This preserves the type distinction between failure of a pairing and absence
of the coefficient object from the physical-dimensional sector.

## Carrier verdict

\[
\boxed{
\text{physical five-site measure}
=
\text{existing rank-three Gram carrier}
+
\text{external-Gram Kummer coefficient}.
}
\]

No new cosmological carrier incidence is required.

## Next falsifier

Pull the 180-term labelled OFPT denominator packet onto the three physical
coordinates \(u_i\). Determine whether every marked pole remains a linear
section over the rank-three Gram carrier and whether the external-Gram Kummer
line is compatible with the occurrence kernel and soft conormal complexes of
Entries 1203--1206. Any nonlinear residual support must be classified before
being proposed as a new carrier datum.

## Artifact

- `research/benincasa/marici-gm/src/bin/five_site_d3_physical_current.rs`
- `research/benincasa/results/five-site-d3-physical-current.json`
