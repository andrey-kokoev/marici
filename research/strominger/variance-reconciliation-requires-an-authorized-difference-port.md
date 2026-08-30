# Variance reconciliation in the magnetic decoration orbit

## Typed square

Let source constructors act covariantly on grades by

\[
T_s(n)=n+s,\qquad s\in\{-1,+1\},
\]

and let the instrument expose the contravariant reconstruction packet

\[
R(n)=\bigl(v_3(d_1(n)),v_3(d_2(n)),v_3(d_3(n))\bigr).
\]

The reconciliation question is whether observational identification is natural under the source action.

## Strict cell fails

The least blind pair is

\[
R(0)=R(1)=(1,2,3).
\]

Both constructor directions split it. For (s=+1), the comparison residual is

\[
R(2)-R(1)=(1,3,4).
\]

For (s=-1), it is

\[
R(0)-R(-1)=(-1,-2,-4).
\]

Thus no strict variance-reconciliation cell descends to the valuation quotient.

## Partial cell fails typing

One might define the cell only on pairs with equal (R). That domain is not closed under either authorized constructor. The composite has no target comparison object after the first split. This is not a nonzero anomaly; it is a partial-domain failure.

## Lax cell exists algebraically

On all grade pairs define

\[
\omega(a,b)=R(b)-R(a).
\]

This is a coboundary. It satisfies pair composition and every tested triple substitution identity exactly. Hence a lax variance-reconciliation cell exists algebraically.

But this repair changes the instrument contract: it adds a full difference port on all pairs, including pairs the original readout distinguishes. Its coherence is proved; its source authority is not.

## Interpretation

The candidate (2+1) architecture is now sharply typed:

1. covariant source composition;
2. contravariant observational reconstruction;
3. a mixed comparison cell.

The magnetic valuation quotient rejects a strict third cell. A restricted partial cell is not composable. A globally lax cell closes algebraically but requires an additional executable observation capability. Therefore the remaining barrier is not higher associativity in this fixture; it is authority for the difference port.

- Checker: `research/strominger/checkers/variance_reconciliation_checks.py`
- Result: `research/strominger/results/variance_reconciliation_checks.json`
- Execution: `structured_command_execution:e_2512_1787934700779750500_24`
