# Support-three doubly stochastic witness: WP1153

## Question

Do support-three doubly stochastic fixed-\(q\) maps exist?

## DPC resolution

- **Problem:** decide the first support class left open by WP1152.
- **Conjecture:** support-three doubly stochastic fixed-\(q\) maps exist.
- **Rivals:** support-two map; support-three algebraic witness; unistochastic
  lift; physical production locality.
- **Risky consequences:** nonnegative entries, row and column sums one,
  \(Pq=u\), and maximum row support three.
- **Falsification attempt:** an exact rational witness passes all four tests,
  refuting a support-three no-go.
- **Residual:** the witness still needs a unistochastic lift, production maps,
  and locality certificates.
- **Disposition:** accept support-three algebraic existence and select the
  unistochastic gate.

The witness has row supports \((3,3,2,3,3,2)\) and column supports
\((3,3,3,2,3,2)\).

Checker: `research/flavor/checkers/wp1153_support_three_witness.py`

Result: `results/wp1153_support_three_witness.json`
