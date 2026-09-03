# Sectorwise coercivity certificates for the physical return

## Question

Can the uniform relative coercivity target be decomposed into independently checkable wall, history, tail, and PV-reciprocal estimates?

## General sector certificate

Suppose the normalized physical coupling has a source-derived decomposition

\[
T_p=A_p^{-1/2}C_pD_p^{-1/2}
=
\sum_{s\in S}T_{p,s},
\]

where every summand descends to the same reduced supports. If

\[
\|T_{p,s}\|\le q_s
\]

uniformly over primes, then

\[
\|T_p\|\le q:=\sum_{s\in S}q_s.
\]

Hence \(q<1\) proves relative block coercivity with \(\eta=1-q\), and gives

\[
1-\|K_p\|\ge1-q^2.
\]

This certificate is insensitive to uncontrolled sector phases because it does not rely on cancellation.

## Orthogonal-sector improvement

If the source decomposition additionally proves cross-Gram orthogonality

\[
T_{p,s}T_{p,t}^*=0
\qquad(s\ne t),
\]

then

\[
T_pT_p^*=\sum_sT_{p,s}T_{p,s}^*,
\qquad
\|T_p\|^2\le\sum_sq_s^2.
\]

If the positive operators \(T_{p,s}T_{p,s}^*\) also have orthogonal supports, the bound sharpens further to

\[
\|T_p\|\le\max_sq_s.
\]

These improvements require proved orthogonality in the physical normalized inner products. Labels such as wall, tail, or PV do not imply it.

## Hostile alignment

Without cross-sector orthogonality, coherent alignment saturates the triangle bound. Two sectors acting on the same normalized direction with strengths \(1/2\) and \(1/3\) produce total strength \(5/6\). Any root-sum-square estimate would be false for that allowed alignment.

Conversely, sectors of strengths \(1/2\) and \(2/3\) on orthogonal source and target directions have total norm \(2/3\), not \(7/6\). Thus a genuine support theorem can turn a failed triangle certificate into strict confinement.

## Source audit target

For each physical sector, the constructor must provide:

1. a map on the same reduced supports;
2. a prime-uniform normalized norm bound;
3. every claimed cross-Gram zero or orthogonal support relation.

If the sum of certified bounds is below one, no phase or Markov theorem is needed. If it is not, the next admissible route is a proved orthogonal decomposition or a direct full-block estimate, not assumed cancellation.

## Verification

`research/aspect/checkers/check_sectorwise_return_bounds.py` verifies an orthogonal-support maximum bound and an aligned triangle-bound saturation with exact rational diagonal maps.

## Disposition

Uniform physical coercivity has a modular sufficient certificate. Current source packets do not yet supply sector maps or normalized bounds, so the certificate is a typed acceptance test rather than a confinement proof.
