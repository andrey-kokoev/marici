# Full seed spectrum through retained rung presentations

## Existing components reused

`check_natural_tower_return.py` derives incoming incidence M from the actual six labelled seed occurrences and checks all four eigenvalues/projectors. It now returns these checked descriptors for reuse; its existing assertions remain intact.

`check_rung_transport_diagram.py` supplies the actual source/target indexing, two candidate two-stage incoming promotions, retained leaves and member-mass means. The bridge imports those functions rather than implementing another tower schedule.

## Retained input and exact decoder

A shared immutable record contains the root label, all four spectral modes (eigenvalue and projector in exact quadratic-field coordinates), ordered primitive occurrences and their ABCD basis. Synthesis sums lambda*P in each quadratic field and checks cancellation of irrational parts. It recovers the integer incidence matrix, verifies its six entries against the occurrence endpoints, and restores primitive order from the retained occurrence manifest.

This manifest contains the given primitive order, not a newly derived execution history or full native Resolve derivation. Spectral data alone cannot recover occurrence provenance.

Six rows, one per original occurrence, reference this complete record. A row's numerical value is six times its elementary incidence matrix, so the unit-mass mean is exactly M. This is a declared column/entry encoding normalization, not a physical amplitude or traversal-energy rule. The full spectrum remains retained, not compressed into the numeric mean.

## Executed diagram

| Rung/role | Actual representation |
|---|---|
|12|Six original occurrence rows with shared spectral record|
|11|Source-indexed rows|
|10|Target-indexed rows|
|9|Existing two-stage incoming-family candidate|
|8,7|Its corresponding indexed transports|
|6|Four inherited-key families or one common-target family|
|5|Source-indexed promoted records|
|4|Target-indexed promoted records with all original leaves accessible|

Both squares and both complete routes commute. At every outer presentation the decoder reconstructs the same M and all six ordered occurrences; the weighted matrix mean also remains M. There is no eigenphase advancement or application of M to a coefficient state during this operation.

## Controls and scope

- Dropping a spectral mode fails the exact reconstruction certificate.
- Reversing the occurrence manifest leaves the synthesized matrix unchanged but changes recovered order. Retaining basis and occurrence data is essential.
- Both horizontal candidates pass, with different final family counts. This bridge does not select between them.
- No physical reference is replaced by the spectral modes. The test reconstructs M at rung4; it does not derive the calibrated rung4 residual or energy.
- No individual evolving packet state is reconstructed from its projector alone. The retained object here is the seed operator and its occurrence data.

Thus one end-to-end seed -> full spectrum -> retained rung presentation -> exact seed reconstruction chain is now executable. It establishes representation closure independently of raw M's lack of finite operator return. It does not identify the two candidates with physical dynamics, realize a proton-electron pair, or supply primitive interaction cost.

## Observation-boundary comparison

The checker now computes the induced linear readers on fixed topology and masses, rather than inferring equivalence from the single reconstructed seed. Numerical perturbation probes are not asserted to be newly admitted spectral packages.

For scalar leaf values x=(x0,...,x5) in the original order AB,BC,CA,BA,AD,DB, both candidates induce the same aggregate reader:

    O(x)=(x0+x1+x2+x3+x4+x5)/6.

Its rank is one and its kernel is the five-dimensional zero-sum subspace. Five independent basis differences against the last occurrence are tested. A fixed common reference subtraction gives an affine reader; its indistinguishability directions are the same kernel, but its zero fiber is a translated set, not generally a linear kernel.

| Declared numerical domain | Aggregate rank | Kernel dimension |
|---|---:|---:|
|Six arbitrary scalar rows|1|5|
|Six arbitrary 4x4 matrix rows|16|80|
|Six edge-supported coefficients, using the bridge's six distinct matrix entries|6|0|

The unrestricted matrix result follows entrywise from sixteen independent copies of the checked scalar map. For supported coefficients, the checker separately computes all six matrix-output columns and verifies rank six. Thus saying simply 'the observation loses five modes' would be wrong for the bridge's actual edge-supported encoding. Neither injectivity result recovers occurrence order or complete provenance from the matrix alone.

A family-resolved scalar reader is finer: inherited transport retains four family means, with rank four and kernel dimension two, whereas common transport retains one, with rank one and kernel dimension five. The perturbation (1,-1,0,0,0,0) survives inherited family readings but disappears in the aggregate and common-family reading. These readers have different output spaces; this is a distinction in available resolution, not an already aligned native comparison certificate. The common candidate still retains the original leaves, so a deliberately leaf-decoding reader could recover the same finer information. Outer summaries are not the entire retained objects.

### Relation to the existing native observation machinery

`research/voevodsky/observation-respecting-boundary-calculus.md` requires an actual filler e and independently supplied aligned observations satisfying s(e(x))=r(x) throughout the declared carrier. Equal aggregate maps above establish only the corresponding finite-model observation equality. No new native filler or Agda certificate was constructed here.

`research/voevodsky/profile-bound-native-comparison-gate.md` binds its readers to the fixed tidal source factory and profiles. It does not authorize this seed incidence reader. Its all-payload calibration requirement cannot be replaced by matching our single seed output.

To promote this bridge to a physical rung4 claim still requires: the seed's admitted carrier/domain; its independently specified physical reader including units, frame and reference; actual native package/filler adapters for these retained presentations; all-domain reader compatibility; and a profile admission policy binding those choices. None is selected by equal reconstruction or equal aggregate readings. No evidence here selects inherited over common transport.

