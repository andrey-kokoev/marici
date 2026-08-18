---
authors:
  - marici.Nima
date: 2026-08-18
---
# 815 — The Generic Soft-Signed A3 Excess Occupies Three Collision Orbits

> **Superseded by Entry 816.** This entry incorrectly treated the five
> occurrences with a marked coordinate (-E) as automatically lying on
> (Lambda=0). They instead retain isolated (A_3) germs with coalesced
> signed branches when the other momentum is nonzero. Its (36/108/72)
> census is withdrawn.

## Question

Entry 813 finds a local (A_3) singularity of rank three at a
double-coordinate, soft--signed corner, with only one direction supplied by
the generic Kato line.  The eight collision orbits of Entry 803 do not all
meet this locus generically: the marked-coordinate equations must be imposed
before cyclic assembly.

## Support gate

The three collision representatives

\[
(g_1,g_2),qquad(g_1,g_3),qquad(g_2,g_3)
\]

have two independently movable marked coordinates.  Their simultaneous
coordinate boundary can therefore meet

\[
P_3=0,qquad E^2=P_1^2\quad\text{or}\quad E^2=P_2^2
\]

at a generic (A_3) point.

For each of the other five representatives, at least one marked coordinate
is exactly (-E).  Its double boundary forces (E=0); the signed condition
then forces an additional soft momentum.  Those occurrences lie on Entry
813's deeper nonisolated soft--triangle corner and must not be counted as
generic (A_3) germs.

## Cyclic count

Each of the three eligible collision orbits has three cyclic occurrences.
Each occurrence has four signed branches: two choices of (P_1) versus
(P_2), and two energy signs.  Hence

\[
N_{A_3}=3\cdot3\cdot4=36
\]

labelled generic germs.

Entry 813 gives rank three, generic Kato rank one, and excess rank two per
germ.  Therefore

\[
\boxed{
\dim V_{A_3}=108,
\qquad
\dim V_{\rm generic}=36,
\qquad
\dim V_{\rm excess}=72.
}
\]

The cyclic action is free on every transported family, so

\[
\chi_{A_3}=(108,0,0),
\qquad
\chi_{\rm excess}=(72,0,0).
\]

Equivalently, the excess is twelve copies of the regular (C_3)
representation tensored with the rank-two local coefficient quotient.

## Meaning for H2

The support gate prevents a spurious factor-of-eight census.  The genuine
frontier is smaller but nonzero: a rank-two local extension on three free
collision orbits.  This is coefficient complexity on already declared
soft--signed intersections, not a new carrier divisor.

Only one source-labelled iterated soft--signed nearby-cycle complex now
needs to be constructed.  If it realizes the two missing local directions,
cyclic naturality transports it across all thirty-six germs.  If it does
not, the current coefficient calculus fails H2 on this corner.

## Scope

The other five collision orbits belong to the deeper nonisolated
soft--triangle audit.  No finite rank is assigned to them here.

## Verification

- checker: `research/nima/audit_a3_soft_signed_occurrence_support.py`;
- packet: `research/nima/a3-soft-signed-occurrence-support.json`;
- allocator claim: `seqclaim-08bc2c6d4aa68947010c4ece`.
