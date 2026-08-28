# The Constant–Delta Veronese Plane Cannot Be an Injective Idelic Trace Sector

## Setup

Let

\[
P_\partial=\operatorname{span}\{1,\delta_0\}
\]

be the external boundary plane. Additive Fourier transform exchanges its two
generators:

\[
\mathcal F1=\delta_0,
\qquad
\mathcal F\delta_0=1.
\]

Aspect's completed sewing map is defined on the injective trace range of
Schwartz--Bruhat sources. Its source formula is

\[
J\tau(\phi)=\tau(\mathcal F\phi).
\]

The tempting extension is to include $P_\partial$ in the source of the same
idelic trace and then take its even symmetric algebra. That extension is
incompatible with the support type of the trace.

## Support obstruction

The delta port is supported at additive zero. Additive zero is not an idele.
Consequently a support-compatible restriction to the idelic locus either is
undefined on $\delta_0$ or sends it to zero:

\[
\widetilde\tau(\delta_0)=0.
\]

The constant port has nonzero restriction:

\[
\widetilde\tau(1)\ne0.
\]

Suppose an extension $\widetilde\tau$ admitted both ports and an invertible
sewing map $\widetilde J$ satisfying Fourier covariance. Then

\[
\widetilde J\widetilde\tau(1)
=\widetilde\tau(\mathcal F1)
=\widetilde\tau(\delta_0)
=0.
\]

Invertibility of $\widetilde J$ would force $\widetilde\tau(1)=0$, a
contradiction.

Therefore no extension can simultaneously have all three properties:

1. support-compatible idelic restriction;
2. injectivity on the constant--delta plane;
3. Fourier-equivariance through an invertible sewing map.

This is a structural obstruction, not a missing choice of finite basis.

## Categorical correction

The boundary plane and the idelic trace range are different objects. The
source-faithful architecture is a cospan

\[
P_\partial\xrightarrow{\ i_\partial\ }\mathcal B
\xleftarrow{\ i_\tau\ }\operatorname{Ran}(\tau),
\]

where $\mathcal B$ is a rigged boundary object retaining both additive-zero
and idelic data. Fourier acts on $P_\partial$ by exchanging the two external
ports. Completed Tate sewing acts on $\operatorname{Ran}(\tau)$. A new
source-derived comparison cell in $\mathcal B$ must specify how these actions
meet. Neither leg may be inferred from the other.

The even Veronese algebra therefore remains attached to the external
controller:

\[
\bigoplus_{l\ge0}H_l
\longrightarrow
\operatorname{Sym}^{\mathrm{even}}P_\partial.
\]

It does not become a subspace of the injective idelic trace range merely by
completion.

## Consequence for the six-channel fixture

The algebraic grade-one exchange matrix on
$\operatorname{Sym}^2P_\partial$ remains valid as a boundary-controller
fixture. It is not yet Aspect's physical $6\times6$ trace-sewing matrix.

Any physical approximation by Schwartz sources must declare families
$c_\epsilon,d_\epsilon$ approximating $1,\delta_0$, together with:

- the topology in which each approximation converges;
- the trace Gram matrix at every cutoff;
- the bias introduced by excluding additive zero;
- the condition number used in metric whitening;
- a uniform or explicitly cutoff-dependent uncertainty threshold.

The delta approximants cannot converge in ordinary $L^2$ with bounded norm,
while the constant port is not in ordinary global $L^2$. Thus an apparently
unitary finite matrix can become singular in the source metric as the
regularization is removed. Euclidean Frobenius error alone does not certify
the limiting boundary correspondence.

## Finite falsifier

For any proposed finite realization, compute the source Gram matrix $G_N$ and
the two incidence columns $v_{1,N}$ and $v_{\delta,N}$. Reject the realization
if either

\[
\lambda_{\min}(G_N)\longrightarrow0
\]

or the Fourier covariance residual fails to vanish in the source metric:

\[
\left\|
J_Nv_{1,N}-v_{\delta,N}
\right\|_{G_N}\not\longrightarrow0.
\]

Passing at a fixed cutoff is insufficient. The same regularization sequence
must preserve both source distinction and Fourier exchange through the
declared completion.

## Decisive outcome

The canonical Veronese incidence has been located, but it lives on the
external constant--delta controller. The idelic trace cannot absorb that
controller injectively while retaining invertible Fourier sewing. The next
constructor is not a larger trace basis; it is the typed comparison cell from
the external boundary controller and the idelic trace range into a common
rigged boundary object.
