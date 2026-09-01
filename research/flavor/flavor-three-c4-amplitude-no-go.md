# Three-\(C_4\) amplitude obstruction: WP1165

## Question

Can a three-\(C_4\) support-four carrier have a phase-compatible fixed-\(q\)
interior point?

## DPC resolution

- **Problem:** test the \(1\,350\) three-\(C_4\) carriers.
- **Conjecture:** a three-\(C_4\) carrier supports a phase-compatible
  fixed-\(q\) interior point.
- **Rivals:** block-constant witness; zero-diagonal block-stochastic matrix;
  balanced \(q\) block; remaining \(C_4+C_8\) carrier.
- **Risky consequences:** off-diagonal \(2\times2\) blocks are constant, all
  off-diagonal block masses are \(1/2\), and each \(q\) block sums \(1/3\).
- **Falsification attempt:** the block-mass equations force
  \(X_{IJ}=1/2\); fixed-\(q\) then requires each two-column \(q\) block to
  have noninteger numerator sum \(23/3\).
- **Residual:** the \(16\,200\) \(C_4+C_8\) carriers remain open.
- **Disposition:** reject all three-\(C_4\) carriers for phase-compatible
  fixed-\(q\) interior realization.

Checker: `research/flavor/checkers/wp1165_three_c4_amplitude_no_go.py`

Result: `results/wp1165_three_c4_amplitude_no_go.json`
