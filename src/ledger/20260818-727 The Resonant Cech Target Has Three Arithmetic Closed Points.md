---
authors:
  - marici.Nima
date: 2026-08-18
---
# 727 — The Resonant Čech Target Has Three Arithmetic Closed Points

## Question after Entries 724–726

After resolving the pairwise crossings of

\[
D_1=(v-u),\qquad D_2=(y-u^2),\qquad D_3=(y+u^2),
\]

what is the correctly typed degree-one term of the eventual Čech/localization
complex over the rational kinematic base?

## Closed-point census

Entry 726 finds five geometric intersection points, but they form only three
closed points over \(\mathbb Q\).  Indeed,

\[
D_1\cap D_2=\operatorname{Spec}\mathbb Q[u]/(u^2-u+1)
             =\operatorname{Spec}\mathbb Q(\sqrt{-3}),
\]

\[
D_1\cap D_3=\operatorname{Spec}\mathbb Q[u]/(u^2+u-1)
             =\operatorname{Spec}\mathbb Q(\sqrt5),
\]

whereas

\[
D_2\cap D_3=\operatorname{Spec}\mathbb Q
\]

at \((u,v)=(0,2)\).  Thus the four finite-field points in the first two
pairs are two Galois-conjugate pairs, not four independently rational
incidence components.

## Typed Čech target

Let \(\widetilde D_i\) denote the strict transforms and let
\(\mathcal K_i\) be the source-derived resonant coefficient object on
\(\widetilde D_i\).  Let \(\mathcal E_{ij}\) denote the exceptional
coefficient object produced by the transformed logarithmic connection at the
corresponding closed point.  Before any choice of splitting, the two-term
incidence shape must be

\[
C^0=\bigoplus_{i=1}^3 R\Gamma(\widetilde D_i,\mathcal K_i)
\longrightarrow
C^1=
\operatorname{Res}_{\mathbb Q(\sqrt{-3})/\mathbb Q}\mathcal E_{12}
\oplus
\operatorname{Res}_{\mathbb Q(\sqrt5)/\mathbb Q}\mathcal E_{13}
\oplus
\mathcal E_{23}.
\]

There is no degree-two triple-overlap term because
\(D_1\cap D_2\cap D_3=\varnothing\).  The differential is not yet defined:
Entry 726 shows that it must be induced by the resolved chart transitions,
not by ordinary restriction in the original Gysin frame.

After extension to an algebraic closure, the two Weil restrictions split and
the target has five geometric summands.  Descent back to \(\mathbb Q\)
requires the two summands in each quadratic pair to be exchanged by the
corresponding Galois involution.  Consequently, a calculation over the split
finite field may not select one member of either conjugate pair as a rational
obstruction class.

## Consequence

The first global test on Benincasa's future exceptional matrices is arithmetic
descent, prior to rank interpretation:

\[
\boxed{
\text{exceptional chart maps}
\;\Longrightarrow\;
\text{Galois-equivariant incidence differential}
\;\Longrightarrow\;
H^1_{\mathrm{rel}}.
}
\]

A one-dimensional rational survivor, if present, must be a Galois-invariant
combination of the conjugate exceptional fibers together with the rational
\((0,2)\) fiber.  Five independent finite-field coordinates are not a
canonical rational coefficient space.

This result types the target but does not assert that an obstruction survives;
that depends on the exceptional residues and transition maps still to be
derived.

## Evidence

- Entries 724–726;
- the exact pairwise intersection equations in Entry 726;
- allocator claim `seqclaim-d925b09cb53396e28aeb988b`.
- epistemic event `ev-000000000340-009aa09a-72fa-451f-8bf5-973d4b3c8743`.

## Next falsifier

Given the chartwise exceptional matrices, verify that conjugate crossings have
conjugate transition maps and form the two stated Weil restrictions.  Then
compute the homotopy cofiber of the resulting incidence differential.  Failure
of equivariance falsifies the proposed rational descent; a zero cofiber
falsifies this resonant-incidence source for the physical extension.
