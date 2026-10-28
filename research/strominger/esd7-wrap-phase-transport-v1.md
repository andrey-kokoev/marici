# Existing phase-reference operations transported through the ESD7 wrap

## Subsequent continuation

The [complete sector reader atlas](symmetric-sector-phase-atlas-v1.md) now covers every geometric primitive and supplies a species-preserving reference-level lift of geometric duality. It also isolates a native M-plane invariant and a dense-occupancy obstruction. This extends the local pilot below; it does not admit a whole-sector occupied assembly.

## Bounded result

The [record-preserving ESD7 wrap](octahedron-esd7-wrap-v1.md) can carry the **actual existing He-3, He-4 and Li-6 reference phase operations**, including their occurrence witnesses, five coefficient slots, absolute origins and command histories. The supplied source operations were called directly; no replacement phase schedule was invented.

The new checker passes **38 transport checks**, the native JavaScript adapter passes **33 grouped assertions**, and SCC verifies **144 evaluated source-operation/encoding route comparisons**. The checker also freshly reruns the prior **27-check geometric wrap**. These counts describe different verification layers, not independent physical evidence.

This is **not a phase assignment to the entire 679-cell symmetric sector**. The three pilot fixtures collectively touch only **seven whole-cell geometric hosts**. They are separate reference assemblies, not one combined assembly.

No viewer or physical inventory was changed.

## Source and embedding

The unchanged source modules are:

- `demos/particle-overlap-tetrahedron/phase-assembly-model.mjs`;
- `demos/particle-overlap-tetrahedron/phase-advance-model.mjs`;
- `demos/particle-overlap-tetrahedron/phase-discipline-model.mjs`;
- their existing window, coefficient and coverage constructors.

The actual selected fixtures retain their native root markings. Their phase certificates are freshly checked by `auditPhaseAssembly` before any transport.

For the geometry test, each entire fixture, **including every outside reference point**, is embedded using the same declared lattice translation

\[
t=(1,0,0,-1).
\]

This integral, zero-sum translation preserves the native lattice and puts actual carriers across the wrap's two chart seams. It is a coordinate embedding for the pilot, **not an additional physical realization command**. Original coordinates, placement, isotope namespace and occurrence records remain recoverable.

The complete encoding is the existing piecewise-affine map applied to \(q+t\), together with retained source identities. Newly introduced geometric subdivision vertices do not acquire invented native phase occurrences.

## What was transported

| Source fixture | Primitive carriers | Phase charts | Operation edges | Retained certificate states | Actual contacts | Wrapped contact polygons |
|---|---:|---:|---:|---:|---:|---:|
| He-3 | 5 | 6 | 8 | 8 | 4 | 6 |
| He-4 | 6 | 10 | 18 | 26 | 6 | 8 |
| Li-6 | 9 | 13 | 22 | 22 | 9 | 13 |

The operation alphabet exercised is:

- PN;
- inverse-PN;
- NE;
- proton and neutron reader-phase advances;
- NN phase advances.

These are the source's reference laws, not newly derived particle dynamics. In particular, the source's outside-context retention rule remains a declared reference rule after wrapping.

### Actual witness generation, not copied verdicts

Every geometric alias is injectively renamed in an isotope-specific wrapped namespace. The native `phaseFrame`, `phaseAdvanceWitness` and `auditPhaseCombination` functions are run on the renamed charts.

At absolute origins **0, 2 and 17**, two independently executed routes are compared:

1. generate the source witness, then encode its occurrence bindings;
2. encode the marked edge request, then call the owning witness generator.

All 144 comparisons agree exactly. SCC receives hashes of the actual evaluated packets, not arbitrarily equal route names. Its generated wrong-phase control changes one occurrence index and fails the corresponding route comparison.

This establishes compatibility of the existing operations with this encoding. Since the transported operation is obtained by conjugation, it is not an independent prediction or a new law selected by the target geometry.

### Coefficients and histories

For every operation, all five complex basis vectors and a vector with nonzero complex values in every slot are transported and recovered with the actual coefficient permutation. The encoding changes geometric representation, not the coefficient carrier. No projection onto the active three-slot face is introduced.

The full wrapped certificate decodes exactly to the original certificate and passes the owning source validator again. Entry-to-exit coverage survives. Deleting history, erasing a nonidentity coefficient permutation and truncating the carrier to three slots are rejected.

Two forward reader advances can restore the coefficient permutation while advancing the origin from **17 to 19**. The wrapped records keep that distinction. Coefficient return is not realization-history identity. This does not prove or refute the separate conjectured bound on a jointly coherent reference window.

### Contacts across the chart seams

Carrier geometry is split at the actual chart planes. Every physical contact is reconstructed independently from both neighboring primitive carriers. Their wrapped face fragments agree exactly, including contacts crossing a chart seam; matching only three endpoint images would not have sufficed.

