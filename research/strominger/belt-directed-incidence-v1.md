# Belt directed-incidence test: radial failure, axial candidate, retained defects

## Source and prospective scope

Obligations: forward realization, attachment transport, route/coherencer compatibility. Protocol: `inputs/belt-directed-incidence-protocol-v1.json`; checker: `checkers/check_belt_directed_incidence.py`; receipt: `results/belt-directed-incidence/verification.json`. SCC freeze: `409db187a86d00c8`.

Replay the existing real-complex arrow frontend and unchanged geometry/cycle assembler in memory. The decoded source, complete geometry and cycle match the retained source outputs exactly. The coordinate permutation `(r,a,b) -> (b,r,a)` identifies all six generated moving faces with the original belt geometry. The positive physical x scaling changes determinant magnitude, not its sign.

The prior directed-incidence rule is `beta_d(u,v)=-det(d,u,v)` with d a directed body-center/face-center displacement. The old calibration is retained. The source arrow record supplies angular motion, not a selected incoming/outgoing radial execution; both radial interpretations are therefore tested explicitly, rather than attributing one to the source.

## Exact outputs

Signs are relative to the six stored outward face orders. Each face's three centroid-edge triangles has one third of its oriented area, so the test covers all eighteen local modes.

| Direction used | Signs |
|---|---|
| Global center to face | -,-,-,-,-,- |
| Face to global center | +,+,+,+,+,+ |
| Constituent tetrahedron center to outer face | -,-,-,-,-,- |
| Outer face to constituent center | +,+,+,+,+,+ |
| Actual scheduled centroid chord | +,+,+,+,+,+ |
| Common upper-to-lower rim axis | -,-,-,+,+,+ |
| Required opposite-branch assignment | -,-,-,+,+,+ |

Thus neither uniform radial interpretation reproduces the target: each mismatches three faces/nine triangles. A different global volume convention merely reverses the uniform pattern. The actual angular chord is also not a body-to-face displacement; it is a separately reported diagnostic, not a licensed substitution.

The common axial vector `(0,-7/10,0)` DOES reproduce the target without per-face fitted signs. Its endpoints are the two retained rim centers, not an invented external vector. This gives a precise candidate extension: use the same ambient-volume contraction with the common directed rim axis. It does not establish that the prior radial rule already meant that axis, or select which rim is source. Reversing the axis reverses all branches. The axial candidate was declared in the prospective protocol before execution.

## Full interface records and transport

Extend each outer sign uniformly to its corresponding positively oriented tetrahedral constituent, exactly as in the prior face-gluing audit. The alternating signed three-chain has six nonzero internal triangular boundary coefficients, all of magnitude two. Exhausting all 64 sign assignments leaves only the two uniform assignments internally seam-free.

The native C3 permutation is reconstructed from the actual inferred arrow action, not from a desired sign map. On every one of the 64 signed chains the exact chain comparison

    boundary(T c) = T boundary(c)

holds, and inverse transport recovers the complete chain. For the alternating chain, C3 preserves the full signed boundary and all six residual faces individually as a set with coefficients. Boundary-of-boundary vanishes. This proves consistent retention and transport of defects, not their cancellation. No extra filling cell or interface mode has been inserted.

These six internal triangular defects are not the 21 selected-mode amplitude seams or their six memory-kernel directions. No identification between these inventories is asserted.

## WG attachment status

Inspected `SeedGeometricResponseState.agda`, `SeedJointParityResponse.agda` and `ActualSeedEndpointTable.agda`. The finite update equations are checked against the actual source text: AB flips the first parity bit, BA the second, and the remaining occurrences preserve them. This is a source audit, not proof extraction or a fresh Agda compilation.

That WG operates over the connected four-vertex source with six occurrences AB,BC,CA,AD,DB,BA. The belt source has six vertices in two separate directed three-cycles and no reciprocal occurrence pair. Equal occurrence counts do not identify these domains. The tested records do not provide a map assigning the WG states, paths or parity questions to belt faces and their integer-valued internal boundary records.

Consequently the requested WG-specific defect-carrying square remains **unestablished**, not rejected by a no-go theorem. The geometry-level chain square above is available as its target specification, but is not relabelled as a WG theorem. The unchanged radial-generation conjecture already fails upstream; the axial extension and a typed WG-to-belt attachment are separate unverified constructions.

## Verification

Fresh focused execution: eight checks pass, including in-memory source replay and all 64 chain transport/recovery controls. Targeted SCC check and frozen challenge both pass; these accept the bounded audit including its negative scientific result. Global SCC enumeration/dashboard returned nonzero in the shared registry; no unrelated entries were repaired.

    python research/strominger/checkers/check_belt_directed_incidence.py
    python research/aspect/scc/scc.py check belt-directed-incidence
    python research/aspect/scc/scc.py challenge belt-directed-incidence research/strominger/checkers/check_belt_directed_incidence.py survives

Only owner-local files were written. Sources are hash-bound and checked unchanged. No Agda theorem, physical branch-selection claim, commit or push is made.
