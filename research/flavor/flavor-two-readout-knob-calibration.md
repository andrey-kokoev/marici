# Two-readout knob calibration (WP401)

## Bounded question

Can an executable detector distinguish the independent curvature and tadpole
errors that could invalidate WP400's locked affine context law?

## Source-error packet and readouts

Let the independent source perturbations be $\delta m$ and $\delta j$. Use the
joint readout

\[
H=M^2+\delta m,
\qquad
A_\star=\frac{J_0+\delta j}{M^2+\delta m}.
\]

Here $H$ is the mediator curvature, operationally accessible through a pole or
susceptibility measurement, and $A_\star$ is the stationary displacement.
Both must be expressed in one calibrated detector frame.

At the baseline, the response Jacobian is

\[
J_{\mathrm{det}}=
\begin{pmatrix}
1&0\\
-J_0/M^4&1/M^2
\end{pmatrix},
\qquad
\det J_{\mathrm{det}}=\frac1{M^2}>0.
\]

For any independently calibrated positive diagonal detector metric $W$,

\[
\det(J_{\mathrm{det}}^TWJ_{\mathrm{det}})
=\frac{w_Hw_A}{M^4}>0.
\]

The joint instrument therefore separates the two source errors locally.

## Exact global inversion

On the healthy domain $H>0$, the errors are reconstructed exactly:

\[
\delta m=H-M^2,
\qquad
\delta j=A_\star H-J_0.
\]

Displacement alone is insufficient. Its first-order kernel contains the
nonzero direction

\[
(\delta m,\delta j)\propto(M^2,J_0).
\]

The curvature readout detects this direction and removes the ambiguity.

## Locked-knob test

WP400's proposed common context knob has source tangent $(1,J_1)^T$. The
predicted detector tangent is

\[
\left(1,\frac{J_1M^2-J_0}{M^4}\right)^T.
\]

Measuring both components tests whether curvature and tadpole shifts really
remain locked. It calibrates the slope $J_1$ but does not explain or select its
value.

## Disposition

WP401 constructs the exact rank-two detector map requested by the earlier
source-support analysis. It is a source-error separator and instrument design,
not a numerical flavor selector.

The remaining physical gate is finite uncertainty: pole width, background,
resolution, and support must leave the smallest singular value distinguishable
from zero. The pole and displacement readouts must also arise from the same
mediator and calibration chain.

Run `uv run --with sympy python
research/flavor/checkers/wp401_two_readout_knob_calibration.py` to regenerate
the result.
