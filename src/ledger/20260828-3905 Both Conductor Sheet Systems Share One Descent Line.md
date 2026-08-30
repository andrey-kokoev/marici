# 3905 — Both Conductor Sheet Systems Share One Descent Line

## Hard-to-vary claim

The first gamma-normal Bockstein found in Entry 3902 is not a repair attached separately to one conductor branch. It is the common missing descent constructor for both independently labelled conductor systems in the \(G_{12}\) chart.

## Frozen test

Use the existing rank-26 physical-half-twist quotient and the two source-derived conductor equations

\[
a^2=\frac{C_1}{x},
\qquad
b^2=-\frac{C_2}{y}.
\]

For each conductor retain:

- both root sheets;
- the source residue weight, including the Jacobian and denominator factors;
- deck trace and anti-trace channels separately;
- the same degree-six numerator packet and the same absolute quotient.

No transition, projector, or correction row is fitted.

## Exact rank result

At primes \(32009\) and \(31957\), the ranks are identical:

\[
\begin{array}{c|c}
\text{packet}&\text{rank}\\
\hline
\text{absolute quotient}&26\\
\text{first conductor sheets}&2\\
\text{second conductor sheets}&2\\
\text{absolute + first conductor}&27\\
\text{absolute + second conductor}&27\\
\text{absolute + both conductors}&27\\
\text{absolute + all four deck channels}&27
\end{array}
\]

Thus the two sheet systems do not create independent descent defects. Their complete deck-resolved images share one quotient line.

## Narrow conclusion

The conductor atlas requires one missing coherence line, not one line per conductor or per sheet:

\[
\dim
\frac{Q_{26}+J_{g_1}+J_{g_2}}{Q_{26}}
=1.
\]

Together with Entry 3902, this identifies the first gamma-normal Bockstein as the unique available source line with the correct rank to repair both conductor systems simultaneously.

This is a rank and incidence theorem. It does not yet prove the chain map, its normalization, or cyclic gluing across \(G_{12},G_{23},G_{31}\).

## Explanatory consequence

The mixed parity seen under bare second-conductor reuse is not evidence for a second constructor. Parity is chart presentation; the common one-dimensional failure after quotient is invariant. The source normal variation supplies one coherence resource whose labelled readouts differ between conductor charts.

## Next falsifier

Transport the common line through the two free cyclic conductor orbits and test the signed order-three composite. The claim fails if:

1. a cyclic image enlarges the defect beyond rank one;
2. the three transitions do not compose to identity on the Bockstein line;
3. the induced normalization differs by a non-source unit;
4. any lower commuting face is altered.

## Artifacts

- `research/benincasa/checkers/check_rank26_two_conductor_common_descent_line.py`
- `research/benincasa/results/rank26-two-conductor-common-descent-line.json`
- `research/benincasa/results/rank26-two-conductor-common-descent-line-p31957.json`

Ledger sequence claim: `seqclaim-53eacdf1eb7f7acca4ebb7e9`.
