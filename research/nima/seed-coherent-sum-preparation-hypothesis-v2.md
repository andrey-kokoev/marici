# Candidate preparation v2: relationship-driven coherent displacement

## Status

This is an explicitly NEW hypothesis, formulated after the bounded prior search found no applicable whole-seed preparation law. It is not derived from the seed, not an autonomous preparation mechanism, and not a particle claim. It uses the existing oscillator/displacement setting and exchange event law; no new feature values or measured constant are fitted.

## Proposed task

Given the retained primitive-edge set E, prepare

    Q_E = sum_(e in E) u_e, w_e=0,

where u_e are the existing unit-normalized probe features. Operationally, each retained primitive relationship authorizes one equal, phase-aligned coherent displacement of the carrier along its supermode. The order of these real coherent displacements does not change their summed amplitude. Records begin at zero.

Then execute the same AB-BA pulses and read the same BA record as before. After deleting an edge, remove only that preparation contribution. Keep probe dictionary, pairing, amplitude per contribution, pulse law and readout fixed; do not renormalize the total preparation.

New assumptions are substantial: a controller can interrogate the entire retained relationship, equal-amplitude feature displacements are available, their phases are aligned, and the preparation is completed before probing. Preparation and phase-reference resources are not free. This constructs an environment-dependent initial state in a candidate apparatus, not a source-derived physical reference connection.

The carrier field is co-prepared from all retained relationships. Its relation to the seam-reference hypothesis remains something to test, not an established identification.

## Derived diagnostic

With empty records and unit probe features, the final BA record after AB then BA is

    w_BA = <u_BA,Q_E> - <u_BA,u_AB>*<u_AB,Q_E>.

This follows from the existing event law. It is linear in the preparation contributions; no interaction coefficient is tuned.

| Retained graph | Endpoint-fixing probes | Directed-transition probes |
|---|---:|---:|
|Full six-arrow seed|0|4/3|
|Delete BC|0|13/9|
|Delete CA|0|13/9|
|Delete AD|0|1|
|Delete DB|0|1|
|Only AB and BA|0|8/9|

All columns use their previously fixed unit probe convention and the same record reader. In each run the exchange preserves that run's prepared quadratic budget. Different graph preparations need not have equal budgets: holding per-relationship displacement fixed is NOT holding total preparation energy fixed. No ratio is introduced to disguise that distinction.

The endpoint-fixing zero is structural: u_AB=u_BA, and the first exchange with an empty record removes that carrier component before the second can read it. It holds for ANY initial carrier field when both records are initially zero. This is not a vanishing of retained history or proof of no interaction elsewhere.

The transition-probe candidate has a genuine change in the surviving experiment when the indirect legs are removed, because the preparation now depends on those legs. Equal-cardinality deletions on opposite sides give different values, so the response is not solely an edge count. The values do not establish triangle-specific physics: other edge sets can give the same overlap sums, and the reader sees this specific linear preparation statistic rather than the entire graph.

## Follow-up: environment dependence is additive, not a joint seam interaction

The checker now compares the full graph E, E without AD, E without BC, and E without both. The AB-BA experiment remains available in all four environments. For its COMPLETE thirty-coordinate final state F, exact arithmetic gives

    F(E)-F(E\{AD})-F(E\{BC})+F(E\{AD,BC})=0.

This holds in both probe models, not just for one named output. It follows generally because Q_E is a sum of individual edge contributions and the fixed AB-BA event operator is linear. Any pair of distinct deletions preserving that word has the same cancellation.

Therefore v2 supplies a response to the environment but not an irreducible joint effect of the two indirect paths in this linear-amplitude observation. A quadratic energy reader could create cross terms, but that would be a different observable, not evidence that the preparation mechanism itself couples the two paths. The earlier mixed PATH-PROTOCOL rectangle varied the executed words; this control varies the preparation graph while keeping the executed word fixed. Their results must not be conflated.

V2 is retained as an explicit additive-preparation baseline. It does not meet the stronger aim of deriving a two-triangle-specific interaction. No nonlinear preparation or graph-dependent exchange kernel is added to evade this control.

## Interpretation and rejection criteria

The previous fixed-preparation deletion test remains correct. The new behavior is attributable entirely to the explicitly changed preparation law; it must not be reported as a consequence of the old exchange hypothesis alone.

This candidate is useful only if an independently justified preparation task can realize those coherent contributions. If the intended construction does not admit externally controlled, phase-aligned displacements, reject this operational proposal rather than calling them internally generated amplitudes. Incoherent sources, adaptive gains, or graph-dependent metrics are different hypotheses and cannot be inserted to rescue an unwanted prediction.

The two channels remain competing interpretations. We do not select transition probes merely because they give a nonzero BA signal, nor discard endpoint-fixing probes for predicting zero in this particular preparation.

## Verification

The existing `check_seed_exchange_structural_controls.py` now also tests this separately labelled preparation hypothesis using exact rational coordinates. All six graph variants, unchanged readers, the analytic two-pulse formula and budget preservation pass. The fixed-preparation controls remain intact.

    python research/nima/checkers/check_seed_exchange_structural_controls.py

No new hardware, native source admission, physical calibration or autonomous preparation was demonstrated.
