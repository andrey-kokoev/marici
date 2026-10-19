# Connecting the source cycle to the Fourier-comb and Mellin representations

## Iteration 1: explicit direct attachment

SCC obligation: attachment transport and route compatibility. Reuse
Strominger's source constructor and actual fixed-Gram projection; attach its
visible cycle to the existing analytic Fourier orbit. This supplies a concrete
comparison map, not an inference from matching dimensions or spectra.

The analytic seed is an explicitly chosen shifted comb with 0<a<1,
a not equal to 1/2. Choosing a is additional input: the finite carrier does not
select an arithmetic shift. Fix the additive Fourier convention
Ff(y)=integral f(x)exp(-2pi ixy)dx and the starting assignment AD -> P_a.
These choices determine the remaining ports by the existing source cycle.

## Direct commuting square

Strominger's C12 acts on directed edges by the vertex cycle A->D->B->C->A.
Its invariant visible orbit is AD->DB->BC->CA->AD. The source coefficient
order begins AD,CA,DB,BC. Let E embed these four coordinates and

  P=(E^T G12 E)^(-1)E^T G12=[I4 | J_(4,8)/14],
  G12=10I12+J12, N=I12-EP, C4=P C12 E.

Here J_(4,8) denotes the all-ones matrix, not the attachment permutation below.
Define four tempered distributions

  v0=P_a=sum_n delta_(n+a),
  v1=C_-a=sum_n exp(-2pi ian)delta_n,
  v2=P_(1-a),
  v3=C_a=sum_n exp(2pi ian)delta_n.

Poisson summation gives F v_j=v_(j+1 mod4). These four distributions are
linearly independent for the stated shifts: the two shifted support sets are
disjoint from each other and from the integers, and the two integer character
sequences are independent unless 2a is integral. At a=1/3 the checker verifies
a four-probe matrix using atoms at 1/3,2/3,0,1. Local smooth test functions
isolating these atoms make this a distributional independence witness.

Let B_a send the j-th cyclic coordinate to v_j. Let J send the coefficient
basis AD,CA,DB,BC to cyclic slots 0,3,1,2. The actual attachment is

  I_a=B_a J,                 R_a=I_a P.

The identities checked exactly on coefficients are

  P C12=C4 P,                J C4=F_cyc J,
  R_a C12=F R_a.

Thus reducing first and applying the analytic Fourier operation gives exactly
the same distribution as applying the source permutation first and then
reducing. Every original arrow has a specified image: the four selected arrows
map to their assigned ports; each other basis arrow maps to
(v0+v1+v2+v3)/14 through the actual P. The kernel of R_a is exactly ker P.

This is a chosen, explicit faithful realization of the four-dimensional
quotient, not an injective realization of all twelve coordinates. The full
source is retained as (R_a x,Nx). Since B_a is injective on its coefficient
space, reconstruction is x=E I_a^(-1)(R_a x)+Nx. The checker verifies its
coefficient version on all twelve columns.

## The generator connects too, but is not the Fourier tick

C12 is orthogonal in the coefficient chart, so the already constructed
D12=C12-C12^T maps to

  R_a D12=(F-F^(-1))R_a.

On the four-port span this gives a continuous finite-dimensional group
exp(t(F-F^(-1))). It is not the additive Fourier operator at a quarter period
on the entire space: the alternating character has Fourier eigenvalue -1 but
skew-generator eigenvalue zero. Exactly, for D4=C4-C4^T,

  exp(pi D4/4)-C4=2 M_minus,
  M_minus=(I-C4+C4^2-C4^3)/4.

The checker retains all four cyclic characters 1,-1,i,-i, and verifies this
rank-one discrepancy. No parity information is erased to manufacture agreement.

## Radial and Mellin continuation of the same map

Compose I_a with the already constructed oriented log-radial map. Retain the
zero atom as an endpoint coordinate: the character ports each have atom
coefficient 1 at zero, and the support ports have none. The endpoint row on
cyclic coefficients is therefore (0,1,0,1). Fourier acts on the complete
reconstructed distribution, not independently on a bulk piece after throwing
away its endpoint.

The existing radial kernel and Mellin calculation then carry this same
Fourier action into G(t) followed by t->-t, where

  G(t)=[[m_+(t),m_-(t)],[m_-(t),m_+(t)]],
  m_sigma(t)=(2pi)^(-1/2+it) Gamma(1/2-it)
             exp(-i sigma pi(1/2-it)/2).

This analytic identity is imported from the prior kernel derivation, not
proved by our finite matrix checks. The ordered comb images are the prior
Hurwitz and periodic-polylogarithm pairs. For example P_a gives
(zeta(s,a),zeta(s,1-a)); C_-a gives
(Li_s(exp(-2pi ia)),Li_s(exp(2pi ia))) after retaining its zero atom separately.

The log half-density parameter t and the Dirichlet exponent s are different
coordinate conventions, not interchangeable symbols. The raw exponent is
s=1/2+it; the reflected argument is 1-s=1/2-it, which occurs in the displayed
gamma factor. These statements use the continued test-dual Mellin pairing of
the earlier notes, not a convergent global Mellin integral of an arbitrary
unsmoothed comb.

We have thereby connected the finite source permutation to an actual Fourier
operation and its existing gamma/Hurwitz representation. This is not yet an
identification of the five scalar zeta-completion arrows with five Fourier
steps. Multiplication by Gamma(s/2) and Fourier transformation are different
operations.

## Metric boundary

Transporting the coefficient Gram through J gives 10I4+J4 on cyclic
coefficients, and F_cyc preserves it. The full metric splits into this visible
part and N^T G12 N. This is a legitimate chosen norm on the finite comb span.
It does not assign a finite L2 norm to a delta comb or establish equality with
an independently specified Green-space Gram. Rigged distribution/test pairing
and a transported coefficient norm are distinct objects.

## What remains of the triangle-history connection

Fresh inspection of `check_triangle_coherent_generator_transport.py` shows
that its operative reader P_n has TWO rows, its section E_n has two columns,
and its tick C is a two-dimensional active rotor tick. Its four endpoint rows
O_n are converted using RBplus; they are not the four independent cyclic ports
constructed above. Reusing the formula E_next=F_n E_n C^-1 is justified only
after matching these representations.

That prior theorem already transports any compatible commuting generator and
hidden component once the reader square is supplied. The next executable
comparison is therefore to recover its actual active tick and match it to the
+i/-i sector of our C4, while explicitly retaining the common and alternating
ports elsewhere. Calling the existing rank-two reader the full Fourier orbit
would erase two characters. No such identification is made in this iteration.

The direct full-permutation square also does not automatically certify every
intermediate step of the six-step schedule: a subspace invariant under the
skew generator need not be invariant under C12 on its stationary sectors.
That schedule requires a separate permutation-level check before importing
all-stage Fourier transport.

## Verification

`uv run research/voevodsky/checkers/check_carrier_fourier_orbit_bridge.py`
reconstructs the source, checks the prior source hashes, the full-permutation
and skew-generator squares, all four character projectors, reconstruction,
the endpoint row, a concrete comb independence witness, and the coefficient
Gram split. Analytic Poisson and Mellin arguments remain imported mathematics.

Artifacts: `results/carrier-fourier-orbit-bridge-v1.json` and the owner-local
SCC manifest. No Strominger or Nima source is modified. No RH proof, physical
clock selection, or independent analytic Hilbert-metric equality is claimed.
