# Translation 729 is detected by a transverse maximal-minor jet

## Exact localization

Compare grades

\[
n=152,\qquad n+729=881.
\]

The source increment satisfies

\[
v_3(C^{729}-I)=7.
\]

Every subsequent constructor layer differs at exactly the same precision:

\[
v_3(\Delta U)
=v_3(\Delta V)
=v_3(\Delta\mathrm{tail})
=v_3(\Delta\mathrm{nested\ commutator})
=v_3(\Delta A)
=7.
\]

Thus the constructors neither amplify nor erase the increment before the determinantal readout.

## Exterior-power response

For the full (4\times3) matrix, the minor packets behave as follows:

| minor size | left gcd valuation | right gcd valuation | minor-vector difference valuation |
|---:|---:|---:|---:|
| 1 | 2 | 2 | 7 |
| 2 | 4 | 4 | 9 |
| 3 | 11 | 12 | 11 |

The first two Smith layers are unchanged. Only the maximal minors split.

The valuation (11) has the first-variation form

\[
11=7+2+2.
\]

The perturbation contributes order seven, while the other two determinant legs contribute order-two base content.

After division by (3^{11}), the four maximal minors reduce modulo three to

\[
(1,1,1,1)
\]

at grade (152), but to

\[
(0,0,0,0)
\]

at grade (881). The normalized difference is

\[
(2,2,2,2).
\]

Thus the (729)-shift cancels the complete leading Plücker vector, raising (v_3(d_3)) from (11) to (12).

## Candidate explanation

The two integral responses are congruent modulo (3^7) throughout the constructor pipeline. The observed split is localized at the maximal-minor readout.

The candidate mechanism has three levels:

1. the source recurrence supplies a perturbation of order seven;
2. two determinant legs supply order-two base content;
3. the maximal-minor readout cancels the resulting order-eleven Plücker jet.

Calling this transverse requires a separate linearized-determinant test. The equality (11=7+2+2) and the normalized Plücker cancellation are necessary evidence, not by themselves a proof of transversality.

## Claim boundary

This packet concerns only the grades (152) and (881). It does not supply a source map to the independent grade-(0/1) observation-quotient repair fixture.

It localizes the period-(729) failure but does not prove that every nonzero period fails. An unbounded theorem requires a recurrence for the normalized maximal-minor jet or another source-derived forcing law.

## Evidence

- Checker: `research/strominger/checkers/period_729_layer_localization.py`
- Result: `research/strominger/results/period_729_layer_localization.json`
- Execution: `structured_command_execution:e_2512_1787936228078589100_37`
