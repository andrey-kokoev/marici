# Finite probe semantics: Lean formalization handoff

## Question

Which finite probe-semantics claims are stable enough to formalize, and which assumptions must appear in their Lean signatures?

## Claim boundary

This packet freezes definitions and theorem targets for the Buzzard formalization lane. It does not edit `research/buzzard/`, does not claim a checked Lean theorem, and does not authorize cross-locus mutation.

## Frozen core

A `FaceSystem` consists of a finite vertex type and admitted finite faces, with the empty face admitted and closure under subsets. Its thin `FaceCategory` has one arrow for each face inclusion. A `ConstraintPresheaf` is a functor from the opposite face category to `Type`; its functor laws are exactly restriction identity and restriction composition.

For a maximal face, a `MatchingFamily` is the subtype of proper-face sections whose restrictions agree on intersections. The `MatchingMap` sends a joint section to its restricted family. This definition avoids requiring abstract limit machinery in the first implementation; an equivalence with the categorical limit can be proved later.

A `ProbeRewrite` contains:

1. an equivalence of the relevant face categories;
2. a natural isomorphism between the source presheaf and transport of the target presheaf.

It does not contain or imply a global rewrite system.

## Theorem dependency chain

1. `matchingMap_natural`: matching maps commute with restriction-preserving morphisms.
2. `rewrite_matching_conjugacy`: a `ProbeRewrite` identifies source and target matching maps through induced isomorphisms.
3. `rewrite_fiber_equiv`: conjugacy induces equivalences of corresponding matching-map fibers.
4. `two_vertex_matching_family`: for the full two-vertex face system, matching data is the pullback of the two singleton sections over the empty-face section.

The fiber theorem establishes preservation of local extension multiplicity. It does not prove confluence, normalization, physical equivalence, or unique reconstruction.

## Assumptions that must remain visible

- `DecidableEq` is needed when faces use `Finset`.
- Universe levels for `Type`-valued presheaves must be declared.
- The matching object needs either chosen finite limits or an explicit compatible-family subtype.
- A rewrite equivalence must transport the proper-face indexing diagram, not only maximal faces.
- Additive cross-effects require additional additive structure and are excluded from the core theorem.

## Hostile obligations

A proposed implementation is incomplete if it can construct a `FaceSystem` lacking a required subface, construct `ProbeRewrite` without naturality, infer unique reconstruction from a nonempty fiber, or use the local fiber theorem as global confluence.

## Disposition

The finite categorical core is statement-stable and has a dependency-ordered formalization contract at `contracts/finite-probe-semantics-lean-handoff.v1.json`. Lean implementation is blocked in this locus because `research/buzzard/` is exclusively owned by `marici.Buzzard`; the blocker is mutation authority, not a missing theorem statement.
