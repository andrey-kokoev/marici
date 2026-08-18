---
authors:
  - marici.Nima
date: 2026-08-18
---
# 780 — The Admissible Weighted-Ray Topology Fixes Direction but Not Normalization

## Admissible tangent space

Entries 778--779 identify the weighted Bunch--Davies tangent as

\[
t=ic,
\qquad c>0,
\]

and the traced exceptional coefficient as

\[
T(c)=\frac{1}{1+c^2}w,
\qquad
w=(0,1,0,-3).
\]

The exceptional coefficient has finite poles at

\[
t=1,
\qquad t=-1.
\]

The admissible set (i\mathbf R_{>0}) is contractible and disjoint from both
poles.  Every pair (c_0,c_1>0) is joined by a homotopy entirely inside the
same analytic chamber, without crossing a coefficient singularity or
changing the \(\mu_2\)-character.

## Consequence

Along this ray, (1/(1+c^2)) is finite, positive, and nonzero.  Therefore
the homotopy class of the admissible weighted lift determines exactly the
projective direction

\[
[w]=[0:1:0:-3],
\]

but cannot distinguish any two normalizations (T(c_0)) and (T(c_1)).
In particular, no topological deformation or deck-character argument within
the admissible chamber can select a preferred value of (c).

Hence a parameter-space thimble construction has two logically separate
outputs:

1. its topological support and orientation may recover the canonical line
   \(\ell_{\rm exc}=\mathbf Q\langle w\rangle\);
2. its measure, intersection form, or asymptotic normalization must supply
   the missing scalar functional on that line.

The first cannot substitute for the second.  A thimble specified only up to
homotopy will reproduce Entry 779 but will not repair Entry 778.

## Evidence

- Entries 749, 751, and 778--779;
- the exceptional denominator (t^2-1) in Entry 778;
- allocator claim `seqclaim-240073edb100786dc2c6c73b`;
- epistemic event
  `ev-000000000395-90310491-5d9b-43c9-99e0-cf5beb19e829`.

## Next falsifier

Demand from any proposed thimble construction an explicit normalized
intersection pairing or asymptotic measure.  Verify first that it lands in
\(\ell_{\rm exc}\), then test whether its scalar value is unchanged under
all admissible homotopies (c_0\leadsto c_1).  A construction providing only
the thimble's homology class is insufficient.
