# Reference checks form a higher fault complex

## Question

What happens when the cycle checks used to diagnose reference relationships
can themselves be faulty?

## Higher construction

A reference graph is only the first two levels of a complex. Vertex frames,
edge relationships, face checks, and checks among face checks form

\[
C^0 \xrightarrow{d_0} C^1 \xrightarrow{d_1} C^2
\xrightarrow{d_2} C^3,
\]

with

\[
d_1d_0=0,
\qquad
d_2d_1=0.
\]

An edge fault produces a face syndrome in \(\operatorname{im}d_1\). A faulty
face check adds a component outside that image. The next differential tests
whether the observed face syndrome is itself coherent.

## DPC

The smallest closed finite witness is the tetrahedron:

- four vertex frames;
- six edge relationships;
- four triangular face checks;
- one tetrahedral relation among the face checks.

The proposal predicts:

1. Vertex-gauge changes produce no face syndrome.
2. Genuine edge-fault syndromes satisfy the tetrahedral relation.
3. A single edge fault flips exactly the two faces incident on that edge.
4. A single face-check fault flips exactly one face result and violates the
   tetrahedral relation.
5. The ten signatures from six possible edge faults and four possible
   face-check faults are distinct, so one fault of either type is located.
6. The kernel of the edge-to-face map is still exactly the vertex-gauge image.
7. A representation of stabilizers on attached readout fibers is required;
   the abstract stabilizer group alone does not determine how higher faults act
   on capabilities.
8. Certification cannot terminate internally at an untrusted top cell. A
   fault in the top checker requires another level, temporal repetition, an
   independently trusted readout, or an explicit terminal fault assumption.

## Resolution

The exact binary checker verifies the tetrahedral complex and exhaustively
enumerates all ten single-fault signatures. It proves that adding one higher
cell converts the triangle's detection-only result into single-fault location
for both relationship faults and face-check faults.

It also isolates the stopping law:

> Every attempt to correct faults in a coherence witness promotes the witness
> to data and requires a higher coherence witness.

This is not a vicious infinite regress when the architecture declares a fault
boundary. It becomes one when a finite system claims unconditional internal
self-certification. A realizable system must state where the tower terminates
and why the terminal observer is trusted, repeated, externally compared, or
excluded from the admitted fault model.

## Cross-sector consequence

The same distinction appears when an abstract symmetry is known but its action
on physical fibers is not: group structure is a check type, while the
representation is the incidence map that makes it operative. Likewise, a
dynamically forced interaction support is a higher compatibility relation; it
does not select the interaction's numerical value.

## Claim boundary

The theorem is finite and binary. It does not construct a physical tetrahedral
apparatus, a nonabelian higher gauge theory, or a terminal trustworthy
observer. It does not claim that all coherence towers must be spatial; time
repetition and independent implementations may supply equivalent higher
checks.

## Disposition

The higher DPC passes. One extra coherence dimension corrects one fault in
either relationships or their checks. Unconditional self-certification remains
impossible without a declared terminal trust or fault boundary.
