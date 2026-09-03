# Boundary-occurrence automorphisms act on matching objects

## Question

When a decorated boundary has repeated occurrences, must a rewrite preserve the full occurrence action on matching data, or is preservation of the orbit quotient sufficient?

## Claim boundary

This packet treats a finite external permutation symmetry of a discrete occurrence index. It distinguishes external presentation automorphisms from automorphisms internal to the index category. It does not assert that occurrence permutations are physical symmetries or authorize quotienting without source-derived equivalence.

## Induced action

Let a boundary presentation have two discrete occurrences \(p_1,p_2\) with the same carrier constraint set

\[
X=\{0,1\}.
\]

Because the occurrences are discrete, its matching object is

\[
M=X\times X.
\]

The nontrivial boundary-presentation automorphism exchanges \(p_1\) and \(p_2\). Reindexing the boundary diagram induces the matching-object action

\[
s(x_1,x_2)=(x_2,x_1).
\]

The identity and \(s\) satisfy the \(S_2\) action laws. If joint sections are also \(X^2\) and the matching map is identity, then the same swap on joint sections makes the matching map equivariant.

This external action is not the same construction as putting an isomorphism \(p_1\cong p_2\) inside the index category. An internal identity-valued isomorphism would impose a compatibility equation in the limit and retain only the diagonal. The boundary certificate must state which construction is intended.

## Orbit quotient and fixed points

The full matching object has four elements. Its orbit quotient under the swap has three elements:

\[
\{(0,0)\},
\quad
\{(1,1)\},
\quad
\{(0,1),(1,0)\}.
\]

The fixed-point subset has two elements, \((0,0)\) and \((1,1)\). Thus

\[
|M|=4,
\qquad
|M/S_2|=3,
\qquad
|M^{S_2}|=2.
\]

These are three different typed objects.

## Hostile quotient fixture

The orbit projection

\[
q:M\to M/S_2
\]

is invariant under the swap but not injective: \((0,1)\) and \((1,0)\) have the same orbit record. The mixed orbit has multiplicity two. Therefore preserving only orbit-valued records does not preserve occurrence-resolved matching fibers or reconstruct the full matching datum.

A quotient may be lawful when the source declares occurrence exchange as an admitted equivalence. Without that declaration, replacing \(M\) by \(M/S_2\) silently erases route or port occurrence information.

## Rewrite criterion

For an occurrence-sensitive reversible rewrite, the induced matching-object isomorphism must be equivariant with respect to the transported boundary automorphism groups:

\[
\alpha_M(g\cdot m)=\varphi(g)\cdot\alpha_M(m),
\]

where \(\varphi\) is the group isomorphism induced by the boundary-index equivalence. Orbit-quotient preservation is weaker and cannot replace this equation.

## Disposition

Boundary-presentation automorphisms induce an action on matching objects. Reversible decorated rewrites must transport that action equivariantly. Orbit quotients and fixed points require separate source-authorized constructions; neither is the occurrence-resolved matching object.
