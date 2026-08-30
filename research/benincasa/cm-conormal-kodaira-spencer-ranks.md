# The conormal Kodaira--Spencer packet has exterior ranks 3, 2, 0

## Packet

For the four labelled exact generators (g_alpha), define

\[
\kappa_j=(\partial_jg_1,\ldots,\partial_jg_4)\in R^4,
\qquad j=1,2,3.
\]

Every component is reduced only in its polynomial coefficient against the
seven-dimensional quotient. Generator labels are retained.

The checker then forms all three labelled pair wedges in

\[
\Lambda^2_RR^4
\]

and the triple wedge in

\[
\Lambda^3_RR^4.
\]

## Result

At A, B, and HOMA and at two primes, the finite-field ranks are

\[
(3,2,0).
\]

Thus:

- the three sections are linearly independent as vectors in the underlying
  28-dimensional finite-field space;
- their three pair wedges span a two-dimensional space;
- their triple wedge vanishes termwise in every labelled component.

Each run has a unique kinematics-dependent relation among

\[
\kappa_1\wedge\kappa_2,
\quad
\kappa_1\wedge\kappa_3,
\quad
\kappa_2\wedge\kappa_3.
\]

## Interpretation

The moving exact ideal has conormal rank two along the three-dimensional base,
despite the three sections remaining independent over the ground field. The
first possible coherence obstruction therefore lives at exterior grade two;
there is no independent grade-three Kodaira--Spencer class.

This is the natural target for the mixed curvature found in Entry 2648. A map
from that curvature to the two-dimensional pair-wedge packet must be derived
from the primitive/Koszul cone before any cancellation claim is made.

## Artifacts

- `research/benincasa/checkers/check_cm_conormal_kodaira_spencer.py`
- `research/benincasa/results/cm-conormal-kodaira-spencer.json`
- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`

