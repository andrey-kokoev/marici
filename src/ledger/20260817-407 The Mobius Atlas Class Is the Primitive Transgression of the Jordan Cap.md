---
id: 407
date: 2026-08-17
title: The Mobius Atlas Class Is the Primitive Transgression of the Jordan Cap
---

# The Möbius Atlas Class Is the Primitive Transgression of the Jordan Cap

Entry 406 left open whether the selected primitive atlas class \(\omega\)
is literally the capped rectangular Jordan fundamental-formula cell or
whether a top-dimensional comparison is required. The cellular degrees
decide this before any further matrix evaluation: literal equality is
mistyped.

Let \(M\) be the Möbius carrier and let \(X=M\cup_{\partial M}O\), where
\(O\) is the octagonal cap supplied by the Jordan fundamental-formula
coherence. Write \(\gamma\) for the primitive core of \(M\). Then
\[
H_1(M;\mathbb Z)=\mathbb Z\langle\gamma\rangle,
\qquad
H_2(X,M;\mathbb Z)=\mathbb Z\langle O\rangle.
\]
The boundary circle of a Möbius band traverses its core twice. Hence the
connecting map of the pair is
\[
\delta:H_2(X,M;\mathbb Z)\longrightarrow H_1(M;\mathbb Z),
\qquad
\boxed{\delta[O]=2\gamma.}
\]

By Entry 406 the normalized atlas cocycle is primitive:
\[
\langle\omega,\gamma\rangle=1.
\]
Consequently its relation to the capped Jordan cell is
\[
\boxed{\langle\omega,\delta[O]\rangle=2.}
\]
This is exactly the previously computed outer-octagon period. Modulo two it
becomes the zero endpoint parity, so the integral and mod-two calculations
now fit in one long-exact-sequence diagram rather than appearing to select
different classes.

## Interpretation

The Jordan cap and \(\omega\) are not two representatives of one chain:
the cap is a relative degree-two homology generator, whereas \(\omega\) is
a degree-one cohomology generator on the carrier. Their canonical comparison
is the connecting-map pairing above. No discretionary top-dimensional
homotopy is needed to repair a mismatch; the required top-dimensional datum
is precisely the cap attachment map of degree two.

This also clarifies what Entries 403--404 established. The four rectangular
Jordan square boundaries vanish and their PC comparison is strict, so the
local square faces introduce no correction to \(\delta[O]=2\gamma\). The
remaining nonzero datum is global: one primitive unit on the crosscap core,
seen twice on the outer boundary.

The conclusion remains additive and cellular. It does not manufacture
invertible transition maps from residue/Gysin cospans and does not assert a
multiplicative holonomy representation.

The executable audit is
`research/voevodsky/check_mobius_jordan_cap_transgression.py`.
