# Level-44 noise and abstention threshold

## Precision gate

Unsigned norm balancing converts a resolved eigenvalue sign into full-scale
phase contrast. It cannot repair noise or coherent error already present in
the synthesized field `Tf`.

Use the conservative lower edge `2e-6` of the preregistered level-44 positive
window. Split it before acquisition:

- at most `1e-6` for independently bounded coherent synthesis bias;
- at most `1e-6` for the one-sided stochastic confidence radius.

The three simultaneous claims are 43-even negative, 44-even positive, and
44-odd positive. A Bonferroni familywise error rate of one percent fixes the
one-sided normal quantile before data are observed.

For pre-gain single-shot quadrature deviation `sigma`, the required number of
independent samples is

`ceil((z sigma / 1e-6)^2)`.

The compiler gives approximately:

- `sigma=1e-4`: about seventy-four thousand samples;
- `sigma=1e-5`: about seven hundred forty samples;
- `sigma=1e-6`: about eight samples.

The exact integers are recorded in the generated result.

## Non-negotiable distinction

Stochastic noise decreases with repetition. Coherent filter error, kernel
truncation error, phase bias, and cross-channel leakage do not. They require
an independent bound below `1e-6` in the normalized quadratic-form units.

If either budget fails, the experiment abstains. It must not report a negative
result, because failure to resolve a near-zero response is different from
observing the wrong sign.

Post-gain signal-to-noise is not admissible evidence for this gate. The noise
must be characterized at the output of the unamplified 43- or 44-channel
operator, before unsigned norm balancing.

## Verification

```text
python research/aspect/checkers/check_level44_noise_abstention_threshold.py
```
