# Common-frame drift defeats spanning self-calibration

## Full span and perfect conditioning can still miss the science frame

Let a two-axis reference generator rotate by a quarter turn relative to the
laboratory. Let the analyzer share the same mount and rotate with it. The
prepared reference matrix is `R`, the analyzer map is its transpose, and their
measured composition is

```text
R transpose times R = identity.
```

Both reference directions span the full module. Every singular value is one.
The internal calibration record is exactly unchanged.

But a science vector fixed to the laboratory does not co-rotate. Its analyzer
coordinates change from `(1,0)` to `(0,-1)`. The instrument has undergone a
large frame motion that its own co-moving reference cannot observe.

This is a gauge freedom of self-calibration: measurements identify the
composition of preparation and readout, not their individual alignment to an
external science locus.

## The missing constructor is a cross-locus anchor

Span coverage and a lower singular bound are insufficient when preparation and
readout share an unobserved symmetry. One additional reference must be anchored
outside the common drifting assembly—for example, a laboratory-fixed
polarization axis, independent angle encoder, frequency comb, or astronomical
source with a separately justified frame relation.

The contextual diagram must record not only reference span but reference
provenance: which physical locus supplies each frame, and which transformations
can move them together while leaving internal overlaps invariant.

## Optical instrument

Mount the polarization generator and analyzer on a common rotation stage, then
compare internal spanning calibration with a fixed external polarizer. Rotate
the common stage by ninety degrees. Internal calibration remains identity; the
external anchor reveals the full rotation. A loop-closure test with references
from two independently mounted loci directly measures the hidden gauge mode.

## Claim boundary

The checker uses exact two-dimensional orthogonal rotations and noiseless
references. General Mueller gauges, imperfect anchors, translations, phase
drift, and finite-sample uncertainty remain open.

## Verification

```text
python research/aspect/checkers/check_common_frame_drift_defeats_self_calibration.py
```
