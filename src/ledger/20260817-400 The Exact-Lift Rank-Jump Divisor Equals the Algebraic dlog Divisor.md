---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# The Exact-Lift Rank-Jump Divisor Equals the Algebraic dlog Divisor

## Record

Status: exact coordinate identity plus finite-field support-and-multiplicity
comparison. This continues Entries 178 and 388--390.

## Hard-to-vary claim

The residual exact-lift conic is not new support. It is one component of the
already source-derived divisor of the canonical algebraic Gysin quotient
\[
\langle e_6,v_{\rm alg}\rangle/\langle e_6\rangle.
\]

## Frozen coordinate comparison

The marked-tangency patch uses
\[
X_1=1,\quad X_2={u+v\over2}-1,\quad X_3={u-v\over2},
\quad E=X_1+X_2+X_3=u.
\]
Therefore
\[
E^2-X_1X_2=0
\iff v=2u^2-u+2,
\]
which is exactly the conic isolated in Entry 388.

Entry 178 independently derived the source-selected quotient connection
\[
\alpha_{\rm alg}=d\log D,
\qquad
D=E^4-X_1^2X_2^2
=(E^2-X_1X_2)(E^2+X_1X_2).
\]

## Two-component falsifier

The same frozen exact-lift presentation was tested on both
\[
D_-=E^2-X_1X_2=0,qquad D_+=E^2+X_1X_2=0.
\]
At exact-form degrees 8 and 10 and for every \(u=3,\ldots,100\):

- each component lowers full presentation rank by one;
- each component adds one projected gauge direction;
- both transverse neighboring fibers remain generic.

Thus each component passes 196 enhancement tests and 196 neighbor controls.

Generic maximal minors were then frozen at
\[
u=3,5,7,11,19,37.
\]
On both components and at both degrees, all 24 specialized minors have
rank defect one and nonzero kernel--cokernel first normal pairing.
Interpolation orders 12 and 16 agree in every case.

## Verdict

\[
\boxed{
\operatorname{Supp}_{\rm rank\ jump}^{\rm exact\ lift}
=
\{D=0\}
\quad\text{with simple tested multiplicity on both components}.
}
\]

The conic of Entries 388--390 is therefore coefficient-presentation support
already predicted by the algebraic dlog quotient, not a new cosmological
carrier stratum. The previously unexplained second component is also detected
by the same frozen rank test.

This closes the support-level provenance loop:
\[
\text{infinity-Gysin algebraic quotient}
\longrightarrow d\log(E^4-X_1^2X_2^2)
\longleftrightarrow
\text{exact-lift Fitting divisor}.
\]

## Epistemic boundary

Equality of support and tested multiplicity does not by itself identify the
new projected gauge vector with the specialization of \(v_{\rm alg}\), nor
construct a canonical chain map between the two presentations. It is not a
symbolic global Fitting-ideal theorem.

The result does not revive \(\mathcal Q\). Existing exact calculations give
\[
\gcd(D,\mathcal Q)=1
\]
and regularity at generic \(\mathcal Q=0\).

## Classification

- existing carrier: unchanged energy/Cut carrier;
- coefficient support: \(D=E^4-X_1^2X_2^2=0\);
- new carrier datum: none;
- \(\mathcal Q\): absent from this mechanism.

## Next falsifier

Express the additional projected gauge direction on each component in the
source master basis and compare it with the specialization of the canonical
algebraic quotient generator represented by \(v_{\rm alg}\). Agreement
would identify the rank jump as the presentation shadow of that quotient
line; disagreement would show that the common divisor supports two distinct
coefficient mechanisms.

## Evidence

- `research/benincasa/exact-lift-dlog-divisor-identity.json`
- `research/benincasa/generic_algebraic_line_provenance.json`
- `research/benincasa/marici-gm/src/bin/marked_tangency_support.rs`
