# Intervention rank for source, detector, and electronics memory

## Question

What minimal optical/readout intervention set separates source memory,
detector-local afterpulsing, and shared-electronics echoes?

## Three memory loci

Freeze an additive covariance model with components from the optical source,
the active detector, and the shared timing/electronics chain. A baseline record
contains all three.

A detector reset or independently calibrated detector reroute removes only the
detector-local component. An electronics reset removes only the shared-readout
component. The resulting three intervention signatures form an exact
full-rank matrix, so baseline, detector-reset, and electronics-reset records
identify all three components.

For measured covariances `C0`, `CD`, and `CE`, the recovered components are

```text
source = CD + CE - C0
detector = C0 - CD
electronics = C0 - CE.
```

## Joint-reset falsifier

Reset detector and electronics together. The additive model predicts that the
remaining covariance equals the recovered source component. This fourth
condition is not needed for rank, but it is needed to test whether reset
actions interact or disturb the source.

The checker freezes a hostile joint-reset record differing by `1/32` from the
prediction. The first three conditions still fit three components exactly, so
the fourth condition is a genuine model falsifier rather than redundant data.

## Experimental requirements

The detector reset and electronics reset must have independently characterized
actuation loci. Power-cycling a shared module is not locus-specific. A useful
implementation uses detector holdoff or physical detector rerouting together
with a separately clocked timing chain or replaceable time-to-digital path.

Reset status, detector identity, clock/electronics identity, and epoch must be
carried with every time tag. If the intervention changes pump statistics,
optical loss, or source temperature, the additive locus model is not admitted.

## Verification

Run:

```text
python research/aspect/checkers/check_memory_locus_intervention_rank.py
```

The dependency-free exact checker verifies full rank, exact component
recovery, the joint-reset prediction, and a deliberate interaction residual.
