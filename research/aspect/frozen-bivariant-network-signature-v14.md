# Frozen degree-five projective-transport signature v14

## Status

Version 14 preserves v13 and extends the preregistered Postnikov profile through degree five.

Degrees two, three, four, and five are frozen before replay. Degree six remains the explicit rejection boundary.

## Degree-four and degree-five gates

The degree-four repair is

\[
\omega_4(a,b,c,d)=(-1)^{abcd}.
\]

The first unused packet is

\[
\omega_5(a,b,c,d,e)=(-1)^{abcde}.
\]

The checker exhausts the full normalized cocycle equations for both packets, not only selected tuples. Both have nontrivial value on the all-ones tuple.

Each declared degree carries its own cocycle representatives, coboundary gauge action, Postnikov invariant, and specialization map. Strictification requires compatible trivializations at every degree through five.

## Anti-vacuity boundary

v14 cannot add a degree-six cell during replay. A degree-six hostile must be rejected or motivate an immutable successor version.

## Conductor control

Benincasa's global conductor cover supplies a strict non-Abelian control. Six independent square classes give deck kernel ((\mathbb Z_2)^6). The occurrence (C_3) action permutes them in two free three-cycles, producing

\[
(\mathbb Z_2)^6\rtimes C_3
\]

of order (192). Its multiplier is (+1), so it strictifies without erasing its ordered non-Abelian transport.

## Verification

```text
uv run python research/aspect/checkers/check_frozen_bivariant_signature_v14.py
```
