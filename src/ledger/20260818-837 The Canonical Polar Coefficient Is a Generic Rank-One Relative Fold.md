---
authors:
  - marici.Nima
date: 2026-08-18
---
# 837 — The Canonical Polar Coefficient Is a Generic Rank-One Relative Fold

## Canonical object

Following the source-defined projection

\[
\pi:\mathcal X_{\rm CM}\longrightarrow B_{\rm ext},
\]

the polar coefficient is typed without a horizontal splitting as

\[
\mathcal P_{\rm pol}=\phi_\pi(\mathcal K_{\rm CM}).
\]

Euler coherence is retained by the cotangent transitivity triangle

\[
\pi^*L_{B_{\rm ext}}\to L_{\mathcal X_{\rm CM}}
\to L_{\mathcal X_{\rm CM}/B_{\rm ext}}\xrightarrow{+1}.
\]

## Exact polar discriminant

Along a fiber-scaling orbit, put \(z=s^2\). Then

\[
K(z)=K_0+zK_2+z^2K_4
\]

and elimination of \(z\) gives

\[
\boxed{\Delta_{\rm pol}=K_2^2-4K_0K_4.}
\]

Writing \(A=a^2\), \(B=b^2\), this is a binary quadratic

\[
\Delta_{\rm pol}=D_{AA}A^2+D_{AB}AB+D_{BB}B^2.
\]

If \(K_2=C_aA+C_bB\) and
\(K_4=P_1^2A^2+C_{ab}AB+P_2^2B^2\), its binary discriminant is exactly

\[
\boxed{
D_{AB}^2-4D_{AA}D_{BB}
=16K_0\left(
P_2^2C_a^2-C_{ab}C_aC_b+P_1^2C_b^2+K_0\Lambda
\right).
}
\]

Exact simplification gives the stronger factorization

\[
\boxed{\Delta_{\rm pol}=\Lambda\,Q_{\rm pol},}
\]

where

\[
Q_{AA}=(E^2-P_1^2)^2,
\qquad
Q_{BB}=(E^2-P_2^2)^2,
\]

and

\[
Q_{AB}=-2\left[
E^4+(2P_3^2-P_1^2-P_2^2)E^2+P_1^2P_2^2
\right].
\]

The binary discriminant of the first normal grade is

\[
\boxed{\operatorname{disc}_{A:B}(Q_{\rm pol})=16E^2K_0.}
\]

The checker supplies exact nonzero rational witnesses. Therefore away from
\(\Lambda E K_0=0\), the polar quadratic is square-free over the external
function field.

## Generic coefficient rank

Away from the displayed binary discriminant and from \(K_4=0\), the two
roots of \(K(z)\) meet by a simple fold. Hence

\[
\boxed{
\operatorname{rank}\mathcal P_{\rm pol}=1
\quad\text{generically.}
}
\]

This rank belongs to the relative vanishing-cycle coefficient object. It
does not define a new carrier divisor and does not select a physical Betti
class.

## Triangle specialization

The canonical specialization is

\[
\psi_\Lambda\mathcal P_{\rm pol}
=\psi_\Lambda\phi_\pi(\mathcal K_{\rm CM}).
\]

The exact factorization shows that the restriction vanishes identically,
but generically to order one. Its first normal grade is \(Q_{\rm pol}\),
which remains square-free away from the already frozen loci \(E=0\) and
\(K_0=0\). Thus the generic triangle specialization contributes the single
uniform \(\Lambda\)-grade expected from the existing triangle Gysin map;
there is no generic rank excess.

The remaining possible excess is confined to the deeper intersections

\[
\Lambda=E=0
\qquad\text{or}\qquad
\Lambda=K_0=0,
\]

which are already marked soft/signed endpoint strata. Their iterated
nearby-cycle comparison is the next finite test.

## Verification

- checker: `research/nima/audit_polar_discriminant_generic_fold.py`;
- packet: `research/nima/polar-discriminant-generic-fold.json`;
- allocator claim: `seqclaim-83a260a54843506c4239f5bd`.
