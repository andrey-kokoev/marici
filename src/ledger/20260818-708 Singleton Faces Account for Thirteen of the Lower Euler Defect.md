---
authors:
  - marici.Nima
date: 2026-08-18
---
# 708 — Singleton Faces Account for Thirteen of the Lower Euler Defect

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

This is a filtration bound, not yet an identification of that residual six
with \(N_2\). The complete homogeneous deletion cube is still required.

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

The candidate square-free route has narrowed from a nineteen-unit sector to
an unresolved higher-support remainder of at most six. No
\(\mathcal Q\)-valuation is admissible until the pair and triple faces are
computed and Möbius-inverted.

## Evidence

- Entry 545 and Entries 698, 703, and corrected 705;
- `research/benincasa/marici-gm/src/bin/generic_lower_sector_groebner_rank.rs`;
- `research/benincasa/check_homogeneous_lower_single_face_census.py`;
- exact replicated `HOMA` and `HOMB` runs over \(\mathbf F_{32003}\);
- allocator claim `seqclaim-1418242891dabeb48fd31f04`.

## Next falsifier

Compute the six homogeneous pair faces individually with bounded runs and
Möbius-invert them against \((7;8,8,8,11)\). If their cumulative proper
loss exhausts the residual six without a square-free conormal initial form,
the direct \(N_2\) route closes. Otherwise retain only the explicitly
labelled surviving pair grades for the derived comparison.
