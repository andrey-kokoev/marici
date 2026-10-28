# Exact prior constructor for the bottom face WITH its filler

## Main discovery

The repository already has the exact dependent constructor requested by the operator. The earlier searches located analytical joint-feature arguments, but did not yet locate this direct implementation.

Read:

- `research/nima/seed-tetrahedron-bridge.md`, titled **Seed tetrahedron bridge: the bottom surface arrives with its filler**;
- `research/nima/retained-tetrahedral-package.md`;
- `research/nima/agda/MarkedTetrahedronCoherence.agda`;
- relevant constructor/projection declarations in `research/nima/agda/RetainedTetrahedralPackage.agda` and `research/nima/agda/SeedTetrahedronBridge.agda`;
- `research/voevodsky/dg-pyramid-signed-lift-audit.md` and the corresponding declaration inventory in `research/voevodsky/agda/DGPyramidSignedLiftAudit.agda`.

These prior sources were inspected, not freshly compiled. No new analytical or formal certification is claimed.

## 1. Constructor, not just a record requiring a filler

In `MarkedTetrahedronCoherence.agda`, the six fixed edge paths determine four face types:

    Face012, Face123, Face013, Face023.

For a=Face012, b=Face123, c=Face013, d=Face023, the type

    Tetrahedron a b c d

is equality of the two retained face-composition routes, including reassociation and whiskering.

The missing-bottom completion type is literally

    Missing123 a c d = Sigma b:Face123. Tetrahedron a b c d.

The source proves

    unique123 a c d : isContr (Missing123 a c d).

This supplies a center consisting of BOTH b and its tetrahedral comparison, and a contraction comparing any other completion with that center. It is not a declaration that a separately supplied arbitrary surface fills.

The implementation constructs an equivalence

    route123 c : Face123 equivalent Route,

using path-whiskering and concatenation equivalences. Its target is the common full three-edge route. It then obtains the missing face and filler as a reversed equivalence fiber over `left-route a d`.

The companion theorem `solve123` says that a prescribed b fills exactly when it agrees with the forced inverse image:

    b = inverse(route123 c)(left-route a d).

That equation is an acceptance condition for an independently supplied bottom, not permission to overwrite it.

## 2. Exact reindexing for the two F736 tetrahedra

The Agda indices are zero based. Local source labels1,2,3,4 correspond to0,1,2,3. Therefore:

| Agda face | local analytical label | T324 | T325 |
|---|---|---|---|
| Face012 = a | H123 | H731 | H734 |
| Face123 = b | bottom H234 | H745 | H760 |
| Face013 = c | H124 | H732 | H735 |
| Face023 = d | H134 | H736 | H736 |

The desired bottom/filler outputs have precisely the types

    (H745,Theta324) : Missing123 H731 H732 H736,
    (H760,Theta325) : Missing123 H734 H735 H736.

These are reindexed constructor shapes, NOT newly supplied analytical inhabitants. The same d=H736 must index both outputs; it cannot be recomputed independently and silently identified afterward.

A useful whole-patch type is consequently

    Sigma d:SharedFace736.
      Missing123 H731 H732 d
      times Missing123 H734 H735 d,

with all edge types, source domains and analytical comparison data retained in the indices. If d or the other faces are independently prescribed, their comparisons must also be supplied. A pair of contractible completion fibers does not manufacture the prescribed physical d or identify its external normalization.

## 3. Prior bridge retains agreement with supplied bottom data

`SeedTetrahedronBridge.agda` returns

    bottom-and-filler : Missing023 ...,

and proves

    bottom-pair-agrees
      : bottom-and-filler = (supplied-bottom,supplied-bottom-filler).

It separately derives the bottom equality and a DEPENDENT path comparing fillers transported along that bottom equality. This avoids comparing fillers as if their different boundary indices were definitionally equal.

Its missing index023 reflects its chosen vertex ordering; for the local F736 bottom index123 use the corresponding `unique123` constructor above.

Crucial scope from the source: one side face in this bridge was generated compatibly from the supplied bottom. The result does not say that four arbitrarily and independently fixed faces agree. It also refuses an easy spine completion that would replace independently retained seed diagonals by composites.

That is directly relevant here: do not redefine E514/E515, or change the supplied physical bottom, just to make the tetrahedron tautological.

## 4. Analytical structured lift already has a formal reduction

`DGPyramidSignedLiftAudit.agda` defines a signed horn completion for a whiskering equivalence R and prescribed boundary b by

    Completion = fiber(R,b).

This includes the recovered face AND its boundary equation. An equivalence gives a contractible completion with a forced center c. For any structured lift family L, the source proves

    (Sigma s:Completion. L(s)) equivalent L(c).

Thus the constructive strategy is not to choose the signed bottom independently, then choose positivity, then certify an unrelated tetrahedron. Carry the analytical/physical structure as a dependent lift over the entire paired completion.

Its `FramedComparison` construction retains:

- an actual DG boundary filler with its boundary equation;
- its comparison to the selected signed completion;
- all existing frame witnesses.

The audit explicitly warns that this reduction does not construct a physical mate, endpoint connectors, positivity, or an analytical comparison into the signed target. It requires an actual comparison map. The source hypothesis is a whiskering EQUIVALENCE, not merely injectivity/faithfulness.

## 5. What this gives the current calculation

The exact prior method is now available:

1. Retain the actual six-edge skeleton and three supplied face witnesses for each incident tetrahedron, with one common H736.
2. In a target where the route-whiskering equivalences are proved, use `unique123` or its analytical equivalence-fiber counterpart to calculate each bottom WITH its filler.
3. If a bottom is independently prescribed, compare the ENTIRE pair with that prescribed pair. Transport the filler along the face equality; do not compare mismatched dependent indices.
4. Attach regulator/domain/endpoint/placement and positive-feature structure as a lift of the paired completion, using the known internal feature construction where its hypotheses are met.
5. Prove the realization comparison from the analytical F736 maps to this completion target. Path-horn completion in an arbitrary type is not automatically a horn theorem for arbitrary noninvertible operator relations.

The internal common-face Gram and Hadamard constructions from the previous search are candidates for the structured feature data. They do not eliminate the need to identify the actual F736 analytical diagrams and inherited regulator placements.

## Disposition

The joint bottom-face/filler constructor is already present and theorem-backed in prior research. It should not be described as a missing generic construction. Its precise F736 shape uses `Missing123`, twice, over the same shared Face023.

What remains is the concrete analytical instantiation and witness-preserving comparison, including any independently fixed bottom data and the required physical/positive lift. This search identifies the actual reusable constructor and prevents substituting a free-spine or scalar-readout completion for the retained source problem.
