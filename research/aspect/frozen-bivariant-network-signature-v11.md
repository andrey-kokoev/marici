# Frozen phase-framed spectral-cover signature v11

## Status

Version 11 is a new frozen local candidate. Version 10 remains unchanged and falsified.

v11 lifts every projector sheet to a phase-framed eigenline or, for higher rank, its determinant line.

## Repair of the v10 hostile

For the positive spin-half eigenline, north and south frames obey

\[
u_S=q^{-1}u_N.
\]

Their projectors agree, but the transition has winding minus one. v11 retains the transition cocycle, connection, curvature, characteristic class, and loop holonomy before applying the projector quotient.

The projector is recovered from a frame outer product; it is explicitly the phase-forgetful quotient.

## Connection gate

Local connection forms obey the unitary gauge-transformation law on chart overlaps. Their curvature represents the declared characteristic class, while loop periods determine holonomy.

Labelled specialization must be horizontal:

\[
dJ+A_{\mathrm{target}}J-JA_{\mathrm{source}}=0.
\]

This incorporates Benincasa's conductor-root result. For (r^2=C_1/x), the odd line has residue (1/2) and monodromy (-1); aggregate forgetting occurs only after this framed identity is checked.

## First unused hostile

A flat line over a circle can have zero curvature and zero first Chern class while carrying half-turn holonomy (-1). Therefore characteristic-class data alone are insufficient. v11 separately retains the holonomy character.

## Next falsifier

Use a degenerate rank-two eigenspace with non-Abelian Wilczek–Zee holonomy. Its determinant line records only the determinant of the transport and may miss an (SU(2)) rotation inside the eigenspace.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_frozen_bivariant_signature_v11.py
```
