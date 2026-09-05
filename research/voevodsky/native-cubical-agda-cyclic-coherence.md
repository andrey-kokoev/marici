# Native Cubical Agda cyclic-coherence skeleton

## Question

Can the JSON-level cyclic signature be represented by native cubical path, square, and cube types, with malformed boundaries rejected by the type checker?

## Claim boundary

The module formalizes the generic lax-cycle signature and an inhabited constant common-fiber cube. It does not instantiate the full RH source objects, prove filler contractibility, or formalize the exact pasting cohomology.

## Construction

`CyclicCoherence.agda` defines a vertex with parameter, object, and residue types plus generator and coherencer maps. `LaxCycle` contains three vertices and the typed transports \(R_A\to P_B\), \(R_B\to P_C\), and \(R_C\to P_A\). On a common type it defines a native path edge, square face, cube filler, and inhabited filler type using Cubical Agda's `Square` and `Cube`.

## Strongest falsification attempt

`negative/BadBoundary.agda` declares a path from zero to one whose body is constantly zero. Agda rejects it at the \(i=1\) face with `UnequalTerms: 1 != 0`. Thus boundary parallelism is enforced by native cubical typing rather than by the string checks used in the JSON/SCC projection.

## Disposition

The first native cubical milestone passes: the valid cube typechecks, and the malformed boundary fails for the predicted reason. The result upgrades the representation from a globular projection to an actual cubical type skeleton. The next formalization target is the nonconstant common fixture and the theorem that its filler quotient has \(H^2=0\).

## Verification

- `research/voevodsky/agda/CyclicCoherence.agda`
- `research/voevodsky/agda/negative/BadBoundary.agda`
- `research/voevodsky/results/cubical_agda_cyclic_coherence.json`
