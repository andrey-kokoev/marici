# The tail is a fixed resolvent, but its zero is only a cross-port cancellation

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact carrier recovery and cross-resolvent obstruction

This packet sharpens, rather than supersedes, the earlier result
`theta-transform-is-a-two-port-cross-transfer-not-yet-a-weyl-determinant.md`.
That packet established the two-port typing. The present contribution derives
the tail–head adjoint pair directly and supplies the minimal explicit
self-adjoint cross-resolvent witness with nonreal zeros.

## Fixed-carrier recovery

The one-sided theta tail

\[
G_s(q)=e^{-sq}\int_q^\infty f(v)e^{sv}\,dv
\]

solves

\[
(\partial_q+s)G_s=-f.
\]

Thus it can be read as a resolvent vector of the fixed translation generator,
with the decaying endpoint condition selecting the appropriate half-plane
resolvent. The homogeneous constant-channel augmentation is not the only
operator presentation.

The integral kernel of the tail operator is

\[
K_s(q,v)=1_{v\ge q}e^{s(v-q)}.
\]

Its Hilbert adjoint is the reflected head operator

\[
(T_s^*g)(v)
=e^{\bar s v}\int_{-\infty}^v e^{-\bar s q}g(q)\,dq.
\]

Carrier orientation reversal therefore supplies the analytic adjoint of the
tail resolvent. This is genuine reverse transport.

## Why this still does not yield RH

The scalar transform is the endpoint observation

\[
G_s(0)=\langle\delta_0,T_s f\rangle.
\]

The source port is \(f\), while the observation port is the distribution
\(\delta_0\). A zero is therefore a cross-resolvent cancellation, not an
eigenvalue of the fixed carrier and not a diagonal positive resolvent
coefficient.

Self-adjointness of the carrier alone places no reality constraint on zeros
of

\[
\langle u,(A-z)^{-1}v\rangle
\]

when \(u\ne v\).

## Smallest exact hostile model

Take

\[
A=\operatorname{diag}(-1,0,1),
\qquad
u=(1,1,1)^T,
\qquad
v=(1,-1,1)^T.
\]

The carrier is self-adjoint and both ports are real, yet

\[
u^T(A-z)^{-1}v
=-\frac{z^2+1}{z(z-1)(z+1)}
\]

vanishes at \(z=\pm i\). Replacing the cross coefficient by the diagonal
coefficient with the same source removes those nonreal zeros in this model.

## Corrected meaning of reverse incidence

There are two different adjoint problems:

1. construct the adjoint carrier evolution;
2. relate the observation port to the adjoint of the source port.

Orientation reversal solves the first. It does not solve the second. The
earlier full-rank Fourier residual tested an attempted internal block repair;
the present resolvent formulation shows the more invariant obstruction is
port mismatch.

The RH-bearing source law must therefore provide a positive or conservative
colligation identifying the theta endpoint observer with the source port in
the completed boundary metric. Equivalently, it must turn the cross matrix
coefficient into a diagonal Gram/resolvent coefficient without dividing by
the scalar section.

The earlier packet
`theta-no-local-l2-metric-identifies-source-forcing-with-endpoint-readout.md`
already rules out achieving this identification by an ordinary local weighted
Hilbert metric. The remaining constructions are therefore a genuinely rigged
boundary colligation or a source-derived exterior/Plücker relation.

## Relation to the Lagrangian programme

The fixed translation carrier now exists, but its scalar zero does not define
a deficiency vector or an intersection with the even Fourier graph. A
zero-to-incidence theorem must promote cross-port cancellation to failure of
transversality of a source-derived colligation. That promotion is exactly the
missing determinant bridge.

## Falsifier

Any claimed confinement theorem that uses only self-adjointness of the carrier
and a cross-resolvent scalar is refuted by the three-point model above. A
successful source metric must make the two ports adjoint-compatible and must
reject that model before inspecting its zeros.

## Scope

The resolvent interpretation, tail–head adjoint relation, and finite
cross-resolvent falsifier are exact. No source-derived positive identification
of the theta source and endpoint ports is established.

## Verification

The checker constructs a self-adjoint three-point carrier whose real
cross-resolvent coefficient has zeros at \(\pm i\), while its diagonal
comparison has only real zeros.
