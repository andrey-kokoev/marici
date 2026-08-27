# Balance-analyzer tradeoff: WP682

## Detuned pole basis

Retain balanced reciprocal vertices but allow the bare masses to differ by

\[
\Delta=M_A-M_B.
\]

For off-diagonal frame mixing (m), the physical pole gap is

\[
G=\sqrt{\Delta^2+4m^2}.
\]

The mass diagonalization angle obeys

\[
\cos 2\theta=\frac{\Delta}{G}.
\]

Transforming the frame fluctuation into the pole basis gives the cross-pole
coupling

\[
g_{+-}=y\frac{\Delta}{\sqrt{\Delta^2+4m^2}}.
\]

## Exact antagonism

At exact exchange balance, (Delta=0), the cross-pole analyzer vertex
vanishes. Near balance,

\[
g_{+-}\sim\frac{y\Delta}{2m}.
\]

Any Fisher or Gram information carried by this transition therefore collapses
at least quadratically in (Delta). The analyzer is not merely unavailable at
one exceptional point: its calibrated gain becomes arbitrarily fragile in
every neighborhood of the proposed exchange locus.

Recovering the analyzer requires explicit exchange breaking. Thus the same
condition proposed to explain balance deletes the operation intended to test
the relative phase.

## Disposition

This is a selector-analyzer antagonism theorem for the present messenger
operator. A viable successor would need a different source-derived analyzer
operator that does not commute with the balanced mass block. Adding a formal
noncommuting matrix without a source vertex would not repair the programme.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp682_balance_analyzer_tradeoff.py

Generated result: results/wp682_balance_analyzer_tradeoff.json.
