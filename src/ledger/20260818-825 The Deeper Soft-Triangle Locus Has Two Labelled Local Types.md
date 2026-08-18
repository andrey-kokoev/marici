---
authors:
  - marici.Nima
date: 2026-08-18
---
# 825 — The Deeper Soft–Triangle Locus Has Two Labelled Local Types

## Support equations

The degeneration left open by Entries 813 and 824 lies on

\[
a_0=b_0=0,\qquad
P_3=0,qquad
E^2=P_1^2\ \text{or}\ E^2=P_2^2,qquad
P_1^2=P_2^2.
\]

The marked-coordinate equations split its eight collision orbits into two
different local types.

## Movable one-scale branches

For

\[
(g_1,g_2),qquad(g_1,g_3),qquad(g_2,g_3),
\]

neither marked coordinate forces (E=0).  After reduction, the deeper
branches are

\[
P_3=0,qquad P_2=sP_1,qquad E=rP_1,qquad r,s\in\{+1,-1\}.
\]

There are four branches per occurrence.  The original choice of whether the
signed condition was written with (P_1) or (P_2) does not double this
count once (P_1^2=P_2^2) is imposed.  Thus

\[
3\text{ orbits}\cdot3\text{ occurrences}\cdot4=36
\]

labelled one-scale strata.

## Forced all-soft points

Each of the other five collision orbits contains a marked coordinate
(-E).  Its double boundary forces (E=0).  Combining this with the signed
and triangle conditions gives

\[
E=P_1=P_2=P_3=0.
\]

All sign branches coalesce into one reduced all-soft point per occurrence:

\[
5\text{ orbits}\cdot3\text{ occurrences}=15
\]

labelled points.

## Aggregate support representation

The reduced labelled support therefore contains

\[
\boxed{36+15=51}
\]

strata, arranged as seventeen free (C_3)-families.  Its permutation
character is

\[
\chi_{\rm supp}=(51,0,0).
\]

## Consequence

The two types must not be assigned a common vanishing rank.  The one-scale
branch retains a nonzero momentum scale; the all-soft point has all
kinematic scales collapsed and may carry additional grading or nonisolated
directions.

The local workload is therefore finite: compute one logarithmic transverse
complex for the movable one-scale type and one for the forced all-soft type.
Only afterward may their ranks be transported through the seventeen cyclic
families.

## Scope

This is a reduced labelled-support census.  It does not infer Milnor ranks,
Tor lengths, coefficient multiplicities, or physical-chain activation.

## Verification

- checker: `research/nima/audit_deeper_soft_triangle_occurrences.py`;
- packet: `research/nima/deeper-soft-triangle-occurrences.json`;
- allocator claim: `seqclaim-6ee5d702fe835f4da6047a9d`.
