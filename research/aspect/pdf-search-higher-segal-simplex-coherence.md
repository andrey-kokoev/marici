# PDF search: coherent simplices and higher Segal structure

## Question

Which indexed references give a precise mathematical interpretation of simplex coherence suitable for organizing the analytical tetrahedron cells?

## Search execution

The page index was rebuilt before searching:

```text
pnpm pdf:search -Rebuild
Indexed 4287 PDF pages
```

Exact phrase searches for `simplex coherence`, `simplex coherencies`, `coherent simplex`, and `simplicial coherence` returned no matches. Proximity and structural searches found the relevant vocabulary under higher Segal spaces, homotopy-coherent diagrams, simplicial identities, associators, and Segal simplices.

## Primary match

`references/1212.3563v1.pdf`, *Higher Segal Spaces I*, is the closest structural source.

- Page 1: a `d`-Segal space is a simplicial space whose locality conditions are indexed by triangulations of cyclic polytopes. The paper develops the `d=2` case and describes higher coherences rather than one chosen decomposition.
- Page 12: the face and degeneracy maps satisfy the simplicial identities. These are the first executable compatibility laws for any cell registry presented as a simplicial object.
- Page 14: homotopy-limit data are organized by paths for composable pairs, triangles for composable triples, tetrahedra for composable quadruples, and analogous fillers for every longer chain. A tetrahedron restricts to the four prescribed triangular faces.
- Pages 45–48: a 2-Segal object produces a multivalued composition span, an associator, unitors, and Mac Lane coherence. The associator is constructed from the 3-simplex object `X3`; triangulations give canonically connected bracketings.
- Page 67: two even 2-faces determine a 3-simplex in the stated discrete 2-Segal setting; its odd 2-faces define two binary operations satisfying identities equivalent to the pentagon equation.
- Page 114: homotopy-coherent diagrams are maps from a simplicial resolution into a complete 1-Segal space.
- Page 179: a Segal simplex is characterized by requiring the Segal cone of every subsimplex of dimension at least two to be a limit diagram.
- Pages 190 and 211: 3-simplex extension and tetrahedral compatibility conditions appear explicitly in span and higher-morphism constructions.

## Secondary matches

- `references/1512.07573v4.pdf`, page 11: the coherent nerve presents the simplicially enriched category of Kan complexes as an infinity-category.
- `references/1011.5676v2.pdf`, pages 6–7: coherent intertwiners on the boundary of a flat 4-simplex and coherent phase cancellation. This is physically suggestive but does not provide the categorical filler laws needed by SCC.
- `references/A_Discrete_and_Coherent_Basis_of_Intertwiners.pdf`, pages 2 and 7: discrete and coherent tetrahedral intertwiner bases share a semiclassical framed-tetrahedron interpretation. This supplies representation-theoretic examples, not a general coherence compiler.

## SCC interpretation

The useful replacement for informal “coherent tetrahedron” language is:

1. objects and edges form the low simplicial degrees;
2. each triangular analytical comparison is a 2-simplex;
3. each tetrahedral coherence is a 3-simplex with four typed face restrictions;
4. face and degeneracy maps must satisfy simplicial identities;
5. competing composites are compared through 2-Segal triangulation maps;
6. a global claim requires these maps to be equivalences on the declared carrier, not merely equality of scalar readouts;
7. higher packets require fillers for every longer composable chain.

This gives a concrete schema test for the repository's hundreds of analytical cells: register each cell by simplicial degree and boundary, then verify horn filling and triangulation comparison rather than assigning coherence from nomenclature.

## Claim boundary

The PDF evidence supplies abstract coherence architectures. It does not identify any Marici analytical carrier with a 2-Segal space, prove that its horn fillers exist, or promote the current coherence-pyramid registry. Those require explicit source-derived face maps, degeneracies, filler maps, and equivalence certificates.

## Disposition

The closest mathematical enrichment is higher Segal structure, especially the 2-Segal associator obtained from `X3`. The immediate executable follow-up is a conservative simplicial registry for existing Aspect cells, with no promotion until all face restrictions and the relevant triangulation comparison are supplied.
