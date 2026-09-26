# An exact vacuum plane wave realizes tidal eigenframe sign return

## Result

The tensor-value loop from the preceding eigenframe study can be realized
along a timelike geodesic of an EXACT vacuum Einstein solution. Its rotating
tidal eigenframe returns with two signs reversed after one profile period,
while a parallel-transported observer frame has constant components throughout.

Thus the eigenframe-cover monodromy is dynamically realizable within supplied
Einstein gravity, but it is not a net rotation of that observer's parallel frame
or holonomy around a closed spacetime curve. This distinction is now explicit.

This uses the standard Brinkmann plane-wave ansatz as a declared exact
realization of the prior radiative lane. The repository already had linearized
TT waves with nonzero source-free curvature; this note adds a specific nonlinear
vacuum realization, not a derivation of Einstein's equations from fibration.

## Prior inputs and scope

- `research/nima/checkers/check_machian_linearized_source_boundary_map.py`
  demonstrates the independent homogeneous/radiative curvature sector.
- `research/nima/marici-machian-gravity-direction.md` identifies the tidal
  tensor along a selected observer and its residual spatial stabilizer.
- `research/voevodsky/tidal-eigenframes-form-stratified-descent-data.md`
  proves the generic V4 ambiguity, projector descent and value-loop sign return.

An exact plane wave is not the isolated two-mass Newtonian solution, nor a
finite-energy asymptotically flat radiation packet. The example is a local/
plane-wave Einstein realization; no global causal gluing theorem is claimed.

## Exact geometry

Use coordinates (u,v,x,y), signature (-,+,+,+), and

    ds^2 = -2 du dv + dx^2 + dy^2 + K(u,x,y) du^2,
    K = A_11(u) x^2 + 2 A_12(u) xy + A_22(u) y^2,

where A is any smooth symmetric 2 by 2 matrix. The inverse metric has

    g^uv=g^vu=-1, g^vv=-K, g^xx=g^yy=1, g^uu=0.

The only potentially nonzero Christoffel symbols, together with their lower
index symmetries, are

    Gamma^a_uu = -(1/2) partial_a K,
    Gamma^v_ua = -(1/2) partial_a K,
    Gamma^v_uu = -(1/2) partial_u K.

With R^rho_{sigma mu nu}=partial_mu Gamma^rho_{nu sigma}
-partial_nu Gamma^rho_{mu sigma}+Gamma^rho_{mu lambda}
Gamma^lambda_{nu sigma}-Gamma^rho_{nu lambda}Gamma^lambda_{mu sigma},

    R_uaub = -(1/2) partial_a partial_b K = -A_ab,
    Ric_uu = -tr A,

and all other Ricci components vanish. Therefore any trace-free A gives an
exact Ricci-flat metric. No small-amplitude truncation is used. The determinant
of its uv block is -1, so the Lorentzian signature is retained for every K.

## A timelike observer and its actual parallel frame

Choose the central geodesic

    x=y=0, u=v=tau/sqrt(2).

Its tangent and a spatial frame are

    U=(partial_u+partial_v)/sqrt(2),
    e_1=partial_x, e_2=partial_y,
    e_3=(partial_v-partial_u)/sqrt(2).

On this curve K, its first spatial derivatives and its u derivative vanish.
All Christoffel symbols vanish there. Hence U is unit timelike and geodesic,
and the three e_i are orthonormal and parallel transported. This is an actual
observer transport law, not an independently fitted comparison of matrices.

The electric tidal tensor E_ij=R(U,e_i,U,e_j) is

    E_transverse=-A(u)/2,
    E_13=E_23=E_33=0.

It governs infinitesimal relative acceleration in this freely falling frame.
The vanishing connection on the curve does not imply vanishing curvature:
transverse derivatives of the connection remain nonzero.

## Rotating profile and eigenframe return

Set kappa>0, omega>0 and

    A(u)=kappa [[cos(omega u), sin(omega u)],
               [sin(omega u),-cos(omega u)]].

This is symmetric and trace-free for every u, so the metric is exactly vacuum.
Let theta=omega u/2. The continuous eigenvectors are

    f_1=cos(theta)e_1+sin(theta)e_2,
    f_2=-sin(theta)e_1+cos(theta)e_2,
    f_3=e_3.

