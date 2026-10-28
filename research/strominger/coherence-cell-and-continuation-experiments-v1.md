# Two candidate RF experiments: intervention-defined cells and retained distinctions

Status: proposed research experiments, not acquisition protocols or measured results.
Purpose: attract scientific attention through a predictive use of Marici, rather than an interactive illustration or a claim of anomalous electromagnetism.

## Shared question

What is the smallest structure sufficient to predict a specified family of preparations, observations, interventions, and continuations?

Keep two routes separate until a bridge is established. Agreement with ordinary RF theory is compatible with success: the proposed gain is an independently specified structural prediction or a demonstrably useful reduction. A tetrahedral wiring diagram alone establishes neither.

## Experiment A: intervention-defined source–probe cells

### Thesis

A source–probe pair selects a minimal sufficient relational structure, identifiable by a pattern of sensitivity and invariance under controlled interventions. Changing the pair changes that structure according to a rule specified before evaluation measurements.

### Medium-level design

Use a network with more controllable structure than a single prewired candidate cell. Measure phase-referenced complex response y(s,p;u), where s is preparation/source, p is probe, and u is a declared intervention or intervention sequence. Candidates include phase changes, attenuation changes, or routing changes, subject to actual hardware capabilities. Keep frequency dependence and repeated measurements; do not infer support from a single-frequency cancellation.

1. Declare candidate cell descriptions, their inclusion order, and how a cell predicts responses to interventions. A cell is initially a relational model, not necessarily a subset of cables.
2. Independently characterize component responses and acquisition variability.
3. Derive an endpoint-to-cell prediction using the Marici model, without fitting the held-out endpoint/intervention responses.
4. Measure calibration pairs and evaluate sealed new pairs, interventions, and compositions.
5. Compare with full calibrated RF network predictions and a generic system-identification reduction at matched data/model budgets.

The response difference Delta_u y = y(s,p;u) - y(s,p;identity) is a useful signature, but individual intervention effects are not enough. Include joint interventions: cancellation can hide a relevant path until another path changes. Include phase-reference/drift controls and loading-aware RF models.

### Meaning of minimal

For a frozen finite test family and numeric error criterion, a candidate cell is sufficient when its predictions meet the criterion across that family. It is inclusion-minimal when no proper admissible subcell is sufficient. An inclusion-minimal cell need not be unique; a least cell is a stronger assertion. Report all surviving minimal candidates or non-identifiability rather than selecting a visually attractive triangle. Finite observations establish only the declared tested domain.

### Decisive result

A compact endpoint-to-cell rule predicts held-out sensitivity/invariance patterns and cell changes without pair-specific refits. Especially valuable: physically different realizations exhibit the same predicted relational structure.

Possible measurable advantages: fewer independent calibration parameters or measurements for matched held-out error; transfer of predictions across realizations; a cell law fixed by the native structure rather than learned from the evaluation matrix. These are competing success criteria to choose, not achievements asserted here.

### Failure tests

Predicted irrelevant interventions change responses beyond tolerance; predicted changes fail; combined interventions defeat a cell inferred from singleton effects; cell choice requires post hoc revisions; generic reduction has equivalent predictive utility without the proposed structural constraints. The last outcome challenges distinctiveness, not necessarily model correctness.

### Open theoretical obligation

The frozen A4 query fragment supplies no source–probe cell law. Derive one or explicitly introduce a new conjecture. Neither ordinary RF reciprocity nor a tetrahedral drawing supplies this obligation. Define mutual entry/exit compatibility separately from reversing electromagnetic transmission direction.

## Experiment B: retained distinctions under continuation

### Thesis

Present observational equality need not imply interchangeability under future operations. A physical realization must preserve the distinctions that the allowed continuation language can subsequently expose.

### Exact anchor in the frozen fragment

Source: research/strominger/contracts/native-query-source-fragment.v1.json.
States are (g,b) in A4 x Bool. Let e be the identity and choose h in A4 with h(A)=B. Prepare x=(e,false) and x'=(h,false). Their current pointer readings coincide. Apply Q_AB:

