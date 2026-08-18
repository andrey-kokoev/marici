---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 706 — The Homogeneous Lower Deletion Cube Localizes the Rank-Nineteen Loss

## Hard-to-vary claim

For the frozen four-pole lower family in factor order

\[
(q_{\mathfrak g_1},q_{\mathfrak g_2},q_{\mathfrak g_3},q_{\mathfrak g_{23}}),
\]

the homogeneous specialization \(P_i=X_i\) changes the proper-support
Euler grades from

\[
(7,5,5,1,5,1,1,1,5,0,1,0,1,0,1,0)
\]

to

\[
\boxed{(7,1,1,0,1,0,0,1,4,0,0,0,0,0,0,0)}.
\]

Thus the rank drop \(34\to15\) is support-localized as

\[
\boxed{19=13_{\rm single}+5_{\rm finite\ pair}+1_{\rm triple}}.
\]

This is an Euler-filtration statement. It does not identify the nearby-cycle
classes or construct the specialization/localization comparison map.

## Frozen calculation

The existing finite-field Groebner census was extended only by adding two
nonsoft homogeneous points,

\[
(X;P)=(2,3,4;2,3,4),\qquad(3,5,6;3,5,6).
\]

At both points the deletion-closed ranks are

\[
\boxed{(7,8,8,9,8,9,9,11,11,12,12,13,12,13,13,15)}.
\]

Möbius inversion on the labelled deletion cube gives the proper grades above.
The generic assertions from Entry 545 remain active in the same executable.

## Facewise loss

The single-support losses are

\[
4[q_{\mathfrak g_1}]+4[q_{\mathfrak g_2}]
+4[q_{\mathfrak g_3}]+1[q_{\mathfrak g_{23}}].
\]

Every finite pair grade disappears:

\[
q_{\mathfrak g_1}q_{\mathfrak g_2},\quad
q_{\mathfrak g_1}q_{\mathfrak g_3},\quad
q_{\mathfrak g_2}q_{\mathfrak g_3},\quad
q_{\mathfrak g_2}q_{\mathfrak g_{23}},\quad
q_{\mathfrak g_3}q_{\mathfrak g_{23}}.
\]

The parallel pair
\(q_{\mathfrak g_1}q_{\mathfrak g_{23}}\) has zero proper grade on both
sides. Of the two generic triple grades, the
\(q_{\mathfrak g_1}q_{\mathfrak g_2}q_{\mathfrak g_3}\) grade survives and
the \(q_{\mathfrak g_2}q_{\mathfrak g_3}q_{\mathfrak g_{23}}\) grade
disappears.

## Relation to the labelled normal module

Entries 185 and 698 attach the five finite pair occurrences to four radicand
types with labelled leading monomials

\[
\nu_1\nu_2,\qquad \nu_1\nu_3,\qquad \nu_2\nu_3,
\]

where the \(\nu_2\nu_3\) direction occurs on three pair supports and has two
distinct signed radicand types. Therefore the square-free normal module

\[
N_2=\langle\nu_1\nu_2,\nu_1\nu_3,\nu_2\nu_3\rangle
\]

is confined, at Euler-support level, to five pair grades that all disappear
homogeneously. The mismatch \(5\) support occurrences versus \(3\) normal
labels is essential occurrence data; it must not be collapsed into a rank
identity.

## Narrow conclusion

The lower-deletion route is not closed. It isolates the only direct home for
the square-free second-normal candidates inside the rank loss: the five
vanishing finite-pair support grades. It does not yet supply a morphism from
those five support occurrences to \(N_2\), nor from either object to the
top-sector physical localization cone.

## Evidence

- `research/benincasa/marici-gm/src/bin/generic_lower_sector_groebner_rank.rs`;
- `research/benincasa/homogeneous-lower-deletion-support.json`;
- Entries 185, 545, 698, and 705;
- allocator claim `seqclaim-82a7d5dc31fd42dfda11f63c`.

## Next falsifier

Construct the associated-grade specialization morphism on the five labelled
pair-support complexes. Test whether its second-normal symbol factors through

\[
\mathbb Q\langle
[12],[13],[23],[2,23],[3,23]
\rangle
\longrightarrow
N_2
\]

with the source-derived radicand labels and occurrence multiplicities. Only
after this map exists may its kernel, cokernel, or continuation toward the
top-sector localization cone be interpreted cohomologically.
