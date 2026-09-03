# Finite local probe-rewrite theorem boundary

## Question

What exact rewrite claim is supported by the positive finite witness and the two independent countermodels?

## Claim boundary

This packet consolidates three executable finite results. It does not promote them to a general categorical theorem, SCC-wide soundness, global confluence, normalization, or physical equivalence.

## Demonstrated finite statement

For the tested full two-probe face system, let \(F\) and \(G\) be lawful finite constraint presheaves. The positive fixture supplies bijections on the joint and singleton constraint sets whose restriction squares commute. The induced coordinatewise bijection on matching data satisfies

\[
\mu_G\alpha_{pq}=\alpha_M\mu_F.
\]

For every matching datum \(m\) in the four-element matching set, the joint-component bijection restricts to a bijection

\[
\mu_F^{-1}(m)
\longrightarrow
\mu_G^{-1}(\alpha_M(m)).
\]

The exhaustive census includes occupied and empty fibers.

## Independent necessity tests

The naturality countermodel keeps equal object cardinalities and exhausts all eight objectwise bijection families. None is natural, and a matching fiber changes from cardinality one to zero.

The invertibility countermodel supplies a natural transformation for which every restriction square commutes, but its joint component collapses two sections to one. The unique matching fiber changes from cardinality two to one.

Thus the tested finite criterion has two independently necessary components:

1. naturality relates the objectwise maps to restriction structure;
2. invertibility makes the induced fiber transports reversible.

## General theorem target

The unproved generalization is: for a finite face system, a face-category equivalence together with a natural isomorphism of constraint presheaves transports the proper-face matching diagram, induces an isomorphism of matching objects, conjugates the matching maps, and therefore induces equivalences of corresponding fibers.

The missing proof step is not another finite fixture. It is a typed construction showing that the face equivalence transports the proper-face indexing category and that natural-isomorphism functoriality induces the matching-object isomorphism. This is the frozen Lean handoff target.

## SCC boundary

The candidate SCC checks cover configuration closure, restriction functoriality, matching-map typing, continuation multiplicity, rewrite naturality, and source identity. They do not currently encode or verify a general induced-limit isomorphism. A live rewrite certificate must therefore remain finite/explicit or provide the missing formal theorem.

## Disposition

The finite local audit is closed: the positive witness and both hostile countermodels agree on the natural-isomorphism boundary. Further finite examples would not strengthen the general claim. The next nonredundant research object is the induced matching-object isomorphism under transported proper-face diagrams.
