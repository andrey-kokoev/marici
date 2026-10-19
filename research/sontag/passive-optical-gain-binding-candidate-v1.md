# Selected physical candidate: passive optical gain with retained loss ports

## Decision and operator scope

The operator permits the bounded mathematical scope (fixed WG nested/flattened histories and exact energy/context instances, with the relation-module bridge separate) and delegates physical candidate selection to Sontag. I select a TWO-CHANNEL PASSIVE OPTICAL ATTENUATION NETWORK with explicit environment outputs. This is a conditional physical-theory candidate, not a claim that hardware has been installed, calibrated or experimentally verified.

This supersedes the decision to merely await a physical candidate, not the recorded missing-apparatus facts. Physical work can now proceed through a specific preparation/intervention/readout design and its hostiles. Shared net dispositions remain unchanged until reviewed.

## Why this candidate

Existing `research/aspect/checkers/reciprocal_lossy_cavity_plant.py` explicitly composes a loss coupler with retained environmental output and energy-normalized amplitudes. `research/nima/optical-plant-endpoint-exchange.md` handles ordered loss ports and warns against erased environmental energy. `exchange-oscillator-preparation-and-measurement.md` supplies the coherent-mode physical framework and calibrated-reader obligations. `exchange-preparation-reset-resource-ledger.md` treats detector loss and fresh vacuum ancillas explicitly.

Use their passive loss-port primitive, NOT their 137-label exchange endpoint or the whole frozen cavity. A reversible signed exchange alone does not implement the energy task's contraction. The proposed primitive is a tunable two-port rotation, with physical control supplied independently of source labels.

## Preparation and intervention map

Take two independently addressable, equal-frequency bosonic signal modes, prepared coherently with amplitudes α,β. Define a=|α|² and b=|β|² in occupation units. Physical signal excess energy is ħω(a+b) under the declared equal-frequency assumption. Phase is retained in the physical/source preparation record; `(a,b)` remains only an energy-task quotient. The selection is not a faithful representation of arbitrary 137-slot native preparations.

For each gain q∈[0,1], couple signal 1 to a fresh vacuum environment through

`R(q)=[[q,sqrt(1−q²)],[-sqrt(1−q²),q]]`.

Couple signal 2 through R(q²). Equivalently apply two R(q) stages with separate fresh vacuum modes to the second signal. Signal coherent means become `(qα,q²β)`, so the summary update is EXACTLY `(q²a,q⁴b)`. This is a same gain vocabulary on the energy task, not a claim of independent source sector actuation.

Intervention control: calibrated coupler angles θ1=acos q and θ2=acos(q²), or the two-stage alternative. An angle schedule must implement these values; q is not physical time. A lossless mixing Hamiltonian and degenerate modes give a unitary dilation; physical switching loss, frequency drift and control work are separate apparatus obligations.

Retain environmental outputs. Lost signal occupation is `(1−q²)a+(1−q⁴)b`; signal plus environment occupation is unchanged in the ideal dilation. Reusing a populated environment violates the vacuum-input precondition and generally breaks the gain law. Finite q=0 corresponds to an ideal swap with vacuum, not finite-time asymptotic cooling or deletion of environment data.

## Measurement is the decisive binding gate

The original exact abstract `read-total` has no additional state update. The supplied physical homodyne reader is destructive and noisy. It CANNOT be substituted as a cost-free intermediate exact reading.

Select two explicit subcandidates:

1. **Open-loop/known preparation:** a,b supplied by a calibrated preparation protocol; use source `target_gain` without an intermediate reading. This realizes the gain/target task conditionally, with final statistical validation. Calibration uncertainty must be bounded.
2. **Observed feedback successor:** tap a known fraction τ of each mode into detector ports; surviving means scale by sqrt(1−τ), and recorded detector outcomes follow a declared statistical instrument. This changes the event dictionary to `tap-read(τ,outcome)` with state/resource effects and an information-state distribution. It requires a versioned successor, not automatic acceptance of the old exact two-reading policy.

I choose (1) as the first executable mathematical/physical comparison candidate, while (2) is the next feedback design gate. Repeated identically prepared trials can estimate a,b but do not provide a free reset of the same unknown specimen. All preparation trials and detector/environment resources must be recorded.

## Prospective tests and remaining evidence

Freeze before evaluation: two distinct preparations `(a,b)=(8,0)` and `(0,8)`; q=1/2; predict signal energies 2 and 1/2 and environmental energies 6 and 15/2 in occupation units. Also test a populated environment hostile, which must fail the source vacuum precondition rather than be silently refitted. A tap with τ>0 must visibly change the signal state.

`checkers/passive_optical_gain_binding_v1.py` checks the ideal dilation, source gain square, resource square, populated-environment hostile and tap back-action symbolically. It does not measure a coupler or certify physical calibration. Remaining independent evidence: named hardware/control implementation and operating ranges, energy normalization/frequency, preparation uncertainty, reader efficiency/outcome model, timing, routing/storage and full apparatus resource budget.

Positive same-source binding is therefore available at the ideal gain/known-preparation subtask, conditional on the stated physical framework. The full exact-observation feedback node is NOT physically bound. The root requires either a licensed statistical successor with comparison to the exact idealization or a genuine admitted nondisturbing readout, plus coverage review. This concrete choice replaces indefinite candidate selection with actionable design work while preserving the earlier negative audit.
