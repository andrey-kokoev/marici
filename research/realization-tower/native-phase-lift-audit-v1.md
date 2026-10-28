# Native phase lift: successor recovered and geometric forgetting tested

## Correction from current prior work

The newer [phase-first assembly](../strominger/phase-first-assembly-v2.md)
supersedes the mixed-index reader constructions. The old helium-core geometry
remains useful, but its unresolved reader/exit status is not the frontier of
all subsequent research.

The current phase-first helium-4 reference supplies six-carrier coverage and
history-bearing entry-to-electron-exit witnesses under its explicit advancing
C/M and outside-context laws. Those laws are supplied reference structure,
not a derived physical interaction.

## Fresh execution on current owning APIs

Imported `selectPhaseAssembly`, `auditPhaseAssembly`, `phaseAdvanceWitness`,
`applyPhasePermutation` and `spectralReadout` directly. Results:

- all **6 carriers** covered; every entered certificate state reaches an exit;
- **18 actual transition edges** checked;
- every full five-slot map passes inverse recovery on a generic complex packet
  and all five basis vectors;
- active spectral readout reconstructs the retained coordinates;
- phase-advance edges carry the declared occurrence and context witnesses;
- the exact six-body geometry fits within the six-step octahedral region under
  **10** tested integer lattice translations, without altering its shapes.

This last result is geometric containment, not an assertion that its entry and
exit centres equal the octahedron's two vertex probes. It neither assigns its
six-carrier census to the whole region nor constructs Pb-208.

## Explicit obstruction to identifying full records by geometry

For an actual same-body neutron re-reading, the current source implements

    [alpha,a,b,c,beta] -> [alpha,c,beta,a,b].

Two forward applications restore all five coefficients and the same geometric
body/chart positions. But the phase frame has advanced from origin 0 to origin
2, with distinct retained occurrences and history. The checker verifies:

    coefficients_after_two = coefficients_before,
    geometric_positions_after_two = geometric_positions_before,
    full_phase_frame_after_two != full_phase_frame_before.

Thus equality of geometric route or even geometry-plus-coefficients does not
license identifying native records. A geometric chain filler is not by itself
a native reader comparison that erases this difference. This does not prohibit
a lift retaining the difference as additional witness data.

Negative controls reject frozen C occurrences, an otherwise locally valid frame
that skips a phase, and an altered map suppressing context-to-active transfer.

## What remains of the requested cross-branch lift

The current native target is now explicit and tested. The existing geometric
comparison system supplies routes, integral face chains and volume fillers.
These have different types from the native assembly's carrier charts,
occurrences and five-slot transition maps.

No source-selected map assigning every one of the 400 shortest vertex paths
and 1,200 face comparisons to those native objects was supplied or constructed
in this audit. Calling the geometric fillers native because both carry
witnesses would skip that obligation.

A valid next adapter must retain:

- the carrier chart and source/target marking;
- absolute C/M origin and occurrence identities;
- all five coefficients, including outside context;
- full transition history and comparison witnesses;
- compatibility of each proposed geometric face/volume comparison with those
  native transitions, rather than only its additive chain boundary.

The audit establishes a source-backed target and a concrete failure control,
not a completed global lift or isotope derivation.

## Verification

```sh
node research/realization-tower/check_native_phase_lift.mjs
```

Fresh result: **PASS**. [Receipt](results/native-phase-lift-v1.json) retains
all embedding coordinates, the actual two advances and the generic packet.
No owning result files were overwritten. No formal closure, proof promotion or
new task admission was performed.
