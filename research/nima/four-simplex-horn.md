# A retained marked 4-simplex horn

## Obligation

Construct one missing tetrahedral face and a higher filler while retaining five vertices, ten edges, ten triangle witnesses and four supplied tetrahedral witnesses. The SCC obligations are forward horn completion and route/coherencer compatibility of shared boundary extraction. This is a path-coherence construction, not an arbitrary relational-WG completion theorem.

## Presentation and compatibility boundary

`agda/FourSimplexHorn.agda` uses an explicit **Cubical presentation of path simplices**. A triangle with edges `p`, `q`, `r` is a dependent path from `r` to `q` while the source follows `p`. A tetrahedron is a dependent path of those triangles. The tetrahedral cube has four triangular boundary faces and collapsed lower-dimensional sides; it is not an arbitrary cube relabelled as a simplex.

`triangle-comparison` proves equivalence with the earlier equation `p ∙ q ≡ r`. `triangle-package-iso` extends this to the complete retained triangle packages, with inverse laws and unchanged vertices/edges. Edge extraction reuses the prior `EdgePackage` directly. **An equivalence of the complete new tetrahedral encoding with the older concatenation-based `MarkedTetrahedronCoherence` encoding is not proved here.** The new top-dimensional theorem is stated and checked in this explicit presentation; it is not silently promoted to that unverified bridge.

## Constructor and recovery

For fixed lower data, `Horn` contains tetrahedra 0123, 0124, 0134 and 0234. The missing face is 1234, opposite vertex 0, so this is an outer horn. The first three supplied tetrahedra construct `Family h`, an interval-indexed family whose endpoints are exactly the types of tetrahedra 0234 and 1234. The fourth supplied tetrahedron is its starting term.

The completion type is

$$
\sum_{t:E_h(1)}\mathsf{PathP}(E_h,t_{0234},t).
$$

`unique` proves this type contractible using Cubical's dependent-singleton theorem. Its center constructs the fifth tetrahedron and the higher filler together. No missing term or top filler is assumed as an input.

`complete`, `forget`, `completion-iso` and `horn-fixed` prove that the supplied horn is retained and recovered exactly, and that completing a recovered package agrees with the original package up to a path that fixes the entire horn. `Request` and `Full` retain all lower data explicitly. A request/answer WG constructs the full package and its completion witness.

`boundary0234`, `boundary1234`, `boundary0134`, `boundary0124` and `boundary0123` identify the five actual tetrahedral restrictions of the constructed 4-cell. The remaining three cubical sides are checked to be the collapsed triangle 234, edge 34 and vertex 4. This makes the representation's boundary convention explicit.

Five extracted `TetraPackage` values retain their surfaces and fillers. Ten `shared...` equations check every pairwise shared triangular face, including all endpoint, edge and face-witness data. These triangles can then be converted to the earlier retained face representation or descended to its edge packages.

## Fully prescribed boundaries remain a different problem

For a fixed candidate fifth tetrahedron, `fixed-face-gate` identifies existence of the 4-cell with equality between that candidate and the transported tetrahedron. `incompatible-fixed-face` rejects a candidate when that equality is refuted. Contractibility of the **missing-face-plus-filler** package does not assert that every fifth tetrahedron can fill the fixed boundary, or that the fixed filler space is contractible.

## Fixture

The fixture retains `(Bool,false)` at vertex 0 and `(Bool,true)` at the other vertices. The connecting path is the earlier Boolean-negation univalence path. Explicit higher cone cells provide a comparison completion. The generated completion agrees with that explicit pair by `unique`, the input horn stays fixed, and extracting the missing tetrahedron recovers the typed vertex `(Bool,true)`. This exercises a nonconstant type-and-term edge but is not a nontrivial higher-homotopy-group example; the theorem itself quantifies over arbitrary well-typed supplied horns.

## Verification and residuals

Fresh safe Cubical Agda passed through `research/nima/checkers/check_cubical_agda.ps1 -Module FourSimplexHorn -Fresh`, with Cubical 0.9. Receipt and log: `results/agda-FourSimplexHorn.json` and `.log`. Only the pre-existing `TypedGeneratorLayers.agda` import warning remains. The SCC model `four-simplex-horn` validates receipt freshness; registration is not mathematical evidence independently of the check.

The retained lower boundary and top filler are checked in the declared Cubical presentation. The full older-tetrahedron presentation bridge, all five horn orientations, arbitrary fully fixed boundary filling, and a general simplicial-object interface with every degeneracy identity remain outside this result. No commit or ledger entry was made.
