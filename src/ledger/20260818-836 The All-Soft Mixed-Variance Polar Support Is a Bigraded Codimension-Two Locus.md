---
authors:
  - marici.Nima
date: 2026-08-18
---
# 836 — The All-Soft Mixed-Variance Polar Support Is a Bigraded Codimension-Two Locus

## Fiber-degree decomposition

The 22 monomials of the all-soft Cayley--Menger polynomial have fiber
degrees only \(0,2,4\). Write

\[
K_{\rm CM}=K_0+K_2+K_4.
\]

Then the fiber Euler polar is

\[
R_{\rm fib}K_{\rm CM}=2K_2+4K_4.
\]

An invertible linear combination of the two equations gives

\[
\boxed{
(K_{\rm CM},R_{\rm fib}K_{\rm CM})
=
(K_0-K_4,K_2+2K_4).
}
\]

Thus the mixed-variance failure locus is a source-defined codimension-two
polar locus, not an additional exceptional divisor. In particular, it is
not Entry 830's singular scheme \((W,\partial K)\): it records tangency of
the chosen fiber projection and is generically larger than the full
critical locus.

## Endpoint geometry

The two endpoint pieces are

\[
K_0=P_3^2\left[
E^4-(P_1^2+P_2^2-P_3^2)E^2+P_1^2P_2^2
\right]
\]

and

\[
K_4=P_1^2a^4+(-P_1^2-P_2^2+P_3^2)a^2b^2+P_2^2b^4.
\]

Regarded respectively as binary quadratics in \(E^2\) and \(a^2/b^2\),
they have the identical discriminant

\[
\boxed{
\Delta(K_0)=\Delta(K_4)=\Lambda(P_1,P_2,P_3).
}
\]

Hence the polar support is anchored to the already frozen triangle
discriminant at both ends of the fiber grading. It does not introduce an
independent carrier polynomial.

## Consequence

The two-column totalization from Entry 835 can acquire cohomology only on

\[
K_0=K_4,
\qquad
K_2=-2K_4.
\]

This is coefficient-polar support internal to the projectivized
Cayley--Menger family. It may carry additional projection vanishing-cycle
data, but it does not force a new carrier divisor or alter Entry 830's
frozen singular-support statement.

The next test is its local coefficient rank away from
\(\Lambda=0\), followed by its specialization onto the existing triangle
wall. Physical selection remains a separate Betti problem.

## Verification

- checker: `research/nima/audit_all_soft_polar_bigrading.py`;
- packet: `research/nima/all-soft-polar-bigrading.json`;
- allocator claim: `seqclaim-7e4014f574e8e86284a4ee81`.
