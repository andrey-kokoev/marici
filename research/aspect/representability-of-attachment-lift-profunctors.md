# Representability of attachment-lift profunctors

## Question

When does correspondence-valued attachment transport reduce to an ordinary contravariant pullback functor?

## Claim boundary

This packet gives the universal-element criterion for one lift profunctor and classifies finite deletion, branching, and symmetry examples. It does not assert that every optical correspondence is representable.

## Lift presheaf

For an optical-network map \(f:M\to N\), the lift profunctor is

\[
P_f:
\operatorname{Att}(M)^{op}\times
\operatorname{Att}(N)	o\mathbf{Set}.
\]

Fix \(D\in\operatorname{Att}(N)\). Then

\[
P_f(-,D):\operatorname{Att}(M)^{op}\to\mathbf{Set}
\]

is the presheaf of compatible lifts of \(D\).

An ordinary pullback attachment \(f^*D\) exists exactly when this presheaf is representable: there is an attachment \(R\in\operatorname{Att}(M)\) and natural bijections

\[
P_f(E,D)
\cong
\operatorname{Hom}_{\operatorname{Att}(M)}(E,R)
\]

for every \(E\).

## Universal lift criterion

Representability is equivalent to a universal lift

\[
u\in P_f(R,D)
\]

such that

\[
\operatorname{Hom}(E,R)
\longrightarrow P_f(E,D),
\qquad
h\longmapsto P_f(h,D)(u)
\]

is bijective for every \(E\). Equivalently, \((R,u)\) is terminal in the category of elements of \(P_f(-,D)\).

The representing attachment is unique up to unique isomorphism. Choosing one representative is presentation; the universal property supplies the authority.

## Finite discrete classification

If \(\operatorname{Att}(M)\) is discrete, then

\[
\operatorname{Hom}(E,R)
\]

is a singleton for \(E=R\) and empty otherwise. Therefore:

- unique singleton support is representable;
- empty support from deletion is not representable;
- support on two branch attachments is not representable.

Thus ordinary pullback is recovered exactly at the unique-lift locus in the discrete finite model.

## Automorphism-rich fibers

Cardinality alone does not decide representability in a non-discrete attachment category. If \(R\) has nontrivial automorphisms, then

\[
P_f(R,D)\cong\operatorname{End}(R)
\]

may contain several witnesses while remaining representable.

For a one-object attachment groupoid with automorphism group \(C_2\), the representable presheaf has two elements with the regular precomposition action. A two-element presheaf with the trivial \(C_2\) action has the same cardinality but is not representable. The action and naturality, not witness count alone, decide.

## Functorial recovery

If every \(P_f(-,D)\) is representable and representing objects are chosen coherently in \(D\), Yoneda transports the second-variable action to a functor

\[
f^*:\operatorname{Att}(N)\to\operatorname{Att}(M).
\]

For composable network maps, profunctor composition becomes ordinary functor composition when the representing choices respect the coend associator. Pointwise representability alone does not automatically supply this cross-map coherence.

## Disposition

Correspondence transport reduces to pullback precisely when each lift presheaf has a universal element. Deletion and unresolved branching obstruct representability in discrete fibers. Multiple symmetry-related witnesses can remain representable when they form the correct hom-set action. Coherent representability, not uniqueness by cardinality, is the exact gate for recovering indexed attachment functors.
