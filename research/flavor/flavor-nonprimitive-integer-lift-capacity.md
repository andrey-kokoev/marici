# Nonprimitive integer lift capacity: WP1036

## Question

Does the nonprimitive WP802 integer family contain an arithmetically compatible
pole packet?

## Exact capacity point

For \(h(C,k)=C\,12\pi^2/(1367k)\), the first nonprimitive slice \(k=2\)
contains

\[
(N_C,N_F,C)=(40,222,23),\qquad
h=\frac{138\pi^2}{1367}\approx0.99634.
\]

Using exact rational upper and lower bounds on \(\pi\), the checker proves this
value lies strictly inside the fitted \(h\)-interval. On the same slice,
\(C=22\) lies below and \(C=24\) lies above. Thus \(C=23\) is unique at
\(k=2\).

## Contextual partition and instrument

At fixed \(k=2\), the integer coefficients partition into \(C\le22\), one
compatible point \(C=23\), and \(C\ge24\). This establishes arithmetic
capacity, not source selection: the source currently provides no theorem that
chooses \(k=2\) or derives the multiplicity \(23\). Threshold transport and a
physical16 instrument remain unestablished.

## Claim boundary

The uniqueness statement is only within the \(k=2\) positive-integer slice.
It supplies no authority for choosing that slice or its coefficient.

## Disposition

Progressive capacity. A compatible integer lift exists, but it is a fitted
arithmetic coincidence until one anomaly-complete representation independently
derives both \(k=2\) and \(C=23\) in a typed pole operator.

Checker: research/flavor/checkers/wp1036_nonprimitive_integer_lift_capacity.py

Result: results/wp1036_nonprimitive_integer_lift_capacity.json
