# RH three-plane dual visualization contract

## Question

How should the existing SCC RH coherence net expose realization, underdetermination, and overpresentation without turning a force-layout coordinate into semantic evidence?

## Claim boundary

The three planes are typed views of one incidence structure. They do not assert that an RH constructor exists, that a realization is physical, or that a displayed quotient is faithful.

## Primary span view

Use the typed span

\[
R \xrightarrow{\rho} Q \xleftarrow{\pi} P,
\]

where `R` contains source realizations, `Q` contains invariant or quotient objects, and `P` contains presentations.

Each constructor receives `semantic_plane: realization|invariant|presentation`. Each cross-plane edge receives `semantic_relation: realizes|quotients_to|presents|compares`. Layout constrains the three planes to fixed depth bands; force simulation acts only within each band. Depth is a display coordinate, not physical time or evidential rank.

For a selected invariant `q`, report separately:

- `realization_fiber`: constructors in the fiber of `rho` over `q`;
- `presentation_fiber`: constructors in the fiber of `pi` over `q`;
- `incidence_pullback`: compatible realization-presentation pairs over `q`.

A realization fiber with more than one unresolved member displays underdetermination. A presentation fiber with more than one member displays overpresentation only when an admitted equivalence or coherence path identifies those members; otherwise display unresolved comparison rather than redundancy.

## Requirement-dual view

Construct a bipartite graph between constructors and typed requirements. A requirement edge records `requires`, `tests`, `detects`, or `coheres`; transport alone grants no authority.

Derive two projections:

1. Constructor nerve: constructors are adjacent when they share requirements. Equal requirement neighborhoods are candidates for underdetermination, not proof of identity.
2. Requirement nerve: requirements are adjacent when they constrain the same constructors. Equal constructor neighborhoods are candidates for redundant presentation, not proof of logical equivalence.

The viewer toggle must preserve selected identity while switching between `span` and `requirement_dual`. A detail panel lists the exact witnesses used for every fiber, equality, or coherence classification.

## Acceptance tests

1. Fixed seed changes do not change semantic-plane membership or fiber counts.
2. Removing an admitted equivalence turns overpresentation into unresolved comparison.
3. Removing a detecting requirement can enlarge a realization fiber but cannot silently merge source entities.
4. The requirement-dual view is computed from the same contract payload as the span view.
5. Nodes without typed plane data appear in an `unclassified` band; layout heuristics never classify them.
6. Existing constructor-admission simulation remains local and does not mutate the contract.

## Disposition

Implement in the Aspect-owned generator and contract compiler only after owner authorization. The current viewer's seeded three-dimensional force coordinate is nonsemantic and must not be reused as the plane classifier.
