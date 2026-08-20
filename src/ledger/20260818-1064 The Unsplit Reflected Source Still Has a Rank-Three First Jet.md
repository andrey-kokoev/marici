---
authors:
  - marici.Nima
date: 2026-08-18
---
# 1064 — The Unsplit Reflected Source Still Has a Rank-Three First Jet

> Numbering repair (2026-08-19): relocated from filename 947 and conflicting
> heading 665 under allocator claim `seqclaim-989154be4a01d7838880f519`.
> The evidential content and scope are unchanged.

## Hard-to-vary claim

Passing from either single occurrence block to the common five-mark
chain-level relative target does not cancel the two transverse first
derivatives of the physical source.  The correctly unsplit reflected source
still has first-jet rank three.

## Common relative target

Retain all five marked denominators

\[
(q_{g_1},q_{g_2},q_{g_3},q_{g_{23}},q_{g_{31}})
\]

and form the chain-level quotient by every column missing any one of these
marks.  Pole levels one and two, the twisted exact differentials, and all
five localization transitions are retained before reduction.

At cutoff degree five, ambient homotopy degree ten, and Kummer weight five,
the resulting common relative quotient has dimension

\[
\boxed{21}.
\]

## Source-compiled unsplit numerator

The physical sum is represented without choosing a splitting:

\[
\frac1{q_{g_{23}}}+\frac1{q_{g_{31}}}
=
\frac{q_{g_{23}}+q_{g_{31}}}
{q_{g_{23}}q_{g_{31}}}.
\]

At the frozen kinematic point its numerator is \(a+b-5\).  Parameter
differentiation includes both the differentiated denominators and the
explicit derivative of this numerator.  Its class is nonzero in the common
relative quotient.

For the resulting source \(s_{\rm unsplit}\),

\[
\boxed{
\dim\langle
s_{\rm unsplit},
\nabla_xs_{\rm unsplit},
\nabla_ys_{\rm unsplit}
\rangle=3.
}
\]

Hence the reflected occurrence sum alone supplies no first-order
cancellation.

## Replication

The rank-twenty-one common target and rank-three source first jet persist

- at Kummer weights five and seven;
- after increasing ambient homotopy degree from ten to eleven.

All calculations are over \(\mathbb F_{32003}\) at
\((x,y,z)=(2,3,4)\).

## Consequence

Entry 1068 left open the possibility that the two reflected algebraic
occurrences cancel each other's transverse derivatives.  The literal
five-mark target falsifies that possibility.  Neither relative reduction
alone nor the source-prescribed reflected sum isolates a flat coefficient
line.

The missing operation must therefore contain data absent from the ordinary
product-pole complex.  The remaining source-derived candidates are the
boundary homotopy of Entry 658 and the physical-chain/Gysin morphism.  Such
data can alter the connection by a secondary term; merely adding marked
denominators cannot.

This also limits the interpretation of Entry 660: the Källén double cover
may type a coefficient cover, but its bare algebraic source does not make
the unsplit relative residue class horizontal.

## Updated frontier

Construct the connecting morphism for the chain-level sequence consisting
of the common proper-face subcomplex, the five-mark product-pole complex,
and the relative quotient.  Evaluate its kinematic commutator on the
unsplit source.  A physical rank-one line can survive only if this secondary
boundary term cancels the two independent transverse derivatives.

## Evidence

- `research/benincasa/physical_four_mark_residue_twisted_derham.py`;
- Entries 658, 660--663, and 1068.

## Outcome contract

~~~json
{
  "claim": "The reflected occurrence sum cancels the transverse first derivatives in the common relative target.",
  "status": "falsified",
  "relative_union_dimension": 21,
  "unsplit_source_nonzero": true,
  "unsplit_source_first_jet_rank": 3,
  "replications": [
    {"gamma": 5, "ambient_degree": 10},
    {"gamma": 7, "ambient_degree": 10},
    {"gamma": 5, "ambient_degree": 11}
  ],
  "next_experiment": "Compute the kinematic commutator of the source boundary homotopy in the chain-level localization sequence."
}
~~~
