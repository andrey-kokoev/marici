# Flavor adaptive-control robustness radius

## Question

How much joint quotient-readout and actuation error can WP993's universal
feedback section tolerate while retaining strict selection of each labelled
configuration?

## Claim boundary

Errors are expressed directly in the invariant effective-control coordinates
\((Q,R)\) and bounded by a symmetric \(\ell_\infty\) box. No detector
calibration, error distribution, covariance, or physical control channel is
assumed.

## Exact radii

Let \((\delta Q,\delta R)\) be the total error after quotient readout,
feedback, and actuation. Requiring every corner of
\(|\delta Q|,|\delta R|<r\) to remain in the target's strict WP992 region
gives

\[
r_{\rm commuting}=\frac{3087}{3088},\qquad
r_{\rm rank\text{-}two}=\frac{24696}{24697},\qquad
r_{\rm full\text{-}rank}=\frac{1}{24697}.
\]

The joint three-label radius is therefore

\[
r_* = \frac{1}{24697}.
\]

The full-rank preparation is the unique bottleneck. At its hostile corner

\[
\delta Q=\frac{1}{24697},\qquad
\delta R=-\frac{1}{24697},
\]

the inequality \(R>24696Q\) becomes equality, so strict selection fails
exactly.

## Disposition

WP993 is not merely pointwise: it has a positive uniform formal robustness
margin on the entire positive quotient because its feedback maps every state to
the same three target points. The margin does not establish a physical
instrument. Admission now requires an independently calibrated joint error
bound strictly below \(1/24697\) in invariant units, with measurement,
feedback, actuation, common-mode covariance, and verification errors composed
in one frame.

## Verification

- `research/flavor/checkers/wp994_adaptive_control_robustness_radius.py`
- `research/flavor/results/wp994_adaptive_control_robustness_radius.json`
