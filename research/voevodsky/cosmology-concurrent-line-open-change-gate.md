# Concurrent-line open-change gate

## Question

Can a genuine surface geometry add the primitive face missing from the exceptional triangle?

## Claim boundary

Changing the three projective boundary lines from a triangle to three concurrent lines removes the cycle. The generic coefficient matrix has determinant one; its dual graph is a 3-cycle and the complement has second cohomology rank one. The concurrent matrix has determinant zero. Blowing up its triple point produces a four-vertex star with first homology zero, while the complement is an affine-line bundle over `P1` minus three points and has second cohomology rank zero.

This is not the original triangle plus a face. Resolution replaces the three pairwise-intersection edges by the star edges, so the original triangle is not retained as a subcomplex. The open complement and its cohomology change.

On a smooth surface, an SNC boundary cannot have three components meeting transversely. A filled three-vertex face therefore requires a non-SNC triple point, higher-dimensional geometry, or a nongeometric attachment.

## Disposition

The concurrent arrangement genuinely kills the primitive class but does not fill the original pair. The next leaf audits the degeneration comparison and vanishing-cycle sequence to determine whether it transports a filler or instead identifies `Xi_log` as precisely the class lost at concurrency.

## Verification

- `research/voevodsky/check_cosmology_concurrent_line_open_change_gate.py`
- `research/voevodsky/results/cosmology_concurrent_line_open_change_gate.json`
