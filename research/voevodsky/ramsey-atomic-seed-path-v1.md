# Package-path admission is not literal source-record equality

## Fresh signature audit

The live net is local revision23. Before asserting that an independently supplied target seed cannot be obtained from a source policy, this turn reads the owning native definitions:

    Package = Sigma Graph Value
    Graph = Sigma Type Node

The span admission predicate contains a witness of `q = port-package c f p`. This is equality of whole native packages, not a comparison of fixed-carrier serialized records.

## Kernel result

For any explicit equivalence e : A equiv B and alignment e(x) = y, univalence gives a path

    atom(A,x) = atom(B,y).

The formal module constructs that path directly, varying both the carrier type and its atomic node. Instantiating e with Boolean negation gives

    atom(Bool,false) = atom(Bool,true),

although false and true remain unequal in the fixed Bool type.

Consequently the singleton path-closed seed predicate

    Admit(q) = (q = atom(Bool,false))

admits `atom(Bool,true)` by the reverse package path. The actual native `Resolve` constructor accepts this as a seed. This does not use a comparison rule or an operational source move.

The kernel also proves that no global function from arbitrary native packages to Bool can recover the raw value of every Boolean atom. Such a function would map the package path to false = true. A hostile attempt to use the package path as a fixed-Bool equality is rejected.

## Meaning for source admission

This is not an inconsistency. It is the ordinary distinction between a path in a universe-indexed package space and equality in a fixed carrier. The chosen package path includes a nontrivial carrier automorphism.

It does, however, rule out interpreting the current path-closed admission predicate as literal-record membership without additional structure. Comparing packet hashes or unequal JSON strings alone is insufficient to prove the absence of such a package path.

The generic theorem applies to any explicitly supplied equivalence/alignment. This turn does **not** construct an actual transposition of the two source packet strings or claim an operational C/M-role transition.

## Existing result remains scoped

The retained four-facet correspondence was built from explicit validated ports and checked concrete restriction/seam terms. Those terms remain well typed and their runtime bindings remain unchanged. The new theorem does not invalidate that scoped construction.

It instead identifies a missing condition in any stronger operational reading: package-path admission must not silently be used as reference-preserving source transport. The specific compiled diagram and all possible inhabitants of a path-closed admission predicate are different claims.

## Next executable step

Define an observation-preserving transition gate with fixed external reference/provenance carriers. An equivalence transporting a package must also preserve the declared source observations; a carrier automorphism that changes them must be refused. Test that gate on the Boolean discriminator before binding it to actual packet reference extractors.

This should be an explicit owner-local interpretation or fixed-carrier/slice condition, not an unreviewed edit to the owning native signature. The test must distinguish raw path-closed admission from the stronger source-semantic map actually required.

## Verification

- Contract: `contracts/ramsey-atomic-seed-path-attempt.v1.json`.
- Formal source: `agda/RamseyAtomicSeedPaths.agda`.
- Checker: `checkers/check_ramsey_atomic_seed_paths.py`.
- Receipt: `results/ramsey-atomic-seed-path-v1.json`.
- Passing freeze: `scc-freezes/ramsey-atomic-seed-path-v1.c26ceb9ce1985b0c.json`.

Fresh safe Cubical checks pass with ignored interfaces and stable compiler/source inventories. Owning signature files are pinned and unchanged. No parent verdict, external graph mutation or Git checkpoint occurred.
