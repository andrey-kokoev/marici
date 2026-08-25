# Two-adjoint renormalizable completion audit (WP128)

Owner: `marici.Figueiredo`.

## Bounded question

Can a power-counting-renormalizable, weak-basis-invariant mediator sector
generate WP125's negative commutator selector and a positive radial completion
at the same matching order?

Pre-objective process report: excitement `10/10`, confidence `7/10` that two
adjoints suffice at degree eight, expected information gain `10/10`. The
immediate reason is that separate linear adjoint sources can represent `H_u`
and `H_d`, allowing their commutator to be formed by a renormalizable quartic.
Confounds are EFT truncation, coefficient freedom, loop/RG corrections, and
the absence of a physical flavon instrument. These reports are non-evidential.

Frozen optionality snapshot: one two-adjoint source class; three
power-counting gates; one exact degree-eight match; one global adjoint-quartic
bound; one hostile ray; three causal derivatives; eleven exact checks.

## Renormalizable mediator sector

Introduce Hermitian `U(3)_Q` adjoints `A,D`, with

\[
\begin{aligned}
V_{AD}={}&\frac{M_u^2}{2}\operatorname{Tr}(A^2)
+\frac{M_d^2}{2}\operatorname{Tr}(D^2)
+\mu_u\operatorname{Tr}(AH_u)+\mu_d\operatorname{Tr}(DH_d)\\
&-\lambda\lVert[A,D]\rVert_F^2
+\rho\left(\operatorname{Tr}A^2+\operatorname{Tr}D^2\right)^2.
\end{aligned}
\]

Every term is invariant under the full weak-basis group. In four dimensions,
the linear source vertices have field dimension three and the two adjoint
quartics have dimension four. Unlike WP127, this mediator sector is
power-counting renormalizable.

For positive masses, the leading heavy-field solutions are

\[
A_0=-\alpha H_u,\quad D_0=-\beta H_d,qquad
\alpha=\frac{\mu_u}{M_u^2},\quad
\beta=\frac{\mu_d}{M_d^2}.
\]

Substitution gives the exact field-degree-eight terms

\[
V_{\mathrm{eff}}^{(8)}=
-\lambda\alpha^2\beta^2\lVert[H_u,H_d]\rVert_F^2
+\rho\left(\alpha^2\operatorname{Tr}H_u^2
+\beta^2\operatorname{Tr}H_d^2\right)^2.
\]

The second term depends only on spectra and therefore does not shift the
fixed-spectrum WP125 angle. Shifts of `A,D` induced by their quartics begin at
field degree six; stationarity cancels their linear contribution, so their
first corrections to the effective potential begin at field degree twelve.
The displayed degree-eight matching is therefore exact within the expansion.

## Stability and exact benchmark

For Hermitian matrices, the Böttcher--Wenzel bound and the arithmetic-geometric
mean inequality give

\[
\lVert[A,D]\rVert_F^2
\le 2\lVert A\rVert_F^2\lVert D\rVert_F^2
\le\frac12\left(\lVert A\rVert_F^2+\lVert D\rVert_F^2\right)^2.
\]

Consequently the adjoint quartic is nonnegative when
`rho>=lambda/2`, and strictly coercive away from zero when the inequality is
strict. Choose

\[
M_u^2=M_d^2=\mu_u=\mu_d=1,qquad \lambda=25,qquad\rho=13.
\]

Then `alpha=beta=1`, `q=lambda alpha^2 beta^2=25`, and the stability margin is
`rho-lambda/2=1/2`. Together with `a=28`, this reproduces
`sin^2(theta_*)=16/25`. On the WP125 hostile spectra, the complete induced
degree-eight coefficient is `1457773/25>0`; the WP127 runaway is removed.

This bound controls the adjoint quartic. A complete scalar theory must also
retain positive flavon radial terms, such as the WP123 sector, and check all
mixed quartics; that larger global vacuum audit is not claimed here.

## Causal response and authority boundary

The matched coefficient is

\[
q=\lambda\frac{\mu_u^2\mu_d^2}{(M_u^2)^2(M_d^2)^2}.
\]

At the benchmark the exact selector responses include

\[
\partial_\lambda x_*=-\frac7{1250},\qquad
\partial_{\mu_u}x_*=-\frac7{25},\qquad
\partial_{M_u^2}x_*=\frac7{25}.
\]

Thus the WP126 causal fingerprint descends through a fully renormalizable
mediator matching map. But the numbers `28,25,13` and the mass/source ratios
were chosen inside this construction; no independent symmetry or dynamics
fixes them. The model demonstrates a source-capable architecture, not a
numerical CKM prediction.

## Disposition

WP128 closes both technical defects isolated in WP127 at field degree eight:
the mediator interactions are renormalizable and the same source sector
supplies a positive stabilizer. It is a **renormalizable conditional mixing
selector constructor** on the fixed-spectrum slice, with exact full-group
descent and causal parameter responses. It is neither a texture rigidifier
nor a reference-port experiment.

Remaining gates: independently derive the dimensionless coefficient ratios;
prove the full coupled vacuum rather than its degree-eight truncation; select
all CKM coordinates and spectra; specify RG and threshold matching; and type a
physical instrument. The smallest authority falsifier remains target-fitting
`lambda alpha^2 beta^2/a`; the smallest truncation falsifier is a degree-twelve
correction that destroys the interior minimum.

Post-objective process report: excitement `10/10`, confidence `9/10` in the
bounded degree-eight completion, realized information gain `10/10`. Raw delta:
one renormalizable mediator branch opens; WP127's dimension-five vertex and
radial runaway are removed at the matched order; three causal derivatives are
constructed; eleven of eleven checks pass; coefficient selection, full-vacuum
control, and a physical instrument remain absent. These reports are
non-evidential.
