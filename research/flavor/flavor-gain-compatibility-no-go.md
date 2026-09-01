# Gain-compatibility no-go: WP1141

## Question

Are the vector event-cell gain and soft-channel reweighting gain compatible as
one source gain?

## DPC resolution

- **Problem:** determine whether WP1064 and WP1075 use one physical gain law.
- **Conjecture:** their gains are compatible as one source gain.
- **Rivals:** common scalar gain; distinct typed cascade gain;
  reweighting-only target gain; event-cell-only conditional gain.
- **Risky consequences:** a common gain must preserve the vector rows
  \(S=1/5,D=2/5\); the reweighting target requires \(g=3/2\); any cascade
  factor must be exactly \(3/2\); and the factor needs production/decay
  provenance.
- **Falsification attempt:** \(g=1\) preserves the vector rows, while
  \(g=3/2\) changes them to \(S=9/20,D=3/5\). No source certificate supplies
  the required cascade factor.
- **Residual:** a future physical16 gain-cascade packet may distinguish and
  derive the two gains.
- **Disposition:** reject common source-gain compatibility and record the
  cascade certificate blocker.

## Exact result

The required cascade factor is

\[
\frac{3/2}{1}=\frac32.
\]

No typed physical16 production/decay certificate currently derives it.

Checker: `research/flavor/checkers/wp1141_gain_compatibility_no_go.py`

Result: `results/wp1141_gain_compatibility_no_go.json`
