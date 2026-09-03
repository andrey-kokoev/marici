# Schwartz density of heat-polynomial tests

## Question

Does the small-mesh approximation of odd monomial-Gaussians hold in the Schwartz topology strongly enough to transport positivity of the Weil distribution?

## Claim boundary

A core/tail argument proves Schwartz-seminorm convergence for every fixed monomial degree and Gaussian scale. Positivity therefore extends conditionally to the odd Schwartz sector. Whether that sector determines RH remains open.

## Scaled coordinate

Set

\[
\phi_h(x)=\frac{1-e^{-hx}}h.
\]

For \(x\geq0\),

\[
0\leq\phi_h(x)\leq x,
\qquad
\phi_h(x)\to x.
\]

The scaled source test for monomial degree \(k\) is

\[
F_{h,k,t}(u)
=
e^{-tu^2/2}\operatorname{sgn}(u)
\phi_h(u^2)^{k+1/2}.
\]

Its pointwise limit is

\[
F_{0,k,t}(u)
=
e^{-tu^2/2}u^{2k+1}.
\]

## Schwartz convergence

Fix a seminorm

\[
\|f\|_{M,N}
=
\sup_u |u^M\partial_u^Nf(u)|.
\]

Split the line at

\[
|u|=h^{-1/4}.
\]

On the core, \(h u^2\leq\sqrt h\). Taylor expansion of \(\phi_h(u^2)\) and its differentiated compositions is therefore uniform. For fixed \(M,N,k,t\), the seminorm of the difference on the core tends to zero.

On the tail, the inequality \(\phi_h(u^2)\leq u^2\) bounds every differentiated term by a fixed polynomial in \(|u|\) times a Gaussian. Since

\[
|u|\geq h^{-1/4},
\]

the Gaussian tail tends to zero faster than every power of \(h\). The same bound applies to the limiting monomial-Gaussian.

Hence

\[
F_{h,k,t}	o F_{0,k,t}
\]

in every Schwartz seminorm.

## Linear combinations

For an odd polynomial

\[
P(u)=\sum_{k=0}^Kc_ku^{2k+1},
\]

choose one mesh-dependent polynomial

\[
p_h(y)=
\sum_{k=0}^Kc_kh^{-k}(1-y)^k.
\]

The corresponding scaled source test converges in Schwartz topology to

\[
e^{-tu^2/2}P(u).
\]

Finite odd Hermite combinations have this form and are dense in the odd Schwartz space. Therefore the closure of the source tests contains the odd Schwartz sector.

## Consequence for the Weil functional

Real-line Schwartz density does not by itself transport Weil positivity. The general-zero representation evaluates analytic continuations at complex spectral points, and those evaluations are not controlled by ordinary real-line Schwartz seminorms.

Thus the heat-polynomial family is large on the real line, but it has not been shown to be a form core for the Weil quadratic form. That promotion requires density in an analytic graph topology controlling all complex zero evaluations and the completed-form convergence.

## Remaining parity gate

An even Weil distribution makes even and odd sectors orthogonal, but positivity on one sector does not abstractly imply positivity on the other. The remaining question is whether the Xi symmetries and complex-zero interpolation make the odd sector determining.

A complete argument must show either:

- every off-critical zero creates a negative odd Schwartz test;
- or an intertwiner transports odd-sector positivity to the even sector.

Absent such an arrow, odd-sector positivity remains a strong restricted criterion rather than the full Weil criterion.

## Disposition

The sparse-family hypothesis is rejected only in real-line Schwartz topology. The next gate is stronger than parity: determine whether the heat-polynomial image is dense in the analytic graph norm that controls complex zero evaluation. Only after that can one ask whether its odd sector detects every off-critical zero.

## Verification

- `research/voevodsky/schwartz-density-of-heat-polynomial-tests-v1.json`
- `research/voevodsky/checkers/check_schwartz_density_heat_polynomials.py`
- `research/voevodsky/results/schwartz_density_heat_polynomials.json`
