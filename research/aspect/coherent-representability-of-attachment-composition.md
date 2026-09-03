# Coherent representability of attachment composition

## Question

When do pointwise representing lift attachments assemble into a contravariant pseudofunctor under composition of system maps?

## Claim boundary

This packet derives the compositor and unit from representable lift profunctors and states their coherence gate. It does not claim strict functoriality when the source correspondence semantics is bicategorical.

## Represented lift profunctors

For a system map \(f:M\to N\), suppose

\[
P_f(E,D)
\cong
\operatorname{Hom}_{\operatorname{Att}(M)}(E,f^*D)
\]

naturally in source attachment \(E\) and target attachment \(D\).

For composable maps

\[
L\xrightarrow{g}M\xrightarrow{f}N,
\]

profunctor composition gives

\[
(P_g\odot P_f)(F,D)
=
\int^{E}
P_g(F,E)\times P_f(E,D).
\]

Substituting the representations and applying co-Yoneda yields

\[
(P_g\odot P_f)(F,D)
\cong
\operatorname{Hom}(F,g^*f^*D).
\]

If the correspondence semantics supplies a compositor

\[
P_g\odot P_f\xrightarrow{\sim}P_{fg},
\]

then Yoneda induces a unique natural isomorphism

\[
c_{g,f}:g^*f^*
\xrightarrow{\sim}
(fg)^*.
\]

This comparison is derived from lift composition; it is not an arbitrary identification of equal-sized attachment fibers.

## Unit comparison

If the identity-map lift profunctor is coherently isomorphic to the hom profunctor, representability gives

\[
u_S:\operatorname{id}_{\operatorname{Att}(S)}
\xrightarrow{\sim}
(\operatorname{id}_S)^*.
\]

The direction may be reversed by convention, but it must be fixed globally.

## Pentagon and triangle gates

For three composable system maps, the two composites from

\[
h^*g^*f^*
\]

to

\[
(fgh)^*
\]

must agree. This is the pseudofunctor pentagon inherited from the associator and compositor of profunctor composition. The unit comparisons must satisfy the two triangle identities.

Pointwise representability does not imply these equations. Arbitrarily choosing representatives or automorphisms can introduce a nontrivial coherence defect even though every individual lift presheaf is representable.

## Automorphism-valued defect

When representing attachments have automorphism group \(A\), changing compositors by elements

\[
c(f,g)\in A
\]

obeys the pentagon exactly when \(c\) is a normalized two-cocycle:

\[
c(g,h)+c(f,g+h)
=
c(f,g)+c(f+g,h)
\]

in an additive central example. A noncocycle choice is an explicit obstruction to pseudofunctorial attachment transport.

## Finite diagnostic

A discrete finite attachment category verifies the co-Yoneda composition: the intermediate representing attachment is the unique object contributing to the coend, and direct and represented composite supports agree.

A one-object attachment groupoid with central automorphism group \(C_2\) is placed over a \(C_3\) composition group. Zero compositor twists satisfy every unit and pentagon equation. A twist supported only at the pair \((1,1)\) violates the pentagon on explicit triples, despite leaving every pointwise representative unchanged.

## DPC cycle

### Governing conjecture

Representable lift correspondences assemble coherently because the source profunctor compositor and unit, transported through universal elements by Yoneda, uniquely determine the pullback compositor and unit. The mechanism is hard to vary: removing source-cell coherence removes the only construction forcing the pentagon.

### Rivals

1. Pointwise representability alone forces coherent composition, regardless of comparison choices.
2. Any failure is detectable from witness cardinalities, so automorphism actions add no obstruction.
3. Pointwise representatives exist, but an automorphism-valued compositor twist creates a genuine cocycle obstruction.

### Risky consequences

The governing conjecture predicts that co-Yoneda identifies composite supports, coherent zero twists satisfy every pentagon, and a noncocycle twist can violate the pentagon without changing any representing object or support cardinality. Rival 1 forbids the last behavior; rival 2 predicts that unchanged cardinalities cannot conceal a defect.

### Falsification attempt

The finite test retained identical pointwise representatives over a C3 composition group and introduced a normalized C2-valued twist supported at one pair. It exhaustively checked all triples. Four pentagon equations failed while coend supports and representative cardinalities remained unchanged.

### Residual

The fixture treats a central finite automorphism group. Noncentral actions and general bicategorical associators require the corresponding nonabelian coherence equations.

### DPC disposition

Rivals 1 and 2 are rejected. Rival 3 survives and refines the governing conjecture: representability yields a pseudofunctor only when source compositors induce cocycle-coherent Yoneda comparisons. This statement is provisionally retained within the stated central finite fixture and supported generally by the co-Yoneda derivation.

## Disposition

Representable lift correspondences assemble into contravariant pullback pseudofunctors only when the profunctor compositor and unit induce coherent Yoneda comparisons. The compositor is canonical once those source cells and universal elements are fixed. Automorphism-valued noncocycles are the exact residual obstructing coherence.
