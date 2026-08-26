# Grothendieck moving-seam cocycle

## Source mapping

Primary source:
`research/grothendieck/theta-moving-seam-projection-cocycle-nonfredholm.md`.
The same defect supplies the moving endpoint in
`theta-labelled-overlap-moving-seam.md`.

`MovingSeamSystem G V` contains a fixed cut `P`, a transport action, the
composition law, and preservation of subtraction. Its defect is

\[
C_g=P-gP.
\]

`MovingSeamSystem.defect_add` proves the exact non-strict coherence law

\[
C_{gh}=C_g+gC_h.
\]

`defect_eq_zero_iff` separates strict invariance from coherent transport, and
`nonzero_defect_rejects_strict_transport` makes the rejection executable.

## Hostile

The parity-reflection fixture uses a two-element additive transport index and
the cut `1 : ℤ`. The nontrivial transport negates the carrier, so its seam
defect is `2`. The two-step cocycle holds exactly, while the nontrivial
transport does not fix the cut. Thus coherence does not collapse the moving
seam into strict equality.

## Analytic boundary

This module formalizes the algebraic cocycle only. It does not infer that the
continuum projection difference is compact, finite rank, Fredholm, or
determinant class. Grothendieck's source proves the opposite on uncompressed
`L²(ℝ)`. A Lean version of that analytic no-go needs a typed multiplication
operator, the positive-measure interval subspace, and a compact-operator
criterion. Any source compression must be supplied before determinant-line
language is admitted.

## Verification

Per Nima's instruction, no Lean build was run. The module is not imported by
`MariciFormal.lean`; elaboration remains unverified.
