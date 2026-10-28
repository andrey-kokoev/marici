# Existing work on the physical-interface bottleneck

## Finding

There is already substantial prior work on this exact distinction. The missing step for our current WG assembly is not to invent another observability criterion. It is to bind a **source-authorized, record-producing interaction with a successor state and apparatus return** to the actual retained operations.

This search inspected notes, two implementation entrypoints and the comparison-loop hardware contract. It did not rerun their suites or obtain apparatus records. No other-owner files, net verdicts or pins were changed.

## 1. The five-part source-closed constructor criterion already exists

Sources:

- `../nima/constructor-lift-withheld-prediction.md`
- `../nima/source-closed-constructor-criterion.md`

The prior criterion requires one source-authorized diagram containing:

1. an independently specified repeatable task;
2. a state-changing interaction J:X->R tensor X';
3. a record marginal of that SAME interaction;
4. preparation and return/reset, or an explicit resource-degradation law;
5. coherent sequential composition and coarse-graining for records AND successor states.

The source-closure requirement rules out assembling individually valid faces from incompatible ambient models. A faithful probe alone does not provide the successor-state leg; a fitted dilation does not provide source authority.

The follow-up reports a held-out cosmology audit whose predicted first failure was Read -> Instrument: its source-normalized, contextually faithful score readout still supplied no outcome-bearing interaction, conditional successor, pointer preparation or reset. This is a prior cross-sector prediction/audit, not a new experiment or an independently rerun result here. The stated necessity/sufficiency criterion organizes the required diagram; it does not itself construct an apparatus.

**Relevance:** our current accepted observation factors remain on the readout side of this boundary. A retained computational execution record is not automatically a physical pointer record.

## 2. Same complete one-use probabilities can hide different instruments

Sources:

- `../nima/instrument-capability-fiber.md`
- `../nima/checkers/check_instrument_capability_fiber.py` (implementation inspected)

For fixed click effect E1=s^2|1><1|, the prior family

    K1(psi) = -i s |psi><1|

has the same one-use probabilities for every normalized successor psi, but different conditional output states. Its capability fibre is CP1. The inspected exact checker uses s=4/5 and includes absorptive, QND, X+ and Y+ successors.

The absorptive and QND examples have respective repeat-click probabilities 0 and 16/25 despite identical one-use click effects. Controlled X/Y/Z analyzers distinguish the sampled successor rays; the note describes reconstruction of the general ray from those coordinates.

**Relevance:** matching our Boolean readout to a detector's outcome law cannot identify its state-changing instrument. This is a ready-made hostile test for a proposed WG-to-physical adapter: compare conditional successors and sequential records, not just effects.

**Boundary:** the analyzer family is an explicit control input, not derived from this six-arrow WG source. No physical apparatus implementation is established by the exact matrix calculation.

## 3. Probe generation and robust separation have a precise architecture

Sources:

- `../nima/source-observability-is-a-constructor-generated-dual-orbit.md`
- `../nima/commutant-separation-does-not-imply-sector-controllability.md`

Given a source state module H, authorized constructor algebra A and rooted observer ell, use the generated family span{ell a : a in A}, not an observer fitted to the desired state. Separation requires the common kernel to vanish. Infinite/completed claims additionally require a uniform positive lower margin; full rank at every finite cutoff is insufficient.

The control counterexample separates another pair of gates: central labels can distinguish two carrier blocks while leaving every noncentral control diagonally locked. Algebraic projectors and observability do not create independently executable actions.

**Relevance:** specify the actual authorized operation alphabet before claiming probe completeness or control. Our BA-parity interpreter is sufficient for its declared probe; it does not establish a complete physical probe orbit or controllability.

## 4. Calibration is an additional source constructor—and needs an external anchor

Sources:

- `../nima/calibration-is-a-source-extension-that-can-restore-observability.md`
- `../aspect/common-frame-drift-defeats-self-calibration.md`
- `../aspect/checkers/check_common_frame_drift_defeats_self_calibration.py` (implementation inspected)

The calibration packet shows why passive postprocessing cannot recover a coordinate erased by a quotient. An independently prepared input can restore it, but this enlarges the source/interaction alphabet. The robust separator condition is rho < sqrt(d^T W d), with W and the uncertainty class independently fixed.

The Aspect counterexample adds a crucial warning: a reference generator and analyzer can drift together while internal calibration stays exactly identity with perfect singular values. A laboratory-fixed science vector changes its readout nonetheless. A cross-locus reference is needed to detect that mode.

**Relevance:** fitting a convenient calibration or checking internal consistency cannot establish the needed external physical identification. Record reference provenance, permitted joint drifts and an independent anchor.

## 5. Physical-record and acquisition interfaces are already concrete

Sources:

- `../aspect/physical-realization-record-and-time-gates.md`
- `../aspect/comparison-loop-hardware-binding.md`
- `../aspect/contracts/comparison-loop-hardware-binding.v1.json` (current contract inspected)
- `../aspect/hardware-bound-pushforward-acquisition.md`
- `../aspect/reset-qualification-acquisition.md`
- `../aspect/raw-acquisition-first-portfolio.md`

These distinguish mathematical attachment, apparatus realization, positive state/effect pairing, detector response, stable record and clock interpretation. A composition index is not physical time.

The comparison-loop contract fixes rotation, phase, loss and statistical error budgets. Its current claim flags explicitly read:

    hardware_identity_bound = false
    physical_calibration_loaded = false
    physical_trials_run = false.

The acquisition interface binds immutable event/run identifiers, raw/packet/compiler/contract/view digests and field provenance. It preserves no-click events and fixes coincidence policy before inspecting the statistics. The note describes synthetic validation, not hardware execution.

Reset qualification is also a predeclared experiment rather than the assertion that a reset exists: two arms, four predecessor states, four targets, complete balanced blocks, no exclusion of reset failures, a minimum no-reset memory effect and a maximum residual spread after the proposed reset. Physical results require apparatus records satisfying that contract.

The acquisition-portfolio note explicitly leaves apparatus capacity measurements and calendar binding absent. These packets supply reusable schemas and falsifiers, not empirical evidence for our WG map.

## What this changes about the next task

The sharper bottleneck is **readout -> source-authorized instrument**, not merely finding a faithful observation map.

A bounded next contract should:

1. Choose one independently specified receiver with a real interaction and apparatus-cycle model, rather than another passive observer complex.
2. Bind our exact retained operation and declared probe to its task, record marginal and conditional successor; preserve the explicit unary-extension versus original-calculus distinction.
3. Test the same-effect/different-successor hostile pair. Reject an adapter that matches only one-use probabilities.
4. Require probe/control authority and an independently anchored calibration, with a positive uncertainty margin.
5. Bind raw acquisition and reset evidence before promoting a mathematical instrument model to physical adequacy.

A small two-outcome quantum-instrument model is a practical mathematical receiver candidate because its successor ambiguity and sequential tests are already explicit. This is a recommendation for a declared new comparison task, not a claim that the six-arrow source selects that model, its Hilbert structure, its analyzer controls or its Born pairing.

No inspected packet supplies the complete WG-to-that-receiver source-authorized bridge. Conversely, the claim that prior work contains only readout abstractions would be incorrect: conditional instrument models, capability classifications, calibration obstructions and detailed acquisition contracts already exist and should be reused.
