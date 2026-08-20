---
title: "The Five-Site Marked Matroids Have Twelve Circuit Profiles"
date: 2026-08-20
entry: 1201
status: active-source-matroid
sector: cosmology
---

# 1201 — The Five-Site Marked Matroids Have Twelve Circuit Profiles

Sequence claim: `seqclaim-06a7eecc5e37f247c0e06e6a`.

## Frozen matroid calculation

For each of Entry 1200's 180 terms, form the exact rational matroid of its
seven, eight, or nine geometric infinity hyperplanes in

\[
\mathbf P^4.
\]

Retain on every flat both its geometric size and the total number of labelled
occurrences lying above it. Enumerate minimal dependent subsets before
constructing any Čech or weight-page differential.

## Circuit census

There are no dependent triples. Across the complete source packet:

\[
\boxed{
\begin{array}{c|c|c|c}
\text{circuit size}&\text{rank}&\text{geometric meaning}&\text{count}\\
\hline
4&3&\text{line concurrence}&650\\
5&4&\text{point concurrence}&180\\
6&5&\text{empty-intersection OS relation}&400.
\end{array}}
\]

A minimal six-circuit is dependent in the rank-five linear matroid but has
no projective intersection. It must enter the Orlik--Solomon relation ideal,
not be represented as a geometric sixfold stratum.

## Twelve profiles

The flat ranks, geometric sizes, and occurrence depths refine the three
mark-count classes into twelve exact profiles:

\[
5\text{ profiles at seven marks},qquad
6\text{ profiles at eight marks},qquad
1\text{ profile at nine marks}.
\]

Every profile count is a union of free (C_5)-orbits.

## Carrier verdict

All dependent sets are relations among the already frozen 26 source facets.
No undeclared incidence generator is needed. The nontrivial correction is
procedural: a naive simplex truncated at pair or triple level would be
wrong, just as it was at four sites. The five-site complex must include:

- line-concurrence cells from four-circuits;
- point-concurrence cells from five-circuits;
- six-circuit Orlik--Solomon relations without fictitious support cells;
- occurrence multiplicities on every geometric flat.

## Next falsifier

Build the occurrence-resolved Orlik--Solomon/Čech complex for one
representative of each of the twelve profiles. Verify (d^2=0), compute its
cohomology, and transport the result across (C_5). Only after this carrier
complex closes may branch-double-cover coefficient objects be attached.

## Artifacts

- `research/benincasa/checkers/five_site_qg_intersection_matroid.py`
- `research/benincasa/results/five-site-qg-intersection-matroid.json`
