# DG pyramid final requirements matrix — iteration 10

## Status

The bounded reusable interface objective is complete. This does not assert existence of a physical pyramid inhabitant; current offline material still lacks the independently specified physical Q/support comparison.

| Requirement | Checked implementation |
|---|---|
| Boundary with J, Q, F | `DGPyramidBoundary`; fields `SourceObj`, `GenericObj`, `SupportedObj`; mathematical accessors `J`, `Q`, `F` |
| q, e, h_M, H_C | record fields `q`, `e`, `hM`, `HC`; accessors `h_M`, `H_C` |
| Differential equations | `morseFace`, `eClosed`, `conductorFace`, `compositionBoundary` |
| No filler in boundary | boundary module ends with an explicit exclusion; filler types occur only in `DGPyramidFiller` |
| Discrepancy H_C - e composed with h_M | `pyramidDiscrepancy`, `namedDiscrepancyEquation` |
| Internally derived closure | `pyramidDiscrepancyClosed`, `namedPyramidDiscrepancyClosed`; no closure field |
| Degree/sign rejection | compile-fail `BadDGPyramidDegree`, `BadDGPyramidLeibnizSign` |
| Hom-zero framed fibre | `Hom⁰JF`, `AdmissibleFiller`, `admissibleFillerShape` |
| Separate support/endpoint/Q/Rees predicates | `PreservesSupport`, `PreservesEndpoints`, `PreservesGenericQ`, `PreservesReesCartier` |
| No automatic frame promotion | only `forgetFrame`; `emptySupportHasNoAdmissibleFiller` regression |
| Normalized nonzero source control | `normalizedSourceCannotBeBoundary` |
| Endpoint jet-annihilation control | `EndpointJetControl`, `literalEndpointRouteIsZero`, `precomposedEndpointRouteIsZero` |
| Target triangle provenance control | `TargetTriangleMasquerade`, impossibility by origin and independently by normalization |
| Future concrete maps | `AdapterSpecification`, map actions and validity predicates; applied source/generic/target accessors |
| q/e/h_M/H_C comparisons | four realization functions and four identifying paths in `DGPyramidAdapter` |
| Both endpoint connectors | separately typed plus/minus connector fields and witnesses |
| Q and Rees/Cartier adapter framing | separately typed comparison cells and validity witnesses |
| Adapter cannot create filler | `AdaptedFiller` requires an existing `AdmissibleFiller` |
| End-to-end positive regression | nonphysical `DGPyramidFixture` |
| Aggregate checked surface | `DGPyramidArchitecture` |

## Final verification

Fresh mutable state was inspected. `relative_morse_fibre_comparison_proof.md` remains the newest offline result and explicitly stops short of the physical Q/support roof, so no physical adapter instantiation is justified.

Six positive interfaces were deleted and rebuilt from the aggregate with Agda 2.8.0.1 and Cubical 0.9 under `--safe --cubical --guardedness`: exit 0, no warnings. Both expected-failure controls exited 42 and matched their required degree/sign diagnostics. Final harness result: `FINAL_SUITE=PASS`.

There are no holes or postulates in the added modules. No Git operation or analytic-interface change was performed.
