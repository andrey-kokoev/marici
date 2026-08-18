---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 838 — The Generic All-Soft Polar Discriminant Splits into Two Labelled Fold Components

## Question after Entries 836–837

Entry 837 canonically types the polar coefficient as

\[
\mathcal P_{\rm pol}=\phi_\pi(\mathcal K_{\rm CM})
\]

and proves generic rank one from square-freeness.  The unresolved generic
question is the complete labelled factorization of its discriminant and
the local inertia on each component.  Triangle-wall specialization is not
computed here.

## Exact factorization

Along a fiber-scaling orbit, with \(z=s^2\),

\[
K(z)=K_0+zK_2+z^2K_4.
\]

Exact expansion over \(\mathbb Z\) gives

\[
\boxed{
K_2^2-4K_0K_4
=
\Lambda(P_1,P_2,P_3)Q_+Q_-.
}
\]

Here

\[
\Lambda
=
(P_1-P_2-P_3)(P_1-P_2+P_3)
\mathbin{\cdot}(P_1+P_2-P_3)(P_1+P_2+P_3)
\]

and

\[
\boxed{
Q_\pm
=
E^2(a^2-b^2)-P_1^2a^2+P_2^2b^2
\pm2EP_3ab.
}
\]

Thus, away from \(\Lambda=0\), the polar discriminant is not an
unlabelled binary quadratic.  It consists of two conjugate occurrence
components \(Q_+=0\) and \(Q_-=0\).

Their difference is

\[
Q_+-Q_-=4EP_3ab.
\]

Consequently

\[
\boxed{
V(Q_+,Q_-)
\subset
V(E)\cup V(P_3)\cup V(a)\cup V(b).
}
\]

The two generic components are disjoint away from already frozen total
energy, soft, and coordinate-boundary support.

## Generic local rank

On \(Q_+=0\), the rational point

\[
(E,P_1,P_2,P_3,a,b)=(-4,1,3,1,1,1)
\]

satisfies

\[
\Lambda=45,qquad Q_-=16,qquad \partial_EQ_+=2.
\]

Hence \(Q_+\) is a reduced transverse discriminant component there.  The
sign-reflected witness gives the same result for \(Q_-\).  At a generic
point of either component, with \(K_4\ne0\), completing the square gives

\[
K(z)=K_4\xi^2-\tau,
\]

and the double cover has local form

\[
\boxed{W^2=\xi^2-\tau.}
\]

Therefore each labelled component carries one relative fold class:

\[
\boxed{
\operatorname{rank}_{Q_\pm}\mathcal P_{\rm pol}=1.
}
\]

## Two distinct inertia statements

The roots of the orbit quadratic are exchanged around \(Q_\pm=0\), so
their reduced degree-zero permutation line has character \(-1\).  The
vanishing generator of the complex-curve \(A_1\) model
\(W^2=\xi^2-\tau\), however, is fixed by its Picard–Lefschetz monodromy:

\[
\boxed{
\chi_{\rm roots}=-1,
\qquad
T_{\rm van}=+1.
}
\]

These must not be conflated.  The former tracks the two branch points;
the latter is the rank-one relative vanishing-cycle coefficient.

## Classification

The factor \(\Lambda\) is the existing momentum-triangle wall.  The
factors \(Q_\pm\) are labelled coefficient-polar support internal to the
source-defined projection.  Their mutual collision occurs only on existing
support.  Hence

\[
\boxed{
\text{existing carrier}
+
\text{two rank-one labelled polar coefficient components}
}
\]

with no new carrier divisor inferred.

## Verification

- exact sparse Rust checker:
  `research/benincasa/marici-gm/src/bin/all_soft_polar_factorization.rs`;
- packet:
  `research/benincasa/all-soft-polar-factorization.json`;
- allocator claim: `seqclaim-24dad1573020b660355ec804`.

## Join point

The next operation is the already typed specialization

\[
\psi_\Lambda\phi_\pi(\mathcal K_{\rm CM}).
\]

It must determine how the two labelled fold lines meet the triangle Gysin
object.  No conclusion about that specialization or physical Betti
selection is drawn here.
