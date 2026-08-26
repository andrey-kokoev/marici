# Higgs quartic second-source gate (WP416)

## Independent source operator

WP415 asks for a second source operation whose response is not proportional to
the Higgs quadratic deformation. The minimal gauge-invariant candidate already
present in the Standard Model action is the quartic operator. Consider

$$
V(\phi;\delta c,\delta\lambda)
=\frac{-\mu^2+\delta c}{2}\phi^2
+\frac{\lambda+\delta\lambda}{4}\phi^4.
$$

Freeze the undeformed broken vacuum $v_0$, where $\lambda v_0^2=\mu^2$, and
retain it as the WP412 reference port. The curvature and relative tadpole are

$$
H_{\rm rel}=2\mu^2+\delta c+3v_0^2\delta\lambda,
\qquad
J_{\rm rel}=v_0\delta c+v_0^3\delta\lambda.
$$

Their two-source response is

$$
J_{\rm src}=
\begin{pmatrix}
1&3v_0^2\\
v_0&v_0^3
\end{pmatrix},
\qquad
\det J_{\rm src}=-2v_0^3.
$$

The wedge is nonzero throughout the broken phase. For a positive calibrated
readout metric $W=\operatorname{diag}(w_H,w_J)$,

$$
\det(J_{\rm src}^TWJ_{\rm src})=4v_0^6w_Hw_J>0.
$$

Thus the quadratic and quartic deformations are locally distinguishable by the
same two relational readouts. The source errors can be reconstructed exactly:

$$
\delta c=-\frac{\Delta H}{2}+\frac{3\Delta J}{2v_0},
\qquad
\delta\lambda=\frac{v_0\Delta H-\Delta J}{2v_0^3}.
$$

## Descent and boundary

Both source terms are gauge-invariant Higgs operators and contain no quark
weak-basis coordinates. Their response therefore descends independently of the
flavor texture charts and the full quark weak-basis groupoid. The readout still
depends on retaining the undeformed broken vacuum as a relational reference;
recentering at the deformed equilibrium removes the tadpole.

The exact falsifier is the symmetric boundary $v_0=0$, where the reference and
response wedge collapse. This is a domain boundary, not an ensemble exception.

## Physical-instrument gate

WP416 closes the source-operator and rank-two algebraic gates, but not the
experimental gate. The Standard Model quartic is a measured coupling, not an
available laboratory control setting. No admitted apparatus independently
varies $\delta\lambda$ while preserving the same vacuum reference and measuring
both curvature and relative displacement. Treating collision energy as a
quartic knob would again confuse a probe coordinate with a source operation.

Run `uv run --with sympy python
research/flavor/checkers/wp416_higgs_quartic_second_source.py` to regenerate the
JSON result.
