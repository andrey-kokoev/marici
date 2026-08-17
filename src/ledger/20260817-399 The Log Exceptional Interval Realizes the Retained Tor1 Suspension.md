---
id: 399
date: 2026-08-17
title: The Log Exceptional Interval Realizes the Retained Tor1 Suspension
---

# The Log Exceptional Interval Realizes the Retained Tor1 Suspension

The next obstruction after Entry 398 is graded rather than combinatorial.
The normalization/conductor pair source retains one \(\operatorname{Tor}_0\)
and one \(\operatorname{Tor}_1\) grade. Earlier finite audits proved that an
ordinary pair of unshifted corridor packets cannot realize them faithfully:
the target must be
\[
 P\oplus P[1],
\]
and a locally constant relative-dualizing line cannot place the two endpoints
in different degrees. The missing object was predicted to be a
wall-supported two-term relative-dualizing complex.

The log blowup used to construct the connector supplies exactly that object.
Its positive real exceptional fiber is an oriented interval with cellular
complex
\[
 \mathbb Z\langle e\rangle
 \xrightarrow{,d,}
 \mathbb Z\langle r_{D03},r_1\rangle,
 \qquad de=r_1-r_{D03}.
\]
Relative to its two boundary rays, the interval has one primitive class in
degree one. Tensoring the two-normal Boolean packet
\[
 P(t)=(1+t)^2=(1,2,1)
\]
with the absolute Tor-zero unit and this relative class gives
\[
 P(t)(1+t)=(1,3,3,1),
\]
exactly the previously required
\(\operatorname{Tor}_0oplus\operatorname{Tor}_1[1]\) profile.

## Endpoint and reflection compatibility

The boundary \(r_1-r_{D03}\) supplies the two endpoint restriction maps with
opposite signs; they are not chosen identity columns. Reflection exchanges
the two rays and reverses the exceptional interval. The relative suspension
orientation is also odd, so the two signs cancel and the total Tor-one
correspondence has degree zero and squares to \(+1\), as required by the
shifted-corridor reflection audit.

Normalized blowdown contracts the exceptional-only edge, but Entry 396
showed that its effect survives in the five-triangle descended Morse
homotopy. Thus the suspension is geometric upstairs and its comparison cell
is retained downstairs; it is not an extra formal shifted copy adjoined to
the literal complex.

## Consequence and remaining boundary

The marked log connector now carries both spectator Tor grades faithfully:
Tor zero uses the ordinary corridor packet, and Tor one uses the exceptional
relative fundamental class. This resolves the relative-dualizing suspension
gate that previously blocked the normalization/conductor realization.

What remains is the branch identification at the two global normalization
endpoints. The interval provides the correctly signed endpoint columns, but
one must still verify that their labelled rays coincide with the two
normalization-sheet costalks in the complete source object. Only that final
branch comparison instantiates the endpoint-fixed mapping fiber and makes
\(p_{\partial,Q}\) evaluable.

The executable audit is
research/voevodsky/check_log_exceptional_tor_suspension.py.
