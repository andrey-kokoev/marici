# Single-Constructor Portal Unavoidability Certificate

## Question

What would a source principle have to derive for the asymmetric portal to be
unavoidable rather than an allowed coefficient (g_n-g_m)?

## The required source object

The smallest adequate principle is not a numerical extremum. It is one
source-natural constructor

\[
\mathcal C:I\longmapsto
(Q,D,\mathcal A,\beta,\mathcal B,\mathcal M,P_{\rm det}),
\]

from primitive oriented incidence (I) to a complete flavor theory and its
realization. Its outputs have distinct jobs:

- (Q) supplies the primitive oriented current and fixes the sign of the
  charge contrast;
- (D) and source action \(\mathcal A\) select the finite completion and
  mixing orientation;
- \(\beta\) and its basin \(\mathcal B\) select the coupling magnitude and
  the realized RG trajectory;
- \(\mathcal M\) is the finite-width, finite-mixing threshold map;
- (P_{\rm det}) is a calibrated labelled physical readout in the same
  source frame.

The word “one” is substantive: every arrow must be derived functorially from
the same admitted source packet. Coordinate compatibility between separately
valid objects is not a constructor.

## Exact conditional prediction

For the primitive current (q=(1,2,3)^T), the oriented portal contrast is

\[
\Delta q=q_3-q_2=1.
\]

If the same source constructor derives the controlled gauge--Yukawa flow

\[
\beta_x=2x^2(-b+cx-dy),\qquad
\beta_y=2y(ay-fx)
\]

with (a=b=d=f=1,c=3), then it selects

\[
x_*=y_*=\frac12,qquad
g_n-g_m=\Delta q\sqrt{x_*}=\frac1{\sqrt2}>0.
\]

The stability eigenvalues are (1/2) and (2), so the packet has a local
two-dimensional infrared basin. This is a complete sign-and-magnitude
prediction only if the constructor derives the coefficients and selects the
trajectory; specifying them by hand merely renames the tuning.

## Six independent gates

1. **Spectrum:** WP836 conditionally excludes every nonempty direct charged
   or neutral completion, but minimization of its functional lacks source
   authority.
2. **Mixing:** WP837 conditionally fixes the normalized reflection (H_q),
   but the reflection attachment law lacks source authority.
3. **Magnitude:** changing only (c:3\mapsto4) preserves the primitive
   incidence but moves (x_*) from (1/2) to (1/3).
4. **Basin:** positive local eigenvalues do not establish a global basin or
   select which trajectory is realized.
5. **Threshold:** an identity matching map preserves the contrast, whereas
   an inclusive rank-one map annihilates it. Matching must be derived, not
   chosen after seeing the answer.
6. **Readout:** two labelled rows have rank two; their inclusive sum has rank
   one and erases the contrast. Aspect's comb reference establishes a common
   comparison frame, but its own contract states that it does not select the
   source flavor value.

These gates are logically independent. Passing five does not infer the sixth.

## Aspect germ type

The marked germ contains the incidence, current attachment, completion-family
comparison port, beta-system provenance, threshold history, detector label,
and calibration epoch. The target relation is the end-to-end composite from
one source identity to one labelled record. Completing any component before
forming a relation that does not descend through its fiber is forbidden.

## Current disposition

No currently admitted flavor object realizes \(\mathcal C\). The present
programme has compatible fragments:

\[
\text{WP820}+\text{WP836}+\text{WP837}+\text{WP821}
+\text{Aspect comb readout},
\]

but their conjunction is not an authority-bearing parallelization. The
strongest justified answer is therefore an acceptance theorem:

> The asymmetric portal becomes unavoidable exactly when one source-natural
> constructor generates the oriented representation, unique finite spectral
> action, controlled fixed-point basin, contrast-preserving threshold map,
> and calibrated labelled realization, with all comparison ports retained
> until their target relations are formed.

The first missing arrow is from primitive incidence and finite spectral data
to a uniquely derived interacting action and its beta coefficients. This is
the next search target. The smallest exact falsifier is the same-incidence
pair (c=3) and (c=4): it preserves all upstream current data while changing
the predicted portal magnitude.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp838_single_constructor_portal_unavoidability_certificate.py
```
