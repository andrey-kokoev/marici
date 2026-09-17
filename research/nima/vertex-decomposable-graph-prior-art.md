# Vertex-decomposable graph prior art for common-tree complexes

## Sources inspected

1. Baker, Vander Meulen, and Van Tuyl, **Shedding vertices of vertex decomposable well-covered graphs**, arXiv:1606.04447.
2. Bıyıkoğlu and Civan, **Vertex-decomposable graphs, codismantlability, Cohen--Macaulayness, and Castelnuovo--Mumford regularity**, arXiv:1205.5631 / Electron. J. Combin. 21 (2014), DOI 10.37236/2387.
3. Woodroofe, **Vertex decomposable graphs and obstructions to shellability**, Proc. AMS 137 (2009), DOI 10.1090/S0002-9939-09-09981-X.

Local copies and extracted text are under `research/nima/prior_art/`.

## Exact graph translation confirmed by prior art

For a graph `G`, pure vertex-decomposability of `Ind(G)` is equivalent to recursive pure vertex-decomposability of `G`:

- `G` is well-covered;
- choose a shedding vertex `x`;
- recurse on `G-x` and `G-N[x]`.

Bıyıkoğlu--Civan Definition 5 gives the useful exchange criterion:

> `x` is shedding iff every independent set in `G-N[x]` can be enlarged by some neighbor of `x`.

For a well-covered graph this agrees with extendability: `G-x` remains well-covered with the same independence number. This is exactly the common-channel universal-flip criterion already derived.

## Known sufficient classes do not contain the general overlap graphs

The literature proves vertex-decomposability for important families:

- well-covered chordal graphs;
- well-covered bipartite or very-well-covered graphs under additional conditions;
- certain girth-at-least-five graphs built from pendant edges and basic 5-cycles;
- `(C4,C5,C7)`-free well-covered graphs via codismantlability;
- graphs obtained by clique whiskering and related expansions.

Common-interval overlap graphs are not generally in these classes. Full polygon crossing graphs already contain induced `C4`, `C5`, and `C7`, have no pendant-edge decomposition, and the six-point recursive obstruction is not codismantlable by neighborhood inclusion.

The special role of `C7` in the literature exactly matches the restriction counterexample found computationally: `C7` is well-covered but not vertex-decomposable, while `C5` is vertex-decomposable.

## Useful negative criterion

Pure vertex-decomposable complexes are Cohen--Macaulay and have nonnegative `h`-vectors. Baker--Vander Meulen--Van Tuyl use negative `h`-vector entries to prove that candidate deletions are not vertex-decomposable. This gives an efficient obstruction test for proposed selector classes, but not an existence proof.

## Best remaining route

No inspected theorem implies vertex-decomposability for overlap graphs of common intervals. The prior art confirms that the needed statement is genuinely new unless these graphs can be identified with a known construction.

The most precise target is now:

> For the overlap graph `O(alpha,beta)` of all admissible common intervals, prove recursively that either it is edgeless or it has an extendable vertex `x` such that both `O-x` and `O-N[x]` retain the same structural class.

A proof must exploit closure properties of the **full common-interval family**. Arbitrary induced restrictions cannot be admitted because they include the `C7` obstruction. A promising definition is the smallest class containing full common-interval overlap graphs and closed only under deletion and closed-neighborhood deletion at extendable vertices. To make this noncircular, that class needs an independent description using the strong common-interval tree or quadrilateral exchange data.
