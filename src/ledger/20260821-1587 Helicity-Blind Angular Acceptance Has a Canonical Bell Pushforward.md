# 1587 — Helicity-Blind Angular Acceptance Has a Canonical Bell Pushforward

Date: 2026-08-21

Sequence claim: `seqclaim-8019a4baee0f04142a405226`

## Result

The pointwise photon Bell packet of Entry 1586 extends canonically to angular
bins.  For a common nonnegative helicity-blind acceptance weight, push forward
the unnormalized density and normalize only after integration:

\[
\rho_R=
\frac{\int_R w(x)|\psi(x)\rangle\langle\psi(x)|dx}
{\int_R w(x)\langle\psi(x)|\psi(x)\rangle dx}.
\]

For the low-energy source amplitudes and the interval \([L,U]\), put

\[
W_j=\int_L^U(1-x+x^2)^jdx,
\qquad W_0=U-L.
\]

Then

\[
I_{[L,U]}=
\frac{8\sqrt2,gfW_1}{g^2W_0+4f^2W_2}.
\]

On the full angular interval,

\[
I_{[0,1]}=
\frac{(20\sqrt2/3)gf}{g^2+(14/5)f^2}.
\]

An exact calculation of all sixteen integrated joint probabilities proves
normalization and both no-signalling families.  This completes the requested
pointwise-to-accepted-event extension under the sharp support condition:
acceptance is one positive scalar on the momentum base and the identity on the
helicity fiber.  Entry 1578 remains the falsifier for outcome-dependent
acceptance.

## Evidence

- `research/nima/check_angular_bin_bell_pushforward.py`
- `research/nima/results/angular-bin-bell-pushforward.json`
- `research/nima/angular-bin-bell-pushforward.md`
- epistemic-graph event: `ev-000000001762-e0315bfb-303d-40ac-9154-77514f31803e`.
