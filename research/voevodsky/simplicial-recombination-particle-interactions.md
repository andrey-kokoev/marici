# Research Note: Simplicial Recombination and Particle Interaction Structures

Date: 2026-10-09
Status: Constructive research, unresolved composition law
Scope: Research preceding the 372:1 frequency-ratio investigation

## Provenance

Imported at the operator's request from a parallel ChatGPT conversation. The supplied note is retained below. Import does not constitute independent verification of its constructions or physical correspondences. The parallel interactive 3D construction mentioned in section 10 has not been imported with this note.

Continuation: [Dimensional Resolution in Simplex Interaction](dimensional-resolution-simplex-interaction.md).

Related local calculation: [Three tetrahedra around the pair axis](three-tetrahedron-belt.md). That calculation verifies the volume-preserving Pachner move; the face-extraction operation described here is additional.

---

## 1. Research objective

Investigate whether experimentally observed particle interactions can be represented by transformations of abstract simplicial complexes.

Use experimental observations as constraints without assuming the established subatomic ontology.

Initial geometric assignments:

| Object | Proposed representation |
|---|---|
| Photon | Filled 2-simplex (triangle) |
| Electron | Oriented 3-simplex complex |
| Positron | Oppositely oriented 3-simplex complex |

The objective is to derive interaction outcomes from simplex structure and composition rather than assign separate rules to each observed reaction.

## 2. Experimental starting point

Three interactions motivated the investigation:

1. Electron + positron → 3 photons
2. Electron + positron → 2 photons
3. Electron + electron → electron + electron

The first two convert an initial pair into different output multiplicities.

The third preserves the two charged particles.

Candidate geometric expressions:

2Δ³ → 3Δ²

2Δ³ → 2Δ²

2Δ³ → 2Δ³

These are distinct channels whose admissibility must ultimately follow from one composition structure.

## 3. First construction: 2Δ³ → 3Δ²

Take five vertices: A, B, C, D, E.

Construct two tetrahedra:

ABCD
ABCE

They share triangle ABC.

Connect the opposite vertices D and E.

Construct three triangles:

ADE
BDE
CDE

They share edge DE.

This establishes an explicit incidence construction relating two tetrahedra to three triangles.

The construction uses the same five vertices throughout.

## 4. Connection to Pachner moves

The 3-dimensional Pachner 2↔3 move transforms:

ABCD, ABCE

into:

ABDE, ACDE, BCDE

The three resulting tetrahedra have pairwise shared faces:

ADE, BDE, CDE.

Our candidate transformation extracts those three faces.

Therefore:

2 tetrahedra
→ Pachner 2→3 recombination
→ 3 internal triangular faces

The Pachner move itself transforms two tetrahedra into three tetrahedra.

The final face extraction is an additional operation.

## 5. Reversible structure

The Pachner move has a canonical reverse.

The initial configuration has a shared triangle ABC.

The recombined configuration has a shared edge DE.

The five vertices partition into complementary subsets:

{A,B,C} and {D,E}.

The combinatorial operation exchanges which complementary simplex is filled and which contributes its boundary.

General formulation:

Δᵖ * ∂Δᑫ ↔ ∂Δᵖ * Δᑫ

Here * denotes simplicial join and ∂ denotes simplicial boundary.

For p=2, q=1, the operation produces the 3-dimensional Pachner 2↔3 move.

The reverse follows by applying the same exchange in the opposite direction.

Reconstruction of two tetrahedra from the three extracted triangles is possible when their common-edge incidence structure and the reconstruction rule are retained.

## 6. Dimension-independent formulation

For an n-dimensional Pachner move:

k ↔ n+2−k

Examples:

| Dimension | Moves |
|---|---|
| 1 | 1↔2 |
| 2 | 1↔3, 2↔2 |
| 3 | 1↔4, 2↔3 |
| 4 | 1↔5, 2↔4, 3↔3 |
| 5 | 1↔6, 2↔5, 3↔4 |

The two sides of a move contain complementary selections of the n-dimensional facets in the boundary of an (n+1)-simplex.

The operation is universal across simplex dimensions.

It preserves the common boundary of the two alternative triangulations.

Our proposed dimension-reducing transformation requires additional structure beyond the Pachner operation.

## 7. Matrix representation

Represent a simplex by a column indicating which vertices it contains.

Initial configuration:

```text
        ABCD ABCE
A         1    1
B         1    1
C         1    1
D         1    0
E         0    1
```

Output configuration:

```text
         ADE  BDE  CDE
A         1    0    0
B         0    1    0
C         0    0    1
D         1    1    1
E         1    1    1
```

The matrices show how vertex participation changes during recombination.

## 8. Edge-incidence difference

Vertex order: A, B, C, D, E.

Initial edge adjacency matrix:

```text
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 0
1 1 1 0 0
```

Final edge adjacency matrix:

```text
0 0 0 1 1
0 0 0 1 1
0 0 0 1 1
1 1 1 0 1
1 1 1 1 0
```

Forward difference (final minus initial):

```text
 0 -1 -1  0  0
-1  0 -1  0  0
-1 -1  0  0  0
 0  0  0  0  1
 0  0  0  1  0
```

