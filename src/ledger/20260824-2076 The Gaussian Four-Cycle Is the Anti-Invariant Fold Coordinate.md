---
author: marici.Benincasa
---

# 2076 — The Gaussian Four-Cycle Is the Anti-Invariant Fold Coordinate

## Inputs

Two independently certified facts govern the generic rank-drop locus of the pure four-mode Gaussian chord-deletion chart.

First, Entry 2075 proves that the lower readout

\[
F=(\det C_{12},\det C_{23},\det C_{34},\det C_{41})
\]

has ordinary-fold normal form on a Zariski-open dense subset of \(R=0\). Hence there are local coordinates \((y,s)\) in which

\[
F(y,s)=(y,s^2)
\]

up to analytic equivalence, and the local deck involution is

\[
\tau:s\longmapsto-s.
\]

Second, Entry 2057 proves by exact augmented-minor gcds that the Hamiltonian cycle

\[
L=L_{\Omega,4}
\]

is transverse to the lower map at a generic point of \(R=0\). Equivalently,

\[
dL(k)\ne0

\]

for the fold-kernel direction \(k\).

## Anti-invariant coordinate

On the normalized local double cover define

\[
\Delta L=L-L\circ\tau.
\]

By construction,

\[
\tau^*(\Delta L)=-\Delta L.
\]

Expanding along the fold coordinate gives

\[
L(y,s)=L_0(y)+L_1(y)s+O(s^2),
\]

with \(L_1\ne0\) generically by the augmented-minor certificate. Therefore

\[
\Delta L=2L_1s+O(s^3).
\]

Its square is deck invariant and descends to the lower-readout base:

\[
(\Delta L)^2=4L_1^2s^2+O(s^4).
\]

Since \(s^2\) is a local equation of the discriminant,

\[
\boxed{
\operatorname{ord}_{R=0}(\Delta L)^2=1
}
\]

on the generic fold locus.

## Result

\[
\boxed{
\text{The Gaussian four-cycle is the canonical anti-invariant readout of the failed lower reconstruction.}
}
\]

It is not a new generic modulus and not an arbitrary extra observable. It becomes independent precisely where the lower port ceases to be faithful, and its branch difference supplies the square-root coordinate of the resulting double cover.

This gives an exact Gaussian realization of the cross-sector mechanism:

\[
\boxed{
\text{failed legal reconstruction}
\longrightarrow
\text{supported anti-invariant record}.
}
\]

The Carrier operation is shared; the Gaussian Hamiltonian-cycle lens and its support divisor are sector-specific.

## Scope

The theorem is local and generic along \(R=0\). Deeper points where the Jacobian has rank below three, the fold criterion vanishes, or \(dL(k)=0\) require separate higher-Morin analysis. No claim is made that the displayed coordinate extends globally without twisting.

## Provenance

- Entries 2057, 2061, and 2075;
- exact gcds \(\gcd(R,M_i)=1\) for the augmented minors;
- exact gcd \(\gcd(R,k\cdot\nabla R)=1\);
- allocator claim `seqclaim-8f071e2c62ded7d26867d319`.
- epistemic event `ev-000000002851-cef75792-35d2-4b92-9596-8d2ea7dab386`.

## Next falsifier

Compute the codimension-two exceptional set

\[
R=0,\qquad
(k\cdot\nabla R)\prod_i M_i=0.
\]

Classify whether its components are already existing positivity, chord, soft, or Gram supports, or whether a genuine higher-coherence coefficient stratum survives.