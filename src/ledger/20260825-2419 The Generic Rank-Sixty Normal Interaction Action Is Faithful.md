---
author: marici.Benincasa
date: 2026-08-25
---

# 2419 — The Generic Rank-Sixty Normal Interaction Action Is Faithful

## Inputs

Entries 2413 and 2416 independently derive the interaction action on the two
diagonal pieces of the generic five-pole localization system:

\[
0\longrightarrow H_{\rm low}^{(34)}
\longrightarrow H_5^{(60)}
\longrightarrow H_{q_G}^{(26)}
\longrightarrow0.
\]

The lower action is faithful on the rank-seven source interaction module.
The restricted action is faithful on its rank-six pullback, whose only new
relation is the principal Cartier kernel.

Sequence claim: `seqclaim-1d9451998083d59471b74b28`.

## Strict normal compatibility

The fifth source pole is

\[
q_{\mathcal G_{12}}=c+X_1+X_2+X_3.
\]

It is independent of all three nonhomogeneous normals:

\[
\boxed{
\partial_{\nu_i}q_{\mathcal G_{12}}=0,
\qquad i=1,2,3.
}
\]

Consequently normal multiplication by every coefficient of
\(K^{-1}\partial_{\nu}K\) commutes strictly with localization and residue on
the source twisted de Rham complex.  The statement extends Entry 700 from
the square-free second-normal labels to the complete finite tower of Entry
2400.

In particular, the rank-thirty-four lower system is an invariant subobject
for the normal interaction action.  No choice of splitting of the
rank-sixty extension is needed to state this.

## Rank sandwich

Let \(\mathcal I^{(7)}\) be the correctly quotiented source interaction
module.  Entry 2413 gives an injective action

\[
\mathcal I^{(7)}\hookrightarrow
\operatorname{End}(H_{\rm low}^{(34)}).
\]

Because \(H_{\rm low}\) embeds as an invariant subobject of \(H_5\), the
full action has rank at least seven.  It factors through the rank-seven
source module, so it has rank at most seven.  Therefore

\[
\boxed{
\operatorname{rank}
(\mathcal I^{(7)}\to\operatorname{End}H_5^{(60)})=7.
}
\]

Equivalently,

\[
\boxed{
\ker
(\mathcal I^{(7)}\to\operatorname{End}H_5^{(60)})=0.
}
\]

The off-diagonal normal connection block may encode a nonsplit extension,
but it cannot erase an interaction class already visible on the invariant
lower subobject.

## Restricted compatibility

The quotient action has rank six, and the restriction map has exact kernel

\[
\langle c^2-E^2\rangle
=\langle(c-E)q_{\mathcal G_{12}}\rangle.
\]

Thus the diagonal actions and their source restriction fit the same
localization sequence.  No unexplained rank discrepancy remains at the
generic algebraic interaction level.

## Result

\[
\boxed{
\text{the generic rank-sixty five-pole direct image is faithful on the
complete rank-seven nonhomogeneous scalar interaction module.}
}
\]

This is the first direct-image-level contextual-faithfulness theorem for the
source-derived interacting scalar kernel.  It is stronger than a rank census
and weaker than physical observability.

## Classification

- generic five-pole cohomology rank: sixty;
- source interaction rank: seven;
- full normal interaction action rank: seven;
- algebraic interaction kernel: zero;
- residue restriction kernel: one principal Cartier line;
- off-diagonal extension: may be nontrivial but cannot create a kernel;
- new Carrier datum: none.

## Scope

The theorem concerns the normal interaction action, not the complete
connection matrices in every base direction.  It does not construct the
physical six-scale relative cycle, contact-weighted finite-q transfer
matrix, tensor vertex, or polarization ports.

## Durable evidence

- Entries 700, 702, 2400, 2413, and 2416;
- `research/benincasa/check_rank60_interaction_action_faithfulness.py`;
- `research/benincasa/rank60-interaction-action-faithfulness.json`.

## Next falsifier

Pull the source-derived physical relative cycle into the generic six-scale
family and evaluate the seven interaction classes through the complete
admissible scalar score/marked-wall port family.  Algebraic injectivity does
not imply physical contextual faithfulness: the remaining possible kernel
is a readout kernel, not a direct-image kernel.