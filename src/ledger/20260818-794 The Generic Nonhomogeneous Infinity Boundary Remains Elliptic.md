---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 794 — The Generic Nonhomogeneous Infinity Boundary Remains Elliptic

## Question

The homogeneous three-site infinity boundary is the elliptic curve

\[
w^2=x^2t^4-(x^2+y^2-z^2)t^2+y^2.
\]

That specialization identifies momentum magnitudes with site energies,
\(P_i=X_i\). The hostile generic test is to keep the source kinematics

\[
(X_1,X_2,X_3,P_1,P_2,P_3)
\]

independent and determine whether the infinity boundary still has genus one
over the frozen Cayley--Menger carrier.

## Frozen residue and compactification

Use the generic Cayley--Menger matrix of the three-site loop and impose only
the source residue

\[
q_{\mathcal G_{12}}=0,
\qquad c=-E,
\qquad E=X_1+X_2+X_3.
\]

Do not impose \(P_i=X_i\). On the infinity chart

\[
b=\frac1s,
\qquad
a=\frac ts,
\]

extract the coefficient of \(s^{-4}\) from the exact determinant. The raw
Cayley--Menger coefficient is

\[
-2\left[
P_1^2t^4-(P_1^2+P_2^2-P_3^2)t^2+P_2^2
\right].
\]

The factor \(-2\) is the same source-fixed determinant unit already present
in the homogeneous compactification. Removing only that unit gives

\[
\boxed{
F_P(t)
=P_1^2t^4-(P_1^2+P_2^2-P_3^2)t^2+P_2^2.
}
\]

In particular, the site-energy sum \(E\) cancels from the boundary.

## Genus and discriminant

For generic nonsoft momentum data, \(F_P\) has four distinct roots. Hence

\[
\boxed{
D_\infty^{\rm gen}: W^2=F_P(t)
\quad\text{has genus }1.
}
\]

Set

\[
H_P=P_1^2+P_2^2-P_3^2.
\]

Then

\[
H_P^2-4P_1^2P_2^2
=\Lambda(P_1,P_2,P_3),
\]

where

\[
\Lambda
=(P_1+P_2+P_3)(P_1+P_2-P_3)
(P_1-P_2+P_3)(P_1-P_2-P_3).
\]

The binary-quartic discriminant is therefore

\[
\boxed{
\Delta_{F_P}
=16P_1^2P_2^2\Lambda(P_1,P_2,P_3)^2.
}
\]

Its support is exactly soft momentum support plus the existing external
momentum-triangle Cayley--Menger divisor.

## Interpretation

The generic pure elliptic quotient does not require a new cosmological
carrier stratum. It is compiled from the momentum side of the already frozen
Cayley--Menger carrier:

\[
\boxed{
\text{external momentum triangle}
\longrightarrow F_P
\longrightarrow H^1(D_\infty^{\rm gen}).
}
\]

The previously derived signed-energy compilation is the physical homogeneous
specialization

\[
P_i=X_i.
\]

Thus one must not promote the homogeneous statement “the elliptic block is
compiled from energy letters” to generic kinematics. The invariant generic
statement is instead:

\[
\boxed{
\text{the elliptic block is compiled from existing Cayley--Menger metric
data, specializing to signed-energy letters on }P_i=X_i.
}
\]

This is a strict refinement of H2: the carrier and comparison calculus may
be shared, while the coefficient compiler depends on the kinematic layer.

## Classification

- existing carrier: external momentum-triangle Cayley--Menger geometry;
- coefficient object: rank-two elliptic Gauss--Manin boundary variation;
- new branch support: none;
- new carrier datum: none;
- full marked relative system: not yet constructed.

## Verification

- exact Rust/Symbolica checker:
  `research/benincasa/marici-gm/src/bin/generic_infinity_boundary_genus.rs`;
- machine-readable packet:
  `research/benincasa/generic-infinity-boundary-genus.json`;
- allocator claim `seqclaim-399cf7d02fe4fa9e7e145d64`.

## Next falsifier

Pull the actual generic marked denominator sections to
\(D_\infty^{\rm gen}\) and compute their collision resultants with
\(F_P=0\). Test whether every new divisor is already a marked-incidence or
Cayley--Menger divisor. A residual irreducible factor outside that frozen
union would be the first evidence for new generic carrier structure.