## Reversible comparison of the two retained candidates

There is now an executable comparison on their canonical image domains. For P_i and P_c the inherited and common transports and L the original-leaf decoder, set

    E_ic=P_c L, E_ci=P_i L.

The admitted domain for each candidate is exactly P_policy applied to six rows with the fixed seed labels, endpoints, unit masses and no primitive members, allowing numerical payload variation. A validator checks both that source skeleton and exact equality with the recomputed canonical family tree. It rejects altered family labels or masses, even if leaves are unchanged.

Since L P_i=L P_c=id on this source domain, the two composites are identities on their respective images. This is an algebraic inverse argument, supported by exact tests on the seed, scalar basis probes and the zero-sum hostile. It is not an inverse on arbitrary family trees, nor does it identify independent execution histories or receipts.

The comparison preserves every reader that factors through the same original-leaf data. The checker explicitly verifies the aggregate and an aligned target-family reader that partitions decoded primitive leaves by their original target. The common candidate therefore can recover all four original target means, despite exposing only one outer mean.

Consequently the difference of outer family counts is not a loss of retained seed information. It does not force choosing one candidate before proceeding with a leaf-based observation. Conversely, a physical reader sensitive to newly created family identities or execution histories need not factor through leaves; no compatibility for such a reader follows here.

This supplies a finite-model equivalence with a specified domain, not an instantiation of the owner's native filler or the tidal profile gate. The remaining physical task is to determine whether the independently justified seed/rung4 reader factors through the retained seed, or genuinely observes additional construction data. Another reconstruction test cannot decide that.

## Source-policy result: resource needs execution data

`docs/theory-page.md`, sections "Rung transports and the physical reference" and "Paths retain traversal resource", separates two statements:

1. The physical reference is at rung4, but its numerical reader and intended horizontal generator remain to be constructed.
2. The proposed path resource is additive and strictly positive per traversal, including attempts with zero state update. An A->B->A return costs two traversals, not zero.

The second statement already obstructs a resource reader that factors only through the static seed operator and terminal endpoint. On this actual seed, compare executed words (AB,BA) and (AB,BA,AB,BA). They use the same primitive registry and spectral record and both return A to A. For positive costs c_AB,c_BA, their resources are c_AB+c_BA and 2(c_AB+c_BA), which differ. This does not say their complete retained execution histories are equal: precisely those histories distinguish them.

The checker verifies composability, return endpoints and strict cost difference with unit and nonuniform positive rational fixtures. Unit costs are a test normalization, not a physical calibration. The obstruction holds symbolically for any positive sum of these two costs.

The comparison of retained presentations extends to supplied receipts simply as (p,h)->(E(p),h). It preserves that resource reading and both inverse laws. Regrouping does not append a traversal receipt: the source has not declared it to be an executed primitive attempt. Thus the positive-cost proposal alone cannot select inherited versus common family transport or turn their family counts into energy.

The structural synthesis is now a separation of channels: retain the seed's spectral/presentation data AND actual execution receipts. A combined reader may preserve static reconstruction while distinguishing different completed paths. The remaining missing adapter is a source-derived execution rule saying which native construction steps emit which primitive events, together with calibrated event costs and the actual rung4 physical reader. This bridge supplies neither that execution schedule nor a proton-electron/energy identification.

## Existing event emitter: usable sector and global obstruction

Source inspection of `check_paw_half_turn_promotion.py` locates a concrete finite emitter:

- `Ledger.half_turn` allocates a fresh event occurrence and flips its endpoint sign.
- `Ledger.promote` retains/concatenates the parents' events; it emits no additional event. It admits only endpoint-returning composites and enforces its depth bound.
- Reusing the same event occurrences as another execution is rejected; replay needs fresh occurrences.
- The identity packet contains no events. This is not an executed comparison attempt with zero update: the latter would still need an event under the path-resource proposal.

The bridge now reuses these operations to check a two-event return and a four-event double return with fresh IDs. This concretely realizes the AB/BA sector after choosing A=+1, B=-1 and a direction convention. Its `variation_in_pi` counts half-turn events, not calibrated energy.

It cannot be extended to all six seed arrows by mapping each to ONE such event with globally consistent endpoint signs. Every edge would require sign(target)=-sign(source). The ABC triangle would then imply sign(A)=-sign(A). The checker exhausts all sixteen assignments of four vertices to +/-1 and finds none. The ADB triangle supplies the same obstruction.

This is a narrow but decisive adapter failure: it excludes the one-arrow/one-half-turn endpoint interpretation, not arbitrary multi-event paths, richer endpoint carriers, or internal contrast-plane phases unrelated to vertex signs. Choosing any such replacement would require new source justification. In particular, the triangle's spectral half-phase is an action on coefficient modes; it is not automatically this ledger's endpoint flip.

We therefore have an existing emitter for a two-state return sector, but not a native full-seed execution adapter. No general event schedule or physical cost rule has been derived. The positive result is reuse of the retained-event mechanism; the stopping boundary is its endpoint typing, before physical normalization.

## Verification

    python research/nima/checkers/check_seed_spectral_rung_bridge.py

Passes exact arithmetic, rerunning the original natural-tower and rung-diagram/DG checks. New assertions verify spectral decode at every outer presentation, route commutation, mass-weighted reconstruction, shared descriptor retention and the two negative/provenance controls. No new Agda closure theorem is claimed.
