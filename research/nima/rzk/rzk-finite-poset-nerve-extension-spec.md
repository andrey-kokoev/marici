# Rzk finite-poset nerve extension specification

## Purpose

Add a sound constructor for the synthetic directed type presented by a finite
poset. This cannot be implemented as an ordinary inductive datatype: ordinary
Rzk inductive types are discrete, so their directed homs contain no presented
nonidentity arrows.

## Required primitive

For an internal finite poset presentation `P`, provide

```text
nerve-poset(P) : U
obj_P           : carrier(P) -> nerve-poset(P)
```

and a natural equivalence on presented objects

```text
hom(nerve-poset(P), obj_P(x), obj_P(y))  ≃  leq_P(x,y).
```

The constructor must not assert `carrier(P) ≃ nerve-poset(P)`. Such an ordinary
type equivalence would transport discreteness and destroy the intended
nonidentity directed homs. `obj_P` is a family of global points, not an
exhaustion theorem in the ordinary identity type.

## Introduction data

For every proof `p : leq_P(x,y)`, introduce a directed arrow

```text
arrow_P(p) : hom(nerve-poset(P), obj_P(x), obj_P(y)).
```

The hom equivalence requires:

- proof irrelevance for parallel order witnesses;
- `arrow_P(refl)` equal to the constant directed arrow;
- `arrow_P(trans(p,q))` equal to Segal composition of `arrow_P(p)` and
  `arrow_P(q)`.

Identity degeneracies are therefore constant simplices, not separately
postulated combinatorial labels.

## Higher simplices and computation

A map from the standard `k`-simplex into `nerve-poset(P)` with presented
vertices must be equivalent to a weak chain

```text
x_0 <= x_1 <= ... <= x_k.
```

Under this equivalence:

- the `i`th face deletes `x_i` and composes adjacent inequalities when needed;
- the `i`th degeneracy repeats `x_i` using reflexivity;
- restriction along simplex-category morphisms acts by precomposition on the
  weak chain.

These computation rules imply the simplicial identities judgmentally or by
specified coherent paths. Merely supplying isolated fillers is insufficient.

## Elimination principle

Elimination into a Rezk type `A` requires:

1. an object assignment `F_0 : carrier(P) -> A`;
2. an arrow assignment for every order proof;
3. preservation of reflexivity and transitivity.

The eliminator returns a function `nerve-poset(P) -> A`, with computation rules
on presented objects and arrows. Uniqueness is contractible once the coherence
data are fixed. This is the internal universal property of the poset nerve.

## Derived structure

The library layer must derive, rather than assume independently:

```text
is-segal(nerve-poset(P))
is-rezk(nerve-poset(P))
```

Segal follows from unique transitive composition. Rezk completeness uses
antisymmetry: an invertible presented arrow supplies both `x <= y` and `y <= x`,
hence `x = y` in the carrier and therefore the identity isomorphism.

## Soundness obligation

The compiler primitive needs an interpretation in Rzk's simplicial/cubical
model as the ordinary simplicial nerve of the finite poset. The implementation
must prove that substitution, shape restriction, extension types, and the new
computation rules are preserved by that interpretation. Treating these clauses
as unchecked `#assume` declarations would enlarge the trusted theory without
constructing the requested capability.

## Acceptance tests

1. **Walking arrow.** For `0 < 1`, obtain two presented points, one
   nonidentity arrow `0 -> 1`, no arrow `1 -> 0`, identity degeneracies, unique
   fillers for every composable chain, and exactly identity isomorphisms.
2. **Diamond poset.** Verify two distinct length-two spines with their own
   composites and no equality between unrelated arrows.
3. **`Fact_5`.** Recover 11 presented dissections, 31 arrows including
   identities, 61 two-simplices including degeneracies, and the previously
   checked ten nondegenerate two-spines.
4. **Generic finite input.** Construct the nerve from data rather than one
   primitive per census.
5. **Regression.** Existing sHoTT modules typecheck unchanged.

The external checker `check_finite_poset_nerve.py` supplies expected simplex
counts and combinatorial behavior for tests 1 and 3; it is an oracle for
regression, not the soundness proof.

## Implementation boundary

This feature requires a new directed higher-inductive/semantic primitive in the
Rzk compiler and model. It cannot be delivered solely by adding an `.rzk.md`
library module under the current language. Compiler-source location, build
contract, and model proof sources must be admitted before implementation; none
are present in this repository or the pinned sHoTT archive.
