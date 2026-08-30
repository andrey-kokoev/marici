# Correlated calibration selector (WP288)

## Joint support instead of a marginal box

WP287 used independent calibration intervals. That is safe but can erase
source-authorized correlations. Consider a weighted triangle whose edge
tensions and local biases depend affinely on one calibrated source error
$t\in[-1,1]$. Choose the biases so that every local selector margin is

\[
h_i(t)-\sum_jJ_{ij}(t)=\frac15.
\]

Because each margin is affine on a line segment, checking its two vertices is
necessary and sufficient. Both endpoints, and hence the entire joint support,
retain a strict selector margin.

## Hostile projection

Projecting the same joint packet to independent marginal intervals permits
edge maxima and bias minima that never coexist in the source model. The box
then has zero worst margin at all three vertices and rejects strict selection.
Therefore a nonfaithful uncertainty projection can create false negatives just
as a measured-coordinate projection can create false uniqueness.

This does not license a convenient correlation. The joint support must be
derived and calibrated before the selector is evaluated. Otherwise the
correlation is merely a projector fitted from the desired answer.

## Classification

The correlated packet repairs robustness only inside the declared calibration
experiment. It is a conditional selector certificate, not a source-derived
`physical16` selector. Admission still requires the joint support, its tails,
the physical dynamics, and the branch-to-flavor map in one common frame.

Run `uv run --with sympy python
research/flavor/checkers/wp288_correlated_calibration_selector.py` to
regenerate the exact vertex and box-projection audit.
