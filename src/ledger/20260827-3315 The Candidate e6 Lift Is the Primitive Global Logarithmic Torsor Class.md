---
id: 20260827-3315
date: 2026-08-27
status: exact-candidate-global-class-theorem
---

# 3315 — The Candidate e6 Lift Is the Primitive Global Logarithmic Torsor Class

## Correction to the fiberwise interpretation

Entry 3311 proves that source reduction at each generic \(v\)-fiber leaves
the \(e_6\)-valued principal row unfixed. Fiberwise freedom does not imply
that every global rational row is triangular-gauge equivalent.

This entry computes the global rational gauge class of the reconstructed
candidate without promoting it to source authority.

## Hom connection

Along \(u=0\), the exact source-derived diagonal connections on \(e_6\) and
\(q_{m top}\) coincide:

\[
A_{e_6,v}|_{u=0}
=
A_{q_{m top},v}|_{u=0}
=
-\frac1{v-2}.
\]

Therefore the induced connection on
\(\operatorname{Hom}(q_{m top},e_6)\) is trivial. A triangular gauge
\(h=a(v)q_{m top}/u\) changes the principal coefficient by

\[
f(v)\longmapsto f(v)+a'(v).
\]

The global gauge question is ordinary rational de Rham exactness.

## Candidate factorization

The source-canonical double-pole coefficient is

\[
C_2=-\frac18.
\]

The reconstructed candidate's signed-energy principal term is

\[
f(v)=\frac1{4v(v-2)}.
\]

Exact factorization gives

\[
f(v)
=
C_2\,d\log\frac{v}{v-2}.
\]

Its residues are

\[
\operatorname{Res}_{v=0}f=-\frac18,
\qquad
\operatorname{Res}_{v=2}f=\frac18.
\]

After dividing by \(C_2\), the residue vector is

\[
(1,-1).
\]

This is the primitive integral logarithmic generator on the twice-punctured
affine line.

## Rational gauge obstruction

The derivative of a rational function has zero residue at every finite pole.
Since \(f\) has nonzero residues, there is no rational \(a(v)\) satisfying

\[
a'(v)=-f(v).
\]

Thus the candidate row is not globally removable by a rational triangular
gauge, even though its value is unfixed in every isolated source fiber.

## Revised classification

Entry 3311's narrow source statement remains valid:

- the current source recurrence does not select a global \(e_6\) row;
- the candidate coefficient cannot yet be called source-normalized.

Its stronger presentation-data interpretation must be refined:

- the candidate represents a nonzero global logarithmic torsor class;
- its scale is exactly the canonical double-pole coefficient;
- its normalized residues are primitive and supported only on the existing
  divisors \(v=0,2\).

Therefore the remaining question is selection among global torsor classes,
not removal of a pointwise gauge artifact.

## Classification

| Datum | Classification |
|---|---|
| Hom connection | trivial |
| candidate global class | nonzero primitive logarithmic class |
| support | existing \(v=0,2\) divisors |
| scale | canonical \(C_2=-1/8\) |
| source selection | unproved |
| new carrier datum | none |

## Next falsifier

Derive, without using the candidate row, the integral residue vector of the
global \(e_6\)-torsor from the conductor occurrence lattice and its oriented
Leray/Gysin comparison. The candidate is selected exactly if that derivation
returns

\[
C_2(1,-1).
\]

Zero would make the candidate class unauthorized; a different primitive
vector would falsify its normalization.

## Durable artifacts

- checker: `research/benincasa/checkers/audit_e6_global_logarithmic_torsor.py`;
- packet: `research/benincasa/results/e6_global_logarithmic_torsor.json`;
- allocator claim: `seqclaim-c196c491c85e288add424f2d`.
