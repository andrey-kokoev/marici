# Prior-art clues for common-tree shellability

## Search scope

Searches used OpenAlex title/abstract indexing, repository-wide text search, and primary-source PDFs. Queries included:

- common/simultaneous polygon triangulations;
- induced subcomplexes of associahedra and cluster complexes;
- noncrossing complexes of permutations;
- subword complexes, shellability, balls, and spheres;
- Cambrian, biCambrian, Baxter-Cambrian, and accordion complexes.

Primary sources downloaded to `research/nima/prior_art/`:

1. Allen Knutson and Ezra Miller, **Subword complexes in Coxeter groups**, Adv. Math. 184 (2004), arXiv:math/0309259.
2. César Ceballos, Jean-Philippe Labbé, and Christian Stump, **Subword complexes, cluster complexes, and generalized multi-associahedra**, J. Algebraic Combin. 39 (2014), arXiv:1108.1776, DOI 10.1007/s10801-013-0437-x.

## Strongest clue: subword complexes

Knutson--Miller prove:

- every subword complex is vertex-decomposable and therefore shellable (Theorem 2.5);
- every subword complex is a topological ball or sphere (Theorem 3.7);
- it is a sphere exactly when the Demazure product of the defining word equals the target element, and otherwise a ball (Corollary 3.8);
- deletion and link at the first word position are again explicit subword complexes, which supplies the induction.

Ceballos--Labbé--Stump prove that finite-type cluster complexes are subword complexes. In type A, the ordinary polygon triangulation complex is therefore a spherical subword complex.

This matches the observed common-tree trichotomy almost exactly:

- no facets;
- full spherical type-A cluster complex;
- proper shellable ball.

It also supplies the kind of recursive selector our direct peeling argument lacks: delete the first position in a Coxeter word, updating the target according to whether left multiplication raises or lowers Coxeter length.

## Exact representation problem

For fixed `alpha`, the common-tree complex is the induced restriction of the type-A cluster complex to diagonals that are also planar for `beta`:

\[
K(\alpha,\beta)=\Delta_\alpha\vert_{D_\alpha\cap D_\beta}.
\]

The decisive question is whether this restriction is itself a subword complex `Delta(Q_{alpha,beta},w_{alpha,beta})`.

This does **not** follow merely from the fact that `Delta_alpha` is a subword complex:

- arbitrary induced restrictions of a subword complex need not be links;
- the forbidden diagonals need not form a face, so the restriction is generally not the link of their union;
- deleting arbitrary word positions is not the same as the first-position deletion used in the Knutson--Miller vertex decomposition.

A proof therefore needs an explicit word and facet bijection, not just matching topology.

## Most promising concrete route

Use the Ceballos--Labbé--Stump type-A word for the `alpha` cluster complex and encode the second cyclic order by the corresponding label permutation. Test whether the `beta`-forbidden diagonal positions can be moved, using subword-complex commutations and rotations, into a deletion sequence for which every intermediate deletion remains pure. If so, repeated Knutson--Miller deletion identifies the final induced restriction with a subword complex and immediately proves vertex-decomposability and the ball/sphere theorem.

Equivalent computational test:

1. construct the standard type-A cluster word `Q_alpha` and its position-to-diagonal map;
2. remove positions corresponding to diagonals not planar in `beta`;
3. search for an ordering of those removals such that each removal is a legal subword-complex deletion;
4. compare the resulting facets with the existing common-tree facets through `n<=9`;
5. infer the Coxeter-word pattern from the successful orders.

## Secondary clues

- Accordion complexes have shellable/polytopal behavior and unique-source/unique-sink flip orientations, but their compatibility rule is defined relative to one reference dissection. No source found identifies arbitrary intersections of two cyclic triangulation complexes with accordion complexes.
- Cambrian and biCambrian literature may encode the interaction of two orientations, but the searches did not locate a theorem directly matching common triangulations for arbitrary label permutations.
- Literature on noncrossing sets and Grassmann associahedra concerns different compatibility relations.

## Computational test of the inherited-word hypothesis

`check_common_tree_subword_representation.py` implements the type-A dictionary from Ceballos--Labbé--Stump Section 2.4. For every Coxeter-element ordering `c`, it:

1. constructs `Q=c w0(c)`;
2. maps word positions to polygon diagonals using their stated formula;
3. retains positions whose diagonals are also `beta`-planar;
4. asks whether the common facets are exactly the complements of reduced expressions of one Coxeter-group target.

The broadest direct inherited-word hypothesis already fails at five points. Allowing every Coxeter-element ordering gives:

- `n=4`: 3 of 3 order orbits represented;
- `n=5`: 11 of 12, including the one empty orbit;
- `n=6`: 49 of 60;
- `n=7`: 283 of 360.

The first nonempty failure is `beta=(0,2,1,3,4)`, whose common complex has two facets. That complex is abstractly a subword complex, but not by simply retaining its allowed diagonal positions in any standard `c w0(c)` realization.

Thus any subword proof needs a new word construction, braid/rotation transformations beyond changing `c`, or an abstract recognition theorem. Simple inherited restriction is falsified.

## Assessment

Subword complexes remain the strongest conceptual match because they provide exactly vertex-decomposable ball/sphere topology. But the obvious representation theorem is false. The viable refined target is:

> Construct a new word `Q_{alpha,beta}` and target `w_{alpha,beta}` whose reduced-subword complements are the common trees; do not require `Q_{alpha,beta}` to be the allowed-position restriction of a cluster word.

If such a construction exists, Knutson--Miller proves the arbitrary-n theorem immediately. Otherwise, their first-position deletion recursion remains a model for designing a direct recursive common-channel decomposition.