- Q_AB(x) has pointer false, since e(A)=A.
- Q_AB(x') has pointer true, since h(A)=B.

Thus the pointer-only present observation merges states that a permitted continuation separates. This is an exact consequence of the declared truth table, not a new physical prediction. The physical experiment asks whether an apparatus retains and acts on that distinction.

For an additional matched endpoint/history control, Q_AB followed by Q_AB restores the complete state, but is not the empty literal history. A final state readout alone cannot establish retained history.

### Medium-level design

1. Identify a physical encoding, preparation map, operation implementation, and pointer measurement. Calibrate each independently of the held-out words.
2. Prepare matched current-pointer states with different carrier labels. If a present read would disturb the state, use separate preparation ensembles for the initial-read control; do not silently insert measurement into the native word.
3. Apply separating continuations and measure pointer response. Include multiple label pairs, both pointer inputs, and held-out compositions.
4. Compare a retention arm with an explicit physical erasure arm that maps the two prepared inputs to the same operational state before the common continuation.
5. Ensure preparation labels do not leak to the continuation controller: otherwise software could supply the answer despite physical erasure. Declare all relevant controller memories, reference channels, timing signals, and auxiliary states.

The erasure control is an added experimental intervention, not a ninth native generator. Discarding a log or hiding a readout is not physical erasure. Equalizing a single measured channel is also insufficient evidence that the complete operational state is equal.

### Decisive result

The same independently calibrated continuation separates the retained inputs as predicted; a validated erasure arm removes the distinction. Held-out words quantify operation preservation rather than a programmed output display. A broader realization claim additionally requires all eight generators to act correctly on all 24 labeled states, with composable successor retention.

### Failure tests

No reproducible separation under the declared implementation; separation explained by label leakage or preparation artifacts; erasure arm still retains an accessible distinguishing channel; generator maps require word-specific refits; pointer agreement hides incorrect carrier successors.

### Scientific positioning

A single hidden-state reveal is familiar physics. The distinctive contribution would be a source-derived account of exactly which distinctions must survive, which continuations witness them, and how those requirements constrain physical realization. Relevant audiences include experimental information theory, automata/system identification, and compositional physical modeling.

## Proposed bridge: observational equivalence under continuations

For a declared observation family O and continuation language W, define x ~_(O,W) x' when O(w(x)) = O(w(x')) for every allowed w (use distributions for noisy instruments). This is a mathematical definition, not a measured all-word certificate.

Experiment B supplies concrete pairs and separating words. Experiment A asks whether endpoint-specific observation/continuation families admit a sufficient cell description of these equivalence classes.

A bridge requires:

1. A mapping from physical endpoint preparations and probes to native states and observations.
2. A mapping from physical interventions to allowed continuations, or an explicitly enlarged language.
3. A proof or finite-domain exhaustive test that the proposed cell retains precisely the distinctions needed by that family.
4. A minimality/uniqueness analysis. Quotient state counts do not automatically identify spatial cells or lattice faces.

There is a productive tension: if the full native continuation language distinguishes all carrier labels, a smaller cell can only arise from a restricted endpoint-specific task, not from globally identifying those labels. This is a question to compute, not a reason to assume the bridge.

## Next intellectual work, before apparatus selection

- Enumerate continuation distinguishability in the frozen finite fragment and extract short witness words.
- Propose endpoint-specific observation and continuation families; state which restrictions have a source justification.
- Determine whether their sufficient descriptions form unique least cells, several minimal cells, or no tetrahedral cell representation.
- Compare the resulting pre-data predictions and scientific payoff with conventional minimal-realization/system-identification methods.
- Only then choose which experiment merits hardware development. Existing KrakenSDR work is infrastructure, not evidence that the required controls exist.

## Related local plans

- research/strominger/native-query-krakensdr-adaptation-v1.md
- research/strominger/contracts/native-query-realization-equivalence.v1.json
- research/kitaev/krakensdr-physical-composition-v1.md

No apparatus selected, acquisition performed, tolerances frozen, or implementation asserted in this proposal.
