# Prior-research clues for completing Su-32 reference comparisons

## Search and disposition

Searched the Strominger, Nima and Voevodsky research notes for reference changes, shared-reference comparisons, retained context, interchange and filler construction. Read the principal notes below and inspected the reference-transition Python implementation, Nima's reanchoring checker, and the Agda comparison-synthesis/interchange constructors.

**Useful constructions already exist on other carriers. No source-bound Su-32 adapter was found in this bounded search.** The correct next move is to test their hypotheses on Su-32, not to infer that all comparison theory is missing or import a theorem solely because it mentions four vertices.

The historical verification claims below are reports from their notes. No Agda closure or those older checkers was freshly executed during this search. Prior Su-32 audits are not changed by these clues.

## 1. Complete-core reference changes: the closest information-level precedent

Sources:

- `research/strominger/field-reference-transitions-v1.md`
- `research/strominger/checkers/field_reference_transitions.py`
- `research/strominger/checkers/check_field_reference_transitions.py`

The implementation extracts a reference-independent operator core from a validated packet. It uses either a certified scalar reconstruction or an already retained operator sidecar; it does not access an unavailable original field. It then regenerates the destination reference view and recomputes its retention obligation.

A concrete reference switch goes from a sufficient view to a deficient view and back. The deficient stage must keep the core as a sidecar. Equal scalar views with different retained cores cannot be glued as equal complete states.

For deterministic complete presentations N_r of a core Omega, extraction returns Omega, so

```
T_(s,t) T_(r,s) N_r(Omega) = N_t(Omega).
```

Current complete packets agree after direct and staged changes; construction histories remain separate.

**Su-32 clue:** changing from the P/P comparison at E+ to one at E- cannot manufacture the independent E- record. The model must specify where that record and its attachment are available. The already reconciled four-record state at central N is a candidate location for a complete core. It is not evidence that either earlier three-record operand independently possesses that core.

**Missing adapter:** define the Su-32 complete core, the admitted contextual views and actual availability/attachment of the complement. The 144 matrix-block core, complex field interpretation and reconstruction certificates belong to another model and must not be copied by analogy.

## 2. Witnessed reanchoring: retention does not freeze current witnesses

Sources:

- `research/nima/witnessed-reference-reanchoring.md`
- `research/nima/checkers/check_witnessed_reference_reanchoring.py`
- `research/nima/comparison-successor-operation-contract.md`

This is the most concrete reference-changing algebra found. Its domain already contains actual maps C_i, a reference d, and witnesses h_i with

```
delta(h_i) = C_i - d.
```

Given an actual witness kappa with `delta(kappa) = d_new - d`, update

```
h_i_new = h_i - kappa
u_new = u + r*kappa
v_new = v + kappa*r
W_new = W + kappa*u + v*kappa + kappa*r*kappa.
```

The actual maps stay fixed. Current unit/triangle witnesses receive new versions, and immutable parents retain every old version. Two updates compose to the update by their summed witness; returning restores current data without erasing the journey. Mixed rectangle defects remain invariant.

**Su-32 clue:** a reference change may need to update the comparison witness while preserving the records it compares. Preserving provenance does not require freezing all current witness fields. This gives a concrete alternative to either erasing histories or treating their mere inequality as an obstruction.

**Missing adapter:** Su-32 currently supplies no differential, map-valued comparisons or kappa witnessing a reference change. The source uses a free DG model with explicitly adjoined weak-return witnesses and a fixed comparison domain. Neither its witness adjunction nor its reference-selection policy is a derived physical law. Its weighted-family and matrix readouts must not be imposed on four arbitrary JSON records.

## 3. Actual comparison synthesis and attachment interchange

Sources:

- `research/strominger/canonical-comparison-synthesis-v1.md`
- `research/strominger/agda/CanonicalComparisonSynthesis.agda`
- `research/strominger/internal-source-comparison-and-interchange-v1.md`
- `research/strominger/agda/InternalComparisonInterchange.agda`

The existing compiler is stronger than a request to supply an arbitrary equivalence. For its generated `Fragment` operands and a declared mode, it computes reader-image compatibility and returns either:

- a full comparison certificate and an admitted comparison retaining the actual operands; or
- a separating reader vertex with an inhabited fiber on one side and an empty fiber on the other, refuting a compatible filler.

The native internal comparison interface requires a whole-carrier law

```
act(mode, read_left(x)) = read_right(e(x))
```

—not merely agreement at one chosen point. Given that structured comparison, the interchange construction derives a comparison between attach-then-compare and compare-then-attach. It retains both route derivations, proves them unequal as raw packages, and permits subsequent attachment under an explicit target-side continuation policy.