Their tidal eigenvalues are respectively -kappa/2, +kappa/2 and 0: all distinct.
This uses a fixed eigenvalue labelling; a constant orientation-preserving
reordering converts it to the ordered convention of the preceding note.

After u advances by T=2*pi/omega,

    A(u+T)=A(u), E(u+T)=E(u),
    (f_1,f_2,f_3)(u+T)=(-f_1,-f_2,f_3)(u).

The proper-time interval is sqrt(2)*T. In contrast, the parallel frame e_i has
not changed components. Relative to it the eigenframe rotates with

    nabla_U f_1 = [omega/(2 sqrt(2))] f_2,
    nabla_U f_2 = -[omega/(2 sqrt(2))] f_1.

So the tidal axes rotate relative to gyroscope-defined axes. Their continuous
oriented lift acquires the V4 sign return, but the instantaneous unoriented
axes and tensor recur. A physical apparatus sensitive to orientations or a
retained tracking history supplies more information than an instantaneous
eigenline readout.

A smooth eigenframe exists along the entire unwrapped observer time line.
What fails is choosing it as a single-valued periodic function of the recurring
tidal data. The two endpoint events are distinct; no closed spacetime loop or
closed timelike curve is used. The eigenframe sign return is not evidence for
nontrivial Levi-Civita holonomy around such a loop.

## What this says about descent

Constant transverse rotations Q give ordinary Brinkmann-chart comparisons,
A -> Q^T A Q, with coherent products when induced from actual charts. This is
a direct spacetime realization of the tensor overlap equation. Its coordinate
cocycle does not fail when the tracked eigenframe changes sign.

A time-dependent eigenframe rotation is different: as a coordinate change it
introduces cross du dx terms and connection terms. One cannot rotate into the
tidal eigenframe and then drop those terms while claiming the same inertial
transport. The retained observer connection is precisely what distinguishes
physical parallel transport from instantaneous spectral diagonalization.

The data hierarchy is therefore

    Einstein solution + observer
       -> connection/parallel frame comparison + tidal tensor
       -> spectral projectors
       -> eigenframe lifts with sign-transition history.

The connection is not reconstructed from E alone. Conversely, a zero connection
along one geodesic does not erase its local tidal information.

The trace-free plane-wave family also allows profiles vanishing at an instant,
where the full SO(3) stabilizer returns. It cannot realize a nonzero axial
three-dimensional tidal spectrum: its eigenvalues always have the form
(-a,a,0). Other vacuum/matter solutions are needed for that stratum. No claim
is made to have realized every earlier degeneration with this single family.

## Verification

Run:

    python research/voevodsky/check_plane_wave_tidal_frame_loop.py

All 17 exact checks passed. The standard-library checker implements sparse
polynomials in (u,v,x,y), constructs the inverse metric, all Christoffel
symbols and all Riemann components, and contracts the full Ricci tensor.
For a nontrivial quadratic-in-u trace-free profile it verifies polynomial
Ricci-flatness, the transverse curvature formula, vanishing longitudinal
tidal components and vanishing connection on the central observer. A
non-trace-free profile is correctly rejected as vacuum.

Further checks use exact rational second jets of the rotating profile and
rational half-angle eigenvectors. They do not replace the written all-u
trigonometric argument. The period/sign controls are endpoint algebra, not a
machine-checked topology theorem. The observer's geodesic and parallel-frame
claims follow from the checked connection restriction and the written
normalization argument.

Receipt: `research/voevodsky/plane-wave-tidal-frame-loop.json` records the
checker hash. No external symbolic-algebra dependency or floating-point solver
is used. No new proof-assistant artifact or nonlinear PDE gluing theorem is
claimed.

## Frontier

There is now an exact gravitational solution and explicit observer transport
behind the generic eigenframe loop. The previous 'merely a matrix loop' gap
is closed for this example.

The larger causal-gluing question remains: can one glue independently supplied
local gravitational solutions and observer records, with their actual overlap
conditions, while retaining the appropriate stabilizer strata? This example
is a single already-global solution and therefore does not establish that
existence theorem. It does show why spectral frame return must not be confused
with a failure of geometric descent or with connection holonomy.
