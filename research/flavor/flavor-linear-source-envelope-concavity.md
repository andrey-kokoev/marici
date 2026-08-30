# Linear-source envelope concavity (WP266)

## General theorem

Let an arbitrary stable mediator sector \(S\) couple linearly to the invariant
mixing coordinate \(x\):

\[
V(S,x)=U(S)-xG(S).
\]

After stable elimination,

\[
F(x)=\inf_S\bigl(U(S)-xG(S)\bigr).
\]

For each fixed \(S\), the expression is affine in \(x\). A pointwise infimum
of affine functions is concave. Therefore stable mediator elimination cannot
generate the positive curvature needed by WP262's interior minimum.

On a differentiable stable branch with mediator Hessian \(H>0\), implicit
differentiation gives

\[
F''(x)=-\nabla G^T H^{-1}\nabla G\leq0.
\]

This contains WP265's Gaussian Schur complement as a special case but does not
require a quadratic mediator potential.

## Exact hostile witnesses

The nonlinear stable potential

\[
U(s)-xs=\frac12s^2+\frac14s^4-xs
\]

has the stationary point \(s=0\) at \(x=0\), positive mediator Hessian one,
and effective curvature minus one. A separate finite three-branch envelope
passes exact midpoint-concavity checks, including its nondifferentiable branch
changes. By contrast, the desired stabilizer \(x^2\) has midpoint concavity
residual minus one between \(-1\) and \(1\).

## Consequence and scope

Neither nonlinear stable mediator self-interactions nor finite competing
mediator vacua repair the sign while the flavor invariant enters only as a
linear source. Progress requires direct nonlinear dependence on \(x\), a
constrained non-minimizing operation, nonequilibrium dynamics, or quantum
effects outside this real stable envelope. Each is additional source structure
whose sign and normalization must be independently derived.

Run `uv run --with sympy python
research/flavor/checkers/wp266_linear_source_envelope_concavity.py` for the
local curvature identity, nonlinear witness, finite-branch midpoint checks,
and hostile positive-stabilizer residual.
