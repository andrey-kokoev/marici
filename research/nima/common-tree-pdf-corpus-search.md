# Indexed-PDF search for common-tree shellability clues

## Method

Searched the repository's indexed corpus with `pnpm pdf:search`, using literal and related terms:

- `subword complex`, `shellable`, `vertex decomposable`;
- `biadjoint`, `double partial`, `common triangulation`;
- `associahedron`, `associahedra`, `cluster complex`, `noncrossing`;
- `triangulations`, `flip`, `subdivision`, `contractible`;
- `regular triangulation`, `secondary polytope`, `Gröbner`.

The index currently contains 30 PDFs. Most concern derived/analytic geometry; the combinatorially relevant items are Dyckerhoff--Kapranov's higher Segal-space paper (`1212.3563v1.pdf`), cosmological-polytope papers, and a recent paper on triangulations of cosmological polytopes.

## Negative result

The corpus contains no matches for:

- `subword complex`;
- `shellable`;
- `vertex decomposable`;
- `biadjoint`;
- `double partial`;
- `common triangulation`;
- `cluster complex`;
- `noncrossing`.

Thus it does not contain the Knutson--Miller or Ceballos--Labbé--Stump machinery found in the external prior-art search, nor an indexed theorem directly addressing common triangulations of two cyclic orders.

## Useful clue: polygonal subdivision locality

`1212.3563v1.pdf` develops 2-Segal spaces using polygonal subdivisions. Relevant passages include:

- p. 9: derived membrane spaces are weakly independent of triangulation;
- pp. 25--27: polygonal subdivisions and acyclic diagrams, with contractibility proved through subdivision posets of normal cones;
- p. 43: induction by cutting a polygon along an internal edge into two smaller polygons;
- p. 47: the pentagon coherence is organized by the poset of all polygonal subdivisions;
- pp. 61--63: a polygonal subdivision yields cooperadic decomposition maps.

This does not prove shellability, but it supports a different proof architecture: organize common partial triangulations by their subdivision poset rather than by greedy facet deletion. The cut/glue product already proved for common trees is precisely the local decomposition expected in a 2-Segal/decomposition-space framework.

The potentially useful target is therefore the poset of common polygonal subdivisions. If its lower fibers or relevant refinement categories are contractible, Quillen-type fiber arguments could prove contractibility of every proper common-tree complex without constructing a shelling. This would establish the homotopy-ball side, though not PL-ball or shellability by itself.

## Secondary clue: regular triangulations and initial ideals

`Triangulations of cosmological polytopes - alco.430.pdf` studies regular unimodular triangulations via Gröbner bases and explicitly characterizes facets from initial monomials. This is not about associahedral common trees, but suggests a stronger possible route:

1. realize the common-tree complex as a regular triangulation or initial complex of a point configuration;
2. obtain shellability from regular/coherent triangulation theory;
3. identify boundary versus sphere geometrically.

No indexed passage supplies such a realization for intersections of cyclic planarity constraints. This is a methodological clue only.

## Assessment

The local PDF corpus does not contain the missing lemma. Its best contribution is to redirect the induction toward the **poset of common subdivisions**:

> prove that common-subdivision refinement fibers decompose over cut regions and are contractible, then use a Quillen/nerve argument.

This route aligns with the arbitrary-n cut/glue theorem and avoids the falsified maximal-free-ridge implication. For the stronger shellable-ball conclusion, external subword-complex or coherent-triangulation machinery remains more promising.