The transformation:

Removes: AB, AC, BC
Adds: DE
Retains: AD, AE, BD, BE, CD, CE

The reverse difference is the negative of the forward difference.

The entire edge-level change concerns four edges.

The six connections between the complementary vertex groups remain unchanged.

## 9. Higher-dimensional information

Edge adjacency alone does not determine which triangles and tetrahedra are present.

The complete simplex transformation must specify the higher-dimensional cells.

Initial complex:

- 5 vertices
- 9 edges
- 7 triangular faces
- 2 tetrahedra

Final complex:

- 5 vertices
- 7 edges
- 3 triangular faces
- 0 tetrahedra

Both have Euler characteristic 1.

The constructed transformation changes the maximal simplex dimension from 3 to 2.

A complete elementary-operation sequence must add DE and its three triangles, remove both tetrahedra, remove the seven original triangular faces, and remove AB, AC, BC.

The reverse sequence reconstructs the original complex.

This supplies a reversible construction history, although the dimensional reduction is not itself a standard Pachner move.

## 10. Second construction: 2Δ³ → 2Δ²

Change the initial incidence condition.

Instead of two tetrahedra sharing a triangular face, make them share an edge.

Example:

ABCD
ABEF

Their intersection is edge AB.

A candidate two-triangle output is:

ACE
BDF

This configuration was incorporated into a parallel interactive 3D construction.

The current construction specifies one possible recombination.

It does not establish a unique or intrinsic selection of those output triangles.

## 11. Third incidence case: shared vertex

Two tetrahedra can also share only one vertex.

This produces three basic intersection types:

| Shared simplex | Shared vertices | Candidate output |
|---|---|---|
| Face | 3 | 3 triangles |
| Edge | 2 | 2 triangles |
| Vertex | 1 | 1 triangle |

The candidate rule is:

Output multiplicity = number of shared vertices.

This remains a conjecture.

The one-photon electron–positron annihilation channel is excluded for an isolated pair in vacuum by observed conservation constraints.

The edge-sharing and vertex-sharing output counts have not been derived from a universal operation.

## 12. Orientation

Assign orientations to the two initial tetrahedra.

Opposite induced orientations on their shared triangular face permit consistent oriented gluing.

Equal induced orientations do not satisfy that condition without reversing one tetrahedron.

This gives an intrinsic orientation compatibility test.

However, compatibility alone does not determine whether recombination occurs or which output multiplicity is selected.

Orientation is therefore a candidate input to the composition structure, rather than an established selection mechanism.

## 13. Attempted universal composition law

We considered complementation among the facets of an enclosing higher simplex.

If F is the facet set and K is a subset:

D(K) = F \ K

Then:

D(D(K)) = K

For the boundary of a 4-simplex, five tetrahedral facets permit a 2↔3 partition.

This recovers the Pachner count and reversibility.

An additional pairwise-intersection extraction produces three triangles.

Assessment:

- Complementation is reversible.
- The Pachner multiplicity follows from facet counting.
- Three-triangle extraction was separately specified.
- Arbitrary output multiplicities were not derived.
- No selection mechanism was obtained.

The attempt did not produce the required universal composition law.

## 14. Acceptance criteria for a universal law

1. Defined through intrinsic simplicial structure.
2. Applies across simplex dimensions.
3. Decomposes into explicit elementary operations.
4. Supports reversible construction.
5. Determines admissible outputs from input structure.
6. Does not encode desired multiplicities.
7. Supports composition of successive operations.
8. Has coherent alternative construction paths.
9. Can incorporate orientation.
10. Generates multiple possible output cardinalities.
11. Recovers known Pachner constructions.
12. Accommodates observed interaction channels.
13. Derives selection restrictions.
14. Produces independently testable predictions.

The proposed constructions currently satisfy only subsets of these requirements.

## 15. Research status before frequency analysis

Established mathematical structures:

- Simplicial incidence representations.
- Pachner 2↔3 recombination.
- Complementary simplex–boundary exchange.
- Reversible Pachner moves in arbitrary dimensions.
- Exact vertex and edge incidence matrices.
- An explicit construction extracting three triangles.
- Reversible cell-by-cell construction histories.

Proposed correspondences:

- Electron/positron ↔ oppositely oriented tetrahedral complexes.
- Photon ↔ filled triangular complex.
- Face-sharing ↔ 2→3 interaction.
- Edge-sharing ↔ 2→2 interaction.
- Vertex-sharing ↔ 2→1 interaction.

Unresolved:

- A single intrinsic law deriving all three intersection-dependent outcomes.
- A unique two-triangle construction for edge-sharing.
- Selection of alternative outcomes from initial-state structure.
- A connection between abstract incidence and measured reaction probabilities.

## 16. Research continuation

The next stage investigates whether interaction frequencies constrain the resolution of simplex incidence.

The proposed distinction is between:

- Edge-sharing configurations, retaining rotational freedom.
- Face-sharing configurations, requiring additional alignment.

The subsequent research note, "Dimensional Resolution in Simplex Interaction," develops this hypothesis using the working 372:1 frequency ratio.

This note records the combinatorial construction independently of that numerical assumption.
