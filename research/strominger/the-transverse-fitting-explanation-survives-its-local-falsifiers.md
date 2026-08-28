# The transverse Fitting explanation survives its local falsifiers

## Falsifiers

The period-(729) explanation made three vulnerable claims:

1. the order-eleven maximal-minor change is the genuine first derivative of the determinant;
2. the effect is exterior-power invariant rather than one preferred-minor artifact;
3. the shift acts selectively near a deeper Fitting stratum rather than changing every grade indiscriminately.

All three were tested exactly.

## Linearized determinant

Write the grade-(152) full matrix and its perturbation as

\[
M=3^2B,qquad
M'=M+3^7H.
\]

For every (3\times3) row minor,

\[
\det(M')-\det(M)
=
3^{11}D\det_B(H)
+O(3^{16}).
\]

The four linearized Plücker coordinates are

\[
D\det_B(H)equiv(2,2,2,2)\pmod3.
\]

The exact normalized minor differences are also

\[
(2,2,2,2)\pmod3,
\]

and the higher-order residual is zero in every coordinate at this scale.

Thus the factorization

\[
11=7+2+2
\]

is not numerology. It is the exact first variation of the maximal exterior power.

## Chart independence

All four maximal minors were tested. Their leading vector changes from

\[
(1,1,1,1)
\]

to zero modulo three. Therefore the rank-stratum contact is detected by the complete Plücker section, not by a selected chart.

## Selectivity

For every grade (0\le n\le200), compare (R(n)) with (R(n+729)).

- (d_1) and (d_2) valuations agree for all 201 grades.
- The (d_3) valuation agrees for 200 grades.
- It changes only at (n=152).

A uniform readout artifact would not have this localization. The shift becomes visible precisely where the base response has the required high-order maximal-minor contact.

## Verdict

The local explanation survives:

> The (729)-shift supplies an order-seven source perturbation. At the exceptional grade (152), the maximal exterior-power derivative converts it into an order-eleven Plücker jet whose cancellation raises the Fitting depth by one.

This is theorem-level for the stated pair and bounded selectivity window. It is not an unbounded theorem about every translation or every grade.

## Evidence

- Checker: `research/strominger/checkers/transverse_fitting_explanation_falsifier.py`
- Result: `research/strominger/results/transverse_fitting_explanation_falsifier.json`
- Execution: `structured_command_execution:e_2512_1787936580561569200_38`
