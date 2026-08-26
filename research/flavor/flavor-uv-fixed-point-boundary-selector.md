# UV fixed-point boundary selector (WP269)

## Candidate selector

Let the renormalized commutator-square coefficient obey the affine UV flow

\[
\frac{dc}{dt}=\alpha c+\beta,
\qquad t=\log\frac{\mu}{\mu_0}.
\]

For \(\alpha\neq0\), the fixed point and exact solution are

\[
c_*=-\frac{\beta}{\alpha},
\qquad
c(t)=c_*+(c(0)-c_*)e^{\alpha t}.
\]

When \(\alpha<0\), the fixed point is UV-attractive and erases the initial
boundary value. This is genuine progress beyond WP268: an admitted UV flow can
select the renormalized coefficient rather than merely transport it.

## Hostile beta-function pair

Attractiveness does not determine the selected number. The equally attractive
flows

\[
\frac{dc}{dt}=-c+1,
\qquad
\frac{dc}{dt}=-c+2
\]

have fixed points one and two. With the same unit linear mixing term, they give
interior selectors \(x_*=1/2\) and \(x_*=1/4\). Both forget their initial
conditions at the same exponential rate.

Thus fixed-point existence and stability supply selector architecture, while
the numerical prediction resides in the beta-function ratio
\(-\beta/\alpha\).

## Classification and next gate

This is a genuine conditional boundary selector, not a presentation
rigidifier. To become a flavor prediction, a complete anomaly-free UV field
content must independently derive \(\alpha\) and \(\beta\), including threshold
and scheme matching. The fixed point, basin, decoupling, three-generation
potential, and physical instrument must then survive without fitting the beta
coefficients from observed flavor.

Run `uv run --with sympy python
research/flavor/checkers/wp269_uv_fixed_point_boundary_selector.py` for the
exact flow, memory loss, hostile fixed points, and numerical-authority test.
