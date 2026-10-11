# Retained phase attachment: local derivation and full-arrow compatibility

## Question and fixed contract

Can the phase correction be obtained from the generated local modes and retained transports, rather than fitted to the assembled return? Does it require an additional complex?

Keep the proposed electron rule: reverse the generating triangle cycles while keeping their selected character fixed. The generated coefficients are the conjugates of the source coefficients; the real transport stage is unchanged.

Specify a frame-registration law: corresponding typed stage/triangle/axis ports may differ by unit scalar phases, with no mixing of channels. Every original coefficient arrow must intertwine. This law is supplied explicitly; it is not derived from identifying two undecorated spatial points.

For a source arrow s→t with coefficient h, require

```text
h d_s = d_t conjugate(h),
so d_t / d_s = h / conjugate(h).
```

All source arrows are nonzero. These equations concern all 1836 arrows on 108 typed ports, not only the rank-one return N.

## Derivation from the local generator

For each triangle, reconstruct the source mode v=X(1,ω,ω²). Cycle reversal gives conjugate(v). All three components are nonzero in these source frames, so set

```text
D_triangle = diag(v_a / conjugate(v_a)).
```

This maps the reversed mode vector back to the source vector and has unit-norm diagonal entries. The source's real tetrahedral rotations transport the seed correction consistently:

```text
D_triangle = R_triangle D_seed R_triangle^T.
```

Hence the correction is reconstructed from the oriented seed frame, selected character, and real transports. It is not an independently fitted 36-coordinate table. The same phase applies to a coordinate at each of the raw, local, and aligned stages.

An independent solve of the 1836 arrow equations produces exactly these geometric phases after one common root normalization. This is a stronger compatibility result than matching N alone.

## Existence and uniqueness

The constraint graph is connected:

- 108 typed ports;
- 107 spanning-tree constraints determine their relative phases;
- all 1729 remaining cycle constraints agree.

There is no phase obstruction around any graph cycle. A common root phase remains free. Fixing `raw/AB/x` to phase 1 gives one solution.

Uniqueness follows without a numerical search: for two solutions d and e, each nonzero arrow implies d_t/e_t=d_s/e_s. Connectedness makes their ratio the same at every port. Thus there is exactly one class modulo a common phase.

If the attachment's absolute common phase is to be observable, this calculation leaves a unit-phase freedom rather than selecting two values. The source operator-matching condition alone does not fix such an external phase observable.

## What retention requires

A sufficient retained record is:

- the oriented seed triangle frame;
- the selected cyclic character;
- the tetrahedral transport frames;
- the correspondence of typed ports.

The phase table can be regenerated from that record. The barycenter's position alone does not contain this information.

Removing the correction while holding both frames fixed breaks 72 raw-to-local arrows and 864 aligned-to-raw arrows. The real transport arrows do not need a correction of their weights.

Nevertheless, a necessary frame correction is not a necessary additional carrier. Re-expressing each electron port in its aligned frame transforms every conjugated arrow coefficient back to the original coefficient. Every source arrow label remains present. Along any path, intermediate phases cancel, leaving only endpoint phases; on a closed path they cancel completely.

This is a bijective change of coefficient frames, not deletion of the 1836-arrow history or a refund of traversal resources. It gives no additional retained path object by itself. An independently specified interface implementation might carry its own resources or history, but those are not selected by these equations.

## Negative control

Multiplying one edge's required relative phase by ω makes the constraint system inconsistent. Thus the solver can detect a genuine cycle obstruction; the absence of one in the source is a result, not something enforced by allowing arbitrary port phases.

## Outcome for hydrogen/deuterium

The phase map is now derived from the local cyclic construction under an explicit registration contract, and checked across the full typed protocol. The former fixed-frame mismatch is resolved by retained frame data.

Under this same scalar-frame contract there is only one phase class, not two inequivalent closures. No indispensable neutron-like complex is obtained. In particular, the hypothesis that this phase mismatch alone forces an additional carrier fails in this class.

This does not rule out an extra retained structure under another independently motivated attachment law or observable. It does mean that merely retaining the current phase correction does not supply the missing isotope distinction. The next issue is no longer finding this phase map, but identifying any additional attachment structure that cannot be absorbed into this full-arrow frame equivalence.

## Verification

```text
python research/voevodsky/checkers/check_retained_phase_attachment.py
```

Sixteen exact checks pass. `results/retained_phase_attachment.json` records the contract, all port phases, a spanning tree, source/checker hashes, fixed-frame mismatch counts, and the negative control. The original source remains unchanged.
