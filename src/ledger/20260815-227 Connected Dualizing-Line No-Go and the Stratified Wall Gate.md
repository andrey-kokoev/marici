# Connected Dualizing-Line No-Go and the Stratified Wall Gate

## Record

Date: 2026-08-15

Status: definitive scoped no-go. The shifted corridor packet of entry320
cannot be the restriction of one relative-dualizing line on a connected
perfect or log-smooth correspondence. This does not exclude a stratified
two-term dualizing complex, a derived wall object, or a correspondence whose
cotangent amplitude genuinely jumps at the wall. No graph admission is
claimed.

## Obstruction

Entry320 proves that Tor-faithful realization requires the two boundary
packets
\[
P\oplus P[1].
\]
Thus their required cohomological shifts are (0) and (1). The two packets
are exchanged by reflection and meet through the corridor wall.

For a connected perfect/log-smooth morphism whose extraordinary pullback is
given by a relative-dualizing line, the virtual relative dimension—and hence
the shift of that line—is locally constant. Restriction to the two boundary
charts must therefore give shifts ((d,d)), never ((0,1)). Equivariance
makes the same obstruction visible immediately: reflection sends
((0,1)) to ((1,0)), while the virtual rank of an equivariant line is
reflection invariant.

This is earlier than the endpoint and generic-(Q) equations. No choice of
orientation, sign, principal-line generator, or integral scalar changes a
cohomological shift.

## Why disconnection is insufficient

Two disconnected line components can carry shifts (0) and (1), but then
they have no common wall restriction. In particular they do not construct
the normal-circle corestriction, the endpoint Beck--Chevalley square, or the
reflection exchange homotopy required by the literal entry143 target.

The minimal additional datum is therefore not another line. It is a
reflection-equivariant stratified relative-dualizing complex with two
perfect boundary restrictions and a wall-supported cone whose restrictions
are (P) and (P[1]). Geometrically this may be supplied by a derived/log
normal-crossing correspondence with a specified vanishing-cycle or excess
triangle. Its wall map must derive the endpoint BC cells and identify the
result with the literal entry143 normal/Cech corestrictions.

## Consequence for the main objective

The finite (P\oplus P[1]) model remains correct, but entry320's proposed
realization specifically as a single relative-dualizing line is falsified.
The next construction must provide the two-term wall triangle. Until it is
constructed, the endpoint/(Q) mapping fiber, (p_{\partial,Q}), its
Bockstein, and the physical (D_8)/Jordan tests remain undefined.

## Executable evidence

Checker:
`research/voevodsky/check_dp6_relative_dualizing_line_no_go.rs`

The checker exhausts the relevant integral shifts, verifies connected
local constancy, checks the reflection exchange, and records why disconnected
line components do not supply the missing wall BC map.

SHA-256:
`e570ed3c0f0edb5a9aae8d7b0c549a51119c44b66512b58ef0d410071892e9ca`

Fresh `rustfmt --check`, warnings-denied optimized compilation, runtime
assertions, and JSON output passed. Native PowerShell was used only because
the user-site structured-command surface is scoped outside this repository
and does not admit `rustc`.

## Outcome contract

~~~json
{
  "claim": "A connected perfect/log-smooth correspondence with line-valued relative dualizing complex has one locally constant shift and therefore cannot restrict to the reflection-exchanged shifted corridor packets P and P[1].",
  "status": "falsified_scoped_connected_relative_dualizing_line",
  "scope": "one connected perfect or log-smooth correspondence whose extraordinary shift is a relative-dualizing line of locally constant virtual rank",
  "desired_boundary_shifts": [0, 1],
  "reflection_sends_shifts_to": [1, 0],
  "excluded_from_no_go": [
    "stratified two-term relative-dualizing complexes",
    "derived wall or vanishing-cycle objects",
    "nonperfect correspondences with genuine cotangent-amplitude jump",
    "disconnected boundary charts equipped with an independently constructed wall connector"
  ],
  "minimal_additional_geometry": "a reflection-equivariant two-term relative-dualizing/excess triangle supported on the corridor wall, with literal entry143 normal-Cech and endpoint Beck-Chevalley realization",
  "unconstructed": [
    "wall-supported dualizing cone",
    "literal entry143 comparison",
    "endpoint connector cells",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_relative_dualizing_line_no_go.rs",
  "checker_sha256": "e570ed3c0f0edb5a9aae8d7b0c549a51119c44b66512b58ef0d410071892e9ca"
}
~~~
