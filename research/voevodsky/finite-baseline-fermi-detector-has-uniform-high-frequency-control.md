# Finite-baseline Fermi separation has uniform high-frequency control

## Result

The previous detector result extends beyond infinitesimal separation for the
specified high-frequency vacuum Rosen family. The exact orthogonal connecting
geodesic is determined by a scalar contraction. It exists uniquely in a fixed
local connector domain for every n>=4 and every initial baseline |b|<=1/4,
with bounds independent of n.

The finite-baseline displacement still tends to zero, although the pointwise
corner tidal tensor stays diag(-1/2,+1/2,0). Growing curvature derivatives do
NOT destroy uniformity in this example. The special plane-wave translation
symmetry permits an exact argument without a truncated curvature-gradient
expansion.

This is the Fermi/orthogonal-geodesic separation observable already defined in
FGHN arXiv:1901.00021, not a radar distance or a finite-arm interferometer model.
It is a local uniqueness statement for a specified connector branch, not a
claim that no other long spacelike geodesic can connect the worldlines.

## Fresh state and source boundary

Fresh resume selected
`issue-tree:marici-project-objective:finite-baseline-detector-error:v1`.
The preceding source-backed detector note and the primary definition of finite
orthogonal separation in
`research/strominger/sources/fghn1901.00021.txt`, lines 213-226, are the physical
interface. No source-owner artifact is changed. The existing Strominger request
remains coordination, not scientific certification or an execution blocker.

## Exact detector pair

Use the existing diagonal Rosen vacuum family

    ds^2=-2du dV+gamma_ab(u)dX^a dX^b,
    beta_n=(1-cos(nu))/n^2,
    r_n''=-beta_n'^2 r_n, r_n(0)=1,r_n'(0)=0,
    gamma_n=diag(r_n^2 exp(2beta_n),r_n^2 exp(-2beta_n)).

Take two exact timelike geodesics

    central: (u,V,X)=(u,u,0),
    neighbor: (u,V,X)=(u,u,b).

Both have proper time tau=sqrt(2)u. At u=0, gamma=I and gamma'=0. The transverse
connector is then a straight spacelike geodesic and the observers' velocities
agree under parallel transport along it. Thus b is a genuine finite initial
rest separation, not merely a coordinate-comoving preparation mistaken for
physical rest.

At a later central event u=t in [0,1], the neighbor event orthogonally paired
to it need NOT have the same u or clock reading. Write its coordinate as t+a.
The observer proper-time offset is sqrt(2)a. This finite simultaneity correction
is retained rather than hidden inside an O(|b|^2) remainder.

## Integrating the connector exactly

Let lambda in [0,1] be affine along the spacelike connector. Since partial_V is
a Killing vector,

    u(lambda)=t+a lambda.

Put H(u)=gamma(u)^-1. The transverse conserved momentum k gives

    X'(lambda)=H(t+a lambda) k,
    B_t(a)=integral_0^1 H(t+a s) ds,
    k=B_t(a)^-1 b.

Orthogonality to the central unit tangent U=(partial_u+partial_V)/sqrt(2)
requires V'(0)=-a. The V geodesic equation gives

    V''(lambda)=(1/2) k^T H'(t+a lambda) k.

Define

    C_t(a)=integral_0^1 (1-s) H'(t+a s) ds.

The endpoint condition V(1)=t+a is exactly

    4a=k^T C_t(a) k,
    a=T_t(a):=(1/4)b^T B_t(a)^-1 C_t(a) B_t(a)^-1 b.

These integral definitions remain valid at a=0. Deriving them by dividing a
secant equation by a and forgetting this limiting equation would spuriously
make equal-clock events appear orthogonally paired in general.

Together with the integrals for X and V, any fixed point supplies an actual
geodesic and its prescribed endpoint. No Jacobi approximation is used here.

## Finite separation components

Let F(t) be the central parallel transverse frame in Rosen coordinates. The
initial tangent S of the connector has coordinate components

    S=(a,-a,H(t)k).

In the central observer's parallel orthonormal spatial frame,

    S_perp=F(t)^T k,
    S_long=-sqrt(2)a,
    |S|^2=k^T H(t)k+2a^2.

It is spacelike for nonzero b. Because lambda spans [0,1] affinely, |S| is the
connector's proper length. The infinitesimal reference at this same event is

    S_J,perp=F(t)^-1 b=F(t)^T gamma(t)b,
    S_J,long=0.

We therefore compare the actual finite geometric observable with its Jacobi
approximation, not a coordinate distance between same-time endpoints.

## Uniform metric estimates for the vacuum family

Extend the smooth source functions to -1<=u<=2 and take n>=4. Their evenness
and the positive Volterra bootstrap give

    1-2/n^2 <= r_n <=1, |r_n'|<=2/n^2, |r_n''|<=1/n^2,
    0<=beta_n<=2/n^2, |beta_n'|<=1/n, |beta_n''|<=1.

