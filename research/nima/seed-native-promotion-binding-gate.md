# Actual seed to native promotion: the filled-source binding gate

## Result

The actual six-arrow table is already formalized and its source/target reindexings recover exactly. The attempted next binding into the inspected filled-tetrahedron feedback instance fails earlier than numerical preparation: there is no source-preserving horn, surface, or complete tetrahedron with the declared seed skeleton in the existing free geometric realization.

This is stronger than saying two face witnesses have not been located. Prior `SeedFaceObstruction` proves that those particular types are empty. The new module carries that existing fact through the exact input contract of the candidate promotion branch.

It does not prove that the intended T9 is impossible, nor that native feedback needs a filled tetrahedron for every payload. It rules out this specific source-preserving filled-payload interpretation.

## 1. What the actual source supplies

`ActualSeedEndpointTable` has precisely the six occurrences

    AB, BC, CA, AD, DB, BA.

Its labels are the occurrence identities. Its source/target maps are the actual A,B,C,D endpoint assignments. It already proves the endpoint matching of both directed triangles and source-index recovery. `TableFibrationCycle.restore-correct` supplies target-index recovery as well.

Those constructions do not turn occurrences into payload equivalences, add face equations, or replace AB with the separately retained BA on reversal. The vertical presentation part is available without a matrix model or tetrahedral filling.

## 2. The exact attempted horizontal input

The candidate traced in `native-promotion-constructor-trace.md` acts on a retained comparison whose payload is a filled tetrahedron. To bind the free seed to that branch, `SeedTetrahedronBridge` fixes the vertex order A,D,B,C and the edge skeleton:

    e01=AD, e12=DB, e02=AB,
    e23=BC, e13=DB followed by BC, e03=reverse CA.

BA remains independent and must not be silently absorbed into reversed AB. The obstruction below already occurs without requiring any BA identification.

A surface with these edges necessarily contains

    AD followed by DB = AB,
    AB followed by BC = reverse CA.

These are faces in the chosen path realization, not merely common endpoints of parallel paths.

## 3. Existing source probe rules out those faces

The free realization has a vertex point and a path constructor for every supplied occurrence, with no face relations. `SeedFaceObstruction.Probe` is a valid Boolean family on that realization: crossing AB flips its fiber; every other primitive preserves it.

Starting at false:

| Source path | Transported reading |
|---|---|
| AD followed by DB | false |
| AB | true |
| AB followed by BC | true |
| reverse CA | false |

Equality of either path pair would force equality of the corresponding readings. Thus neither required face exists in this realization. This probe is a mathematical separator, not a newly selected physical detector.

## 4. New formal binding theorem

`agda/SeedNativePromotionBindingGate.agda` proves:

- `no-source-horn`: no horn over the declared vertices whose edge package equals the original skeleton;
- `no-source-surface`: no such complete surface, using the forward face;
- `no-source-surface-abc`: the independently available ABC obstruction also rejects it;
- `no-source-package`: adding a filler cannot repair that missing surface;
- `no-source-full`: allowing propositional vertex identification and transporting the package still cannot produce the required skeleton;
- `spine-not-source`: the existing inhabited spine construction cannot have the required original edge package.

The last result checks the relevant positive control: a filled tetrahedron exists when independent diagonals are replaced by composites. Its existence is not evidence that the unchanged seed has been filled.

The same module retains the actual source/target table recovery and the already inhabited forward and return path-question records. Their direct and indirect paths remain distinct.

## 5. Corrected structural disposition

The earlier wording "supply the two missing faces" was too weak for this particular source interpretation. One cannot supply inhabitants of types already proved empty while keeping that interpretation unchanged.

There are distinct possible directions:

1. **Remain in the free source:** retain the parallel paths as questions/discrepancies and seek the intended constructor on that object. Do not require them to be equal just to enter a filled-payload adapter.
2. **Use a different interpretation:** map the free source into a setting where selected faces exist. Declare which distinctions the interpretation forgets and which original occurrence/probe records remain alongside it. This is not filling the original free realization itself.
3. **Use the existing admitted filled fixture:** continue its conditional feedback calculations, but do not present it as generated from the unchanged six-arrow seed.

No choice among these is made merely to obtain a commuting square. In particular, applying generic feedback to an arbitrary atomic wrapper of the seed would establish packaging/retention, not that the intended T9 was recovered.

The most source-conservative next object is already present: `SeedSeamPathComparisonBoundary.ForwardQuestion` and `ReturnQuestion`. Their existence does not supply an equality witness, an action on them, or a physical response. The horizontal-constructor search should use that question-bearing boundary rather than continue through the now-rejected free-seed-to-filled-tetrahedron binding.

## Relation to the confirmed diagram

- Left vertical maps: actual seed-table reindexing is available.
- Candidate filled-native input to T9: rejected under the frozen free-realization/skeleton interpretation.
- Intended T9 on retained questions: not yet identified by this result.
- Right table presentation and rung4 observation: cannot be inherited from the rejected binding; they still require the actual chosen constructor.
-137-row matrix fixture: not invoked or modified. This gate precedes its amplitude, memory, and detector questions.

This is a scoped source-constructor gate, not another compatibility test between unrelated numerical dynamics.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module SeedNativePromotionBindingGate -Fresh

Fresh safe/cubical/guardedness closure passed with ignored interfaces and stable inputs. The dependency closure includes the actual endpoint table, table reindexing, seed realization, face obstruction, and retained free-path questions. No postulates, hole fillings, face identifications, or changes to existing update laws were introduced.

Receipt: `results/agda-SeedNativePromotionBindingGate.json`.

The earlier native feedback trace was not changed by this gate. Its positive theorems remain valid on its admitted filled input; the new result prevents identifying that input with the specified unfilled source.
