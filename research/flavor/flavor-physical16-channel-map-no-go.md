# `physical16` channel-map no-go: WP1174

## Question

Can a sourced six-branch-to-`physical16` channel map be derived from the
certified modulus?

## DPC resolution

- **Problem:** test whether \(q\) and a normalized 16-output target identify
  the production channel.
- **Conjecture:** the modulus and \(q\) determine the `physical16` channel.
- **Rivals:** unique stochastic channel; rank-one output channel;
  source-derived kernel; common coupling scale.
- **Risky consequences:** a \(16\times6\) stochastic channel has \(90\)
  parameters; exact output and normalization impose \(21\) constraints,
  leaving a generic \(69\)-dimensional fiber.
- **Falsification attempt:** two explicit positive stochastic channels,
  \(A_0\) and \(A_0+D\), have the same input \(q\) and output \(y\).
- **Residual:** only localized source dynamics can select the physical kernel
  and gain.
- **Disposition:** reject channel identifiability from modulus and output
  alone.

Checker: `research/flavor/checkers/wp1174_physical16_channel_map_no_go.py`

Result: `results/wp1174_physical16_channel_map_no_go.json`
