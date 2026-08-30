# A Stable Decoder Requires an Authorized Actuator Lift

Let (xin X) carry residual (Rxin Z), and let the seam observation be
(Hxin Y). Stable inference provides a decoder (S:Y\to Z) with

\[
R=SH.
\]

An actuator is a map (B:Y\to X) used in the correction

\[
x\longmapsto x-BHx.
\]

It cancels the residual for every admitted state exactly when

\[
R(I-BH)=0,
\]

or equivalently

\[
R=RBH.
\]

Thus the inferred decoder must lift through the residual map:

\[
S|_{\operatorname{ran}H}=(RB)|_{\operatorname{ran}H}.
\]

Existence of a bounded (S) does not imply existence of an authorized (B).
The actuator image

\[
\mathcal D_{\mathrm{act}}
=\{RB:B\in\mathcal B_{\mathrm{authorized}}\}
\]

must contain the required decoder on the observed range.

## Minimal hostile

Take (X=Y=Z=\mathbb R^2) and (H=R=I). Observation and decoding are perfect,
with (S=I) and decoder norm one. Suppose the authorized actuator space
contains only maps with image in (\mathbb R e_1). Then every authorized
(B) has a zero second row under (R=I), so no (RB) equals (I). The state
(e_2) is perfectly diagnosed and never corrected.

Adjoining (B=I) repairs the hostile algebraically, but this is admissible only
when the source constructor list independently authorizes control of both
coordinates. The compiler may identify the missing actuator direction; it may
not manufacture it.

## Stability and protected structure

Even an authorized lift needs more than pointwise cancellation:

- (B_N) must remain uniformly bounded in the source and target topologies;
- the update must preserve protected constraints and local repair equivalence;
- sheet, real-frame, and successor coherence must commute with the feedback;
- controller faults and actuator faults remain distinct;
- a correction selected from several lifts requires a source rule or declared
  optimization criterion.

The exact hierarchy is therefore

\[
\text{faithful observation}
\;<\;
\text{stable decoder}
\;<\;
\text{authorized actuator lift}
\;<\;
\text{coherent executable correction}.
\]

## Falsifiers

- (R=SH) holds but (S\notin\mathcal D_{\mathrm{act}}).
- The actuator corrects only a proper residual subspace.
- An unauthorized right inverse of (R) is silently inserted.
- Actuator norms diverge with cutoff.
- Feedback cancels the scalar residual while violating seam or frame
  coherence.
- A preferred lift is selected without a source criterion.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. Stable inference, actuator lift, cancellation, and authority were frozen
as separate gates.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The missing compiler arrow became the exact lift equation (S=RB) on
the observed range. Perfect decoding was shown compatible with a one-direction
actuator deficiency, cleanly separating knowledge from control.
