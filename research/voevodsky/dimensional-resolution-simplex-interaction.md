# Research Note: Dimensional Resolution in Simplex Interaction

Date: 2026-10-09
Status: Structural hypothesis
Subject: Geometric origin of unequal interaction multiplicities

## Provenance and admission caveat

Imported at the operator's request from a parallel ChatGPT conversation. The supplied note is retained below; no new calculation or physical validation accompanies this import.

The ratio 372 is a working input, not a verified universal electron–positron annihilation branching ratio. A physical comparison needs a source and specified initial state, spin preparation, energy, and event definition/cuts, including whether free annihilation or positronium decay is intended.

The existing `three-tetrahedron-belt.md` calculation verifies a 2↔3 Pachner move between two and three **3-simplices**, with the same outer boundary. It does not establish conversion into two or three **2-simplices**, or photons. The photon-output interpretation remains an additional hypothesis, as acknowledged among the unresolved results below. The rotational degree counts condition on an already identified shared simplex; they do not themselves define a measure on unconstrained encounters.

---

## 1. Observational input

Electron–positron annihilation has two established channels:

- 2 → 2: electron + positron → 2 photons
- 2 → 3: electron + positron → 3 photons

Adopt the working frequency ratio:

P(2→2) / P(2→3) = 372

We seek a geometric explanation for this ratio without assuming a particular subatomic particle model.

## 2. Geometric representation

Represent electron and positron as oppositely oriented 3-simplex complexes.

Represent each outgoing photon as a 2-simplex complex.

Candidate correspondence:

| Initial intersection | Transformation |
|---|---|
| Shared edge | 2Δ³ → 2Δ² |
| Shared face | 2Δ³ → 3Δ² |

The face-sharing 2→3 construction has an explicit incidence realization through the Pachner 2↔3 configuration.

The edge-sharing 2→2 construction remains a candidate.

## 3. Geometric degrees of freedom

Consider two congruent, rigid tetrahedra.

Their relative rotational freedom depends on their shared simplex.

| Shared simplex | Dimension | Remaining rotational DOF |
|---|---:|---:|
| Vertex | 0 | 3 |
| Edge | 1 | 1 |
| Face | 2 | 0 |

When two tetrahedra share an edge, one can rotate around that edge relative to the other.

Face-sharing requires alignment of an additional vertex, restricting that remaining rotational freedom.

Consequently, face-sharing configurations occupy isolated positions within the continuous edge-sharing orientation space.

This gives a candidate mechanism for the unequal occurrence frequencies.

## 4. Resolution hypothesis

Let:

Ω = total admissible relative angular range

δ = combined angular range classified as face-sharing

Assume uniform angular distribution and exhaustive classification into edge-sharing and face-sharing outcomes.

Then:

P(edge) = (Ω − δ) / Ω

P(face) = δ / Ω

Therefore:

P(edge) / P(face) = (Ω − δ) / δ

Setting the ratio to 372:

(Ω − δ) / δ = 372

Ω / δ = 373

δ / Ω = 1 / 373

If Ω = 360°:

δ ≈ 0.965147°

Thus the model requires face-sharing to occupy approximately 0.2681% of the angular configuration space.

The ratio determines the required resolution. It does not independently derive that resolution.

## 5. Incidence multiplicities

A tetrahedron contains:

- 4 triangular faces
- 6 edges
- 4 vertices

If interaction frequencies scale with the number of available simplex features:

P(edge) / P(face) = 6wₑ / 4wₒ

where wₑ is the effective weight per edge and wₒ is the effective weight per face.

For a frequency ratio of 372:

wₑ / wₒ = 248

Alternatively, counting all possible pairings between two tetrahedra gives:

- 36 edge–edge pairings
- 16 face–face pairings

In that model, the required per-pair weight ratio is:

wₑₑ / wₒₒ = 496 / 3

These are different encounter measures. The geometry must determine which counting measure applies.

## 6. Structural interpretation

The proposed mechanism involves a reduction in the dimensionality of admissible relative configurations.

Edge-sharing permits one continuous rotational parameter.

Face-sharing fixes that parameter to isolated configurations.

Exact face alignment has zero measure under a continuous angular distribution.

A nonzero face-sharing frequency therefore requires an additional structure, such as:

- Finite angular resolution
- Discrete admissible orientations
- A nonuniform encounter measure

The observed frequency ratio constrains that structure.

## 7. Relation to simplicial duality

The Pachner construction exchanges complementary simplex completions.

For the five-vertex configuration:

Initial common simplex: ABC

Complementary edge: DE

The underlying combinatorial exchange is:

Δ² * ∂Δ¹ ↔ ∂Δ² * Δ¹

This transformation is reversible.

The current hypothesis proposes that relative geometric alignment determines which simplex incidence structure is realized during interaction.

The combinatorial exchange and the statistical selection mechanism are separate components of the proposed model.

## 8. Established and unresolved results

Established within the construction:

1. Two rigid tetrahedra sharing an edge retain one relative rotational degree of freedom.
2. Face-sharing imposes an additional alignment constraint.
3. A Pachner 2↔3 move exchanges complementary simplex completions.
4. The assumed ratio 372 determines an angular acceptance fraction of 1/373 under a uniform one-angle model.

Not established:

1. That edge-sharing necessarily produces two 2-simplices.
2. That face-sharing necessarily produces three 2-simplices.
3. That the encounter measure is uniform.
4. That simplicial geometry independently determines the required resolution.
5. That the proposed incidence model predicts observed scattering frequencies.

## 9. Research target

Construct an intrinsic resolution measure on simplicial interactions.

Required properties:

1. Derived from incidence, orientation, composition, or intrinsic simplex geometry.
2. Applies to edge-sharing and face-sharing through one rule.
3. Determines their relative admissible configuration measures.
4. Produces output multiplicities without prescribing them.
5. Supports reversible transformations.
6. Produces a numerical frequency ratio independently of observational input.

The principal unknown is the resolution measure.

The central conjecture is that observed scattering multiplicities and their relative frequencies arise from dimension-dependent constraints on admissible simplex incidence configurations.

The next constructive task is to identify a natural measure on the space of relative simplex configurations and calculate its edge-sharing and face-sharing weights without fitting them to 372.
