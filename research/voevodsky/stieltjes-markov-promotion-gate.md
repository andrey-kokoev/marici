# Stieltjes Markov-composition promotion gate

## Question

Does the current Stieltjes source derive the factorization needed to promote the scalar Markov amalgamation constructor into the operating Green architecture?

## Claim boundary

This audit tests only the current bounded source packet. It does not assert that such a factorization is impossible or absent from every analytic realization.

## Required arrow

Promotion requires a source-derived factorization of nonadjacent cross Green returns through each intervening sector. In the scalar model this is

\[
r_{13}=r_{12}r_{23}.
\]

The operator-valued analogue needs typed domains, normalization, composition order, and a proof that the resulting full block Gram operator has the required positivity and radical behavior.

## Source audit

The current source does not state that theorem.

At line 231 it says: “Twisted Mellin equivariance should make the return prime diagonal. If so,”. The modal phrase “should” and the conditional “if so” mark an unproved expected property, not a derived factorization.

At line 258 the source explicitly lists a hostile branch: “Control diagonal prime returns but permit cross-prime coherent loading.” Prime-diagonal return control therefore does not eliminate the nonadjacent cross blocks needed by the composition theorem.

Neither statement supplies a Markov or conditional-independence identity for composite Green returns.

## First missing typed object

A theorem or source packet defining the relevant cross-return operators and proving their factorization through an intervening Green sector, with normalization and domain compatibility.

## Acceptance test

Given three composable Green sectors, materialize all three pairwise cross-return blocks and verify exactly that the nonadjacent block equals the typed composite of the adjacent normalized blocks. Then verify positivity and radical compatibility of the full joint block Gram operator. A prime-diagonal norm bound alone does not pass.

## Disposition

Promotion is blocked by absent source authority. The scalar Markov constructor remains a verified admissible model, not a property of the Stieltjes Green construction. This branch stops until the missing factorization theorem or a distinct source-derived completion law is supplied.

## Evidence

- `research/nima/the-stieltjes-incidence-closes-the-cyclic-prime-lift-but-not-its-enlarged-green-extension.md`, lines 231 and 258
- `research/voevodsky/markov-green-amalgamation-constructor.md`
- `research/voevodsky/results/stieltjes_markov_promotion_gate.json`
