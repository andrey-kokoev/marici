---
author: marici.Grothendieck
sequence_claim: seqclaim-d281dad99bccdccd6714c445
supersedes: 2477
---

# 2483 — Unitary Coupling Turns Theta Vacuum Zeros into Full Excited-Sector Defects

## Correction to entry 2477

Entry 2477 correctly established that separate reciprocal determinants are
trivial and that character closure is infinite. It incorrectly left vacuum
orthogonality and full-sector nontransversality unrelated on the real
character axis.

Unitarity supplies the missing exact relation.

## Universal coupled theorem

For a unitary operator decomposed relative to a normalized vacuum,

\[
 U=
 \begin{pmatrix}
  a&\beta\\
  \gamma&D
 \end{pmatrix},
 \qquad
 a=\langle\Omega,U\Omega\rangle,
\]

the excited compression obeys

\[
 D^*D=I-\beta^*\beta,
 \qquad
 \det(D^*D)=|a|^2.
\]

Therefore

\[
 a=0
 \quad\Longleftrightarrow\quad
 \ker D\ne0.
\]

For real theta character transport,

\[
 \det(D_x^*D_x)
 =
 \left|\frac{X(x)}{X(0)}\right|^2.
\]

A critical-axis theta zero is exactly a full excited-sector defect.

## Revised boundary

Off-axis character transport is nonunitary, so this defect identity no longer
holds. Moreover, a nonconstant holomorphic family cannot preserve one fixed
Hermitian metric \(J\) on an open complex domain: differentiating
\(F(z)^*JF(z)=J\) forces \(F'(z)=0\).

The viable RH-bearing object is therefore not a holomorphic \(J\)-unitary
continuation, but a source-derived \(J\)-contractive half-plane transfer
function with unitary boundary values and positive defect kernel.

## Durable conclusion

\[
\boxed{
\text{on the critical axis, zero means complete coupled defect;}
\quad
\text{off-axis, that meaning is unavailable}.}
\]

RH sharpens to the claim that the completed overlap cannot vanish where its
unitary full-sector defect interpretation has ceased to exist.

## Scope and evidence

- Supersedes the vacuum-minor conclusion of ledger entry 2477 while retaining
  its separate-sector and infinite-closure conclusions.
- Research packets:
  research/grothendieck/theta-unitary-vacuum-defect-determinant-theorem.md and
  research/grothendieck/theta-holomorphic-j-unitary-continuation-no-go.md.
- No source-derived \(J\)-contractive transfer function, off-axis exclusion,
  or RH theorem is claimed.
- Graph admission:
  ev-000000003411-0f89bc33-2925-498b-95be-df425202033b.
- Ledger allocation: seqclaim-d281dad99bccdccd6714c445.
