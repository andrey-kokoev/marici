# 1782 — The Six Five-Site Threshold Orbits Assemble Thirty Morse Lines

## Inputs

Entry 1236 proves that every compatible labelled pair belongs to a free
(C_5)-orbit. Entry 1238 isolates exactly six free disjoint-cut mixed-pair
orbits. Entries 1777–1780 prove that each representative produces a distinct
degree-six divisor whose generic critical point has nonzero transverse
Hessian.

No occurrence labels are identified.

## Local coefficient object

At a generic smooth point of any one of the six divisors, the nonzero
transverse Hessian gives a holomorphic Morse critical point. Its reduced local
vanishing-cycle space is therefore a rank-one line (W_r):

\[
\dim W_r=1,
\qquad r=1,\ldots,6.
\]

This is an algebraic/local coefficient statement. Entry 1781 separately shows
that the literal positive physical chain does not activate these lines.

## Labelled cyclic assembly

Because each source occurrence orbit is free, its coefficient object is the
regular representation

\[
\mathbb Q[C_5]\otimes W_r.
\]

Consequently all six assemble as

\[
\boxed{
\mathcal V_{\rm disj}
=
\bigoplus_{r=1}^{6}\mathbb Q[C_5]\otimes W_r,
\qquad
\dim_{\mathbb Q}\mathcal V_{\rm disj}=30.
}
\]

Its cyclic character is

\[
\boxed{
\chi_{\mathcal V_{\rm disj}}=(30,0,0,0,0).
}
\]

Over (mathbb Q),

\[
\mathcal V_{\rm disj}
\simeq
6\bigl(\mathbb Q_{\rm triv}\oplus\mathbb Q(\zeta_5)\bigr).
\]

## Narrow conclusion

The new five-site coefficient support is not six unlabelled scalar divisors.
It is thirty occurrence-resolved local Morse lines arranged in six regular
(C_5)-orbits. Any global source connection, nearby-cycle comparison, or
physical contour map must preserve this character.

Collapsing a cyclic orbit to its scalar equation would discard four fifths of
the labelled coefficient object and is not authorized by cyclic invariance
alone.

## Next falsifier

Construct the analytically continued source relative-cycle map for one
labelled representative. If it exists, test cyclic naturality before
transporting it to the remaining 29 occurrences. If the source does not fix
the continuation path or sheet, retain the rank-30 algebraic coefficient
object while classifying its physical activation as unselected.

## Provenance

- Entry 1236: free (C_5)-orbit census
- Entry 1238: six disjoint-cut mixed-pair orbits
- Entries 1777–1780: elimination, saturation, and Hessian certification
- Entry 1781: literal-chain support test
- allocator claim: `seqclaim-d5c9699b629108611706ddea`
