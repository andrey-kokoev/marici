# A minimal complementary probe for the Cut-null sector

## Question

Can the known Cut-null elliptic extension sector be equipped with a minimal complementary probe that detects both unresolved parity bits and respects site exchange?

## Claim boundary

This constructs the unique finite algebraic probe type up to exchanging wall labels. It does not identify the probe with an existing detector or physical current.

## Null sector

The unresolved integral extension classes form

\[
K=\mathcal A_{--}/2\mathcal A_{--}
\cong(\mathbb Z/2)^2,
\]

with labelled coordinates

\[
(a,b)
\]

from

\[
2m=a e_6+bv_{\rm alg}.
\]

The established physical Cut map restricts to zero on this elliptic coinvariant information:

\[
q_{\rm Cut}|_K=0.
\]

## Complementary probe

Define

\[
q_\perp:K\longrightarrow(\mathbb Z/2)^2,
\qquad
q_\perp(a,b)=(a,b).
\]

Then

\[
(q_{\rm Cut},q_\perp):K
\longrightarrow
0\oplus(\mathbb Z/2)^2
\]

is injective. The complementary channel is therefore jointly faithful with the null Cut channel, and two binary outputs are minimal: no map from the four-element set \(K\) to one binary coordinate can be injective.

## Conductor realization

The two conductor factors have parity characters

\[
\ell_1=(1,0,1),
\qquad
\ell_2=(0,1,1).
\]

For a conductor class represented by \(v\in\mathbb Z^3\), define its syndrome

\[
s(v)=\bigl(\ell_1v,\ell_2v\bigr)\pmod2.
\]

This descends to an isomorphism

\[
\operatorname{coker}J\xrightarrow{\sim}(\mathbb Z/2)^2.
\]

Thus a candidate comparison sends the cusp extension coordinates \((a,b)\) to the two wall syndromes.

## Exchange constraint

Let site exchange swap both coordinates. Among invertible linear maps

\[
K\longrightarrow(\mathbb Z/2)^2
\]

that commute with this swap, exactly two remain: the identity and the swap itself. They differ only by relabelling the two walls.

Hence exchange symmetry reduces the six possible abstract isomorphisms to one comparison type up to wall-label reversal. A source orientation or ordered global thimble marking would select between the two representatives.

## Physical interpretation gate

The outputs of \(q_\perp\) are parity syndromes, not raw detector counts and not temporal states. A physical realization would need two calibrated binary observables whose joint kernel on \(K\) is zero and whose site exchange matches the wall swap.

No existing Aspect packet supplies these observables. The construction gives their exact algebraic contract:

1. each output is binary;
2. the pair is jointly faithful on the four extension classes;
3. site exchange swaps the outputs;
4. the known Cut channel remains zero on this sector.

## Disposition

A minimal complementary probe for the null sector exists algebraically and is unique up to wall exchange. The unresolved step is to realize its two syndrome coordinates by source-derived physical observables or by the missing ordered Picard-thimble pairings.
