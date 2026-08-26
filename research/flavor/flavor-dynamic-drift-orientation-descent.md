# Dynamic drift orientation descent (WP279)

## Hostile frame change

WP278 uses the rotation generator

\[
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

It commutes with orientation-preserving rotations. Under the reflection

\[
Q=\operatorname{diag}(1,-1),
\]

however,

\[
QJQ^{-1}=-J.
\]

Thus the drift is intrinsic to an oriented two-dimensional module, not an
unoriented quotient. Its rank-two observation and control towers do not repair
this failure: faithfulness and descent are independent gates.

## Exact distinction

The original and reflected score towers both have rank two and observation
Gram determinant one. They reconstruct their local coordinates perfectly, yet
assign opposite drift directions to the same unoriented object. A mathematically
faithful probe family can still fail to define a physical quotient operation.

Covariance can be repaired by a pseudoscalar \(\omega\) that flips under
reflection, using \(A_{\mathrm{phys}}=\omega J\). But \(\omega\) must be
derived from the flavor source. Adding an external orientation instead creates
a new relational experiment over the orientation-preserving stabilizer
groupoid; it does not reveal an absolute orientation of the original module.

## Classification

WP278 remains a positive architecture on an oriented deviation module. It has
not yet descended to the full unoriented flavor groupoid. Progress requires a
source-derived orientation or CP-odd tensor, or a replacement drift built only
from already admitted quotient tensors.

Run `uv run --with sympy python
research/flavor/checkers/wp279_dynamic_drift_orientation_descent.py` for the
exact conjugation residual, pseudoscalar repair, and rank-versus-descent test.
