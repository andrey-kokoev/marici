# Projective direction selector (WP303)

## Changed state domain

Suppose the admitted lens identifies positive rescalings,

\[
x\sim\lambda x,
\qquad \lambda>0.
\]

On this projective quotient, WP302's vectors $(1,1)$ and $(2,2)$ are the
same physical ray. Swap symmetry selects the single fixed ray $[1:1]$ in the
positive affine chart. The formerly free amplitude is gauge only relative to
this explicitly changed groupoid.

This is a genuine projective ratio selector as well as a direction
rigidifier. It is not yet a selector on the original `physical16` quotient,
where absolute ordered masses and invariant magnitudes are physical.

## Normalization lift

Lifting the selected ray with radius $\rho$ gives

\[
x(\rho)=\frac{\rho}{\sqrt2}(1,1).
\]

Radii 1 and 2 produce distinct physical points while retaining the same
projective coordinate. The first missing arrow is therefore `selected ray ->
source-normalized physical16 point`.

A normalization port does not reveal an absolute scale hidden in the
projective experiment. It defines the lift through an additional physical
operation. Its source, units, calibration, and uncertainty must be declared.

## Classification

Progress is relative to the admitted domain: symmetry can select a proper
projective lens even though it cannot select full `physical16`. To promote the
result, positive scaling must first be proved redundant for the target flavor
subproblem, and every physical radial coordinate must be restored by an
independently derived normalization.

Run `uv run --with sympy python
research/flavor/checkers/wp303_projective_direction_selector.py` to regenerate
the exact quotient-and-lift audit.
