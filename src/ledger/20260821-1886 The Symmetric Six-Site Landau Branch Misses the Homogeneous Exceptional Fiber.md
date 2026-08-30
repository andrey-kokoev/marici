# 1886 — The Symmetric Six-Site Landau Branch Misses the Homogeneous Exceptional Fiber

## Corrected deformation

Entry 1885 forbids inversion of the rank-three regular-hexagon routing Gram
matrix.  Introduce one predeclared cyclic normal parameter \(\kappa\) in the
opposite-site pairing.  The regular hexagon is \(\kappa=0\), and

\[
\det H_6(\kappa)=-\frac14\kappa(6+7\kappa).
\]

Rather than invert and then specialize, multiply both cover equations by the
actual Gram determinant and eliminate in the stabilizer-fixed sector

\[
y_1^2=y_3^2=y_5^2=x,
\qquad
y_2^2=y_4^2=y_6^2=z.
\]

## Exact resultant

The denominator-cleared symmetric critical resultant is

\[
-\frac1{32}\kappa^2(6+7\kappa)^3 P(\kappa,z),
\]

where

\[
P=
36-60\kappa+18\kappa z+55\kappa^2-12\kappa^2z
-4\kappa^3+2\kappa^3z.
\]

The prefactor is inherited Gram multiplicity.  Its removal is forced by the
strict transform, not fitted after observing the answer.  On the exceptional
fiber,

\[
\boxed{P(0,z)=36.}
\]

Hence the strict-transform divisor has empty finite intersection with
\(\kappa=0\).

## Narrow result

\[
\boxed{
\text{No stabilizer-fixed six-site Landau divisor specializes to the
homogeneous hexagon.}
}
\]

The apparent \(\kappa^2\) support is entirely the pre-existing Gram
degeneracy.  It is not a new cosmological coefficient divisor and cannot be
promoted to a Carrier stratum.

This closes only the \(C_3\)-fixed critical sector.  Nonsymmetric critical
orbits at generic six-site kinematics remain untested.

## Meta-level consequence

The five-site physical orbit does have a six-site source incidence, but its
most symmetric higher-arity continuation escapes the finite homogeneous
fiber.  Thus systematic assembly is not “the same polynomial at every
arity.”  Carrier incidence survives while coefficient support may disappear
under a singular kinematic specialization.

## Next falsifier

Decompose the full three-free-coordinate critical module under the
\(C_3\) stabilizer.  Test the two-dimensional nontrivial character sector in
the same \(\kappa\)-Rees family.  A surviving strict-transform class there
would be a genuinely nonsymmetric six-site continuation; its absence closes
this incidence pattern at homogeneous arity six.

## Durable verification

- `research/benincasa/marici-gm/src/bin/six_site_disjoint_pair_triple_symmetric_landau.rs`
- `research/benincasa/results/six-site-disjoint-pair-triple-symmetric-landau.json`
- allocator claim: `seqclaim-e7e1ba4cb956e74a65e1e36b`
- epistemic event: `ev-000000002248-e3cb82bb-9817-47fa-8cc3-8c99e6d5fe89`
