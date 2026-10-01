# Mandatory stagewise geometric positivity

Status: adopted requirement for the twelve-triangle formation/minimality problem.

## Admissibility

A proposed formation network is admissible only if EVERY stage, including intermediate stages, supplies a positive geometric realization and every transition preserves the specified geometric structure. A positive final projector, positive closed-walk weights, or PSD intermediate operators alone do not satisfy this requirement.

For each stage, supply:

1. **Realization:** explicit oriented cells and their embedding, or an atlas with explicit embeddings and compatible overlap maps. Complex coordinates are permitted as charts, not as a substitute for a real geometric realization.
2. **Incidence:** shared vertices and edges agree under the declared identifications. Prescribed boundary relations must hold. Assembly stages may have declared exposed boundaries; undeclared cracks are not allowed. Once a closed carrier is present, a transition must preserve its closure.
3. **Strict positivity:** every intended top-dimensional cell is nondegenerate and positively oriented; interiors do not overlap incompatibly. An enclosed three-dimensional carrier has strictly positive volume. Positive total volume alone cannot compensate for inverted or collapsed cells.
4. **Transition witness:** an explicit map or geometric correspondence explaining how the next stage is realized, preserving the required incidences, orientations and boundary data. Chart changes must agree on overlaps. Dimension changes require a declared geometric construction, not an unexplained rank collapse.
5. **Retained data:** any embeddings, frames, decoders or reference geometry needed to reconstruct an intermediate state are part of the declared model. A discarded carrier cannot be silently reintroduced later. Passing a fixed carrier through a stage is allowed only when explicitly represented and distinguished from geometric formation.

These are the operational geometric positivity conditions for the current oriented-cell model. Claims of positivity in the stronger canonical-form sense additionally require the corresponding forms and boundary-residue compatibility.

## Revised minimization problem

Minimize the number of distinct primitive directed endpoint arrows over networks that:

- realize the prescribed collective return on the stated input domain;
- satisfy the stagewise geometric conditions above;
- use a common, declared accounting of geometry, transport and reconstruction operations.

Declare the input domain before testing. Evidence for one fixed configuration is not a universal preservation theorem. Fixed-reference and co-transported-reference tests must be distinguished.

Coordinate compression is neither automatically forbidden nor automatically admissible. It must supply the same geometric witnesses as any other transition. If decoding requires additional primitive interactions, those interactions count under the same arrow convention. No numerical count is privileged by this requirement.

## Certification gate

Missing geometric witnesses mean **uncertified**, not a pass. An explicit violating realization means that realization **fails**. Minimality in the strengthened class may be claimed only after both an admissible construction and a lower bound within that same class are established.

Current status:

- **Bare coefficient networks:** their literal spatial-coordinate interpretation fails; coefficient positivity alone does not certify geometry.
- **Atlas-augmented networks:** [explicit witnesses](stagewise-positive-atlas-witness.md) now certify every intermediate stage for the declared registered positive-homothetic tetrahedral family. The 1836-, 576-, 73- and 72-arrow variants all pass in that model.
- **Conditional minima:** 73 for three-stage and 72 for two-pass coefficient networks with the declared shared atlas. Static atlas descriptions are not additional interaction arrows in this accounting.
- **General geometric-formation minimum:** not established; atlas storage, arbitrary geometry domains or additional reconstruction circuitry require their own accounting and admissibility proofs.

The existing stagewise audit checks selected necessary conditions and records these open gates. It is not a general positive-geometry verifier.

Evidence: [stagewise audit](stagewise-geometric-positivity.md), implemented in `checkers/check_stagewise_geometric_positivity.py`.
