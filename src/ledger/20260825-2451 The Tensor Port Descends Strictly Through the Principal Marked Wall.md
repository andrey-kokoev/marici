---
author: marici.Benincasa
date: 2026-08-25
---

# 2451 — The Tensor Port Descends Strictly Through the Principal Marked Wall

## Question

The parity-even tensor trace is an element of the generic rank-seven
interaction module.  Does localization at

\[
q_{\mathcal G_{12}}=c+E=0
\]

create an additional tensor kernel or a new supported class?

Sequence claim: `seqclaim-222a748f82e0e30d1f4875ce`.

## Frozen localization map

Entry 2416 independently derived the complete source quotient

\[
\mathcal I_{\rm low}^{(7)}\longrightarrow\mathcal I_{q_G}^{(6)}
\]

with the single principal kernel

\[
\boxed{
D_3-E^2U=c^2-E^2=(c-E)(c+E).
}
\]

No tensor-dependent relation is added to this map.

## Exact tensor restriction

Let (Q_1^{\rm even}=Y_1^2-Z_1^2) be Entry 2445's physical tensor
multiplier.  Its unique coordinates in

\[
(L_1,L_2,L_3,D_1,D_2,D_3,U)
\]

were derived before restriction.  On (c=-E), apply the frozen quotient
rule

\[
D_3\longmapsto E^2U.
\]

The resulting six coordinates agree coefficientwise with an independent
solve of (Q_1^{\rm even}|_{c=-E}) in

\[
(L_1|_{c=-E},L_2|_{c=-E},L_3|_{c=-E},D_1,D_2,U).
\]

Both source matrices have their expected ranks:

\[
\operatorname{rank}\mathcal I_{\rm low}=7,
\qquad
\operatorname{rank}\mathcal I_{q_G}=6.
\]

Hence the tensor multiplier creates no additional kernel.

## Residue compatibility

The multiplier is regular in the marked normal direction and obeys

\[
Q_1^{\rm even}-Q_1^{\rm even}|_{c=-E}
=(c+E)Q_{1,\perp}
\]

with no (c+E) denominator.  Therefore Poincare residue commutes strictly:

\[
\boxed{
\operatorname{Res}_{q_G}
\bigl(Q_1^{\rm even}\omega\bigr)
=
Q_1^{\rm even}|_{q_G}
\operatorname{Res}_{q_G}(\omega).
}
\]

The Ward endpoint score is a coefficient in the external momenta and obeys
the same restriction identity.  Thus no extra marked-wall homotopy is
required at this grade.

## Result

\[
\boxed{
\text{the physical tensor port descends through the existing principal
marked-wall localization sequence without additional kernel.}
}
\]

This is strict compatibility of the source module and residue map.  It is
not inferred from the equality of ambient and restricted ranks.

## Classification

- ambient interaction rank: seven;
- restricted interaction rank: six;
- marked-wall kernel: the predeclared principal Cartier line;
- additional tensor kernel: zero;
- residue coherence defect: zero;
- new Carrier support: none.

## Durable evidence

- `research/benincasa/check_tensor_marked_wall_localization.py`;
- `research/benincasa/tensor-marked-wall-localization.json`;
- Entries 2416 and 2445.

## Scope and next falsifier

This does not compute the total-energy nearby cycle or its intersection with
elliptic and Landau degeneration.  The next finite test is to transport the
same parity-even tensor class through (E_T=0), retaining the Kummer/Tate
split and the second normal grade.
