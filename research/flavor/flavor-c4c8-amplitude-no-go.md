# \(C_4+C_8\) amplitude obstruction: WP1166

## Question

Can a \(C_4+C_8\) support-four carrier have a phase-compatible fixed-\(q\)
interior point?

## DPC resolution

- **Problem:** test the final regular support-four carrier class.
- **Conjecture:** a \(C_4+C_8\) carrier supports a phase-compatible
  fixed-\(q\) interior point.
- **Rivals:** \(C_4+C_8\) witness; amplitude equality classes; \(45\) label
  classes; fixed-\(q\) nonnegative polytope.
- **Risky consequences:** \(16\,200\) carriers, sixteen reduced variables,
  rank-13 systems, and three free variables.
- **Falsification attempt:** \(43\) label classes have no nonnegative reduced
  point; two reach only boundary points with a zero amplitude class. No
  strictly positive interior point exists.
- **Residual:** no regular support-four phase-compatible interior class
  remains; boundary or irregular support classes need reassessment.
- **Disposition:** reject all \(C_4+C_8\) carriers for phase-compatible
  fixed-\(q\) interior realization.

Checker: `research/flavor/checkers/wp1166_c4c8_amplitude_no_go.py`

Result: `results/wp1166_c4c8_amplitude_no_go.json`
