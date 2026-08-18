---
id: 471
authors:
  - marici.Benincasa
date: 2026-08-18
---
# The Length-Three Local Fiber Is Conormal Plus Matrix-Factorization Data

## Record

Status: categorical typing of the local associated fiber from Entries 468--470.

Let

\[
S=\mathbb Q[z],
\qquad
R=S/(z^2),
\qquad
I=(z^2).
\]

The even and odd resonant blocks have different categorical origins.

The even Koszul relation cell of Entry 469 is the conormal term in the derived
self-intersection of the doubled carrier:

\[
\operatorname{Tor}_1^S(R,R)
\cong
I/I^2
\cong
R.
\]

It therefore has Cartier length two. It is a perfect relative relation over
the ambient ring \(S\); it becomes zero if one passes only to the singularity
category and forgets the relative self-intersection.

The odd matrix factorization of Entry 468 induces

\[
\operatorname{coker}(z:R\to R)
\cong
R/(z),
\]

with Cartier length one. This is the genuinely singular, reduced
anti-invariant contribution.

Consequently the local associated resonant fiber is typed as

\[
\boxed{
\mathcal R_{\rm loc}
\simeq
\operatorname{Tor}_1^S(R,R)_+
\oplus
\operatorname{coker}(z:R\to R)_-
}
\]

and has

\[
\operatorname{length}_{\mathbb Q}\mathcal R_{\rm loc}
=
2+1=3,
\qquad
\operatorname{rank}_{\rm red}=1+1=2.
\]

Entry 470's monodromy idempotents make this sum canonical for any
deck-equivariant specialization map. The result also sharpens the required
coefficient calculus: a pure matrix-factorization or singularity-category
description is insufficient because it erases the even conormal cell. The
minimal local framework must retain both relative derived self-intersection
and singularity data.

## Classification

- doubled carrier: existing Cartier thickening;
- even block: conormal/derived-intersection coefficient data;
- odd block: matrix-factorization coefficient data;
- cross-parity extension: forbidden by Entry 470;
- new carrier stratum: none.

## Next falsifier

Construct the complete deck-equivariant carrier-reduction morphism separately
in the \(+\) and \(-\) eigenspaces. Test whether its fibers are exactly

\[
I/I^2
\quad\text{and}\quad
R/(z),
\]

or whether same-character quartic-tail classes survive. This is the remaining
global comparison; the local length-three calculation alone does not settle
it.

## Evidence

- research/benincasa/marici-gm/src/bin/soft_axis_derived_fiber_typing.rs;
- Entries 468--470.
