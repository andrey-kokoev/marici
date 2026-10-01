# Photon source-witness recovery — iteration 2

## Question

Does the native branching construction supply the primitive comparison witnesses needed to identify the current coefficient phase with spatial transport?

SCC obligations: **forward realization** of the composable-pair carrier, followed by **readout descent**. The source inputs were freshly read. No deterministic routing, S4 edge policy, new spatial carrier, or physical clock was installed.

## Claim boundary

### Correction: the primitive is a row, not an unspecified comparison

`ActualSeedEndpointTable.agda` declares six occurrences, their endpoint functions, and their table. Its six named triangle seam proofs establish equalities of the form

    target(e) = source(f).

These are the witnesses needed to compose adjacent records. They are not equivalences carrying a payload from the source of e to its target. This corrects the iteration-1 framing that six hidden S4 fillers might be recovered as fields of the primitive construction.

The source already distinguishes these roles in `primitive-seed-arrow-role-audit.md`, `seed-seam-native-witness-construction-audit.md`, and `prior-seed-semantics-recovery-after-matrix-domain-gate.md`. Requiring per-edge S4 fillers belongs to an additional adapter, not to the native row datatype.

### What the native constructors actually support

The composable-pair carrier is

    P = Sigma e:Occurrence. Sigma f:Occurrence. target(e)=source(f).

The native `E-header` and `paths-header` supply these carrier constructors. On the supplied endpoint definitions P has ten rows: the six named triangle seams and four additional matches. All matches are definitionally equal endpoint constructors; none specifies a spectator action.

Its two projections give

    Occurrence <-prefix- P -final-> Occurrence.

Neither projection is injective. For example, `(AB,BC)` and `(AB,BA)` have the same prefix; `(CA,AB)` and `(BA,AB)` have the same final occurrence. The generic grouping/recovery equivalence identifies a grouped ten-row presentation with the same ten rows. It does not identify the six-row and ten-row carriers.

`NativeTableRules.compare-kind` still requires an actual supplied equivalence and marked-value proof. Its distribution equivalence repackages supplied dependent data; it does not add rational coefficients. `NativeTableResolution` retains an explicit `Admit` parameter. Representability in this syntax is not a new source-admitted physical derivation.

### Exact recovery of the existing coefficient operation

The registered `RetainedSuccessorLedger` gives the already declared rational realization:

    L = prefix pullback: copy each parent coefficient to every admitted child,
    A = final pushforward: sum coefficients with the same final occurrence,
    K = A L.

Their ranks are respectively 6, 6, and 4. L is reversible onto its image, not onto the entire ten-dimensional coefficient carrier. The existing bilinear path product reproduces L when its right input is the all-ones primitive family. Changing that supplied input changes the operation.

This arithmetic is the declared coefficient realization; the native dependent-sum constructor is not itself numerical addition.

The checker reproduces the exact registered extension and phase-summary squares through three appends, with 6, 10, 16, and 26 retained words. The original coefficient vector returns at three appends, and the previously attached clock reads pi. No temporal authority is inferred from the span itself.

### The phase step is not carried independently by each primitive branch

On the declared plane E with columns `(U,W)`, the full K obeys

    K E = E C,
    C^3 = I.

But every one of the ten individual composable-pair channels has rank one and sends some vector of this plane outside the plane. The same failure holds for all six channels grouped by final primitive occurrence. Only their sum preserves the plane.

For the complex eigenvector `v=U+i*sqrt(3)*W`, each retained child receives its parent's coefficient unchanged. Multiplication by omega appears in the final-occurrence aggregate. It is therefore incorrect to read the aggregate eigenphase as an already supplied phase rotation on every primitive traversal.

This rules out that particular identification on the selected two-dimensional plane. It does not rule out a separately specified larger payload representation whose individual operations leave that plane.

### Spatial readout must retain the appropriate domain

