# 3213 — The Quarter Adapter Defects Are Reduced Transverse Fibers

## Input

Entry 3210 derives the finite-field adapter divisor

\[
(4\gamma+5)^5(4\gamma+7)^7
\]

after removing the previously certified torsion factors.  At the two roots, the augmented pencil loses respectively five and seven ranks, while the source pencil remains regular.

## Claim

At each quarter root, the local Smith factors belonging to the new adapter defect are all linear.  Equivalently, the new local torsion has Cartier length one in every lost direction.

## Derivation

Let \(t\) be a local parameter at one of the quarter roots.  Write the nonunit invariant factors of the regular part of the augmented pencil as

\[
t^{e_1},\ldots,t^{e_c},
\qquad e_i\geq1.
\]

The special-fiber corank is \(c\), while the divisor valuation is

\[
e_1+\cdots+e_c.
\]

At \(\gamma=-5/4\), both quantities equal five.  At \(\gamma=-7/4\), both equal seven.  Since every \(e_i\) is positive, equality of the sum with the number of summands forces

\[
e_1=\cdots=e_c=1.
\]

Therefore the local modules are, on the finite-field packets,

\[
\bigl(R/(4\gamma+5)\bigr)^5
\]

and

\[
\bigl(R/(4\gamma+7)\bigr)^7,
\]

up to direct sums with modules supported on the already separated factors and a locally free part.

## Consequence

The quarter supports are not infinitesimal thickenings and do not carry a higher local Jordan chain in the exponent direction.  Any explanation of multiplicities five and seven must account for that many independent transverse readout directions, rather than one direction with Cartier lengths five or seven.

This narrows the next mechanism test.  A fitted interpretation such as “five marks plus two base directions” is still unauthorized, but it can now be tested as a decomposition of reduced defect fibers rather than as a statement about torsion thickness.

## Scope

This is an exact local-algebra consequence of the finite-field packet in Entry 3210.  Its characteristic-zero promotion remains conditional on the exact rational certificate requested there.

Ledger number authority: `seqclaim-99f652c938442caa763c7676`.
