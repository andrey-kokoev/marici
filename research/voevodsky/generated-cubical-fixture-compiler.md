# Generated Cubical Agda fixture compiler

## Question

Can the declared cyclic signature, common fixture, and SCC overlay be translated deterministically into a native Agda module whose semantic obligations are checked rather than copied as statuses?

## Claim boundary

The compiler validates the declared fixture interface and generates a module importing the checked integer realization. It does not derive the descriptive analytic and arithmetic sorts from their source packets, and therefore does not establish source-global naturality.

## Construction

`generate_cubical_agda_fixture.py` reads the cyclic signature, common interface, SCC overlay, and `native-cubical-fixture.v1.json`. The native contract gives explicit source and target sort identifiers, composable edge paths, oriented faces, chain bases, integer boundary matrices, completion data, and residual-promotion fields. The generator checks those interfaces and emits `RHGeneratedFixture.agda` with its boundary maps computed from the JSON matrices, plus chain, exactness, and completion obligations.

The generator performs no subprocess execution. Agda typechecking remains a separate governed command.

## Strongest falsification attempt

Six semantic mutations are required to fail before generation: clockwise orientation, a nonparallel edge cell, reversed transport A, dropped completion preservation, inserted promotion authority, and promotion of source-global naturality. All six were rejected. A seventh mutation flips the first incidence coefficient in the structured matrix; it is intentionally emitted, and Agda rejects the resulting chain theorem with `a + a != 0`.

The source signature contained a stale contradiction: `cycle_cell.status` and `global_coherence_modality` denied fixture inhabitation while `realization_state.Omega_ABC` asserted it. Those fields were repaired to the demonstrated fixture-level status before generation.

## Disposition

The JSON-to-Agda fixture pipeline passes and the generated module typechecks with Agda 2.8.0 and Cubical 0.9. Acceptance now combines descriptor validation, hostile mutation rejection, deterministic generation, and native typechecking. The remaining first missing arrow is a source-derived interpretation of the descriptive sector sorts and maps.

## Verification

- `research/voevodsky/checkers/generate_cubical_agda_fixture.py`
- `research/voevodsky/agda/generated/RHGeneratedFixture.agda`
- `research/voevodsky/results/cubical_agda_fixture_generation.json`