Consequently, in operator norm,

    (1/2) I <= gamma_n <= (4/3) I,
    ||gamma_n'||<=4/n, ||gamma_n''||<=4.

For example the lower estimate follows from
(7/8)^2 exp(-1/4)>=(7/8)^2(3/4)=147/256>1/2.
The second-derivative bound follows from

    exp(4/n^2)[8/n^4+6/n^2+16/n^3+2] <=85/24<4.

Thus, writing B0=4/3 and lambda0=1/2,

    ||H'|| <=16/n <=4,
    ||H''|| <=2 lambda0^-3 ||gamma'||^2
                 +lambda0^-2 ||gamma''|| <=32.

Third derivatives need not be uniformly bounded; the proof does not use them.

## Contraction and uniqueness in the retained connector domain

For t in [0,1] and |a|<=1/4, all connector u values lie in the controlled metric
interval. Positivity implies ||B_t(a)^-1||<=B0. Differentiation under the
integrals gives

    ||C_t(a)||<=||H'||/2,
    ||B_t'(a)||<=||H'||/2,
    ||C_t'(a)||<=||H''||/6.

Therefore

    |T_t(a)| <= B0^2 ||H'|| |b|^2/8,

    |T_t'(a)| <= [B0^3 ||H'||^2/8+B0^2 ||H''||/24]|b|^2.

For |b|<=1/4 these are at most 1/18 and 4/9 respectively. Hence T_t maps
[-1/4,1/4] into itself and is a uniform contraction. There is a unique retained
local connector and its dependence on the supplied metric is controlled.
In particular,

    |a| <= (32/(9n)) |b|^2.

No baseline shrinking with n is necessary in this normalized family. The
numbers 1/4 and 1 refer to the explicitly fixed affine/proper-time and metric
scales; they are not universal laboratory distances or times.

## Finite-baseline error and the actual observable limit

Since ||B_t(a)-H(t)||<=|a| ||H'||/2,

    ||k-gamma(t)b|| <= B0^2 |a| ||H'|| |b|/2.

Using ||F||<=sqrt(2) gives

    ||S_perp-S_J,perp||
      <= [4096 sqrt(2)/(81 n^2)] |b|^3
      <= (76/n^2)|b|^3,
    |S_long| <= [32 sqrt(2)/(9n)] |b|^2.

The prior exact Jacobi result on [0,1] is

    ||S_J,perp-b|| <= (5/n^2)|b|.

Thus the finite Fermi displacement satisfies, uniformly in t,

    ||S(t)-(b,0)||
      <= (5/n^2)|b|+(76/n^2)|b|^3
          +[32 sqrt(2)/(9n)]|b|^2 ->0.

At t=0, a=0 is the unique fixed point and S(0)=(b,0), so the reference is the
actual prepared separation. Norm changes are bounded by the same expression.
The longitudinal finite-baseline correction decays more slowly than the
linear transverse response, but still vanishes at fixed baseline.

This proves a finite-size result for THIS family, not stability of every Fermi
detector under unconstrained C1 convergence. The uniform second-derivative bound
was used to establish a common normal connector branch. On this controlled
class, the exact fixed-point formula also provides continuous dependence on
H,H' with the retained uniform contraction margin.

## Independent exact connector control in flat spacetime

To check signs and factors, take p=1+c u, q=1. This Rosen metric is flat, with
Minkowski coordinates x=pX and v=V+(c p X^2)/2. For a detector at X=b,Y=0,
exact Minkowski orthogonality gives

    a=-c p(t)b^2/(4+c^2 b^2).

The integral formula yields B=1/[p(t)p(t+a)] and
C=-c/[p(t)^2 p(t+a)], reproducing precisely the same equation. The actual
transverse separation is p(t+a)b, not p(t)b. Same-clock endpoints fail the
orthogonality test when c b is nonzero. This flat example is a connector
validation; its constant-coordinate detectors need not be physically at rest
initially, unlike the specially prepared hostile family above.

## Verification and programme disposition

Run:

    python research/voevodsky/check_finite_baseline_fermi_detector.py

All 30 exact rational controls passed: three independent Minkowski/Rosen
connector comparisons, spacelike length and simultaneity factors, uniform
metric/inverse bounds, the 4/9 contraction margin, and decreasing finite-
baseline envelopes. Receipt:
`research/voevodsky/finite-baseline-fermi-detector.json`.

The all-n source estimates, fixed-point existence and finite-baseline convergence
are written proofs. The checker tests the exact identities and constants, not
a sampled nonlinear solution claimed as universal evidence. No proof-assistant
artifact or arbitrary-spacetime normal-neighborhood theorem is asserted.

The selected finite-baseline leaf is resolved within its stated plane-wave
scope. The remaining nonredundant operational issue is whether a causal light-
signal/radar readout, rather than spacelike Fermi separation, has the same
completion behavior with explicitly retained emission/reception clock data.
That question should use an existing optical observable, not rename the
spacelike connector a directly measured interferometer signal.
