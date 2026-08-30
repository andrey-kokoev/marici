# Parity-groupoid relative-reference theorem

## Bounded question

What does the categorical form of WP630 permit that the scalar-potential
formulation obscures? In particular, can a legal source construction replace
the impossible absolute sign selector by a descended relative observable?

## Original action groupoid

Let the two sign-related entrance vacua be \(X=\{+1,-1\}\), with the sector
parity group \(G=Z_2\) acting by sign reversal. The physical presentation is
the action groupoid \(X\mathbin{//}G\). A probe descends precisely when it is
constant on each isomorphism class.

The action is transitive, so the quotient has one isomorphism class. Exhaustive
enumeration of all Boolean probes gives two descended probes, both constant,
and two sign-separating probes, neither descended. Write \(D\) for the
descended probes and \(S\) for the sign separators. Then

\[
D\cap S=\varnothing.
\]

This is the categorical core of WP630. An explicit odd source does not repair
descent; it exits the original morphism class.

## Relative-reference extension

Add a second odd source object with state \(r\in\{+1,-1\}\). On
\(X\times R\), let \(G\) act diagonally:

\[
(x,r)\longmapsto(-x,-r).
\]

The extended action groupoid has two isomorphism classes, distinguished
exactly by

\[
I(x,r)=xr.
\]

The invariant \(I\) is jointly faithful on the two relative classes. Forgetting
the reference sends both classes to the single original class, so no inverse
construction recovers \(I\) from the original experiment. The reference port
creates a relative observable; it does not reveal an absolute sign.

## Categorical factorization

There are therefore only two typed routes:

1. an odd wall-lifting operation leaves the original parity-equivariant
   category and forfeits exact protection;
2. a source-derived odd reference enlarges the state object, after which the
   diagonal quotient admits the relative invariant \(I\).

The second route is constructive but changes the physical groupoid. If the
diagonal parity is gauged, simultaneous sign reversal is gauge, while the
relative class remains physical. That successor must still derive the
reference field, its coupling, its prepared relation, discrete-gauge anomaly
freedom, and the resulting defect spectrum. Algebraic existence of \(I\) is
not executable control or an instrument.

## Disposition

Category theory sharpens the branch structure and identifies a genuine
window: replace absolute sign selection by source-derived relative-class
selection in a new diagonal stabilizer groupoid. It does not by itself supply
the reference constructor. On the current connector source, WP629 remains a
presentation rigidifier and no numerical `physical16` selector follows.

The next bounded test is whether an already admitted odd field can serve as
the reference without importing a fitted orientation or reopening the
eighteen-coordinate RG debt.

## Reproduction

Run:

    python research/flavor/checkers/wp631_parity_groupoid_relative_reference.py

The generated result is
`research/flavor/results/wp631_parity_groupoid_relative_reference.json`.
