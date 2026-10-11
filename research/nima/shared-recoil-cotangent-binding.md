# One shared recoil/cotangent reading of the six-port exchange

**Closed successor comparison (7 October 2026):**
`old-spatial-recoil-poisson-obstruction.md` proves that the old reader A*q
cannot be canonically paired with three C1 functions of this representation's
real recoil momenta, even with reference-pair access: the full mixed bracket
has rank at most one. The shared embedding below remains valid; this result
excludes combining its momenta with that different configuration reading.

## Frozen problem and scope

SCC obligations: attachment transport and readout descent for the existing
six-port pulses. Keep their supplied metric, AB preparation, interpolation,
source records and nonzero-anchor domain. No electric coupling, physical clock,
new free Hamiltonian or physical mass calibration is inserted.

Conjecture: the old REAL-amplitude elastic reading extends to one faithful
cotangent embedding of the current phase-neutral state, but preserving all
its named local carrier/record readings may require internal carrier directions
beyond three-dimensional translation.

Freeze two nested architectures before testing:

1. One ordinary three-component carrier body and six partner bodies. Each port
   is an elastic normal collision, with arbitrary positive masses, one fixed
   kinetic isometry, and the OLD mixed adapter for both local amplitudes (not
   only its difference/reflection channel). Contact directions may vary by port.
2. A generalized carrier on V=span(F), with its inherited positive Gram
   D=F^T H F, and six partner momenta along the source unit directions. Use
   the old endpoint geometry to split V into three vector and remaining
   internal directions; retain the whole split. This is an explicit candidate
   mechanical representation, not a claim that the channel labels are particles.

Rivals: a separate mass basis for every port; matching only the reflection
normals while changing the local sum reading; calling a quadrature relabelling
physical selection; deleting internal components; demanding a momentum-only
kick at arbitrary positions; silently replacing the pulse by free-body dynamics.

Risky consequences: one map must preserve every port generator and endpoint,
the kinetic pairing, cotangent form, original readings and source histories.
Both local sum and difference responses must match. A three-dimensional Gram
rank defect rejects architecture 1, not all mechanics. Architecture 2 must
supply a literal common map and inverse on the retained sector, not merely
compatible dimensions.

## Why the old local reading rejects the three-component carrier

Let nu_i be the source's unit reflection normal and sigma_i its normalized
local SUM direction. From the actual feature/record vectors, for i!=j,

    <nu_i,nu_j>=C_ij,
    <sigma_i,nu_j>=C_ij,
    C=(I+D)/2.

Every off-diagonal C_ij is nonzero. The normals lie in the prepared invariant
linear carrier, so this comparison does not require varying inaccessible
anchor directions.

For an ordinary vector collision star, let M be the carrier mass, m_i the
partner mass and n_i its unit contact direction. In mass-weighted momenta,

    nu_i=(sqrt(m_i/(M+m_i))*n_i at carrier,
          -sqrt(M/(M+m_i))*n_i at partner i),
    zeta_i=(sqrt(M/(M+m_i))*n_i at carrier,
            sqrt(m_i/(M+m_i))*n_i at partner i).

The old mixed single-port adapter sends sigma_i to the pair center-of-momentum
direction zeta_i. Against another port j,

    <zeta_i,nu_j>=sqrt(M/m_i)*<nu_i,nu_j>.

Preserving BOTH old local readings therefore forces m_i=M for every i.
Consistent axis reversals cannot change the squared ratio. A concrete two-port
hostile matches the reflection-normal overlap with masses (M,m_0,m_1)=(1,2,1)
but changes the old sum overlap by C_01*(1/sqrt(2)-1). Merely matching normals
would miss this defect.

With equal masses the contact-direction Gram must be

    <n_i,n_j>=(2*C-I)_ij=D_ij.

The exact D has rank six and is positive definite. Six such independent
contact directions cannot live in a three-dimensional carrier. This rejects
architecture 1 even with arbitrary contact directions and inactive spectators.
It does NOT classify all three-dimensional mechanics, other body incidences,
nonlinear/non-isometric readings, or maps that change the old local sum reading.

## A common generalized-body map does exist

Use V=span(F), in its six labelled coefficient coordinates and metric D.
The source directions e_i have unit D-norm. Model one carrier on V and six
partner channels along e_i. Equivalently, the partners can be V-valued bodies
whose transverse coordinates are retained inactive spectators. These are
representation roles, not a derivation of seven physical particles.

Write K=I+D, b=K^-1*s, s=D*e_AB and R=|c|. From the already checked relative
canonical coordinates (q,p), set

    P0=b*R-D*q,     pi=b*R+q,
    X0=K^-1*p,      x=-K^-1*p.

P0 is the generalized carrier momentum COVECTOR; pi_i is the partner's scalar
momentum along e_i. X0 and x_i are their conjugate coordinates. In this
numerical unit-mass convention the common kinetic form is

    T=(P0^T D^-1 P0+pi^T pi)/2.

At the supplied real reference frame, (P0)_i and pi_i are exactly the old
carrier projection and record amplitude. For an arbitrary common phase frame
g=c/R, the complete complex source is recovered by

    y=g*F*(D^-1*P0-i*X0/2),
    r=g*(pi-i*x/2).

