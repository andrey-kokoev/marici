# Support-three realizability gate: WP1260

## Question

Does support three admit a unistochastic-compatible fixed-\(q\) solution?

## DPC resolution

- **Problem:** decide whether support three admits a fixed-\(q\) doubly
  stochastic solution, then derive source phase authority selecting a
  production map.
- **Bold conjecture:** a support-three fixed-\(q\) map may be both doubly
  stochastic and unistochastic-compatible.
- **Named rivals:** support-three algebraic witness; single-overlap
  obstruction; support-three graph search; support-four search.
- **Risky consequences:** the WP1153 witness is nonnegative, doubly
  stochastic, target-compatible, and row support at most three; rows 0 and
  2 have one shared column with product \(11/480\); 297,200 support-three
  patterns are searched; all 200 admissible graphs are two complete
  \(3\times3\) blocks.
- **Strongest falsification attempt:** the witness cannot cancel one
  overlap term, and fixed-\(q\) block balance would require three integer
  numerators summing to \(23/2\); no support-three graph survives.
- **Exact residual:** test support-four sparse candidates.
- **Disposition:** accept algebraic support-three existence; reject
  unistochastic-compatible support three.

Checker: `research/flavor/checkers/wp1260_support_three_realizability_gate.py`

Result: `results/wp1260_support_three_realizability_gate.json`
