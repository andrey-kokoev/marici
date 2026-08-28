# The Charge-Recursive Potential Selects the Primitive Spurion Orbit

WP849 removes WP848's two-dimensional VEV-ratio fiber with the positive
gauge-invariant potential

\[
\begin{aligned}
V={}&\lambda_1(|s_1|^2-v^2)^2
+\lambda_2v^2\left|s_2-\frac{s_1^2}{v}\right|^2\\
&+\lambda_3v^2\left|s_3-\frac{s_1s_2}{v}\right|^2,
\qquad \lambda_i>0.
\end{aligned}
\]

Its zero locus is the single orbit

\[
v(e^{-i\theta},e^{-2i\theta},e^{-3i\theta}).
\]

Gauge fixing gives ((s_1,s_2,s_3)=(v,v,v)). The zero orbit is independent
of all positive coefficient values, the gauge-fixed Hessian is positive
definite, and the lifted kernel becomes (v^2(1,2,3)^T). Thus the projective
primitive ray is selected without coefficient-ratio tuning or dependence on
the VEV scale.

This is a genuine conditional spurion-alignment selector. The remaining
authority question is why this recursive sum-of-squares action is forced and
why additional gauge-invariant terms are absent. Pre-vacuum character
transport through complete symmetry breaking, the diameter beta law, finite
threshold matching, and calibrated holonomy `physical16` readout remain open.

Verification: 12 of 12 exact checks pass in
`research/flavor/checkers/wp849_charge_recursive_spurion_alignment_selector.py`.
