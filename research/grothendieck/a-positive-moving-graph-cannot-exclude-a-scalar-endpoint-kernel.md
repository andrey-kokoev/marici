# A Positive Moving Graph Cannot Exclude a Scalar Endpoint Kernel

## Source-derived graph candidate

On a finite moment quotient \(V_N\), a positive source measure supplies the
Hankel Gram matrix

\[
(H_N)_{ij}=\int v^{i+j}\,d\mu(v),
\qquad 0\le i,j\le N.
\]

If the measure has support on more than \(N\) points, \(H_N\) is positive
definite. Its graph

\[
\Gamma(H_N)=\{(x,H_Nx):x\in V_N\}
\]

lies in the hyperbolic double \(V_N\oplus V_N^*\). For the canonical
cross-form

\[
Q((x,\alpha),(y,\beta))=\alpha(y)+\beta(x),
\]

the graph has positive quadratic value

\[
Q((x,H_Nx),(x,H_Nx))=2x^TH_Nx>0
\]

for every nonzero \(x\).

This is the cleanest finite model of a source-derived positive moving graph.

## Prime covariance

Let \(A_{p,N}\) be the prime Pascal transport on moments. The hyperbolic action

\[
A_{p,N}\oplus A_{p,N}^{-T}
\]

sends \(\Gamma(H_N)\) to the graph of

\[
H_{p,N}=A_{p,N}^{-T}H_NA_{p,N}^{-1}.
\]

Congruence preserves positive definiteness. Thus the graph is not fixed by
prime transport, but it moves covariantly and remains positive. This is the
correct typed behavior anticipated by the reciprocal architecture.

## Dimension obstruction to endpoint exclusion

Let \(\lambda_N\) be any nonzero scalar linear readout on
\(\Gamma(H_N)\). Since projection to \(V_N\) is an isomorphism, the graph has
dimension \(N+1\). For \(N\ge1\), rank-nullity gives

\[
\dim\ker(\lambda_N|_{\Gamma(H_N)})=N.
\]

Therefore the positive graph necessarily contains nonzero states with zero
scalar endpoint readout.

For the natural zeroth-moment readout, take any nonzero

\[
x=(0,x_1,\ldots,x_N).
\]

Then the endpoint coordinate vanishes while

\[
Q((x,H_Nx),(x,H_Nx))>0.
\]

This is stronger than a completion warning. The angle between the whole
positive graph and the scalar endpoint-kernel is already zero at every finite
rank \(N+1\ge2\), because their intersection is nontrivial.

## Consequence

A positive moving graph can supply:

- a source-derived norm;
- reciprocal covariance;
- lossless primal–observer coupling;
- a candidate completion topology.

It cannot, by itself, exclude scalar endpoint zeros for arbitrary admissible
graph states. Positivity of the full relationship and nonvanishing of one
scalar coordinate remain different properties.

The missing object must restrict the admissible zero-state family further. A
viable option must provide at least one of:

- a distinguished source-generated ray or nonlinear orbit inside the graph;
- a cone whose projectivization avoids the endpoint kernel off the seam;
- a dynamical equation making the kernel intersection unreachable;
- a second independent scalar port jointly faithful on the admissible orbit.

Merely choosing another positive \(H_N\) cannot repair the dimension
obstruction.

## Completion reading

Smallest-eigenvalue estimates for \(H_N\) remain relevant to whether the graph
norm survives completion. But no positive lower eigenvalue can make the graph
transverse to a scalar hyperplane when its dimension exceeds one. Endpoint
transversality must be proved on the distinguished source-state subobject, not
on the entire positive graph.

This separates two gates that had been too close:

1. graph positivity and completion stability;
2. source-orbit transversality to the endpoint kernel.

The second is the RH-bearing gate.

## Falsifier

For any proposed positive-graph explanation, compute the dimension of the
declared admissible state family after imposing all source equations. If it
contains a two-dimensional linear subspace and the physical readout is one
scalar linear functional, a nonzero null-readout state exists automatically.

## Scope

This proves a finite dimension no-go for scalar zero exclusion by positive
moving graphs. It does not reject a distinguished nonlinear source orbit,
construct a jointly faithful second port, prove completion stability, confine
zeros, or prove RH.
