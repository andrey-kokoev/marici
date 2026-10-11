# Existing tetrahedral equalities versus the Wolfram expression

Actor: marici.Voevodsky. Date: 2026-10-06. Textual comparison only; no new Agda theorem or compilation claimed.

## Source equations, without choosing new boundary data

`research/nima/agda/MarkedTetrahedronCoherence.agda`, module `Tetrahedra.Over`, supplies the following dictionary. `RetainedTetrahedralPackage.agda` packages the same boundary and preserves it under completion.

| Cell | Actual type/equation |
| --- | --- |
| Four vertices | x0, x1, x2, x3 in a common type X |
| Six edges | eij : xi = xj, for i < j |
| Face 012, alpha | e01 composed with e12 = e02 |
| Face 123, beta | e12 composed with e23 = e13 |
| Face 013, gamma | e01 composed with e13 = e03 |
| Face 023, delta | e02 composed with e23 = e03 |
| Interior | Equality between the two pasted face routes from (e01 composed with e12) composed with e23 to e03 |

Write a dot for path composition, star for whiskering, and a for the reassociation path from (e01 dot e12) dot e23 to e01 dot (e12 dot e23). Then the exact filler equation is

\[
(\alpha * e_{23})\cdot\delta
=
a\cdot\bigl((e_{01}*\beta)\cdot\gamma\bigr).
\]

Given alpha, beta and gamma, completion constructs delta and this equality. At the level of path algebra, the missing face is obtained by solving

\[
\delta=(\alpha*e_{23})^{-1}\cdot
\bigl(a\cdot((e_{01}*\beta)\cdot\gamma)\bigr).
\]

The code uses the equivalence `route023` and its contractible fiber, rather than asserting this displayed expression is its definition. The supplied four-face boundary need not have a filler if its selected fourth face is incompatible. Solving a three-face horn and filling an arbitrary prescribed surface are distinct operations.

`TetrahedronPresentationBridge.agda` compares this marked route equation with a cubical/pathover presentation, including the fourth face. That changes presentation, not the underlying logical operation into NAND.

## What the Boolean construction supplies

`QBooleanity.agda` constructs joint refutation N(A,B) = (A × B) → empty and proves W(A,B,C) equivalent to double negation of C. Its Boolean domain is `StableTruth`, the set of small stable propositions. The code explicitly proves `set-stable-truth`.

Path composition and NAND have different signatures and laws. Composition is a dependent operation on matching endpoints and has identity/cancellation/coherence structure. NAND is a binary operation on truth objects and is not associative. In particular, replacing each dot in the filler equation by NAND is not a typed interpretation.

## Test the direct interpretations

1. **Vertices are stable truth objects.** Six supplied paths require the four vertices to be equal as stable truths. Because `StableTruth` is a set, its path types are propositions and higher coherence between existing paths has no independent Boolean operation content. This cannot represent four independent Boolean atoms.
2. **Vertices remain retained states and are mapped to stable truths.** A map carries paths to paths; endpoints connected by an edge have equal images. The image tetrahedron again compares equality witnesses. It does not thereby produce joint refutation on three independently varying propositions.
3. **Truth questions are predicates about retained cells or routes.** This can retain a substantive connection: interpret cell-existence, compatibility, or recoverability questions by stable propositions and construct operations on those questions. But the actual predicate assignment and its behavior on constructors must be supplied and checked. Neither of the first two interpretations supplies it automatically.

Thus the directly available correspondence is tetrahedral coherence to equality coherence in the Boolean domain, not to Wolfram's NAND equation. This is a limitation of these interpretations, not a refutation of every possible retained-question interpretation.

## A separating example

Take the ordinary two-point set as X. It admits the generic path-coherence/horn-completion construction. On that same set put the binary operation x | y = y. For this operation the Wolfram left-hand side is a, so the axiom fails whenever a differs from c. Generic tetrahedral completion therefore cannot force the Wolfram axiom for an unconstrained additional binary operation.

This example does not refute the constructed joint-refutation NAND, whose semantic definition supplies additional structure. It isolates the missing condition: the proposed Boolean operation must be related to the cell constructors, rather than placed on the same carrier and presumed to inherit their laws.

## Exact remaining identification

To make Wolfram a filler formula, identify three independently variable questions A, B and C on the existing retained boundary; give the constructor interpretation that sends their joint refutation to the relevant cell operation; and show that the resulting filler question has the nested type

\[
N(N(N(A,B),C),N(A,N(N(A,C),A))).
\]

Then compare completion with the already proved double-negation recovery maps. Neither the four-channel count nor the six NAND occurrences establishes this assignment. No tetrahedron chosen using an already supplied Wolfram proof should be counted as a derivation of that proof.

The source-level audit establishes the exact filler equation and rejects a direct path-composition-to-NAND substitution. It leaves the retained-question interpretation open. Relevant prior sources are `RetainedNandPhases.agda`, `RetainedTetrahedralPackage.agda`, `MarkedTetrahedronCoherence.agda`, and `TetrahedronPresentationBridge.agda`.
