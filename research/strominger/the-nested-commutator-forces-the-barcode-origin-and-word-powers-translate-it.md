# The Nested Commutator Forces the Barcode Origin and Word Powers Translate It

## Source factorization

Write the eta-squared word as

\[
W=[U,V],
\qquad
U=[c_{31},c_{13}],
\qquad
V=[c_{31},c_{22}].
\]

Under the reflection response, both inner commutators satisfy

\[
R_U-I\in4M_4(\mathbb Z),
\qquad
R_V-I\in4M_4(\mathbb Z),
\]

and neither difference is divisible by eight. Thus both enter at exact
two-adic depth two.

Let

\[
A=(R_U-I)/4,
\qquad
B=(R_V-I)/4.
\]

Their leading grades commute modulo two:

\[
[A,B]=0\pmod2.
\]

The ordinary depth-four leading term of the outer commutator therefore
vanishes. The first surviving response occurs at depth five, where

\[
\frac{R_W-I}{32}\equiv
\begin{pmatrix}
1&1&1&1\\
1&1&1&1\\
1&1&1&1\\
1&1&1&1
\end{pmatrix}
\pmod2.
\]

This is the rank-one gauge map. The source word therefore creates common
translation response before it creates relational response. Quotienting the
gauge line removes this entire leading grade and delays the first quotient
Smith depth from five to seven.

## Counterfactual word composition

Let \(W^m\) denote source-authorized repetition of the same residue word and
let \(R\) be the response of \(W\). Then

\[
R^m-I=(R-I)(I+R+\cdots+R^{m-1}).
\]

Since \(R\equiv I\pmod{32}\), if \(s=v_2(m)\), the geometric sum is \(2^s\)
times an invertible matrix over \(\mathbb Z_2\). Consequently every nonzero
two-primary Smith depth shifts by exactly \(s\):

\[
(5,9,13)\mapsto(5+s,9+s,13+s),
\]

and

\[
(7,12)\mapsto(7+s,12+s).
\]

The derived barcode retains its shape and translates rigidly by \(v_2(m)\).
Odd repetition leaves its location unchanged.

## Explanatory status

This supplies both pieces of Deutsch's test:

1. the origin at depth five is forced by nested-commutator cancellation in
   the associated graded response;
2. an authorized counterfactual operation, word repetition, moves the entire
   barcode by a predicted amount.

The remaining finer question is to derive the later depths nine, twelve and
thirteen directly from higher associated-graded commutator terms, without
using maximal-minor Smith computation.

## Replay

```powershell
python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py
```
