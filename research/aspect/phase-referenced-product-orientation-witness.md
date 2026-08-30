# Phase-referenced optical product orientation

## Question

Can an optical experiment distinguish two ordered products that every polarization-only state and intensity view identifies?

## Ordered words

Use ideal Jones operations `X` and `Z`. Physically, these are half-wave-plate actions in two orientations: `X` swaps horizontal and vertical polarization, while `Z` applies opposite signs to them.

Their ordered products satisfy `XZ = -ZX`. Acting on any input density matrix, the global sign cancels. The two words therefore induce exactly the same polarization channel on every matrix unit. No downstream polarization analyzer or intensity detector without a phase reference can distinguish them.

This is stronger than equality on a finite list of static contexts: the complete polarization state channel is identical.

## Source-authorized reference

Place the unknown ordered word in one arm of a balanced interferometer. In the reference arm, apply `X` so that a horizontal input reaches the recombiner with vertical polarization in both arms.

For the signal word `XZ`, the signal and reference amplitudes agree. The plus output is bright and the minus output is dark. For `ZX`, the signal amplitude has the opposite sign. The plus output is dark and the minus output is bright.

Thus the ordered words give identical polarization-only records but opposite interferometric port records.

## Why this is not reconstruction from the old atlas

The reference arm supplies a new relational context. It converts an otherwise global phase into a relative phase. The old polarization channel has a canonical forgetting map from the interferometric experiment, but it contains no canonical choice of reference phase and therefore no canonical lift back to the oriented word.

The experiment does not prove that one product orientation is universally preferred. The source preparation, arm labels, reference transformation, and recombiner convention authorize which ordered amplitude is being compared.

## Relation to Sontag's hostile

Sontag's ordinary and opposite matrix products share their commutative contexts and Jordan symmetrization but differ under an ordered `Y`-paired continuation. The interferometer gives that antisymmetric distinction a direct optical record: coherent reference converts the sign of the ordered product into a bright/dark port exchange.

## Claim boundary

This is a finite exact ideal-Jones and balanced-interferometer theorem. It does not include path loss, phase drift, imperfect visibility, detector noise, wave-plate dispersion, or a laboratory calibration certificate. It establishes existence of an authorized orientation-sensitive context, not uniqueness of reconstruction from arbitrary sequential data.

## Robust interferometric extension

The companion robustness checker allows unequal reference and signal arm
transmissions, partial coherence, a calibrated lower bound on phase alignment,
dark clicks, and bounded systematic error. If the arm intensity transmissions
are `t_reference` and `t_signal`, coherence is `visibility`, and the calibrated
phase cosine is at least `phase_cosine`, then the two orientations differ in
plus-port probability by

```text
visibility sqrt(t_reference t_signal) phase_cosine.
```

After dark-click mixing and adversarial systematic errors on both orientation
records, the worst-case margin is

```text
(1 - dark_click) visibility sqrt(t_reference t_signal) phase_cosine
- 2 systematic_error.
```

The exact benchmark uses arm transmissions `1` and `81/100`, visibility
`9/10`, phase cosine `4/5`, dark-click probability `1/100`, and systematic
error `1/100`. The surviving criticism margin is `7769/12500`.

## Drift-balanced acquisition

A static margin is not enough if the two orientations are measured in two
long consecutive blocks. Common detector or source drift can then imitate an
orientation difference. The companion drift checker uses four equally spaced
blocks at normalized times `-3, -1, 1, 3` with orientation schedule
`XZ, ZX, ZX, XZ`.

The two orientation groups have the same mean time. Their contrast therefore
cancels every common constant and affine drift exactly. If the magnitude of
the quadratic drift coefficient is bounded by `kappa`, the worst adversarial
contrast bias is `8 kappa`.

With `kappa = 1/10000` and the existing systematic error budget, the robust
orientation margin remains `7759/12500`. A consecutive `XZ, XZ, ZX, ZX`
schedule fails this protection: an affine slope contributes four times its
magnitude and can cancel the orientation signal.

Run:

```text
python research/aspect/checkers/check_drift_balanced_phase_orientation.py
```

## Correlated phase-outage hostile

Marginal visibility does not determine run-level reliability. Model each of
the four acquisition blocks as either phase-coherent or in a quadrature outage.
Both an independent model and a persistent two-state Markov model can have
coherent marginal probability `9/10` in every block.

Under independent blocks, the probability that all four blocks are in outage
is `1/10000`. Under the frozen persistent model, a coherent block enters outage
with probability `1/100`, while an outage recovers with probability `9/100`.
The same stationary coherent fraction is `9/10`, but the all-outage probability
is `753571/10000000`, more than seven hundred times larger.

With the current orientation margin, any one coherent block is enough to keep
the deterministic contrast positive after systematic error. The all-outage
event is therefore the exact failure event in this finite model. Static
visibility alone cannot certify its probability; the protocol needs a
mixing-time bound, block reset, or phase-monitor record.

Run:

```text
python research/aspect/checkers/check_correlated_phase_outage_hostile.py
```

Run:

```text
python research/aspect/checkers/check_robust_phase_orientation_witness.py
```

## Verification

Run:

```text
python research/aspect/checkers/check_phase_referenced_product_orientation_witness.py
```

All checkers are dependency-free and use exact arithmetic.

## Imperfect phase-monitor repair

Add a monitor record to every acquisition block and accept a run only when
all four records report a coherent phase. This is a selection channel, not a
coherence-restoration channel. The signal record remains exactly as acquired;
the monitor only identifies records that should not support the orientation
claim.

The frozen monitor misses an outage with probability `1/20` and falsely
rejects a coherent block with probability `1/100`. Conditional on the hidden
phase-state sequence, monitor errors are independent. Exact enumeration of all
sixteen Markov sequences computes the run acceptance probability, the joint
probability of accepting a failed run, and the failure probability conditional
on acceptance.

Because failure requires four outage blocks, accepting a failed run requires
four simultaneous monitor misses. The joint failed-and-accepted mass is the
original persistent-outage failure probability multiplied by `(1/20)^4`.
A perfect outage detector makes that mass zero; a blind detector leaves it
unchanged. This makes the monitor's epistemic role explicit and falsifiable.

Run:

```text
python research/aspect/checkers/check_imperfect_phase_monitor_repair.py
```
