---
title: "Five-Site Radial Endpoint Collisions Form a Doubled Cartier Layer"
date: 2026-08-20
entry: 1209
status: active-supported-symbolic
sector: cosmology
---

# 1209 — Five-Site Radial Endpoint Collisions Form a Doubled Cartier Layer

Sequence claim: `seqclaim-3408fa9ac5ef8cdca7a90fbf`.

## Projective radial branch

Homogenize Entry 1208's radial polynomial:

\[
P(z,w)=K_4z^2+K_2zw+K_0w^2,
\qquad
D_{\rm rad}=K_2^2-4K_0K_4.
\]

The two endpoint divisors are \(K_0=0\), where a root reaches \(z=0\),
and \(K_4=0\), where a root reaches \(z=\infty\).

## Exact endpoint restrictions

On the finite chart \(w=1\),

\[
P(z,1)|_{K_0=0}=z(K_4z+K_2),
\qquad
D_{\rm rad}|_{K_0=0}=K_2^2.
\]

On the infinity chart \(z=1\), with \(\xi=w/z\),

\[
P(1,\xi)|_{K_4=0}=\xi(K_0\xi+K_2),
\qquad
D_{\rm rad}|_{K_4=0}=K_2^2.
\]

Thus both collision intersections are nonreduced but source-forced:

\[
\boxed{
(K_0,D_{\rm rad})=(K_0,K_2^2),
\qquad
(K_4,D_{\rm rad})=(K_4,K_2^2).
}
\]

Each carries Cartier length two transverse to its reduced support.

## Triple endpoint corner

At the intersection of both endpoints,

\[
\boxed{
(K_0,K_4,D_{\rm rad})=(K_0,K_4,K_2^2).
}
\]

Its reduced support is \((K_0,K_4,K_2)\), and its transverse coefficient
ring is

\[
\mathbb Q[K_2]/(K_2^2).
\]

The sequence \((K_0,K_4,D_{\rm rad})\) is regular in the universal
coefficient ring, so its positive Koszul homology vanishes. The length-two
structure is the ordinary nonreduced Cartier intersection, not excess Tor.

## Classification

\[
\boxed{
\text{existing endpoint carrier}
+
\text{length-two coefficient structure}
+
\text{no new carrier datum}.
}
\]

This is exactly the kind of layer H2 permits: the carrier divisors remain
unchanged while the sector-specific coefficient object remembers a doubled
collision.

## Remaining comparison

No canonical statement about the physical relative chain follows from the
scheme calculation. The next finite test is to construct the endpoint
specialization maps into this doubled layer and determine whether its
nilpotent generator is supplied by the existing finite/infinity Gysin
comparison. Failure of that map would be a coefficient-coherence defect, not
yet a new carrier stratum.

## Artifact

- `research/benincasa/marici-gm/src/bin/five_site_radial_collision_corners.rs`
- `research/benincasa/results/five-site-radial-collision-corners.json`
