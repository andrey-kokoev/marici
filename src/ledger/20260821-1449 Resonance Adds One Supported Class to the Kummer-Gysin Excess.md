---
author: marici.Nima
---

# 1449 — Resonance Adds One Supported Class to the Kummer–Gysin Excess

## Status

Exact resonant continuation of Entry 1448. The generic exceptional line
extends across trivial Kummer monodromy, but the resonant fiber acquires one
additional class supported at the character divisor. This remains coefficient
complexity on the existing singleton-energy collision carrier.

## Character-Rees complex

Let

\[
h=\lambda-1,
\qquad
R=\mathbb Q[h],
\]

where \(\lambda=e^{2\pi i\alpha}\) is the Kummer monodromy. The exceptional
three-punctured line retracts to a wedge of two labelled circles. The loop
around the Gysin divisor has monodromy \(1\), while the loop around the Kummer
divisor has monodromy \(\lambda\). Its cellular cochain complex is therefore

\[
R\xrightarrow{d}R^2,
\qquad
d(1)=(0,h).
\]

This is a character-Rees model: it retains the deformation parameter before
specialization and therefore avoids inferring a nearby-cycle module from
fiber ranks alone.

## Exact module

The Smith invariant of \(d\) is \(h\). Hence

\[
H^0=0,
\qquad
\boxed{H^1\simeq R\oplus R/(h).}
\]

Over the generic field \(\mathbb Q(h)\), the torsion term vanishes and

\[
\dim H^1_{h\ne0}=1,
\]

recovering Entry 1448. At resonance,

\[
d\otimes_R R/(h)=0,
\]

so

\[
\dim H^0_{h=0}=1,
\qquad
\dim H^1_{h=0}=2.
\]

The jump is not a second generic exceptional line. It is the specialization
of the canonical supported summand \(R/(h)\), accompanied by the invariant
section in degree zero.

## Classification

\[
\boxed{
\text{free rank-one Kummer--Gysin excess}
+
\text{one resonance-supported coefficient class}.
}
\]

The support equations remain

\[
X_1+y=0,
\qquad
h=0.
\]

Thus resonance refines the coefficient complex on a predeclared carrier
intersection. It supplies neither a new energy wall nor a new Cut operation.

## Scope boundary

The cellular certificate determines the local character-direction module. It
does not select a physical resonant cycle, fix a logarithm branch, or prove a
global comparison for simultaneous endpoint collisions.

## Next falsifier

For the two-endpoint intersection

\[
X_1+y=X_2+y=0,
\]

form the occurrence-resolved tensor product of the two character-Rees
complexes before imposing the physical diagonal. Test whether its derived
Tor class is exactly the product of the two singleton supported objects or
requires an additional coherence cell.

## Durable evidence

- `research/nima/check_resonant_kummer_gysin_excess.py`;
- `research/nima/results/resonant-kummer-gysin-excess.json`;
- allocator claim `seqclaim-8842d97013465f3e5be77d39`.
