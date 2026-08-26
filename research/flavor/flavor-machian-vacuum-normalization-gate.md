# Machian vacuum-normalization gate

Work package: WP581  
Owner: marici.Figueiredo

## Question

Can WP580's dimensionless step \(h=1/2\) be identified with a Machian vacuum
energy?

No such identification currently descends from an admitted source map. A
vacuum energy density \(\rho_{\mathrm{vac}}\) has mass dimension four, while
\(h\), \(r\), and \(q\) are dimensionless. The smallest dimensionally legal
candidate is the relational ratio

\[
\eta={\rho_{\mathrm{vac}}\over M^4},
\]

where \(M\) is a declared physical reference scale.

## Normalization nonuniqueness

Changing only the reference \(M\mapsto sM\) gives

\[
\eta\mapsto{\eta\over s^4}.
\]

For the same nonzero \(\rho_{\mathrm{vac}}\), any desired positive number
\(h_*\) can be obtained by choosing

\[
M=\left({\rho_{\mathrm{vac}}\over h_*}\right)^{1/4}.
\]

In particular, \(h_*=1/2\) follows from \(M^4=2\rho_{\mathrm{vac}}\). This is
an encoding by the reference scale, not a prediction of one half. A
source-derived Machian law would have to determine both the relevant vacuum
functional and the reference scale independently of the flavor target.

The smallest exact hostile keeps \(\rho_{\mathrm{vac}}\) fixed and compares
\(M\) with \(2M\). Their dimensionless readouts differ by a factor of sixteen.
Therefore the dimensional vacuum datum alone does not determine \(h\).

## Source-rank consequence

Grant, conditionally, one admitted Machian scalar \(\eta\) and a local portal
law

\[
z=z_0+a\eta,
\qquad
\lambda_s=\lambda_{s0}+b\eta.
\]

Its invariant flavor readout is

\[
(r,q)
=
\left(
z,
{\lambda_s z^2\over\lambda_H}
\right).
\]

The response to \(\eta\) is one column. Multiple settings of the same scalar
remain collinear to first order and have rank at most one. Thus one Machian
vacuum ratio cannot supply WP577's two independently generated portal
directions. It could define a correlated one-dimensional source curve, but it
would neither identify the full two-coordinate source state nor select a
distinguished point without an additional source law.

Two independent Machian source variables could change this rank count, but
their operations, normalization, common frame, and physical instruments would
all need independent derivation. Adding \(M\) as a tunable reference port
defines a new relational experiment; it does not reveal an absolute vacuum
energy or retroactively make WP580's arbitrary test step physical.

## Cross-sector typing

The current Machian graph claim fixes linearized Riemann curvature as a
gauge-descended local codomain but explicitly does not construct the
stress-energy or boundary-to-curvature source map. Flavor therefore has no
authorized arrow from a Machian vacuum object to \((r,q)\).

WP581 is a negative normalization-and-rank gate, not a claim against all
Machian flavor mechanisms. A progressive replacement requires:

- a source-derived vacuum functional and reference scale;
- an invariant map into physical16 or the portal source coordinates;
- enough independent source variables for the claimed rank;
- a calibrated physical instrument for the relational vacuum quantity;
- an independently predicted flavor consequence surviving the fitted
  ensemble.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp581_machian_vacuum_normalization_gate.py

The generated result is
research/flavor/results/wp581_machian_vacuum_normalization_gate.json.
