# Whole-package E/Pi and higher-comparison generators

## Representation

`WholePackageSigmaPi.agda` defines an inductive-recursive universe:

* Code retains the expression, dependent index families, comparison endpoints, maps and explicit provenance.
* El(Code) is its interpreted value type.
* Complete is the pair of a Code and an actual value of that type.

El is an observation of a package. Operations return Complete, not just El. Codes for path types can be formed before a filler exists; a Complete path package additionally requires the actual witness.

The retained grammar has atoms, dependent E and Pi, paths, maps, equivalences, provenance retention and witnessed comparisons. Earlier complete Sigma/Pi chain records are embedded as atoms without reducing them to their underlying source values.

## Whole-package E and Pi

For a dependent family F:I->Complete:

* E-package(I,F,i) retains the entire family and resolves its selected fibre i.
* Pi-package(I,F) retains the entire family and its family of resolved values.

Each input's expression AND value are stored in the output code's provenance. The checked recovery functions and E-retains-family/Pi-retains-family theorems recover every supplied input, including the unselected E branches. Thus choosing a fibre does not delete the family's retained data.

The explicitly whole-package entry points E-whole and Pi-whole reify every prior Complete as a value before assembling it. Their entry-recovery theorems return the exact original Complete objects. These are the strict third-level operations requested: prior expressions, values, maps and comparison witnesses remain inside the new resolved values.

Index types are explicit parameters. The implementation does not choose a privileged index family for the intended E/Pi calculus.

## Comparisons and higher comparisons

A comparison package carries a,b,e,p, with

p : e(value(a)) = value(b).

Both full endpoints, e and p survive. The implementation supplies identity, inverse and composite comparison packages. E and Pi lift entire families of comparisons, preserving all their supplied witnesses in provenance. Dependent Pi-Sigma distributivity is an explicit invertible generator with both inverse laws.

Path packages retain their boundary and its filler. The same path constructor applied to a path code yields comparisons of comparisons and repeats at any specified finite height. There are concrete higher packages for associativity, unit and cancellation paths, plus the checked equivalence-induced path lift. Whole-package paths use the type Complete itself as their boundary type.

This is a typed formation-and-composition specification. Arbitrary supplied higher witnesses are checked against their boundaries; the signature does not claim that every boundary has a filler or that it can decide or enumerate all inhabitants of an arbitrary type. The constructors do not impose uniqueness of higher comparisons.

## Resolution signature

`WholePackageResolution.agda` supplies twelve typed generator schemas:

1. E family resolution;
2. Pi family resolution;
3. witnessed comparison;
4. identity comparison;
5. inverse comparison;
6. comparison composition;
7. higher comparison;
8. reflexive path;
9. equivalence-induced path lift;
10. dependent distributivity;
11. E action on comparisons;
12. Pi action on comparisons.

Each schema specifies its actual dependent premise family and complete output. This replaces the earlier unary/binary-only rule interface. Resolve stores the generator and every premise derivation, so differing orders and actual proof witnesses remain present. Seed inclusion and flattening have checked left/right unit and associativity laws.

Indices may be infinite. Resolution trees are inductively well-founded and may be infinitely branching; the earlier finite-tree interpretation applies when the premise index families are finite. No idempotence claim is made about raw histories.

## Self-application and universe levels

`reify-history` turns the entire endpoint-and-resolution-tree pair into a new Complete value. Its recovery theorem returns the exact prior derivation. That package can be assembled by E-whole/Pi-whole, compared, and reified again.

Reifying Complete at level l requires level l+1, because the package contains type-valued syntax. The construction is universe-polymorphic; it does not postulate a universe containing itself. Ordinary formation within the small code universe and reflective reification of the entire package are separate checked operations.

## Concrete integration

`WholePackageSigmaPiInstance.agda` embeds the earlier full dependent-chain SourceRecord and TargetRecord, forms their witnessed package comparison, and builds its actual resolution derivation. It reifies that derivation as next-Q, then applies both whole-package E and Pi. The recovery theorems confirm that next-Q, including the complete previous history, remains present. Whole-package path and higher-path interfaces are instantiated as well.

This realizes a concrete package-level signature. A completeness theorem saying these schemas generate every equivalence between all possible resolutions, and a universal higher-categorical completion, are separate questions. The arbitrary Python normalizer also remains a separate implementation.

## Verification

A fresh check of the instance rechecked all three new modules and the earlier dependency chain:

```
agda --ignore-interfaces --transliterate -i research/nima/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/nima/agda/WholePackageSigmaPiInstance.agda
```

Exit 0 under Agda 2.8.0.1 / Cubical 0.9. All local modules use `--safe --cubical --guardedness`; no new postulates or holes.

Files:

* `research/nima/agda/WholePackageSigmaPi.agda`
* `research/nima/agda/WholePackageResolution.agda`
* `research/nima/agda/WholePackageSigmaPiInstance.agda`
