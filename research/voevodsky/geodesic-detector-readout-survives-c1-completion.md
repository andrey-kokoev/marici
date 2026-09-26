# A source-defined geodesic detector survives the C1 tidal-loss limit

## Fresh tree state and source recovery

Objective resume returned selected.node_id=null and a nonempty frontier whose
first item is `detector-relative-tidal-completion:v1`. This turn works that node
and uses a version-2 nodes-mode revision, rather than pretending it was selected.

The required physical observable already exists in the repository:

- `research/nima/marici-machian-gravity-direction.md` distinguishes nearby
  inertial geodesic detectors from fixed-angle BMS detectors.
- `research/strominger/subsubleading-memory-candidate.md` points to Flanagan,
  Grant, Harte and Nichols, arXiv:1901.00021.
- Direct primary read: `research/strominger/sources/fghn1901.00021.txt`, lines
  213-242, defines initial/final separation using orthogonal connecting geodesics
  and gives the double-curvature-integral displacement in a parallel frame.
  Lines 2070-2105 define the linear Jacobi propagators, without requiring a
  first-order expansion in curvature.

The primary's equation (2.1) has BOTH small-separation and small-curvature
remainders. We use its operational observable and the full LINEAR Jacobi
problem, not that Born approximation as an exact formula. No arbitrary detector
window was selected to repair the earlier counterexample.

## Selected detector and regime

Supply a central timelike geodesic, its proper-time interval, a parallel frame,
an infinitesimal initial separation xi0 and relative velocity v0. The readout is

    D(Tau)=xi(Tau)-xi0-Tau*v0,

in that parallel frame, to first order in separation/relative velocity but with
no weak-curvature truncation. It compares neighboring geodesic motion with the
corresponding inertial extrapolation. Its evolution is

    d^2 xi/dtau^2 = -E(tau) xi.

Integrating twice gives the exact linear-deviation integral equation

    D(Tau)=-integral_0^Tau (Tau-s) E(s) xi(s) ds.

The triangular weight and the dynamically evolving separation are fixed by the
initial-value problem. Replacing xi(s) by xi0 is an additional Born approximation,
not part of the exact reconstruction below. Endpoint terms are retained.

We study finite-duration displacement, not necessarily a burst followed by a
stationary final era. No persistent asymptotic memory or experimental noise
model is inferred. The detector is first order in baseline, not a finite-arm
interferometer theorem.

## Exact response in the existing Rosen plane-wave sector

Use

    ds^2=-2du dV+gamma_ab(u)dX^a dX^b,
    central worldline X=0, u=V=tau/sqrt(2).

