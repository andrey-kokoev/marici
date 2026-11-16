# esd₇ neutral-pair geometry and a proposed Ramsey traversal connection

2026-11-09. Reproducible audit: `check_esd7_neutral_projection.py`. All finite incidence statements in this note were independently enumerated from the canonical Freudenthal algorithm in Marici `research/voevodsky/checkers/check_esd7_explicit_analytical_census.py`; the user's semantic assignment `R,B,N₁,N₂` is additional to the repository's geometric census.

## Geometry and visible quotient

Use barycentric vertices `(r,b,n₁,n₂)∈ℕ⁴` with sum `m=7`. The source cumulative coordinate is `(x,y,z)=(r,r+b,r+b+n₁)` with `0≤x≤y≤z≤7`. The visible projection

`π(r,b,n₁,n₂)=(r,b,n₁+n₂)`

forgets `z` while preserving `(x,y)`. It is a simplicial map onto `esd₇(Δ²)`, and admits the simplicial section `s(r,b,n)=(r,b,0,n)`.

The full f-vector is `(120,560,784,343)`; the visible quotient has `(36,84,49)` in dimensions 0,1,2. Fibers over a visible `(r,b,n)` have exactly `n+1` full vertices, linked in an interval by neutral-only elementary edges. There are 84 neutral-only edges. This geometric quotient alone has no unfillable topological obstruction: all visible simplices can be lifted by the displayed section.

For central T184, corners `R=(1,2,2,2)`, `B=(2,1,2,2)`, `N₁=(2,2,1,2)`, `N₂=(2,2,2,1)` project to three distinct states with the two N corners identified. The signed tetrahedral boundary maps to zero: the two RBN triangular faces cancel; the other two faces become degenerate. Loss of a 3-chain is not evidence of nonexistence of a categorical coherence filler.

## Neutral exchange and source triangulation

The coordinate transposition `σ(r,b,n₁,n₂)=(r,b,n₂,n₁)` is a geometric symmetry of the coarse FCC complex but not a simplicial automorphism of its fixed 343-tetrahedron subdivision. Exact audit:

- Of 560 fine edges, 504 are preserved and 56 are not.
- Of 343 fine tetrahedra, 119 are preserved and 224 are not.
- The 56 offending edges are exactly the fine diagonals with cumulative-coordinate mask `101`, hence barycentric displacement `(1,-1,1,-1)`.
- Every such diagonal is a **pair** of independent transfers `B→R` and `N₂→N₁`. Its source has `b≥1,n₂≥1`, giving `binom(8,3)=56` possible sources.
- Each diagonal admits four two-step root paths, with the intermediate transfers, in order: `(B→R, N₂→N₁)`, `(N₂→N₁, B→R)`, `(B→N₁, N₂→R)`, `(N₂→R, B→N₁)`. All 224 corresponding triangles exist in the original census.
- Every one of the 224 fine tetrahedra containing a presentation diagonal is changed by `σ`; all 119 diagonal-free tetrahedra are preserved. T184 belongs to the preserved 119.

This independently reconstructs the *same* 56 presentation diagonals and 224 diagonal-route comparison faces documented by Marici, `research/strominger/fcc-first-sector-transport-v1.md` and `research/strominger/fcc-face-flag-binding-v1.md`. Do not conflate the 224 comparison **faces** with the 224 subdivided-octahedron **tetrahedra**: they are different object sets with the common count `56×4`.

The mismatch is a noncanonical triangulation choice, repairable by changing the octahedral diagonal and transporting retained comparison faces. It is **not** automatically a Ramsey obstruction.

## A separate 16-state parity phenomenon

The visible states with **odd** neutral total `n=n₁+n₂` have no `σ`-fixed full lift because `σ`-fixed implies `n₁=n₂` and hence even `n`. For side length 7, the odd-n visible states occur in four rows of sizes `7,5,3,1`, giving `16` states. There are 20 even-n visible states, which do have fixed lifts.

The user's proposed obstruction length for `(ℓ,k)=(3,7)` is `ℓ+(2k−1)=16`. Thus the number of visible neutral-exchange-unfixed states exactly matches the proposed adversarial move count. Together with `7+16=23`, this suggests a concrete combinatorial test, but it is **not** an established map from states to moves, nor an upper-bound proof for `R(3,7)`.

For arbitrary edge length `m`, the corresponding odd-neutral count is

`S(m)=∑_{n odd,1≤n≤m}(m−n+1)=⌊(m+1)²/4⌋`.

The numerical equality `S(m)=3+(2m−1)` holds for positive integer `m` only when `m=7`. This distinguishes seven arithmetically relative to the *proposed* traversal length, but neither premise is proved to impose Ramsey constraints.

The original 16 states are not themselves a canonical 16-cycle, an affine `F₂⁴`, or sixteen necessarily invalid moves. For odd neutral totals the exchange creates paired choices, not impossibility of choosing a lift.

## Research frontier

Attach the *actual adversarial perfect-information traversal rules* to the four root-route alternatives in each diagonal/octahedron. An obstruction requires that all admissible ways to resolve the same source-to-target comparison are incompatible with the red-triangle/blue-7 constraints (or that an explicit adversarial strategy forces a forbidden clique); choosing another diagonal currently resolves the geometry.

A meaningful constructive test must derive a coloring-dependent transport/acceptance map for the four routes and an order-preserving interpretation of the 16 odd-neutral states as the user's 16 simplex moves. A count match alone is not enough. The 23 graph vertices still have not been derived from the 120 geometry vertices or 36 visible states.

## Source files

- `research/voevodsky/checkers/check_esd7_explicit_analytical_census.py`
- `research/strominger/fcc-first-sector-transport-v1.md`
- `research/strominger/fcc-face-flag-binding-v1.md`
- `research/strominger/esd7-seven-stage-handoff-v1.md`
- `research/voevodsky/coherence-pyramid-nonabelian-3-horns.md`
