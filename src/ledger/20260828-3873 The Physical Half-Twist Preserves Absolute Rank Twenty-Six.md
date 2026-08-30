---
authors:
  - marici.Benincasa
date: 2026-08-28
---
# 3873 — The Physical Half-Twist Preserves Absolute Rank Twenty-Six

## Test

The stabilized rank-26 connection had been computed with the finite-field
twist parameter set to (\gamma=5). The active-conductor analysis instead
uses the physical grade

\[
\alpha=-\frac12+\epsilon.
\]

To separate an absolute rank jump from a relative wall resonance, rerun the
complete five-wall product-pole reduction at (\epsilon=0), representing

\[
\gamma=-\frac12
\]

exactly in each finite field.

At ambient relation degree 14 and cutoff degree 7, the results are

\[
\begin{array}{c|c|c|c}
p&\gamma&\dim\mathcal M_{\rm abs}&
\dim\langle\nabla^k\Omega_{\rm src}\rangle\\
\hline
32009&16004&26&26\\
65521&32760&26&26
\end{array}
\]

The source class is nonzero at both primes, and its first jet has rank three.

## Result

The physical half-twist does not enlarge the absolute five-wall module. The
wall restriction is nevertheless resonant because

\[
K|_{q=0}=R^2,
\qquad
2\alpha=-1
\]

at grade zero. Therefore the active-conductor class found in Entries
3861--3869 is not a missing twenty-seventh absolute master. It is relative
specialization data carried by the wall-collision cone.

This gives a finite separation:

\[
\text{absolute coefficient rank}=26,
\qquad
\text{conductor specialization costalk rank}=1
\]

per active labelled conductor, away from existing triangle support.

The next construction remains the same: derive the labelled specialization
map from the physical rank-26 module to that rank-one costalk and test its
Gauss--Manin compatibility. Enlarging the absolute basis would be a mistyped
repair.

## Verification

- checker: `research/benincasa/checkers/check_rank26_physical_half_twist_absolute_rank.py`;
- packet: `research/benincasa/results/rank26-physical-half-twist-absolute-rank.json`;
- allocator claim: `seqclaim-4380e4f81869db950dc02be5`.
