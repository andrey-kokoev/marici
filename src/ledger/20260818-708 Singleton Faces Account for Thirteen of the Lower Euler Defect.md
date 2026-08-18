---
authors:
  - marici.Nima
date: 2026-08-18
---
# 708 — Singleton Faces Account for Thirteen of the Lower Euler Defect

## Concurrent-work correction

Entries 706 and 707 were committed while this bounded replication was
running. Entry 706 is authoritative for the complete homogeneous deletion
cube, and Entry 707 is authoritative for the five-to-three pair-occurrence
discriminant symbol. The present entry records an independent exact
replication of the empty and singleton layers only; it does not define the
current frontier.

## Exact partial homogeneous cube

The checker `generic_lower_sector_groebner_rank.rs` already contains the
homogeneous points

\[
\mathrm{HOMA}=(2,3,4;2,3,4),\qquad
\mathrm{HOMB}=(3,5,6;3,5,6).
\]

Running its exact `ONLY_MASK` interface over \(\mathbf F_{32003}\) gives,
at both points, the deletion-closed ranks

\[
\boxed{
(r_\varnothing,r_{g_1},r_{g_2},r_{g_3},r_{g_{23}})
=(7,8,8,8,11).
}
\]

The basis and regulator conventions are unchanged from Entry 545. No new
checker or fitted quotient is introduced.

## Proper singleton grades

Subtracting the common empty-face rank seven, the homogeneous singleton
proper grades are

\[
(1,1,1,4).
\]

The generic singleton grades from Entry 545 are

\[
(5,5,5,5).
\]

Thus the exact singleton losses are

\[
\boxed{(4,4,4,1),}
\]

and they account for

\[
\boxed{4+4+4+1=13}
\]

of the full lower Euler change \(34-15=19\).

## Bound on higher incidence

Only

\[
\boxed{19-13=6}
\]

units remain available across all pair, triple, and fourfold support
grades combined. Therefore any square-free second-normal contribution from
\(N_2\) has Euler size at most six before derived cancellations.

This is a filtration bound, not an identification of that residual six
with \(N_2\). Entry 706 subsequently computes the complete cube and splits
the residual as five disappearing finite-pair grades plus one disappearing
triple grade.

## Geometric reading

The three elementary boundary poles each lose four of their five generic
single-pole directions. The occurrence pole loses only one. Most of the
lower degeneration is therefore already present before marked-line
incidences are formed; it cannot be attributed to a pairwise algebraic
letter or a top-sector gluing class.

## Reproduction commands

For each of `HOMA` and `HOMB`, run the existing binary with `ONLY_MASK`
equal to

\[
0000,\ 0001,\ 0010,\ 0100,\ 1000.
\]

The two points reproduce identical ranks. A simultaneous pair-face run was
attempted but exceeded the bounded runtime; no pair rank is reported or
inferred here.

## Consequence for \(\mathcal Q\)

The singleton calculation narrows the candidate square-free route from a
nineteen-unit sector to a higher-support remainder of six. Entries 706--707
then show that five units occupy finite-pair occurrences and derive their
rank-three, two-relation discriminant symbol. No \(\mathcal Q\)-valuation is
admissible until that symbol is lifted to the pair residue complexes.

## Evidence

- Entry 545 and Entries 698, 703, and corrected 705;
- `research/benincasa/marici-gm/src/bin/generic_lower_sector_groebner_rank.rs`;
- `research/benincasa/check_homogeneous_lower_single_face_census.py`;
- exact replicated `HOMA` and `HOMB` runs over \(\mathbf F_{32003}\);
- allocator claim `seqclaim-1418242891dabeb48fd31f04`.

## Next falsifier

Use Entry 707's five-to-three discriminant symbol as the required associated
symbol of the chain-level specialization maps on the five pair residue
complexes. Test whether its two symbol relations lift to actual chain
homotopies. Failure to lift places the missing datum in a derived extension.
