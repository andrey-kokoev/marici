# Decorated boundary-index transport for probe rewrites

## Question

What additional data replaces automatic proper-face transport when face categories have automorphisms, repeated occurrences, or geometric decorations?

## Claim boundary

This packet gives sufficient typed boundary-transport data for the matching-object construction and a finite counterexample showing that abstract category equivalence alone is insufficient. It does not assert minimality among all equivalent categorical presentations or infer physical equivalence from decorated transport.

## Boundary presentation

For an object \(\sigma\in\mathcal C\), do not define its boundary merely as an object predicate. Supply a boundary presentation

\[
(\mathcal I_\sigma,j_\sigma,\lambda_\sigma),
\]

where:

- \(\mathcal I_\sigma\) is the category of boundary occurrences;
- \(j_\sigma:\mathcal I_\sigma\to\mathcal C\) sends an occurrence to its carrier face;
- \(\lambda_\sigma:j_\sigma\Rightarrow\Delta\sigma\) is the incidence cone.

Occurrences are retained even when two objects of \(\mathcal I_\sigma\) have the same carrier. This prevents automorphisms or repeated faces from being erased by object-level quotienting.

For a presheaf \(F:\mathcal C^{op}\to\mathbf{Set}\), the matching object is the limit of the boundary diagram obtained by restricting \(F\) along \(j_\sigma^{op}\). The matching map is induced by applying \(F\) to the incidence cone.

## Transport package

Let \(E:\mathcal C\simeq\mathcal D\), choose \(u:E\sigma\mathrel{\cong}\sigma'\), and let \((\mathcal I'_{\sigma'},j'_{\sigma'},\lambda'_{\sigma'})\) be the target boundary presentation. A boundary transport consists of:

1. an equivalence \(e:\mathcal I_\sigma\simeq\mathcal I'_{\sigma'}\);
2. a natural isomorphism

\[
\kappa:E j_\sigma\mathrel{\cong}j'_{\sigma'}e;
\]

3. incidence coherence: for each boundary occurrence, the route through \(E(\lambda_\sigma)\), followed by \(u\), equals the route through \(\kappa\) and \(\lambda'_{\sigma'}\).

Together with a presheaf natural isomorphism \(\eta:F\cong G E^{op}\), these data induce an isomorphism of boundary diagrams. Reindexing along \(e\) and taking limits then constructs the matching-object isomorphism. Incidence coherence makes its conjugacy with the matching maps follow from the same projection calculation as in the thin case.

## Counterexample without boundary transport

Take a category with objects \(a,b,\sigma\), nonidentity arrows \(a\to\sigma\) and \(b\to\sigma\), and no relation between \(a\) and \(b\). Use the identity category equivalence and the identity presheaf comparison, but choose source boundary index \(\{a\}\) and target boundary index \(\{b\}\). Let

\[
F(a)=\{0,1\},
\qquad
F(b)=\{*\}.
\]

The source and target matching objects then have cardinalities two and one. The ambient category equivalence and presheaf isomorphism are exact identities, yet no matching-object isomorphism exists. The missing datum is precisely an equivalence of the selected boundary presentations compatible with their carriers and incidences.

## Consequence

For decorated Interaction Nets, rewrite certificates must transport boundary occurrences and incidence maps, not only node objects or ambient categories. An automorphism of the ambient category is insufficient if it does not preserve the declared occurrence-indexed boundary.

## Disposition

The thin-skeletal hypothesis can be removed by making boundary presentation and transport explicit. The sufficient package is \((e,\kappa,u)\) plus incidence coherence. Untyped boundary selection is rejected by a finite cardinality counterexample.
