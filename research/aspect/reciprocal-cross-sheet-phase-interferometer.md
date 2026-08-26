# Reciprocal cross-sheet phase interferometer

## Result

A finite two-shell optical circuit separates the phase-erasing positive-square route from a phase-retaining reciprocal cross-sheet route. The result is an implementation witness and falsifier, not an arithmetic constructor or a zero-confinement theorem.

## Source and typed ports

The source emits two phase-locked copies into reciprocal signal and reference ports. Two declared delay shells carry weights 3 and 1. A separate low-frequency monitor carries the DC endpoint; it is not inferred by fitting the oscillatory channel.

## Constructor order

The reciprocal copies are split, delayed by the two shell times, recombined across sheets, and only then projected by balanced homodyne detection. Swapping the cross-sheet recombination for same-sheet intensity formation changes the constructor: the former retains relative phase, while the latter cancels it.

## Phase, calibration frame, and exact finite readout

Let the calibrated phase token be (z=e^{i\tau}). The mixed readout is

\[
M(z)=3\operatorname{Re}(z)+\operatorname{Re}(z^2).
\]

At (z=1,i,-1), its exact values are (4,-1,-2). The zero-to-quarter-turn difference is 5. By contrast, the positive same-sheet square is (3^2+1^2=10) at every phase. The homodyne local oscillator supplies the phase frame; without it, intensity detection collapses the distinction.

The DC port is calibrated independently at (3/2). Keeping the tuple

\[
(M,\;P,\;D_{\mathrm{DC}})
\]

prevents a boundary convention from being hidden in a transfer-function fit.

## Conserved quantity and detector kernel

Ideal splitters preserve total optical norm across all accessible output ports. Balanced homodyne reads a signed cross-sheet quadrature. Direct intensity reads the positive square and has a vertical-phase kernel: every tested phase produces 5. The independently digitized DC monitor distinguishes a constant boundary carrier from oscillatory phase response.

## Smallest hostile

The hostile apparatus uses the same source weights, delays, and detector gain but forms each sheet's positive square before summing. It preserves the scalar norm and all three intensity records while erasing the vertical phase that the mixed channel detects.

## Completion and authority boundary

This finite experiment can falsify any claim that a positive Hankel square reproduces a vertically oscillatory forcing. It can also test whether a proposed reciprocal mixed block has the required phase signature. It does not derive prime-labelled incidence, authorize a defect port, identify an unbounded inverse derivative, establish continuum Hardy completion, or constrain theta zeros.

## Reproduction

Run:

    python research/aspect/checkers/reciprocal_cross_sheet_phase_interferometer.py
