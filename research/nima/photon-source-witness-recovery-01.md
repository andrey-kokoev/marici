# Photon source-witness recovery — iteration 1

## Question

Recover the primitive comparison witnesses from the native construction and test their joint phase/space action without selecting a rule to produce propagation. This is the operator's requested source audit, not permission to install either conditional edge policy from `photon-spatial-phase-return.md`.

SCC obligation: **attachment transport**, at the interface between actual source comparisons and the six-packet continuation. Stratum: the exact directed seed, its declared coefficient plane, and the existing tetrahedral area representation. Physical time and propagation are not inferred from this finite calculation.

## Claim boundary

The audit follows the concrete Agda inputs, rather than just the generic compare-rule signature:

| Source operation | Recovered action | Test against the photon continuation |
|---|---|---|
| `WholePackageSigmaPiInstance.package-comparison` | Uses `R.recordLift` | Preserves the original source and trace; their coefficient readers cannot implement the nonidentity phase step |
| `SeedAttachedObserver.O.expansionIso` | Projects canonical traces to their original source sections | Re-presentation, not a next-edge operation |
| `NativeTableRegression.actual-filler-equivalence` | `idEquiv` on the supplied filler | Retains the equivalence; does not select another one |
| `BoundaryGeneratedQuestions.swap-filler` | Swaps coordinates of `Bool × Bool`, fixing `(false,false)` | Actual witness, but not yet a map on seed vertices or packet occurrences |
| Nonidentity automorphism of the actual six-arrow seed | `(AB)(CD)` on vertices | Joint coefficient/spatial symmetry, not continuation |
| `SeedAttachedObserver.cycle` | Section `(AD,BC,CA,DB)` | Induces a four-cycle but omits AB/BA and fails the photon-plane test |
| `SeedAttachedObserver.other` | Section `(AB,BC,CA,DB)` | Its target map is nonbijective, so it is not an S4 equivalence of vertices |

The last two are source sections, not originally declared comparison fillers. Testing their target maps as candidates does not promote them to physical transport.

### Recovered record comparison versus the coefficient update

`DependentSigmaPiCoherence.Retained` instantiates the record construction with the inverse of `routeA`. The concrete equivalence is

    (q, trace, p) -> (q, trace, cong(e, p)),
    e = inverse(routeA).

`ProofRelevantCoherenceClosure` supplies `source-retained`, `trace-retained`, and `witness-transported`. The map is not identity on its whole typed package: the comparison path changes type. It is identity on every reader factoring through the retained pair `(q,trace)`.

The present photon coefficients are read from retained packet coefficients, not from a separately supplied comparison path. On their basis `(U,W)`, the continuation acts by

    C = [[-1/2, 1/2], [-3/2, -1/2]],
    det(C-I) = 3.

Consequently the record-preserving operation cannot implement this step on any nonzero vector of the photon plane through that reader. The first-step seed is `(-1/2,1/2,-1,1/2,-1/2,1)`, rather than the original seed. Recovering an equivalence has not established that it is the needed operation.

### Joint action that does follow from the seed

Parsing the six directed arrows from `SeedAttachedObserver.agda` and exhausting their vertex relabellings gives exactly identity and `s=(AB)(CD)`. No identification of Boolean points with vertices is used.

In packet order `(AB,BC,CA,BA,AD,DB)`, this symmetry exchanges the first and last triples. Its matrix S obeys

    S K = K S,
    S [U W] = -[U W],
    rho(s) = diag(1,-1,-1).

The actual target-incidence spatial reader intertwines S with this existing proper area action. Transporting complete packet words also commutes with prefix extension. The checker verifies this on the histories at depths zero through three, retaining all 6, 10, 16, and 26 words respectively.

This transport preserves the attached clock value and does not append a packet. Its coefficient action is `-I`, not C or any power of C; `det(C+I)=1` rules out agreement with one continuation step on every nonzero vector. It transports the endpoint task A->B and its reverse, but none of the other four seed arrows. The body centre remains fixed.

This is a joint relabelling law, not a photon motion law. A symmetry that commutes with an update is not that update.

### The source-selected four-cycle is not the six-packet update

The unit-family adapter has exactly four source sections. Interpreting a section as choosing one outgoing arrow per source gives a deterministic routing. Each routing keeps four of the six arrows; all four send the current seed outside its photon plane.

Only the explicitly named `cycle` has a bijective target map:

    A->D->B->C->A.

Its existing area action has order four and fixes the body centre. But it omits AB and BA, whose prepared coefficients are nonzero. It is not even a relabelling automorphism of the unchanged six-arrow seed: AB and BA would become DC and CD. Thus neither its spatial return nor its name licenses replacing the branching continuation by this selected routing.

The Boolean swap's image `(0,2,1,3)`, the seed symmetry's image `(1,0,3,2)`, and this section's image `(3,2,0,1)` refer to distinct typed constructions. Equal carrier cardinalities do not identify them. S4 is used here only for permutations of the declared four vertices, not as the automorphism group of a Boolean algebra.

## Disposition

**Problem:** the previous spatial test required witnesses absent from the six-packet endpoint description.

**Conjecture tested:** an already supplied native comparison or explicit source section implements the current continuation and determines its spatial action.

**Rivals:** record re-presentation; seed relabelling; a selected four-edge routing; genuinely branching continuation through the retained composable-pair carrier.

**Risky consequence:** the recovered operation must match K on the full declared photon plane while retaining the same input/output packet types, not merely share a return period.

**Falsification:** the recovered record map preserves source readers (`det(C-I)=3`); the seed symmetry acts by `-I` (`det(C+I)=1`); all four deterministic source sections fail plane preservation. The explicit Boolean witness has no supplied vertex/packet identification in this audited chain.

**Surviving scope:** a concrete source comparison and a joint seed-symmetry action are recovered, but six primitive comparison witnesses implementing the photon update are not. The candidate substitutions above are rejected, not repaired by fitting a transport policy.

### Nonredundant executable continuation

Inspect `NativeTableRules.agda`, `NativeTableResolution.agda`, and the indexed composition source for the actual composable-pair span

    six occurrences <- ten composable pairs -> six occurrences.

The current retained continuation already uses this branching domain. The next test is whether the native constructors supply its typed operation and retained witnesses, rather than assuming a continuation must be a four-vertex bijection. It must reproduce prefix extension and the existing phase-summary square before any spatial attachment is evaluated. This is not a request to choose one branch or another edge policy.

### Verification

`python research/nima/checkers/check_photon_source_witness_recovery_01.py`

Passed in fresh structured-command processes, directly and through SCC model `nima-photon-source-witness-recovery-01`. Exact rational arithmetic; Agda source equations and source hashes audited; **no fresh Agda elaboration claimed**. Result: `results/photon-source-witness-recovery-01.json`.

Internal report and operator stimulus were admitted under proposal `ep_1bbefa1e-70d2-42d6-b8bf-d452eecb136e` (ledger head `4f8cca33e9fbc9e83a25c6cc3ad8b9e94a318ae6f641ab0c4b89f8d1822f42a3`). This is communication provenance, not scientific certification. The contribution and owner-local artifacts remain without a Git checkpoint; no Git commit or site/ledger publication was performed.
