# Historical phase audit: withdrawn admission and necessary checks

**Superseded for the current viewer:** see
[phase-first assemblies v2](phase-first-assembly-v2.md). The corrected He-3,
He-4 and Li-6 reference constructions advance both phase families, carry context
into the active window, and retain complete phase histories. The frozen-C and
mixed-index models audited below remain withdrawn; their failures do not prove
that explicit phase-advancing comparisons are impossible.

## Correction

The Li viewer assigned C/M suffixes by sorting geometric vertices and counting
them. Those numbers were not derived realization-phase occurrences. This was
incorrect. Invertible five-slot maps, norm preservation, geometric closure,
and entry/exit reachability did not repair or test that error.

The Li construction is **withdrawn**, including its selector and published
model assets. No replacement phase-admitted Li construction has yet been found.
Research instantiation now requires `researchOnly: true`, returns
`status: 'unadmitted'`, and exposes its failed phase audit. Its geometric IDs
are neutral `vertex-*` names, never automatically generated C/M phase indices.

## Separate the data

- A geometric vertex has an opaque coordinate-based or neutral ID.
- A phase occurrence has an explicit C/M role and integer index.
- A tetrahedron has an ordered three-occurrence window and fourth context.
- A reader occurrence has its own identity and, when known, a declared origin.
- A combination must supply explicit interface/occurrence identifications.

Neither vertex coincidence nor equal complex coefficients identifies two
phase occurrences. A coefficient's omega exponent is not a replacement for its
realization-occurrence index. No modulo quotient or jump is inferred.

The implemented gate uses the existing source templates, not a new invented
particle grammar:

```
P: C0 M0 C1 [M1]
N: M0 C1 M1 [C2]
E: M1 C1 C2 [M2]
```

It checks ordered roles, local phase spacing, context, distinct tetrahedron
vertices, and consistent phase origins across explicitly identified shared
occurrences. Declared origins cannot be overwritten to force a match. PN and
NE must use their target window as the shared interface. Combinations must
be connected by supplied relations. Unknown NN or reader-comparison steps
remain unadmitted without a phase witness.

An explicit same-channel successor `M2 -> M4` is rejected; `M2 -> M3` passes
that necessary check. This is not a claim that every visit or inverse traversal
is a forward successor. Repeated occurrences and inverses need their own
specified relations rather than being silently reinterpreted as successors.

These are **necessary retained-template checks**, not a completed universal
phase theory. More general transitions or distinct phase occurrences at the
same geometric point need explicit witnesses. This gate does not manufacture
such witnesses to admit a desired isotope.

## Concrete NN failure

The old NN proposal identifies these shared face slots:

| Shared geometric vertex | Source phase occurrence | Target local occurrence | Required target-origin shift |
| --- | --- | --- | ---: |
| M vertex | M1 | M0 | +1 |
| first C vertex | C1 | C1 | 0 |
| second C vertex | C2 | C2 | 0 |

There is no single target realization origin satisfying all three demands.
Changing an omega factor or preserving all three numerical face coefficients
does not fix this mismatch. Choosing a different origin separately for each
vertex would destroy the tetrahedron's local phase discipline.

All **240** previously algebra-compatible Li assignments fail the phase gate.
Their old permutation-order and geometry results survive only as diagnostic
algebra, not as admitted realizations.

## He-3 / He-4 also require repair

The audit is not limited to the newly numbered Li vertices. For example, the
old second-proton window `C3 M1 C2 [M0]` cannot be one shifted instance of
`C0 M0 C1 [M1]`: its required offsets disagree even within the tetrahedron.
Other mixed-index windows and reader comparisons also remain unresolved.

The viewer therefore retains He-3 and He-4 only as **geometry under review**,
using neutral vertex labels and no phase coverage claim. The native single
P/N/E packet passes the necessary source-template checks. This does not admit
the separate assumed two-cycle boundary identification.

## Viewer controls

Only **Previous item** and **Next item** remain. They undo/replay assembly
DISPLAY prefixes with stable geometry. This is not a transport loop or a law
requiring one atom to grow into the next one item at a time. The reference
transport methods are no longer exposed through the viewer API.

## Verification

- `node research/strominger/checkers/check_phase_discipline.mjs`
- `node research/strominger/checkers/check_fiber_space.mjs`
- Receipt: `results/phase-discipline/verification.json`
- Current UI receipt: `results/fiber-space/verification.json`
- Withdrawn Li algebra receipt: `results/lithium6-assembly/verification.json`

Checks cover the local templates, phase gaps, incompatible declared origins,
shared-face contradictions, explicit occurrence identification, conservative
rejection of unsupported interfaces, and assembly-display reversibility.
Browser checks verify exactly two action buttons, no Li selector, neutral
labels for unverified geometry, stable meshes, and desktop/mobile behavior.

Next research step: supply phase-admitted tetrahedron and interface assignments
for a whole assembly before rendering it as a realization. No old candidate
is admitted merely by changing its labels.
