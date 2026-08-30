# 1864 — The Homogeneous Five-Site Slice Excludes Every Active-Soft Endpoint

## Frozen compatibility equation

For the active region-pair representative

\[
g_{123}=g_{125}=0,
\]

eliminating the common homogeneous site-energy scale requires

\[
y_3+y_5-y_2-y_4=0.
\]

On the homogeneous five-site physical slice, the edge energies are the
Euclidean distances from the loop point to the five fixed polygon vertices.
At a soft endpoint the loop point is one of those vertices.

## Certified endpoint census

Exact rational interval arithmetic gives the signs of the compatibility
mismatch at the four active soft endpoints:

\[
(+,-,+,-).
\]

Every interval excludes zero.  Numerically, the four mismatch intervals are
centered near

\[
2.25018,qquad -0.255873,qquad 0.255873,qquad -2.25018.
\]

Hence none of the four active-soft endpoints lies on the homogeneous
five-site slice.

## Narrow result

The coefficient-zero rays and the third-Rees acceptance formula of Entries
1860--1863 describe a valid boundary type of the dehomogeneous source family,
but that boundary type is not activated by the homogeneous five-site physical
specialization.

This is an exclusion result, not a proof that the dehomogeneous boundary is
empty.  It introduces neither a new carrier stratum nor a physical higher-Rees
class.

## Consequence

The present active-soft branch cannot answer the homogeneous five-site loop
question.  Continuing it requires an independently justified dehomogeneous
physical specialization and its source-fixed normal current.  Without that
input, the correct action is to retain the endpoint formula as a conditional
coefficient test and redirect the homogeneous search.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_homogeneous_active_soft_exclusion.py`
- `research/benincasa/results/five-site-region-pair-homogeneous-active-soft-exclusion.json`
- Entries 1851 and 1860--1863
- allocator claim: `seqclaim-e5fc0ff13254980efde0102c`
