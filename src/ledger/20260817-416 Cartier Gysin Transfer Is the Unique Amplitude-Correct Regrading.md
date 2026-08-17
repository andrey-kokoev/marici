---
id: 416
date: 2026-08-17
title: Cartier Gysin Transfer Is the Unique Amplitude-Correct Regrading
---

# Cartier Gysin Transfer Is the Unique Amplitude-Correct Regrading

Entry 415 proved that the independent Tate--Cartier tensor totalization
cannot embed strictly into the facewise PC target: its amplitude is six
rather than three. The purity theorem of Entry 131 indicates the correct
repair. Every Cartier degree carries a codimension-one Thom orientation and
a compensating Gysin shift.

Let \(p\) be Tate carrier degree and \(q\) Cartier exterior degree. Before
transfer the total degree is \(p+q\). If a uniform Gysin correction \(c\) is
applied per Cartier degree, with an overall shift \(s\), then
\[
\deg_{c,s}(p,q)=p+q-cq+s.
\]
Requiring all sixteen occupied bidegrees \(0\leq p,q\leq3\) to land exactly
in the target degrees \(0,1,2,3\) has the unique integral solution
\[
\boxed{c=1,\qquad s=0.}
\]
Thus
\[
\boxed{\deg_G(p,q)=p.}
\]
All three external Cartier degrees must be transferred; transferring only
the exceptional interval or only one marked normal cannot repair the
amplitude.

## Collapsed profile

After this Gysin regrading, each Tate generator carries the full
eight-dimensional Cartier coefficient packet without acquiring additional
chain degree. The degree profile becomes
\[
(1,3,3,1)\cdot(1+3+3+1)
=\boxed{(8,24,24,8)}.
\]
This fits degreewise inside the fixed endpoint quotient
\[
\operatorname{rk}(F_K/F_V)=\boxed{(12,57,87,43)}.
\]
Hence the amplitude and raw rank obstructions disappear simultaneously.
This is only a capacity statement, not yet an embedding theorem.

The regrading also determines the type of the two differentials:

- the Tate/carrier differential remains a chain differential of degree
  \(-1\);
- the Cartier differential becomes degree zero after Gysin transfer and
  must be represented as a filtered Bockstein/can--var operator.

This explains why the desired realization is a filtered PC map rather than
an ordinary map from the seven-degree tensor complex. The vertical
Cartier direction survives as coefficient and filtration structure; it is
not another cellular boundary direction in Entry 143.

## Next gate

The next finite construction should work degree by degree with the collapsed
profile \((8,24,24,8)\). It must place the eight Cartier states over each
Tate carrier generator using Entry 131's purity maps, and verify:

1. the carrier boundary gives \(N,1-r,\epsilon\);
2. the transferred degree-zero operator gives the three first Cartier
   symbols;
3. the normalized blowdown connector commutes with that operator; and
4. the nonzero generic \(Q\) roof and both endpoint residues survive.

The executable audit is
\`research/voevodsky/check_cartier_gysin_regrading.py\`.
