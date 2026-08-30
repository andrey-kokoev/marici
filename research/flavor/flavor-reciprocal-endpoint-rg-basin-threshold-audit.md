# Reciprocal Endpoint RG Basin and Threshold Audit

## Question

Can the marked endpoint algebra of WP854 make a nonzero portal magnitude a
global attractor, and does that magnitude survive threshold transport?

## Unique reciprocal endpoint generator

On the two endpoint states, every continuous-time probability generator has
the form

\[
Q(a,b)=
\begin{pmatrix}
-a&b\\
a&-b
\end{pmatrix},
\qquad a,b\geq0.
\]

Requiring covariance under exchange of the two endpoints forces (a=b=\kappa).
For 
(p=\Pr(P_0)), the resulting flow is

\[
\dot p=\kappa(1-2p),
\qquad
p(t)=\frac12+\left(p(0)-\frac12\right)e^{-2\kappa t}.
\]

For every 
(\kappa>0), the whole interval ([0,1]) is the basin of the unique fixed
point (p_*=1/2). In particular, (p=0) is not a fixed point: reciprocal
endpoint transport generates a nonzero weight without an initial portal
seed. The Lyapunov function ((p-1/2)^2) decreases strictly away from the
fixed point.

## Conditional portal magnitude

If a source-derived kinetic normalization identifies endpoint probability
with squared portal amplitude,

\[
|g_n-g_m|^2=p,
\]

then the fixed point predicts

\[
|g_n-g_m|=\frac1{\sqrt2}.
\]

WP854's marked current fixes the relative orientation, so a coherent lift can
choose the antisymmetric amplitude ((1,-1)/\sqrt2). This inference is
conditional in two distinct ways:

1. the reciprocal endpoint semigroup must be the physical flavor RG rather
   than an auxiliary stochastic clock;
2. the source must supply a coherent lift and the kinetic identity between
   endpoint weight and the canonically normalized portal coupling.

A classical stationary distribution alone does not authorize a coherent
relative phase.

## Complete swap-intertwining threshold family

Every two-endpoint stochastic threshold channel commuting with endpoint swap
has the form

\[
T_r=
\begin{pmatrix}
r&1-r\\
1-r&r
\end{pmatrix},
\qquad 0\leq r\leq1.
\]

It preserves the stationary probability packet exactly, but acts on the
oriented current (J=(1,-1)^T) as

\[
T_rJ=(2r-1)J.
\]

Thus fixed-point survival and physical-current survival are different. The
smallest rational hostile (r=3/4) preserves (p_*=1/2), exchange covariance,
positivity, and total probability while attenuating the portal current by one
half. At (r=1/2), the endpoints merge and the current is erased completely.

Exact oriented numerical survival requires (r=1). The alternative (r=0)
preserves magnitude but reverses orientation. Hence a threshold theorem must
intertwine the marked endpoint projections isometrically; ordinary
swap-covariant matching is insufficient.

## Classification

The reciprocal endpoint generator is a conditional nonzero global magnitude
selector with an entire physical interval basin. Combined with the marked
boundary orientation, it is the first current architecture to make a zero
seed flow to the candidate magnitude (1/\sqrt2). It is not yet an admitted
flavor RG theorem, a coherent source lift, or a threshold-survival theorem.

The remaining readout gate is WP855's pre-projection referenced difference
instrument. The full construction becomes progressive only if one microscopic
source derives the endpoint RG, coherent kinetic normalization, isometric
marked-port matching, and calibrated `physical16` response together.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp856_reciprocal_endpoint_rg_basin_threshold_audit.py
```
