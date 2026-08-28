# Deutschean Conjecture: Two-Adic Authority and the Center Eight

## Conjecture

Let the nonzero order-two Moore filling class be represented by the
three-generator signed source packet. The conjecture was:

1. the order-two source relation uniquely authorizes the 2-adic valuation
   observer;
2. the three signed source ports force the conductor center \(2^3=8\);
3. therefore

\[
\kappa_C(\omega)=4(8-\omega)
\]

is explained by source structure rather than merely recovered from its two
values.

This is deliberately stronger than the exact affine identity. It asserts a
constructor for the observer and a constructor for the center.

## Hostile 1: alternative prime observers

The conductors are

\[
\kappa_C(+1)=28=2^2\cdot7,
\qquad
\kappa_C(-1)=36=2^2\cdot3^2.
\]

The 2-adic observer is blind, but the 3-adic and 7-adic observers distinguish:

\[
\begin{array}{c|cc}
&C_+&C_-\\
\hline
v_2&2&2\\
v_3&0&2\\
v_7&1&0.
\end{array}
\]

Order two makes \(v_2\) relevant to the filling quotient. It does not by
itself authorize \(v_2\) as the exclusive observer of the integral response.
The frozen packet contains no such authority map.

## Hostile 2: center ambiguity

Several typed source counts are immediately available:

\[
\begin{array}{c|c|c}
\text{source feature}&r&2^r\\
\hline
\text{signed generator ports}&3&8\\
\text{Moore faces}&4&16\\
\text{nonrepeated tail ports}&2&4\\
\text{commutator nesting depth}&2&4.
\end{array}
\]

No declared constructor selects the first count and rejects the others.
Consequently the statement that source combinatorics forces \(8\) is
underdetermined.

## Hostile 3: cross-stratum universality

The endpoint strata have the same order-two class and three-generator source,
but their extension moduli are

\[
\mu_{A_+}=505222245120,
\qquad
\mu_{A_-}=606017838336.
\]

They do not satisfy the proposed universal three-port conductor law. The
center-eight law is therefore \(C\)-stratum-specific, not a universal
consequence of order two plus three source generators.

## Disposition

The Deutschean conjecture is falsified.

The exact survivor is:

\[
\kappa_C(\omega)=4(8-\omega)
\]

on the bounded legal \(C\) stratum. Its explanatory promotion remains blocked
by two missing constructors:

1. a two-primary observer-authority map from the order-two filling relation to
   the \(v_2\) port, explicitly scoped to the homotopy quotient;
2. a \(C\)-stratum center selector deriving \(8\) from deletion and Artin data
   before evaluating either conductor value.

Until those maps exist, \(8-\omega\) is an exact compressed law but not yet a
source explanation.

## SCC compilation

The result packet follows the Stratified Coherence Compiler stages:

- packet: the legal signed eta-squared census over the integers;
- stratum: \(C_\pm\), with \(A_\pm\) retained as a hostile;
- ports: full matrix, integral Smith packet, and \(v_2,v_3,v_7\);
- static coherence: affine identity passes, exclusive authority and center
  selection fail;
- dynamic coherence: not invoked because no parameterized process is claimed;
- hostiles: alternative primes, competing center counts, and endpoint
  universality;
- admission: exact identity only, with two missing constructors.

## Replay

Run:

    python research/strominger/checkers/deutschean_two_adic_source_selection_checks.py

The checker verifies seven of seven hostile-disposition gates.
