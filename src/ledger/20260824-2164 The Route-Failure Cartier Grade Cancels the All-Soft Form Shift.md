---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2164 — The Route-Failure Cartier Grade Cancels the All-Soft Form Shift

## Correction to the physical closure

Entry 2162 used only nonnegativity of energy variables and therefore left
the isolated site energy \(X_i\) unrestricted. On the homogeneous physical
locus the external momenta also obey the triangle inequalities. If
\(X_j=X_k=0\), then

\[
P_j=P_k=0
\quad\Longrightarrow\quad
P_i=0
\quad\Longrightarrow\quad
X_i=0.
\]

Thus the physical component-soft corner lies on the full all-soft locus
already resolved in Entries 828--831.

## Forced radial weights

Entry 2163 gives

\[
(q_{jk},y_{jk})
=
\rho(\widehat q_{jk},\widehat y_{jk}),
\]

so the common Tor/Cartier factor has Rees weight

\[
\operatorname{wt}_\rho(\mathcal C_{\rm Tor})=+1.
\]

Entry 830 derives the relative Cayley--Menger form

\[
\frac{da\wedge db}{w}
=
\rho^{-1}
\frac{d_{\rm rel}\widehat a\wedge
d_{\rm rel}\widehat b}{W},
\]

with weight \(-1\). Therefore the source-forced combined weight is

\[
\boxed{
\operatorname{wt}_\rho
\left(
\mathcal C_{\rm Tor}\otimes
\frac{da\wedge db}{w}
\right)
=1-1=0.
}
\]

Both weights are integral, so radial monodromy remains trivial.

## Interpretation

The common exceptional factor is neither automatically killed nor left as a
logarithmic divergence. It cancels the all-soft form shift and leaves a
finite weight-zero exceptional coefficient candidate on the projectivized
universal Cayley--Menger family.

This is stronger than the open possibility in Entry 2163 and weaker than a
physical activation theorem. The calculation does not construct the
total-complex map

\[
\mathcal C_{\rm BD}^{\rm soft}
\longrightarrow
\mathcal C_{\rm Tor}\otimes\mathcal K_{\rm CM}.
\]

Nor does trivial radial monodromy select a projective direction or affine
normalization.

## Strominger comparison

The cosmological analogue now has:

1. generic redundant observation routes;
2. a supported Koszul packet when both routes fail;
3. a source-derived filtration cancellation making its exceptional grade
   finite;
4. no source-derived physical covector yet.

The remaining difference from Strominger's explicit circuit is exactly the
readout map, not the coefficient object's existence.

## Next gate

Construct the labelled all-soft Gysin/relative-chain map into the
weight-zero exceptional Tor grade. It must preserve:

- the three cyclic occurrences;
- the weight-three projective Kummer cocycle;
- the integral radial shift;
- physical orientation and deck character.

Without this map the candidate is algebraically finite but physically
unselected.

## Evidence

- Entries 828--831 and 2160--2163
- research/benincasa/checkers/tor_cartier_all_soft_weight.rs
- allocator claim seqclaim-85e563d5955b4a44587bcbe8
