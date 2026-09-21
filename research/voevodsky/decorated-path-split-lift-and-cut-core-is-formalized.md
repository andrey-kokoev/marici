# Decorated path split-lift and cut core: first Agda verification

## Delivered

`agda/ClosureDecoratedPathCore.agda` formalizes the combinatorial core of Grothendieck's endpoint-decorated history for an arbitrary small typed source graph. It uses `--safe --cubical --guardedness`, with no postulates or unsolved holes.

Checked constructions and proofs:

- endpoint-indexed paths, including a separate identity at each vertex;
- Boolean-style retained/forgotten decorations indexed by the entire underlying path;
- the all-retained decoration and uniqueness of any surviving decoration;
- the additive marked lift represented as a list of basis summands;
- `split-lift-coefficient`: the total all-retained projection coefficient of that list is exactly one, for every finite path;
- typed cut positions, their common vertex, and their prefix and suffix paths;
- splitting and joining decorations at a fixed cut;
- `join-split` and `split-join`: the two operations are inverse;
- typed path and decoration composition, preservation of the all-retained marking, and associativity of underlying path composition.

Because every decoration of w retains w as its underlying typed path, the coefficient theorem supplies the basiswise content of A L = identity. Extending it to rational linear combinations is a mathematical scalar-extension step; a general rational-linear category implementation is not included in this module.

Likewise the split/join inverse proofs give the cut-by-cut correspondence between a whole-path marking and independent prefix/suffix markings. This is the indexing bijection used in the source coproduct proof. The module does not yet package the full coalgebra equation as an equality of rational formal sums, nor prove enumeration/composition compatibility of all lists.

## Endpoint regression

`agda/ClosureDecoratedPathCoreRegression.agda` instantiates the graph containing

- 2 -> 4 -> 12;
- 2 -> 6 -> 12.

Both wholly forgotten routes reconstruct from their cut data. Their middle cut vertices remain respectively 4 and 6. The lift coefficients are one for both routes and for the typed empty path at 4. The all-retained projection gives coefficient zero to the wholly forgotten route, as required; it is not the coefficient observation that sends forgotten arrows to 1.

This fixture represents the arithmetic diamond explicitly. It is not yet an imported formalization of all sixteen prime-cube vertices or all 168 paths.

## Fresh verification after the transport-safe refactor

Command, completed with exit code zero:

```
agda --ignore-interfaces --transliterate -Werror \
  -i research/voevodsky/agda \
  -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 \
  research/voevodsky/agda/ClosureDecoratedPathCoreRegression.agda
```

The initial indexed-datatype implementation emitted `UnsupportedIndexedMatch` warnings. Decorations and cuts have now been refactored into recursively defined families, with explicit underlying-path arguments. The fresh regression closure passes Agda 2.8.0.1 with `-Werror`, without warning suppression. This removes the compiler's flagged transport-computation limitation; it does not by itself establish a new naturality theorem for an external realization.

## Boundary of the result

This is a formal path-level prerequisite, not the final map into `ClosureTreeBoundarySemantics`.

Still required:

1. package composition and the complete cut-sum equality in the chosen linear-category interface;
2. prove the specific transport/naturality laws required by the native semantics;
3. assign the prescribed pieces, boundary maps, and attachment cells to decorated arrows and gaps;
4. prove the resulting local data respect route composition and the complete polarized attachments.

Forgotten arrows have not been contracted to identities. This module adds no inverse source arrows, cofiber realization, Clark metric, or positivity assertion.

Subsequent inputs sharpen the remaining integration task. Grothendieck's `../grothendieck/formal-marked-cut-theorem-and-split-stable-realization.md` supplies a larger formal cut-index theorem and a categorical split exact realization in perfect path-algebra modules. Its stable proof need not be reconstructed here; comparison with the selected native realization remains separate. `clark-tail-polarity-gives-an-exact-dagger-between-history-receivers.md` supplies a polarity mate between analytic carriers, not an invariant terminal metric or an identification of formal history dagger with Hilbert adjoint.
