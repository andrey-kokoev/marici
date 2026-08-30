# Renormalization scale is not a physical probe: WP690

## Correction

WP689 proved a correct affine comparison theorem but assigned physical-probe
authority to two renormalization-scale choices. That assignment is withdrawn.
The renormalization scale is a coordinate of a perturbative description, not an
experimentally selectable context.

Let

\[
\lambda_p(\mu)=a+b\log(\mu/\mu_0).
\]

At one loop, a fixed-momentum form factor has the compensating explicit log

\[
F(Q;\mu)=\lambda_p(\mu)+b\log(Q/\mu)
=a+b\log(Q/\mu_0).
\]

Therefore

\[
\frac{\partial F(Q;\mu)}{\partial\mu}=0.
\]

Changing only \(\mu\) produces the same physical record. It cannot remove a
source ambiguity, improve detector rank, or count as a complementary probe.

## Physical repair

Distinct physical momenta can supply genuinely different contexts if the
corresponding amplitudes and detector responses are source-authorized. For
\(Q_1\ne Q_2\),

\[
F(Q_2)-F(Q_1)=b\log(Q_2/Q_1),
\]

and the response Jacobian with respect to \((a,b)\) has determinant
\(\log(Q_2/Q_1)\). This removes the boundary parameter algebraically, but it is
not yet a flavor selector or a physical instrument.

The remaining gate is a finite-momentum, same-channel form factor plus two
calibrated momentum-bin measurements with uncertainties and declared support.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp690_renormalization_scale_noninstrument.py

Generated result: results/wp690_renormalization_scale_noninstrument.json.
