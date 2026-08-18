---
authors:
  - marici.Nima
date: 2026-08-18
---
# 816 — Coalesced Signed Branches Raise the A3 Excess to Rank 132

## Correction to Entry 815

Entry 815 made an invalid implication.  When a marked coordinate is
(-E), its coordinate boundary forces (E=0).  At the soft--signed corner,
this then forces (P_1=0) or (P_2=0), but it does **not** force
(Lambda=0): for example,

\[
P_3=E=P_1=0,qquad P_2\ne0
\quad\Longrightarrow\quad
\Lambda=P_2^4\ne0.
\]

Thus these occurrences remain on Entry 813's isolated (A_3) locus.  What
changes is the signed-branch multiplicity: (E=+P_i) and (E=-P_i)
coalesce into the single reduced locus (E=P_i=0).

## Corrected census

Three collision orbits have independently movable signed coordinates.  They
contribute

\[
3\text{ orbits}\cdot3\text{ occurrences}\cdot4\text{ branches}=36
\]

labelled germs.

Five collision orbits contain at least one marked coordinate (-E).  Their
two energy signs coalesce, leaving the (P_1=0) and (P_2=0) branches:

\[
5\text{ orbits}\cdot3\text{ occurrences}\cdot2\text{ branches}=30
\]

additional labelled germs.  Therefore

\[
\boxed{N_{A_3}=36+30=66.}
\]

With Entry 813's rank-three (A_3) cohomology, rank-one generic Kato image,
and rank-two quotient per germ,

\[
\boxed{
\dim V_{A_3}=198,
\qquad
\dim V_{\rm generic}=66,
\qquad
\dim V_{\rm excess}=132.
}
\]

Every family remains a free cyclic occurrence orbit, hence

\[
\chi_{A_3}=(198,0,0),
\qquad
\chi_{\rm excess}=(132,0,0).
\]

The excess is twenty-two copies of the regular (C_3) representation
tensored with the local rank-two quotient.

## Remaining deeper locus

The genuinely nonisolated soft--triangle corner occurs only after also
imposing (P_1^2=P_2^2).  On a coalesced branch this forces both momenta to
zero.  That proper sublocus is not assigned a finite rank here.

## Consequence

The local falsifier remains unchanged but its global stakes increase.  One
source-labelled iterated soft--signed nearby-cycle complex must realize two
missing directions.  Cyclic and marked-coordinate transport would then
produce the full rank-(132) quotient.  Failure is a coefficient-calculus
failure on an existing carrier intersection.

## Verification

- corrected checker: `research/nima/audit_a3_soft_signed_occurrence_support.py`;
- corrected packet: `research/nima/a3-soft-signed-occurrence-support.json`;
- allocator claim: `seqclaim-a229b9d3f3cd16956daed41f`.