At linear order a transverse coordinate separation X(u) between neighboring
geodesics obeys

    (gamma X')'=0,
    X(u)=X0+S(u) P0, S(u)=integral_0^u gamma(s)^-1 ds.

This follows from the transverse translation Killing symmetries, or directly
from the geodesic equation. The first-order orthogonal separation agrees with
this Jacobi field; distinctions between finite connecting-geodesic conventions
enter beyond the asserted baseline order.

Let F be the orthonormal parallel frame in Rosen coordinates:

    F'=-(1/2)gamma^-1 gamma' F.

For gamma(0)=I and F(0)=I, the physical initial data imply

    X0=xi0,
    P0=sqrt(2)*v0-Gamma(0) xi0,
    Gamma=(1/2)gamma^-1 gamma'.

Then

    xi(u)=F(u)^-1 [xi0+S(u) P0],
    D(u)=xi(u)-xi0-sqrt(2)*u*v0.

The sqrt(2) factors convert u to proper time. Constant Rosen coordinates are
not in general a physically initially resting detector pair: the initial
connection term must be subtracted. This is explicitly tested on a nonzero-
expansion source instead of silently assuming it away.

This formula is an exact solution of the linear Jacobi system on the admitted
plane-wave geometry. It involves gamma and gamma', not gamma''. The same field
can therefore have an unstable pointwise curvature readout and a stable
finite-duration displacement readout.

## C1 continuity with a scoped extension bound

On [0,T], fix source bounds

    lambda I <= gamma,eta <= B0 I, lambda>0,
    ||gamma'||,||eta'|| <= B1,
    gamma(0)=eta(0)=I, initial frames I.

Hold xi0,v0 and the proper-time calibration fixed. Write delta=||gamma-eta||_C1,
K=B1/(2lambda), and L_Gamma=(1/lambda+B1/lambda^2)/2. The prior transport bound
already gives

    ||F_gamma-F_eta|| <= T exp(KT) L_Gamma delta.

Metric compatibility implies ||F^-1||<=sqrt(B0), hence

    ||F_gamma^-1-F_eta^-1|| <= B0 T exp(KT) L_Gamma delta.

Also

    ||S_gamma-S_eta|| <= T lambda^-2 delta,
    ||S|| <= T/lambda,
    ||P0_gamma-P0_eta|| <= (1/2)||xi0|| delta.

Put M=sqrt(2)||v0||+(B1/2)||xi0|| and M_X=||xi0||+T M/lambda.
Product estimates now give

    ||D_gamma-D_eta||_C0 <= L_D ||gamma-eta||_C1,

    L_D = B0 T exp(KT) L_Gamma M_X
          +sqrt(B0)[T M/lambda^2+T||xi0||/(2lambda)].

Thus D extends uniquely to the C1 closure of the bounded smooth source class
with this retained observer/initial-data interface. Its compatible image is
that actual closure, not all arbitrary metric/readout pairs. The extension
preserves the detector observation and its normed distinctions in this scope.

This does NOT assert that every limit has a classical pointwise vacuum Ricci
tensor. A C1 metric need not have one. The response extends by its first-order
transport/conserved-momentum formula; the pointwise E readout may fail to extend.
No general uniqueness theorem for geodesics of arbitrary C1 spacetimes is used:
the explicit Rosen symmetries control this particular detector problem.

## The previous hostile now has a different answer

Reuse the exact vacuum family on 0<=u<=1:

    beta_n=(1-cos(nu))/n^2,
    r_n''=-beta_n'^2 r_n, r_n(0)=1,r_n'(0)=0,
    p_n=r_n exp(beta_n), q_n=r_n exp(-beta_n).

It has gamma_n=diag(p_n^2,q_n^2)->I in C1, but
E_n(0)=diag(-1/2,+1/2,0) for every n. Because beta_n'(0)=r_n'(0)=0,
Gamma_n(0)=0. A physically initially resting pair has P0=0. Therefore its
parallel-frame separation components are

    xi_1(u)=p_n(u) xi_1(0), xi_2(u)=q_n(u) xi_2(0).

For n>=2, 1-1/(2n^2)<=r_n<=1, 0<=beta_n<=2/n^2<=1/2 and exp(beta_n)<2.
The mean-value bound gives, uniformly on [0,1],

    |p_n-1|, |q_n-1| <= 5/n^2.

Hence the fractional displacement tends to zero, even though the corner
relative-acceleration coefficient does not. This conclusion is exact in the
linear-baseline model, not based on truncating in curvature amplitude. The
choice of observable changes the completion requirement; it does not rescue
the failed pointwise observation by renaming it.

## A nontrivial exact source control

The earlier vacuum profile p=u^(6/5), q=u^(3/5), on u>0, permits a closed-form
resting Jacobi propagator in either direction. For p=u^alpha at corner u=1,

    K_alpha(u) = [(1-alpha)/(1-2alpha)] u^alpha
                 -[alpha/(1-2alpha)] u^(1-alpha),

with K(1)=1,K'(1)=0 and K''=alpha(alpha-1) K/u^2. The velocity propagator is

    H_alpha(u)=[u^(1-alpha)-u^alpha]/(1-2alpha),

with H(1)=0,H'(1)=1. These retain the required initial-state distinction.
For u=(6/5)^5, the two resting responses are

    K_6/5=124781/109375, K_3/5=108/125.

The same plane wave has opposite transverse tidal coefficients because
(6/5)(1/5)+(3/5)(-2/5)=0. This verifies an actual nonflat detector response,
not only disappearance of a high-frequency perturbation.

## Verification, ownership and next gate

Run:

    python research/voevodsky/check_geodesic_detector_completion.py

All 22 exact checks passed: two propagators and their initial conditions/Jacobi
identities, conserved-coordinate-momentum reconstruction, the nonzero initial
expansion hostile, exact endpoint responses, and the stated shrinking analytic
envelopes. Source text and prior note hashes are recorded in
`research/voevodsky/geodesic-detector-completion.json`.

The all-n uniform bounds and C1 extension are written proofs. No finite test
certifies them universally; no physical detector hardware, noise budget or
finite-baseline nonlinear correction is checked. Strominger's source artifacts
were read but not changed.

The leaf's bounded question is resolved: a preexisting geodesic-displacement
observable, with its exact linear response, survives the same C1 completion
that destroys the pointwise tidal observation. The next nonredundant question
is whether the physical finite-baseline correspondence and error bounds are
uniform in the high-frequency sequence, rather than promoting an infinitesimal
detector theorem to an unrestricted instrument statement.
