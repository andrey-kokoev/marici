# A specialization kernel falsifies frozen v6

## Result

Version 6 is falsified. Its holonomy-naturality square can commute while specialization deletes the complete nontrivial-holonomy sector.

## Hostile packet

Let the nearby route space be two-dimensional with Euclidean metric and loop holonomy

\[
H_{\mathrm{near}}=\operatorname{diag}(1,-1).
\]

Let the exceptional route space be one-dimensional with holonomy

\[
H_{\mathrm{exc}}=(1).
\]

Use the nonzero specialization map

\[
J=\begin{pmatrix}1&0\end{pmatrix}.
\]

Then the v6 naturality law holds exactly:

\[
JH_{\mathrm{near}}=H_{\mathrm{exc}}J.
\]

This is not the trivial zero-map loophole. The map has rank one and faithfully transports the invariant line.

## Failure

The kernel of (J) is the second coordinate line. That is exactly the half-turn sector on which nearby holonomy acts by (-1).

The nearby holonomy-invariant space has dimension one inside a two-dimensional route space, so its retained boundary port has dimension one. The exceptional invariant space fills its one-dimensional route space, so its retained boundary port is zero.

Thus the square commutes while the entire boundary obstruction disappears into the specialization kernel.

v6 records the intertwiner but does not retain its kernel, cokernel, mapping cone, or vanishing-cycle object. Nor does it require specialization to be conservative on the boundary port. Its claim that specialization-compatible holonomy prevents silent erasure is therefore false.

## Required successor

A successor must replace bare naturality by an exact specialization defect packet. At minimum it must type:

- the specialization kernel and cokernel, or the full mapping cone;
- the induced holonomy on that defect;
- an exact relation among nearby, exceptional, and defect boundary ports;
- a prohibition against declaring strict descent until the defect port is sewn or explicitly retained.

The natural object is a vanishing-cycle triangle, not a stronger injectivity axiom: genuine degenerations may legitimately lose rank, but the lost transport sector cannot become invisible.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_v6_specialization_kernel_falsifier.py
```
