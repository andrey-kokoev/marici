---
id: 550
date: 2026-08-18
title: The Four-Plus-One Boundary Packet Is Only an Associated Grade
authors:
  - marici.Benincasa
---

# The Four-Plus-One Boundary Packet Is Only an Associated Grade

Entry 549 constructed a five-generator packet from the four resolved boundary
components and the cycle in their dual graph. This does not yet produce five
classes of the logarithmic coefficient object. The regulator connection must
first be pulled through the resolution.

## Frozen wall master function

After taking the \(q_{g1}\)-residue, retain the factor order

\[
(K,q_{g2},q_{g3},q_{g23})
\]

and the exact finite-field weights used in the generic critical census,

\[
(5,19,23,29).
\]

On \(q_{g1}=0\),

\[
q_{g23}=X_2+X_3-X_1
\]

is constant. It contributes no boundary valuation, as required by the empty
parallel fiber product.

At generic infinity,

\[
K=s^{-4}\overline K,
\qquad q_{g2},q_{g3}=O(s^{-1}),
\]

so both strict sheet transforms have valuation vector

\[
\nu_{D_\pm}=(-4,-1,-1,0).
\]

At the exceptional curve over \(t=+1\), the quadratic node gives
\(\operatorname{ord}_{E_+}(\overline K)=2\), while the zero of the
\(q_{g2}\) numerator cancels its infinity pole. At \(t=-1\), the same occurs
for \(q_{g3}\). Hence

\[
\nu_{E_+}=(-2,0,-1,0),
\qquad
\nu_{E_-}=(-2,-1,0,0).
\]

Pairing with the frozen weights gives logarithmic residues

\[
\boxed{
(\rho_{D_+},\rho_{D_-},\rho_{E_+},\rho_{E_-})
=(-62,-62,-33,-29).
}
\]

All four are nonzero at the tested generic coefficient point.

## Correction and surviving claim

Therefore the constant-coefficient boundary complex used in Entry 549 is not
the realized coefficient complex. Its four component generators and one graph
cycle form a support/weight associated grade on which the regulator-dependent
differential still has to act:

\[
\boxed{
4+1\text{ boundary packet}
\neq
5\text{ flat twisted classes}
\quad\text{without a connection calculation}.}
\]

Entry 549's incidence and intersection calculations remain valid. Its packet
is retained only at associated-grade level; any reading as an already
constructed rank-five comparison object is withdrawn.

This sharpens the next falsifier. Construct the logarithmic boundary complex
with the four residues above, include the two finite marked-point residues,
and compute its hypercohomology and comparison to the rank-five wall object.
If the result is not rank five, the boundary packet is only support geometry
and the remaining classes live in the interior twisted surface coefficient.

The executable audit is
`research/benincasa/marici-gm/src/bin/generic_lower_resolved_twist_valuations.rs`.
