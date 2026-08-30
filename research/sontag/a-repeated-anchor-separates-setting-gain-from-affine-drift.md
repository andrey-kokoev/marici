# A Repeated Anchor Separates Setting Gain from Affine Drift

## Question

When four gain calibrations are acquired sequentially, how can the instrument
distinguish setting dependence from temporal drift?

## Confounded one-pass schedule

After sign adjustment, model the zero-correlation calibration record as

\[
z(t,i)=a+bt+\delta_i,
\]

where \(a+bt\) is a common affine gain mode and \(\delta_i\) is a persistent
setting offset. Fix \(XX\) as the reference, so \(\delta_{XX}=0\). The unknown
coordinates are

\[
(a,b,\delta_{YY},\delta_{XY},\delta_{YX}).
\]

Measuring \(XX,YY,XY,YX\) once at times zero through three gives only four
records for five coordinates. More sharply, the setting offsets

\[
(0,1,2,3)
\]

on a static common mode generate the record sequence \((0,1,2,3)\), exactly
the same sequence as zero setting offsets under the affine drift \(z(t)=t\).
Setting and time are observationally aliased.

## Five-record anchored schedule

Repeat the reference setting after the other three:

\[
(XX,YY,XY,YX,XX)
\]

at times zero through four. The corresponding design matrix for the five
unknown coordinates has full rank five.

The two \(XX\) anchors determine the common affine trajectory. Each interior
record then supplies one independent setting residual. In the hostile above,
the first and last reference records are both zero, forcing zero common drift;
the three nonzero interior records are exposed as setting offsets.

Thus five direct scalar records are sufficient and worst-case necessary for
joint identification of affine common drift and all three relative setting
offsets under this model.

## Bounded-error version

Let the two reference anchors determine intervals at times zero and four. Under
the affine model, convex interpolation transports them to a predicted common
gain interval at each interior time. Sign-adjust the interior calibration
interval and compare it with the prediction.

- Disjoint intervals falsify zero setting offset.
- Overlapping intervals retain a bounded relative offset set.
- The three offset sets and the endpoint uncertainty jointly define the gain
  reachable set for the science packet.

Point interpolation is justified only when the affine model and anchor lineage
are admitted. With bounded-rate but nonlinear drift, use the corresponding
reachable tube instead.

## Schedule semantics

The repeated anchor repairs time/setting aliasing; it does not prove that the
gain law remains affine between anchors. Cheap additional falsifiers include:

- a midpoint repetition of the reference setting to test curvature;
- reversal of the setting order to expose hysteresis;
- a second anchored block to test reproducibility;
- randomized order with a continuously monitored common-mode port.

These are different experiment designs because they falsify different sensor
dynamics. They should not be pooled into one generic “calibration repeated”
claim.

## Marici consequence

Task ordering is part of the calibration instrument. The same multiset of five
setting labels can have different observability rank depending on their times
and repetitions. A calibration packet therefore needs the schedule, not only
the collected values.

This is another direct control contribution to Marici: the Carrier state is
not identifiable from an unordered record bag. Persistent excitation and
temporal anchoring are constructors that create the missing rank.

## Verification boundary

The dependency-free exact checker computes rank four for the one-pass design
and rank five for the repeated-anchor design. It constructs the exact affine
alias, shows the fifth record breaks it, and recovers the three setting offsets
from the anchored hostile.

The result assumes affine common drift and constant setting offsets within one
block. It does not cover hysteresis, switching transients, or coupled dead-time
dynamics.

