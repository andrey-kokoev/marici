---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 828 — The All-Soft Strict Transform Is the Projectivized Universal Cayley-Menger Family

## Question

Entry 826 leaves the all-soft point as a projectivized normal-cone problem.
The carrier-level falsifier is whether radial resolution forces an
exceptional incidence not already present in the frozen energy,
coordinate-boundary, triangle, and Cayley--Menger arrangement.

## Exact radial transform

Scale

\[
(E,P_1,P_2,P_3,a,b)
=
\rho(\widehat E,\widehat P_1,\widehat P_2,\widehat P_3,
\widehat a,\widehat b).
\]

Since \(A=a^2\) and \(B=b^2\), exact substitution in the frozen polynomial
gives

\[
\boxed{
K_{\rm CM}(\rho\,\widehat{\boldsymbol k})
=
\rho^6K_{\rm CM}(\widehat{\boldsymbol k}).
}
\]

With

\[
w=\rho^3W,
\]

the strict transform is

\[
\boxed{
W^2=K_{\rm CM}
(\widehat E,\widehat a,\widehat b;
\widehat P_1,\widehat P_2,\widehat P_3).
}
\]

It is independent of \(\rho\). Hence:

- there are no higher radial correction terms;
- radial transport creates no extension class;
- radial coefficient monodromy is trivial, since \(W\) has integral
  weight three.

## Exceptional arrangement

The exceptional divisor carries the projectivized universal
Cayley--Menger family itself. Its singular and marked strata are therefore
the projectivizations of already frozen loci:

\[
\begin{gathered}
E=0,\qquad E=\pm P_i,\qquad P_i=0,\qquad
\Lambda(P_1,P_2,P_3)=0,\\
a=0,\qquad b=0,\qquad
\text{marked-coordinate intersections},\qquad
K_{\rm CM}|_S=0.
\end{gathered}
\]

Entry 807's critical-locus audit applies chartwise on this projective
family. Radial blowup introduces only the exceptional divisor demanded by
the predeclared Rees/flagged-normal carrier; it introduces no additional
incidence generator.

Thus

\[
\boxed{\text{new exceptional carrier incidence count}=0.}
\]

## Coefficient qualification

The result does not turn the 15 all-soft points into fixed-rank objects.
Their exceptional coefficient system remains the full direction-dependent
Cayley--Menger family. Different projective directions meet different
existing discriminant strata.

The correct classification is therefore:

\[
\boxed{
\begin{array}{c|c}
\text{carrier}&\text{existing radial Rees/CM arrangement}\\
\text{coefficient}&\text{projectivized universal CM family}\\
\text{radial monodromy}&1\\
\text{common finite rank}&\text{not defined}\\
\text{new carrier datum}&\text{none}
\end{array}
}
\]

## Consequence for H2

The all-soft frontier does not falsify H2 at carrier level. It gives a
particularly direct instance of the refined architecture:

\[
\text{shared flagged-normal carrier and calculus}
+
\text{sector-specific coefficient family}.
\]

Physical activation remains separate. A projective coefficient direction
is not selected until a source-derived relative chain or regulator map
chooses it.

## Verification

- exact Symbolica checker:
  research/benincasa/marici-gm/src/bin/all_soft_radial_strict_transform.rs;
- packet:
  research/benincasa/all-soft-radial-strict-transform.json;
- allocator claim seqclaim-fd67efd90ae62b62960be545.

## Next falsifier

Test gluing between projective charts of the all-soft exceptional family.
The chart transitions must preserve the labelled occurrence, residue
orientation, and Cayley--Menger Kummer line. A nontrivial transition unit is
coefficient gluing; a transition requiring a new incidence divisor would
reopen the carrier question.
