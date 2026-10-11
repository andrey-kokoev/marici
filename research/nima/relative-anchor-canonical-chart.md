# A relative-anchor canonical chart for the retained six-port interaction

## Frozen question and test

Can the existing nonzero conserved anchor supply phase-neutral canonical
coordinates while retaining every old state, pulse, spatial reading and history?
SCC obligations: attachment transport and readout descent on c!=0. Pulse area
remains the declared angular parameter, not a physical duration calibration.

Candidate: retain c, form xi=r/c, pull back the inherited symplectic structure,
and derive rather than guess the conjugate coordinates. Any centering and
normalization must come from the existing metric. The global form must retain
reference terms; a fixed-anchor fiber is not silently a phase quotient.

Rivals: a gauge-trivial reference; intensity-only compression; uncorrected
quadratures claimed canonical; deletion of the zero-anchor locus; a mixed
coherence matrix treated as rank one; a three-coordinate spatial projection
that hides an internal response; replacing the ordered pulses by the flow of
their summed Hamiltonian.

Acceptance tests: all-port intertwining and Hamiltonian equality, exact form
pullback, full state and rank-one coherence recovery, common-phase neutrality,
reference transport, actual 68-word midpoint/endpoints, source spatial
covariance and a retained internal-sector test. No mass or new interaction is
to be fitted to a failed identity.

## Metric-derived centering

The preceding exact reduction gives eta=(c,r), z=T eta, and inherited metric

    M = [[1,-s^T],[-s,K]],  K=I+F^T H F.

Its positive square completion determines, with no fitted coefficient,

    b=K^-1 s,
    mu=1-s^T K^-1 s > 0,
    w=r-b*c,
    eta^dagger M eta=mu*|c|^2+w^dagger K w.

Here the conserved source anchor is still a=f_AB*c. Centering changes neither
that anchor nor any operation. K and mu refer to the previously declared
exchange metric; this does not newly derive that metric from native incidence.

## Relative coordinates that really are canonical

For c!=0 set R=|c| and g=c/R. The successful coordinates are

    u=conjugate(g)*(r-b*c),
    q=Re(u),
    p=2*K*Im(u).

In terms of the proposed ratios xi=r/c, these are
q=R*Re(xi-b) and p=2*R*K*Im(xi-b). Thus bare ratios alone were not silently
declared canonical: both the reference amplitude and the actual metric enter.

Common phase multiplies c and r together. It leaves q,p invariant while
transporting g. On a local reference-angle chart g=exp(i phi), define the old
conserved phase quantity

    Q=mu*R^2+E(q,p),
    E(q,p)=q^T K q+(p^T K^-1 p)/4.

The FULL inherited form, not merely its fixed-anchor restriction, becomes

    Omega = sum_i dq_i wedge dp_i + dQ wedge dphi.

Consequently the reference canonical pair is (phi,-Q). The minus sign is a
symplectic convention, not a construction of a negatively charged species.
The domain is Q>E(q,p), with

    R=sqrt((Q-E)/mu),
    c=R*g,
    r=b*c+g*(q+i*K^-1*p/2).

Together with T these formulas recover the original state exactly. The
reference phase is local modulo 2*pi; no winding or source history is replaced
by its endpoint. The existing pulses fix c, so phi is not another clock.

The action primitive also transports exactly:

    -Im(eta^dagger M d eta)
      = sum_i p_i dq_i - Q dphi - d(q^T p)/2.

The last term is an endpoint term that must be retained when comparing actions.
This identity does not identify Bargmann cycle phases with classical action.

Fixing c gives the previously declared affine state fiber. Separately, after
this global calculation, fixing Q and quotienting the common phase has radical
exactly the phi direction and leaves the canonical form on the open domain
E<Q. These are different restrictions, now explicitly related by the full form.
The full recovery packet keeps the reference rather than silently quotienting it.

## One chart for every existing port

For port i, the original projector Hamiltonian transforms into

    h_i(q,p)=(K*q)_i^2/2+p_i^2/8.

The corresponding angular-parameter equations are

    q'_j=delta_ji*p_i/4,
    p'_j=-K_ji*(K*q)_i,
    Q'=0,  phi'=0.

