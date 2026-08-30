# Frozen non-Abelian degenerate-mode signature v12

## Status

Version 12 is a new frozen local candidate. Version 11 remains unchanged and falsified.

v12 retains the full rank-(r) eigenbundle and its (U(r)) transport before determinant, projector, or aggregate quotients.

## Repair of the v11 hostile

For the rank-two packet with loop holonomies

\[
U=iX,
\qquad
V=iZ,
\]

v12 stores the ordered matrices themselves. It therefore retains

\[
UVU^{-1}V^{-1}=-I,
\]

even though every determinant involved equals one.

## Full matrix connection

Each multiplicity stratum carries orthonormal rank-(r) frames, (U(r)) transition functions, a matrix connection, conjugation-covariant curvature, and an ordered path-groupoid holonomy representation.

Specialization is horizontal at matrix level:

\[
dJ+A_{\mathrm{target}}J-JA_{\mathrm{source}}=0.
\]

Only after this identity and all path or braid relations pass may the apparatus take determinant-line, projector, or aggregate-resolvent quotients.

## First unused hostile

Compare the holonomy pairs

\[
(iX,iZ)
\qquad\text{and}\qquad
(iX,iX).
\]

Every individual loop matrix has the same trace, determinant, and spectrum. But the first pair has commutator (-I), while the second has commutator (I).

v12 distinguishes them because individual conjugacy classes do not replace the ordered joint representation.

## Next falsifier

Attack projective coherence: construct matrix transports that agree projectively on every loop but differ by a central cocycle on triple composition. That tests whether a bundle connection is sufficient or whether a gerbe or 2-group lift is required.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_frozen_bivariant_signature_v12.py
```