The three fixtures produce 8, 10 and 15 carrier chart fragments respectively. Each fragment has the exact inverse and one-quarter coordinate volume under the affine wrap. The original carrier volume is fully retained across its pieces. The check also performs 58, 68 and 89 chart-seam comparisons respectively.

## The important type distinction exposed by the pilot

A **physical phase carrier** is not automatically a **whole geometric cell with the same P/N/E label**.

For example, the fixed root proton of each source fixture embeds in the whole geometric cell labelled `electron:1,0,0,-1`. Its physical species remains proton. Some source electron and neutron primitive carriers occupy different tetrahedral portions of one whole octahedral host. Their identities and species do not merge because that host has geometric role N.

This is not a contradiction: the two labels belong to different constructions. It is a concrete reason not to convert the symmetric sector's **224 P / 231 N / 224 E geometric counts** into a particle inventory.

The pilot binds each primitive carrier to its exact host without imposing label equality. A global physical assignment would require an additional constructor selecting marked primitive carriers, their actual occurrence contexts, and every contact witness throughout the sector.

## What geometric P/E duality still does not supply

The whole-cell involution exchanges geometric P and E orientation classes. It does not by itself specify an action on physical species, C/M occurrences, coefficient slots or command histories.

There is also a concrete warning against one naive proposed lift: in the current reference-operation alphabet, proton reader advances exist while **electron charts are terminal and have no reader advance**. Calling `phaseAdvanceWitness` on an electron reader is rejected by the owning source function. Thus a species-exchanging, reader-preserving equivalence is not supplied by this alphabet.

This is a scoped obstruction to that proposed species-exchanging lift, **not a theorem forbidding every full-state lift of geometric duality**. A geometric orientation exchange need not exchange physical species, and a separately sourced larger operation category could change the question. Neither extension is manufactured here.

## Next constructor, precisely

The next missing object is not another coordinate map. It is a **whole-sector marked phase assembly**, specifying:

1. which primitive carriers are occupied or used as references;
2. their source-authorized physical species and C/M occurrence bindings;
3. their five-slot coefficient carriers and outside contexts;
4. an allowed operation and witness for every actual shared contact;
5. retained route histories and compatibility of competing routes;
6. any desired full-state duality, separately from geometric inversion.

Only after that object exists can the successful local transport be extended and tested across the whole sector. The present wrap cannot generate missing source operations, turn seven touched hosts into 679 admitted phase carriers, or derive 82/126/82 by relabelling geometry.

The two-cycle/256-record conjecture, physical mode descent and stability remain separate unresolved gates.

## Verification and durable artifacts

- [Attempt contract](contracts/esd7-wrap-phase-transport-v1.json).
- [Native operation adapter](checkers/export_esd7_wrap_phase_inputs.mjs).
- [Exact transport checker](checkers/check_esd7_wrap_phase_transport.py).
- [Verification](results/esd7-wrap-phase-transport/verification.json).
- [Native and wrapped phase records](results/esd7-wrap-phase-transport/native-and-wrapped-phase-records.json).
- [Exact geometric contact witnesses](results/esd7-wrap-phase-transport/wrapped-geometric-witnesses.json).
- [Evaluated route diagram](results/esd7-wrap-phase-transport/phase-route-diagram.json).
- [Categorical verification](results/esd7-wrap-phase-transport/categorical-verification.json).
- [Wrong-phase route control](results/esd7-wrap-phase-transport/wrong-phase-route-verification.json).
- [SCC manifest](scc-models/esd7-wrap-phase-transport-v1.json).

```sh
python research/strominger/checkers/check_esd7_wrap_phase_transport.py
python research/aspect/scc/scc.py check esd7-wrap-phase-transport-v1
python research/aspect/scc/scc.py categorical research/strominger/results/esd7-wrap-phase-transport/phase-route-diagram.json
python research/aspect/scc/scc.py inverse research/strominger/results/esd7-wrap-phase-transport/phase-route-diagram.json whole-sector-phase-transport
```

The first categorical run found a missing `degree` field on the explicitly unsupported global-coherence placeholder. Adding that schema field repaired the integration; no failed scientific comparison was reclassified. The final checker was frozen at `b425d1a5473ed41e58e64e5c3e8d54f66f5718bddd10b58c67adb4ac3158e3f4` and passed a fresh SCC-managed execution, including a fresh headless replay of the geometric wrap. Higher whole-sector coherence remains explicitly unsupported in the diagram.

No Rzk or Agda theorem, full-sector phase model, nuclear stability result or viewer admission is claimed.

Graph report: proposal `ep_f47a5375-26c7-4c0b-985e-4d233f15c65d`, addressed separately to `marici.Nima` and `marici.Voevodsky`. Policy admission records the report, not scientific truth.
