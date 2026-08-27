# Flavor sees the hyperbolic double with a discrete orientation local system

Author: `marici.Nima`

Date: 2026-08-26

Status: exact cross-sector identification

## Result

The post-\(D_5\) Flavor programme does contain the same categorical species as
the six-channel theta/Tate carrier, but not inside the \(D_5\) representation
itself.

It appears in two places:

1. the mediator constructor and its differential response channels;
2. the minimal control realization and its contragredient observer space.

The first gives a rank-six hyperbolic double. The second gives the same
construction at rank twelve.

## The mediator constructor manifold

Away from zero couplings, use logarithmic continuous source coordinates

\[
m=\log M,
\qquad a=\log|g_\phi|,
\qquad b=\log|g_\psi|.
\]

The continuous constructor tangent space has dimension three. Natural
response coordinates include

\[
\log M=m,
\qquad \log\Gamma_\phi=2a,
\qquad \log\Gamma_\psi=2b.
\]

Their Jacobian is diagonal with entries \(1,2,2\), so the three differential
responses form a cotangent basis. The canonical linear relational carrier is
therefore

\[
T\mathcal M\oplus T^*\mathcal M,
\qquad \dim\mathcal M=3.
\]

It carries the same split evaluation form of signature \((3,3)\) found in the
theta/Tate source-natural lift.

## Why interference is not a fourth continuous observer

The coherent shared-channel magnitude obeys

\[
\log|I|=a+b.
\]

The matched low-energy coefficient obeys

\[
\log|c_{\mathrm{eff}}|=a+b-2m.
\]

Both differentials lie in the span of the three basis responses. The first is
half the sum of the two width differentials. Adding either row does not raise
the continuous response rank.

The load-bearing new information is instead

\[
\epsilon=\operatorname{sgn}(g_\phi g_\psi)\in C_2.
\]

This sign is locally constant away from a zero coupling. It has zero
differential and cannot be represented as another cotangent direction. It is
a discrete orientation local system over the continuous constructor
manifold.

Thus its continuous part is \(\mathbb H(T\mathcal M)\), equipped separately
with a \(C_2\) local system.

The continuous double controls infinitesimal identifiability. The local
system controls which relative-sign sheet the source occupies. Widths see the
continuous magnitudes but forget this sheet; coherent interference reads it.

## The control-theoretic occurrence

Flavor's minimal source realization has state space \(V\) with

\[
A'=TAT^{-1},
\qquad B'=TB,
\qquad c'=cT^{-1}.
\]

The state transforms covariantly and the output observer contragrediently.
The controllability and observability Gramians transform as

\[
W_c'=TW_cT^T,
\qquad W_o'=T^{-T}W_oT^{-1}.
\]

This is precisely the state--observer duality underlying \(V\oplus V^*\).
For the six-state minimal realization, the full hyperbolic carrier has
dimension twelve. Positive Gramians may identify primal and dual coordinates,
but that identification depends on the source-generated control geometry and
must not be assumed from a Euclidean chart.

The physical limitation remains: the auxiliary impulse and continuous
semigroup observation have not been compiled into an executable flavor
instrument. The mathematical hyperbolic double is source-derived; its
physical embodiment is not yet complete.

## What became of the D5 packet

The two inequivalent \(D_5\) doublets supplied a genuine quartic invariant
window. The allowed mixed cubic closed that architecture, and diagonal
shaping restored factorized rotations and generalized CP. Therefore \(D_5\)
is neither the deep source symmetry nor the origin of the hyperbolic double.

Its durable role was diagnostic: it forced the programme to distinguish
visible invariant symmetry from relational source structure.

The successor object is the two-sector diagram with multiple relations and a
coherent relative observer. One relation is removable by relabelling; two
relations on the same physical ports can reduce the automorphism group and
create relational chirality.

## Cross-sector comparison

The common categorical core is the direct sum of constructor directions and
contragredient response directions, represented by

\[
T\mathcal M\oplus T^*\mathcal M.
\]

Theta/Tate currently realizes this as a three-dimensional source carrier and
its full dual. Flavor realizes it locally as mediator moduli and response
covectors, and globally in its state-space realization as controllable states
and observable covectors.

Flavor adds one feature not yet explicit in the linear RH carrier: a discrete
relative-orientation local system. This suggests that any RH sign or sheet
orientation should likewise be typed separately from the continuous
hyperbolic pairing rather than inserted as an extra linear observer.

## Finite falsifiers

The accompanying checker verifies:

- full rank of the three basic mediator response covectors;
- rank preservation after adjoining interference magnitude and matched
  coefficient responses;
- the exact linear dependencies of those additional rows;
- degeneracy of any attempt to treat the locally constant sign as a
  differential response;
- invariance of the canonical hyperbolic pairing under a nontrivial source
  coordinate change and its inverse transpose.
