# A non-Abelian degenerate mode falsifies frozen v11

## Result

Version 11 is falsified. Its determinant-line fallback for higher-rank eigenspaces erases internal non-Abelian transport.

## Hostile packet

Take a constant rank-two degenerate eigenspace over a base with two independent loops. The spectral projector is the identity on that two-dimensional mode space.

Compare two flat transport packets. The first has trivial loop holonomies. The second has

\[
U=iX,
\qquad
V=iZ,
\]

where (X) and (Z) are Pauli matrices.

Both matrices are unitary and have determinant one. Therefore both loop transports induce trivial holonomy on the determinant line, exactly like the trivial packet.

## Decisive difference

The full matrix commutator is

\[
UVU^{-1}V^{-1}=-I.
\]

For trivial transport it is (I). Yet both commutators have determinant one.

Thus the projector, determinant line, determinant holonomies, first Chern data, and aggregate resolvent can all agree while the internal rank-two transport differs by a central non-Abelian phase.

This is the Wilczek–Zee version of the Berry hostile. An optical instrument with coherent access to the two-dimensional degenerate mode space can distinguish the packets by ordered loop interferometry.

## Exact defect in v11

v11 retains a full phase-framed line only for rank one. For higher rank it names the determinant line, which is the abelianized shadow of the frame bundle. It has no full (U(r)) connection or matrix holonomy representation.

## Required successor

A successor must retain:

- the full rank-(r) degenerate eigenbundle;
- its (U(r)) transition cocycle and connection;
- matrix-valued curvature and ordered loop holonomies;
- horizontal specialization before taking determinant, projector, or aggregate quotients;
- braid and path-groupoid relations at the matrix level.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_v11_nonabelian_holonomy_falsifier.py
```
