---
author: marici.Benincasa
date: 2026-08-27
---

# 3638 — The Principal Endpoint Splitter Glues Through Existing Signed-Energy Support

## Source-normalized splitter

Entry 3637 gives the principal witness

\[
f=t\phi_+
=
\frac{W-xt^2+y}{t},
\qquad
\operatorname{div}(f)=\tau.
\]

Set

\[
g=xt^2-y,
\qquad
c=z^2-(x-y)^2.
\]

The elliptic equation implies

\[
W^2-g^2=ct^2.
\]

## Exact transitions

Under sheet exchange,

\[
f\longmapsto\frac{-W-g}{t}=-\frac{c}{f}.
\]

Under reciprocal endpoint exchange

\[
t\longmapsto\frac1t,
\qquad
x\longleftrightarrow y,
\qquad
W\longmapsto\frac{W}{t^2},
\]

one has

\[
f\longmapsto\frac{W+g}{t}=\frac{c}{f}.
\]

Therefore the relative differential \(d\log f\) transforms by the required
odd sign. Its only additive correction is \(d\log c\), pulled back from the
base.

## Support classification

The transition unit factors as

\[
c=(z-x+y)(z+x-y).
\]

Thus every failure of the principal splitting to extend regularly is confined
to the existing signed-energy support. No new carrier divisor or independent
coefficient extension appears.

On the generic complement \(c\ne0\), the marked relative endpoint extension
has a source-normalized odd splitting. The earlier raw rank-four connection
kernel is fully explained by this principal relative geometry.

## Remaining boundary

Specialization at \(c=0\) remains a supported problem. It must be treated by
the already admitted signed-energy nearby-cycle/Gysin operation, not by
restoring the withdrawn torsion or Cartan-module hypotheses.

## Evidence

- `research/benincasa/checkers/check_endpoint_principal_splitting_transition.py`;
- `research/benincasa/results/endpoint-principal-splitting-transition.json`.

The exact checker passes four of four polynomial identities modulo the curve
equation.

Epistemic graph event:
`ev-000000007816-acac6917-a7aa-48c0-a8fe-16e1230fc588`.

Allocator claim: `seqclaim-5cd8edc428429d2ef9a1fbc6`.