Thus these are phase-neutral extensions of the old readings; raw signed
amplitudes in other frames are recovered with g, not erased.

The image has the explicit constraints

    X0+x=0,
    P0+D*pi=s*R,  R>0.

It is a constrained cotangent embedding, not twelve newly independent source
pairs. Its pulled-back body form is sum dq_i wedge dp_i. With the retained
reference pair the full source form is

    Omega=sum dX0_j wedge dP0_j + sum dx_i wedge dpi_i + dQ wedge dphi.

The action primitive transports as

    -Im(eta^dagger M d eta)
      =P0^T dX0+pi^T dx-Q dphi+d(q^T p)/2.

The endpoint term has not been discarded. Keeping phase, charge and the source
record gives an inverse on precisely this image; foreign position sections,
anchor lines, budgets and reference phases are rejected.

## All six pulses, including their intermediate motion

The old generator at port i becomes EXACTLY

    h_i=(pi_i-(P0)_i)^2/2+(x_i-(D*X0)_i)^2/8.

One matrix embedding intertwines its continuous Hamiltonian generator with
the previous generator for every port. It is not an endpoint-only match or
six independently chosen body maps. The source angular parameter is unchanged.

At area pi, put delta=pi_i-(P0)_i at the start of the pulse. Then

    Delta P0=D*e_i*delta,
    Delta pi=-e_i*delta,
    P_total=P0+D*pi is conserved.

The two local longitudinal momenta swap; the same T is preserved at every
exchange endpoint. The position map is the reciprocal transpose of the
momentum reflection. It fixes the corresponding longitudinal contact section
x_i=(D*X0)_i, not arbitrary positions.

On all 68 original paths, the final-pulse midpoint and endpoint are recovered:
136 full states with their SAME registered family, path slot and pulse sample.
There are 62 nonzero final-pulse impulses, 62 nonzero midpoint configurations,
and 68 nonzero endpoint momentum packets. All 68 real endpoints lie on the
zero-configuration contact section, with T=1/2 in the supplied preparation.
This accounts for the earlier zero-momentum census: that census used the
other canonical polarization.

Between endpoints, T alone need not be conserved. The retained quadratic budget
is

    Q=2*T+(X0^T D X0+x^T x)/4.

Both terms belong to the reconstructed whole. This conserved quantity has not
been independently selected as laboratory energy.

## Three endpoint-vector directions and three internal directions

Let A be the existing 3-by-6 target-vertex matrix (called X in the earlier
checker). The inherited D-orthogonal split is

    H_sp=(A D^-1 A^T)^-1,
    L=D^-1 A^T H_sp,
    N=I-L*A.

Then A*L=I, rank(N)=3 and

    D=A^T H_sp A+N^T D N.

This preserves the kinetic form and its cotangent splitting. H_sp is the
induced positive spatial tensor, not an assumed scalar inertial mass in the
old Euclidean coordinates. The internal contact-Gram contribution has rank
three; every port has a nonzero internal component. Deleting it changes the
fixed pairing. All 24 source frame transports preserve this construction.
This is a split of the generalized carrier, not additional independent modes
for every displayed body component.

The old canonical endpoint-vector reader A*q is still recovered, but as

    A*q=A*(pi-b*R).

It is momentum-affine in this reading, not the new configuration A*X0.
Consequently the construction has NOT identified the old spatial reader with
measured body positions merely by swapping coordinate names.

## Disposition and physical boundary

The old recoil interpretation now has one shared, phase-neutral cotangent
embedding for all six ports, with exact opposite generalized impulses and
retained internal response. Its common Hamiltonians are the existing pulses.
The strict three-dimensional carrier-only version is rejected by rank six.

The surviving representation has the following unclosed physical interfaces:

- A common positive mass parameter remains free under P->sqrt(m)*P and
  X->X/sqrt(m), with reciprocal Hamiltonian transport. Equality of the formal
  mass parameters in this reading does not select a physical mass value.
- Each h_i contains only the selected relative-mode kinetic term, not the
  full free-body T. No free-flight velocity law or center-of-mass drift was
  added. Coordinate derivatives must be computed from h_i, not from an
  unimplemented free Hamiltonian.
- The generalized configurations require a source-selected localization/body
  interpretation. The actual native spatial readings and full records have
  been recovered, not identified with those new configurations.
- Electric charge coupling, physical duration and preparation/resource
  normalization remain outside this calculation.

## Verification

    uv run --with sympy python research/nima/checkers/check_shared_recoil_cotangent_binding.py
    uv run --with sympy python research/aspect/scc/scc.py check nima-shared-recoil-cotangent-binding

The checker freshly reruns the 22-control single-port reading and the
882/455-control relative-chart/response chain. New controls include the actual
source sum/normal Gram, a normal-only matching hostile, whole kinetic and
symplectic maps, continuous generators, action endpoints, actual histories,
source covariance and domain refusals. Receipt:
`results/shared-recoil-cotangent-binding.json`, with code hashes.

No new formal proof root, NumPy/137-port numerical comparison, apparatus test,
physical particle identification or electric-force law is claimed. SCC
orchestrates the exact checker; its admission is not physical verification.
