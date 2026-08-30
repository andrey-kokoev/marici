---
author: marici.Benincasa
date: 2026-08-25
---

# 2439 — Weighted Gram Base Change Preserves the Faithful Rank-Sixty Interaction Action

## Question

Entry 2436 proves that the physical weighted chart recovers the complete
rank-seven source interaction module at a generic Gram wall. The remaining
algebraic comparison is whether that chart remains compatible with the
rank-sixty marked localization sequence, or creates an additional kernel
after the physical replacement $w=\theta^2$.

## Frozen rank data

The source-derived direct-image results are:

\[
\operatorname{rank}\mathcal I_{\rm low}=7,
\qquad
\operatorname{rank}\mathcal I_{q_G}=6,
\qquad
\operatorname{rank}\mathcal I_{\rm full}=7.
\]

The restricted rank-six object has one principal Cartier kernel,

\[
D_3-E^2U=(c-E)q_{\mathcal G_{12}},
\]

and no additional direct-image kernel. Entry 2419 proves that the full
rank-sixty action is faithful on the rank-seven source quotient.

## Formally étale weighted chart

At a generic physical Heron wall, Entry 2436 supplies

\[
(u,v,w)
=
(\delta P_1^2,\delta P_2^2,\theta^2)
\longmapsto
(\nu_1,\nu_2,\nu_3)
\]

with Jacobian determinant

\[
\boxed{-P_1P_2.}
\]

Hence this is a formally étale base change on the generic nonsoft locus.
The failure set $P_1P_2=0$ is already frozen soft support.

## Strict marked compatibility

The complete five-wall family is

\[
\begin{aligned}
q_{g_1}&=c+b+X_1,\\
q_{g_2}&=c+a+X_2,\\
q_{g_3}&=a+b+X_3,\\
q_{g_{23}}&=c+b+X_2+X_3,\\
q_{\mathcal G_{12}}&=c+E.
\end{aligned}
\]

Every wall is independent of $(u,v,w)$. Exact differentiation gives

\[
\partial_uq=\partial_vq=\partial_wq=0
\]

for all five labelled walls. Therefore weighted base change commutes
strictly with deletion, restriction, and marked localization on the source
twisted de Rham complex. No fitted homotopy or projector is required.

Since a formally étale base change is flat, it preserves the already proved
injective lower action and the localization exact sequence. Consequently

\[
\boxed{
\operatorname{rank}\mathcal I_{\rm full}^{\rm weighted}=7,
\qquad
\ker_{\rm additional}=0.
}
\]

The cubic source normal can produce $w^3=\theta^6$, so this theorem retains
the physical angle tower through order six.

## Result

\[
\boxed{
\text{the rank-sixty marked-relative interaction action remains faithful
under the physical weighted Gram specialization.}
}
\]

The generic Gram wall introduces neither a marked Beck--Chevalley defect nor
a physical observer kernel. Its only exceptional locus is existing soft
support.

## Scope

This is an algebraic Gauss--Manin/base-change theorem assembled from the
verified rank-thirty-four, rank-twenty-six, and rank-sixty source packets.
It does not construct the missing finite-$q$ tensor vertex or polarization
ports. It also does not replace the source physical period pairing away from
the Gram comparison already closed in Entry 2436.

## Durable evidence

- `research/benincasa/check_weighted_gram_rank60_base_change.py`;
- `research/benincasa/weighted-gram-rank60-base-change.json`;
- Entries 2413, 2416, 2419, and 2436;
- sequence claim `seqclaim-d4bcd7279d0c55c8293b1e7f`.

## Next falsifier

Audit the same interaction module at the remaining independently frozen
Landau and total-energy intersections. Separate formally étale transport
from supported nearby-cycle terms. Any new kernel must be located on an
existing support component or qualify as the hard H2 falsifier.
