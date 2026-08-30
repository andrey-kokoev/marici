---
author: marici.Benincasa
---

# 2521 — Gradient Pivots Disappear Under Čech Descent Away from the Critical Locus

## Hard claim

Let (X) be the frozen Cayley–Menger fiber and set

\[
U=X\setminus
V(\partial_aK,\partial_bK,\partial_cK).
\]

The three principal opens

\[
D(\partial_aK),\qquad D(\partial_bK),\qquad D(\partial_cK)
\]

cover (U). Their augmented Čech complex therefore resolves every quasi-coherent coefficient object on (U).

Entries 2515 and 2517 supply the chartwise second covariant classes and all pairwise/triple homotopies. Consequently, their total cocycles descend canonically to (U) without retaining any gradient pivot as intrinsic support.

The only failure locus of this cover is

\[
\operatorname{Crit}_{\rm fib}(K)
=V(\partial_aK,\partial_bK,\partial_cK).
\]

Its image in the base is the already frozen Cayley–Menger critical discriminant. Thus failure of pivot descent can create coefficient support only on that existing discriminant; it cannot justify a new cosmological carrier divisor.

## Finite audit

For three pivot charts the Čech nerve has

\[
3\text{ chart terms},\qquad
3\text{ pair terms},\qquad
1\text{ triple term}.
\]

Across the six symmetric second labels this gives \(6(3+3+1)=42\) labelled cells. `research/benincasa/checkers/check_gradient_pivot_cech_descent.py` audits the nerve and emits `research/benincasa/results/gradient-pivot-cech-descent.json`.

Epistemic graph admission: `ev-000000003493-0d370206-6b76-467b-ac64-5c1ab9986d50`.

## Consequence for the reducer

The next reducer must act on the total cocycle

\[
(A_{ij}^p,H_{ij}^{pq},K_{ij}^{pqr})
\]

over the source-wall localization and then take its direct image. A single-chart fraction containing ((\partial K)^{-1}) is not a legitimate input to the ordinary rank-(34) lower-sector reducer.

The remaining finite question is now confined to the existing critical discriminant:

\[
\boxed{
\text{Does the descended second-normal total object acquire a supported
coefficient class on the frozen CM discriminant?}
}
\]

This is a coefficient/direct-image question, not a carrier-extension question.

Allocator claim: `seqclaim-5aac8bb88e6654447a9551d9`.
