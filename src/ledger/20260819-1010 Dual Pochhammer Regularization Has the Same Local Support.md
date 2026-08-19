# 1010 — Dual Pochhammer Regularization Has the Same Local Support

## Local dualization

Entry 1009 showed that the frozen KLT contraction does not itself provide the
dual regularization map required by the minus-recombination chamber cochain.
The primary twisted-cycle construction nevertheless fixes the local effect of
dualization.

For a rank-one local system with monodromy (M), the local Pochhammer closure
coefficient is

\[
c(M)=\frac{1}{M-1}.
\]

The dual local system has monodromy (M^{-1}).  Therefore

\[
\boxed{
c(M^{-1})
=\frac{1}{M^{-1}-1}
=-\frac{M}{M-1}
=-M c(M).
}
\]

In the Laurent coefficient ring

\[
\mathbb Q[M,M^{-1},(M-1)^{-1}],
\]

the factor (-M) is a unit.  Hence primal and dual Pochhammer regularization
have exactly the same resonance divisor and local valuation.

## Consequence for the minus primitive

The passage from the chain variance used in Entry 949 to the required dual
variance cannot by itself create or remove support on any recombination edge:

\[
\boxed{
\operatorname{Supp}c(M^{-1})
=
\operatorname{Supp}c(M)
=V(M-1).
}
\]

Thus the unresolved Betti status in Entries 1007 and 1009 is narrower than an
unknown local regularization problem.  The local dual coefficient is fixed.
What remains unconstructed is the global assembly that assigns these local
coefficients to the labelled chamber cochain:

- the chain/cochain intersection pairing;
- incidence and residue-orientation signs;
- the identification of the six chamber vertices with the dual twisted-cycle
  basis;
- compatibility with the occurrence transition of Entry 974.

Any genuine obstruction must live in this global pairing/incidence packet, not
in a new local divisor or a different local pole order.

## Scope

This does **not** prove Betti exactness.  Multiplication by the local units
(-M_e) need not preserve a global coboundary unless the vertex-edge incidence
and pairing are transported coherently.  Applying the unit independently on
each edge would be another fitted map.

## Next falsifier

Construct the occurrence-labelled dual incidence matrix.  Each edge column
must carry the source-forced coefficient (-M_e/(M_e-1)) and the independently
derived residue orientation.  Test whether the Entry 1002 primitive maps to a
global dual coboundary.  Failure after this fixed assembly would be the first
genuine Betti-lattice obstruction in the minus recombination sector.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_dual_pochhammer_unit.rs`;
- packet:
  `research/benincasa/string-six-point-dual-pochhammer-unit.json`;
- primary source:
  Mizera, *Combinatorics and Topology of Kawai–Lewellen–Tye Relations*,
  arXiv:1706.08527;
- allocator claim:
  `seqclaim-2b10fe2fde0d9433abe7c644`.
- epistemic event:
  `ev-000000000629-d87a9fec-a84c-4260-9481-f1d88c0b7331`.