**Su-32 clue:** give each proposed contextual comparison a complete typed reader/attachment interface, then seek a computable acceptance or refusal criterion. Do not try to infer filler existence from equal final records alone. Once an attachment-compatible comparison exists, derive the mixed witness rather than freely choosing a tetrahedral filler.

**Missing adapter:** no embedding of the Su-32 contextual record carriers into the compiler's restricted generated fragment is supplied. Its six-arrow source, stay/exchange modes, normal forms, sethood/reader-injectivity theorems and continuation convention are substantive hypotheses, not consequences of having four signed labels.

## 4. One common anchored source can force coherence

Source:

- `research/voevodsky/a-common-graph-presentation-generates-all-opposite-edges-at-fixed-realization-dimension.md`

A complete presentation retains a common source x together with a displayed coordinate q_i(x). Its chart is `e_i(x)=(x,q_i(x))`, and changes are `E_ij=e_j e_i^-1`. Inverse, triangle and tetrahedral equations follow from common-source factorization. The unanchored shadows can remain lossy.

**Su-32 clue:** a conservative candidate completion can distinguish a contextual display from its full retained state. With the same complete state genuinely available, coherence may be forced rather than an independent hierarchy of freely chosen fillers.

**Limit:** adding a source anchor makes inversion possible by construction. It does not establish that Su-32 transports that anchor through the actual cells, or that changing a display is a physical process. The source's analytic completion/closability conditions also do not transfer to Su-32 by naming a common object.

This gives no nontrivial reference holonomy by itself: the E_ij compose strictly on complete states. A separate circle-fiber construction would still need its own native data.

## 5. Conditional interchange, not a tetrahedron inferred from counts

Sources:

- `research/nima/binary-arity-square-is-the-duoidal-skeleton.md`
- `research/nima/gray-coherence-cube-refactors-the-arity-tetrahedron.md`

Rooted substitution and physical cutting give distinct composition actions; transverse instances have strict mixed Beck–Chevalley interchange. The coherence cube distinguishes changing input/output arity from changing the order of operations.

This is a useful architectural clue for Su-32's two reconciliation orders. But no binding of those two operations or their transversality hypotheses to the Su-32 shared-record joins was found. The Gray cycle or a tetrahedral drawing is not that binding.

## Warnings from the same prior work

- `research/strominger/finite-comparison-trees-v1.md`: evaluation coherence is proved for a particular generated fragment with justified filler uniqueness. It neither equates raw histories nor supplies arbitrary mixed attachment coherence.
- `research/strominger/two-comparison-two-attachment-coherence-v1.md`: a retained inverse-facing higher comparison exists under explicit local injectivity assumptions; the forward/forward case is separate.
- `research/voevodsky/a-source-rooted-trace-diamond-exposes-the-first-missing-four-cell.md`: equal endpoints and even joining traces do not automatically compare the actual higher-cell paths.
- `research/nima/coherence-realization-depth-is-a-dependent-filler-tower-not-a-source-cutoff.md`: a filler type is not a chosen inhabitant; but common-source hypotheses can also force higher coherence, so an endless sequence of additional degrees must not be assumed.
- `research/strominger/native-reader-comparison-v1.md`: an invertible coefficient change can fail occurrence compatibility and change another retained observer. Algebraic recovery is not native reverse execution.

## Recommended bounded construction

Start with **complete-core contextual presentations**, not a Chern class or a new matrix action:

1. At the actual central reconciliation location, specify a retained core containing all four records, their attachments and both derivations.
2. Specify P/P-at-E+ and P/P-at-E- as views of that core. Keep their active readings distinct from their complete state.
3. Declare exactly what operation changes the active reference and which witness fields it updates. Preserve immutable parents.
4. Test identity/composition and full reader/attachment compatibility. Refuse attempted changes from an isolated view that lacks the other independent reference record.
5. Only then ask whether the existing internal-comparison compiler or interchange theorem applies via an explicit typed adapter.

This would be a **proposed Su-32 completion**. Its first falsifier is failure of the required availability or reader/attachment law, not failure of a new topological invariant. If common-core reconstruction passes but no native attachment exists, report that precise boundary rather than claiming physical realization.

The central lesson of the search is that there are already mechanisms for preserving records, updating reference witnesses, and deriving coherence. The missing work is to bind a justified mechanism to the actual Su-32 contexts—not to invent higher coherence from scratch, and not to assume an existing theorem already has the right domain.
