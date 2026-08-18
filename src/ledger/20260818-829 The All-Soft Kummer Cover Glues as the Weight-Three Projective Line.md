---
authors:
  - marici.Nima
date: 2026-08-18
---
# 829 — The All-Soft Kummer Cover Glues as the Weight-Three Projective Line

## Question after Entry 828

Entry 828 identifies the all-soft exceptional object with the
projectivized universal Cayley--Menger family

\[
W^2=K_{\rm CM}(\widehat{\boldsymbol k}).
\]

The first gluing test is whether the scalar cover itself requires an
additional overlap divisor.

## Chart transition

Let \(x_i\) be any of the six homogeneous coordinates

\[
E,\ P_1,\ P_2,\ P_3,\ a,\ b.
\]

On \(U_i=(x_i\neq0)\), define

\[
W_i=\frac{w}{x_i^3}.
\]

Because \(K_{\rm CM}\) has degree six, on \(U_i\cap U_j\)

\[
\boxed{
W_j=\left(\frac{x_i}{x_j}\right)^3W_i.
}
\]

On triple overlaps,

\[
\left(\frac{x_i}{x_j}\right)^3
\left(\frac{x_j}{x_k}\right)^3
=
\left(\frac{x_i}{x_k}\right)^3,
\]

so the cocycle closes exactly. The inverse Kummer generator transforms by
the dual weight:

\[
\frac1{W_j}
=
\left(\frac{x_j}{x_i}\right)^3\frac1{W_i}.
\]

The deck involution \(W_i\mapsto-W_i\) commutes with every transition.

## Carrier consequence

Every transition factor is a unit on its declared overlap. Its zeros and
poles occur only on the already present projective coordinate hyperplanes.
Therefore

\[
\boxed{\text{new scalar-overlap incidence divisor}=0.}
\]

The exceptional Kummer coordinate is globally typed by the weight-three
projective line, equivalently the corresponding \(\mathcal O(3)\) cocycle;
the anti-invariant Kummer generator carries the dual weight.

## Remaining gluing gate

This closes only the scalar cover. The labelled residue orientation,
transformed differential forms, and support maps must still be checked
chartwise. A failure there would be coefficient or mixed-variance gluing,
not a failure of the homogeneous Kummer cocycle.

## Verification

- checker: research/nima/audit_all_soft_projective_kummer_gluing.py;
- packet: research/nima/all-soft-projective-kummer-gluing.json;
- allocator claim: seqclaim-809f900c0e9fcd36f68d5bab.
