# `Fact_n` genuine-construction capability audit

## Question

Can the finite fixtures already checked in Rzk be promoted, with the pinned sHoTT library, to a genuine Segal/Rezk type of polygon-dissection refinements and then to a generic `n`-gon face-product theorem?

## Fresh library inspection

The pinned sHoTT source used by `check-factn.ps1` was searched directly. No declaration or module was found for:

- a nerve constructor from a strict category or poset;
- a precategory-to-Segal-type construction;
- Rezk completion;
- simplicial objects as external degree-indexed diagrams.

The library exposes predicates and operations for types already carrying Segal/Rezk structure, including `is-segal`, `is-rezk`, canonical composition, and fillers. The existing Marici modules consume these structures as premises. They do not construct a directed type from finite object and arrow tables.

The same source contains no generic `List`, `Fin`, or `Vec` declaration, no finite-set library, and no set-quotient constructor located by the audit. These are required to define an arbitrary `n`-gon, finite diagonal families modulo order, pairwise noncrossing dissections, and their region components.

## Consequence for the checked fixtures

Modules `02` through `08` are valid checked finite data and equality proofs. Module `05` proves an equivalence between two ten-constructor types representing nondegenerate two-spines and filled triangles. It is not yet the Segal map of a genuine simplicial type. Calling it a “Segal fixture” is acceptable only with this qualification.

An ordinary inductive eleven-element dissection type cannot serve as `Fact_5`: if treated as a discrete type, its directed homs contain only identity behavior and do not recover refinement arrows. The refinement graph must be realized by an explicit directed-type constructor, a nerve construction, or an assumed realization axiom.

## First missing typed objects

The first missing object is not another polygon lemma. It is a reusable constructor

```text
nerve-poset : Poset -> U
```

with proofs that:

```text
hom (nerve-poset P) x y  ≃  (x <= y),
is-segal (nerve-poset P),
is-rezk (nerve-poset P).
```

After that, generic polygons require a finite-family layer:

```text
Fin(n), List(A), membership, permutation-insensitive finite subsets,
pairwise predicates, connected components or an equivalent region encoding.
```

## Disposition

The genuine simplicial realization and generic `n`-gon theorem are blocked in the current pinned library by absent constructors, not by a failed mathematical identity. Continuing with larger constructor enumerations would not close either theorem.

Two admissible routes remain:

1. implement a poset nerve and finite-family library in Rzk, then define generic polygons internally;
2. import a separately verified external finite-poset nerve through an explicit interpretation interface, retaining the construction as an assumption boundary.

The first route is the only one that proves the requested theorem wholly in Rzk. Its first acceptance test is a two-object chain whose nerve has one nonidentity arrow and a checked Segal/Rezk structure; polygon code should not resume until that test exists.
