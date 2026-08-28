# Frozen degree-twenty projective-transport signature v15

## Status

Version 15 preserves v14 and preregisters the Postnikov profile through degree twenty.

Degrees two through twenty are frozen before replay. Degree twenty-one is the explicit rejection boundary.

## Twenty-level cocycle tower

At every declared degree (n), the finite hostile packet is the normalized monomial cocycle on \(\mathbb Z_2\):

\[
\omega_n(a_1,\ldots,a_n)=(-1)^{a_1\cdots a_n}.
\]

The checker exhausts the complete normalized cocycle equation at all nineteen degrees from two through twenty. It also verifies the nontrivial all-ones value separately at every degree.

This is a tower resolving cocycles at twenty possible degrees. It does not assert the existence of twenty independent cohomology classes in an arbitrary source packet.

## Anti-vacuity boundary

v15 cannot add a degree-twenty-one cell during replay. A valid degree-twenty-one hostile is rejected unless a later immutable profile preregisters it.

Greater depth also cannot repair a missing constructor of another type. In particular, Benincasa's rank-one sheet-evaluation defect still requires a source-derived specialization-cone cell; it cannot be relabelled as a higher cocycle.

## Verification

```text
uv run python research/aspect/checkers/check_frozen_bivariant_signature_v15.py
```