The existing fixed-tetrahedron reader does assign positions to every endpoint path. At three appends, compare

    prepared AB; append BC,CA,AB: displacement (0,0,0),
    prepared CA; append AB,BA,AB: displacement (0,-2,-2).

Both end with AB. The difference of unit coefficient payloads on those two complete words has zero final-occurrence summary but nonzero displacement reading `(0,2,2)`. Thus this spatial reader does not factor through that summary on arbitrary 26-word payloads. This is a linear-reader test, not an expectation value or a particle trajectory selected from the branches.

The hostile is outside the unchanged-copy image, and the checker verifies that fact. **At fixed depth, on the two-dimensional image obtained by copying the original photon plane, the summary is injective.** It can reconstruct that restricted payload when its depth and extension map are retained. The general non-descent result must not be promoted into ambiguity on this smaller domain.

All 26 endpoint paths remain within the supplied tetrahedron; 10 close and 16 do not. This does not decide placement in a larger realization.

### The named larger spatial source does not fill this interface

The remaining sections of `research/chatgpt/marici_native_spatial_three_extension.md` were read. They supply coordinate-ring restrictions, cochain maps, and an equivariant derived comparison for a normalization/conductor complex on occurrence strata. Their domain is not the clocked path coefficient carrier. No map from the latter into that complex, followed by a spatial-position reader, is supplied in the inspected chain. Equal occurrence counts or cyclic incidence matrices do not create this map. Its own physical comparison boundary remains explicit.

## Disposition

**Problem:** recover the source operation behind the proposed photon phase/spatial attachment.

**Conjecture tested:** native composition witnesses already implement local phase/spatial transport, with the coarse period inherited from those operations.

**Rivals:** seam compatibility alone; an aggregate spectral response of a branching span; an additional payload-action adapter.

**Risky consequence:** each recovered branch must admit the claimed phase-plane interpretation, and the proposed spatial reading must descend through any summary used in its place.

**Falsification:** all ten pair channels and all six final-edge channels fail phase-plane preservation; an explicit retained-payload difference defeats spatial displacement descent on the full path carrier. The exact positive survivor is the retained-span/aggregate-phase square, with the restricted injectivity control above.

**Disposition:** stop the search for six primitive comparison fillers in this source. They are not unspecified fields of these rows. The first missing object for the photon claim is a source-defined response/realization map from retained path packages into the intended phase/spatial payload, compatible with the established aggregate update. No such map was recovered, and no policy was chosen to produce propagation.

This reinstates the existing stopping boundary in `two-triangle-cycle-consolidation-and-stop.md`; it is not a claim that every possible native realization is impossible. Resume only when an independently specified response map or a concrete new source locator is available. Repeating filler enumeration, adding another scheduler, or renaming a regrouping as propagation would not be a nonredundant continuation.

## Verification

- `python research/nima/checkers/check_photon_source_witness_recovery_02.py`: passed in a fresh structured-command process. It reuses the registered path implementation and records exact source hashes in `results/photon-source-witness-recovery-02.json`.
- SCC model `nima-photon-source-witness-recovery-02`: passed with the residuals retained, not promoted to physical verification.
- A fresh Agda closure was attempted with `check_cubical_agda.ps1 -Module SeedSeamPathComparisonBoundary -Fresh`. The launch failed before elaboration: `Cannot run a document in the middle of a pipeline: C:\Users\andrey\tools\cubical-agda\agda-2.8.0\agda.exe`. Execution ref: `structured_command_execution:e_25120_1790859160188953700_33`. No old formal receipt is presented as fresh verification; Agda claims here are source inspection, not a new formal pass.
- No new Agda module, transport rule, Git commit, or site/ledger publication was made.
- Internal correction/report admitted as proposal `ep_d3741ce7-7cd9-4680-b2d9-a05c3100efc9`, ledger head `ff57cfda7d6df7c95b7d1bbc4683b8a5e8cf2da25dedef27c7785e7250cac78b`. This communication and the owner-local artifacts have no Git checkpoint; admission is not truth certification.