All six equalities are checked against the original generators, not against a
newly assigned oscillator model. Each generator A_i obeys A_i^3=-A_i, giving
its exact sine/cosine pulse. At area pi the map is a cotangent lift:

    q -> R_i q,  p -> R_i^(-T) p,
    R_i=I-e_i e_i^T K.

The same source budget E is conserved by every port. The port Hamiltonians
are not mutually commuting. Replacing their ordered execution by one flow of
their sum would change the protocol and is not done. The coefficient 1/8 is
in the chosen dimensionless angular/canonical normalization, not a calibrated
inertial mass or a supplied free-flight law.

## Exact state, reading and history recovery

All 68 original labelled paths are checked at the midpoint and endpoint of
their final pulse: 136 exact state reconstructions. Each chart packet retains
the actual registered family object, its path slot and pulse sample. Inversion
returns that SAME source record and recovers all old carrier, record and
cross-term readings. Recovering the vectors also preserves their Gram data.

Common rephasing changes only the retained reference frame. Complex
conjugation instead preserves q and reverses p, retaining the distinction
that intensity-only readings lost. In this particular real preparation all
completed real-exchange endpoints have p=0, while nonzero momenta occur inside
pulses. These are oscillator-chart momenta, not a demonstrated particle
scattering recoil.

For a pure coherence matrix C=eta eta^dagger,
xi_i=C_i0/C_00 and C_ij=C_i0*C_0j/C_00 recover the same relative state.
A mixed-rank matrix is rejected. This nonlinear reconstruction explains why
the earlier 49-direction linear closure is not a state-dimension obstruction.

Zero anchor, vacuum, invalid reference phase and zero reconstructed radius are
refused. A nonzero zero-anchor state still has a regular original pulse: the
failure is of this chart, not loss of a state or zero physical amplitude.

## A covariant three-vector pair, with internal modes retained

Use the existing endpoint geometry to define the 3-by-6 matrix X whose i-th
column is the target vertex of port i. Set

    W=(X X^T)^-1 X,
    x=X q,  pi=W p,
    N=I-X^T W.

Then rank(X)=rank(N)=3 and the pair (x,pi) is canonical. It Poisson-commutes
with the internal projected variables (Nq,Np), and

    q=W^T x+Nq,  p=X^T pi+Np

recovers all six pairs. The internal variables have three independent pairs;
no arbitrary basis in their kernel is required. Under each of the 24 source
vertex relabellings, x and pi transform by the existing orthogonal spatial
matrix and N transports consistently.

Every port couples this spatial block to the internal block (response rank
two at each port). A state-domain hostile with equal x,pi, reference phase
and Q, but opposite internal momenta, gives opposite same-port spatial
responses. Those hostile states are not claimed to be two of the fixed 68
forward histories. Dropping internal modes therefore does not yield an
all-state autonomous three-vector mechanics.

The vector pair is an algebraic source-covariant chart, not an identification
with measured positions and mechanical momenta. A passive anchor-basis phase
change induces a canonical quadrature rotation; the checker preserves all
port Hamiltonians under it. A unique physical configuration/momentum
polarization has not been selected merely by finding canonical coordinates.

## Disposition and verification

The relative-anchor candidate survives: a single phase-neutral canonical
six-pair chart intertwines every port, retains the reference phase/charge pair,
and recovers the original source states and records. No new force, metric,
reference oscillator or Born rule was inserted. The earlier noncanonical
intensity-position result remains true for its DIFFERENT reading.

Physical position, inertia, charge coupling and dimensional normalization are
still not derived. The improvement is an actual canonical chart for the SAME
interaction, rather than another incompatible per-port mechanical analogy.

Run:

    uv run --with sympy python research/nima/checkers/check_relative_anchor_canonical_chart.py
    uv run --with sympy python research/aspect/scc/scc.py check nima-relative-anchor-canonical-chart

The checker reruns the 455-check exact response construction, retaining its
source-extraction boundary (no fresh NumPy/137-port comparison). Its new tests
cover full forms and action primitives, all six generators, recovery, reference
transport, source covariance and deliberate domain/closure hostiles. The
receipt is `results/relative-anchor-canonical-chart.json`. No new formal proof
root or laboratory verification is claimed; SCC orchestrates the exact checker.
