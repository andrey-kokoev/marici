# Blowdown Beat Compression Does Not Start

## Result

The actual D03 barycentric blowdown

\[
b:G_{03}\longrightarrow X
\]

does not factor by the proposed sequence of ring-compatible ordinary
beat-point retractions.  On the complete 581-cell barycentric carrier, there
is no first beat point whose beat neighbour has the same blowdown label.

The executable census is

\[
581\text{ active cells},\qquad
0\text{ equal-label beat removals},\qquad
45\text{ distinct target labels}.
\]

Thus the proposed length-one-at-each-step costandard compression cannot be
used to type \(\omega_b=b^!\mathcal O_X\).

## Exact boundary

This is a falsification of one compression strategy, not a proof that
\(\omega_b\) is non-perfect.  Ordinary beat-point removal requires the
strict upper or lower neighbourhood of the removed point to have a universal
comparable neighbour.  The barycentric face poset has no compatible point of
that kind at its initial state.

A weak-point or discrete-Morse collapse would establish only a topological
or chain contraction unless its homotopy is also shown to respect the
ringed incidence-module adjunction.  It therefore cannot be substituted
silently for the missing bounded finite-projective resolution.

The remaining gate is unchanged: compute the actual incidence module
\(\omega_b\), then either exhibit a bounded finite-projective resolution or
produce a module-theoretic obstruction.  Only after that decision is a
supported comparison with Entry 176 meaningful.

## Evidence

`research/voevodsky/check_d03_blowdown_beat_compression.rs` reconstructs the
45 old faces, 51 stellar-blowup faces, and barycentric census
\([51,194,240,96]\).  It tests both upper- and lower-beat conditions in the
full induced order and requires equality of the actual initial-face blowdown
labels.  The checker asserts that the removal count is zero.

Worker-delegation run `run-e2275878c16b4ac7883dfbb507118c08` was requested
as a low-cognition audit of stronger collapse criteria.  It is not evidence
for the result above unless and until it returns a substantive certificate.
