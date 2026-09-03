# Attachment sections and adjunction gates

## Question

When does instrument attachment define a functor, and when is that functor adjoint to the forgetful projection?

## Claim boundary

This packet treats attachment as a section of the Grothendieck projection. It does not claim that an arbitrary instrument choice is canonical, physically realizable, or freely generated.

## Functorial attachment

Let

\[
\operatorname{Att}:\mathcal S^{op}\to\mathbf{Cat},
\qquad
U:\int\operatorname{Att}\to\mathcal S.
\]

An attachment functor over the base is a section

\[
A:\mathcal S\to\int\operatorname{Att},
\qquad
UA=\operatorname{id}_{\mathcal S}.
\]

It consists of:

1. an attachment \(D_S\in\operatorname{Att}(S)\) for every system \(S\);
2. for every \(f:S\to T\), a comparison map

\[
\alpha_f:D_S\to f^*D_T;
\]

3. identity and composition coherence for the \(\alpha_f\), including the pseudofunctor coherence cells when reindexing is not strict.

A parameter \(P\) at one system supplies only one fiber object. It defines \(A_P(S)=(S,P)\) locally but does not define a functor on \(\mathcal S\). A family \((P_S)\) without the comparison maps is likewise insufficient.

## Free attachment

Suppose each fiber \(\operatorname{Att}(S)\) has an initial object \(0_S\). Define

\[
A_0(S)=(S,0_S).
\]

For every \(f:S\to T\), there is a unique map

\[
0_S\to f^*0_T,
\]

so these maps satisfy functorial coherence by uniqueness. The resulting section is left adjoint to \(U\):

\[
A_0\dashv U.
\]

Indeed, maps from \((S,0_S)\) to \((T,E)\) over a fixed \(f:S\to T\) correspond to maps \(0_S\to f^*E\), of which there is exactly one. Therefore projection induces a natural bijection

\[
\operatorname{Hom}_{\int\operatorname{Att}}(A_0S,(T,E))
\cong
\operatorname{Hom}_{\mathcal S}(S,T).
\]

Conversely, a normalized section \(A\) with identity unit and \(A\dashv U\) selects an initial object in every fiber: restrict the adjunction bijection to maps over \(\operatorname{id}_S\).

The word “free” is justified only by this universal property. It must not be applied to an arbitrary chosen apparatus.

## Cofree attachment

A right-adjoint section requires more. If each fiber has a terminal object \(1_S\) and every reindexing functor preserves the chosen terminal objects, then

\[
U\dashv A_1,
\qquad
A_1(S)=(S,1_S).
\]

For a map over \(f:S\to T\), uniqueness requires \(f^*1_T\) to be terminal in \(\operatorname{Att}(S)\). Fiberwise terminality without reindexing stability does not suffice.

## Separation of gates

Functoriality, left adjunction, and right adjunction are distinct:

- a coherent family defines a section;
- fiberwise initial objects define a free left-adjoint section;
- reindexing-stable terminal objects define a cofree right-adjoint section.

A noninitial coherent choice can be functorial while failing the free-attachment universal property.

## Finite witness

Use a two-object base poset and the attachment poset \(0<1\) in each fiber, with identity reindexing. Choosing \(0\) gives the left adjoint; choosing \(1\) gives the right adjoint. Both choices define sections. The hostile claim that the \(1\)-section is free fails because there is no vertical map \(1\to0\), although the corresponding base identity exists.

## Disposition

Instrument attachment is functorial exactly when attachment choices extend to a coherent section of \(U\). Canonical free attachment requires fiberwise initial attachments; an arbitrary parameterized instrument does not supply it. Cofree attachment additionally requires terminal choices stable under reindexing.
