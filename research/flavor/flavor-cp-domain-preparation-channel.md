# CP-domain preparation channel (WP328)

## Thermal preparation

Treat the two WP327 branches as domains with energies (-\epsilon c_0) and
(+\epsilon c_0). A thermal preparation channel at inverse temperature
(\beta) gives

\[
p_+=\frac{e^{\beta\epsilon c_0}}
{e^{\beta\epsilon c_0}+e^{-\beta\epsilon c_0}},
\qquad
\log\frac{p_+}{p_-}=2\beta\epsilon c_0.
\]

At zero bias the domains occur with equal probability. A positive bias favors
the positive branch but does not make it certain at finite temperature.

## Faithfulness and kernel

Repeated calibrated CP-sensitive branch counts identify one log-odds
coordinate. The response Jacobian with respect to
((\beta,\epsilon,c_0)) has rank one and a two-dimensional kernel. The counts
therefore identify only the product \(\beta\epsilon c_0\), not the temperature,
bias, and CP scale separately.

This is a stochastic preparation selector, not unique source identification.
Observing one domain is weaker still: it is one Bernoulli outcome rather than a
calibrated probability measurement.

## Instrument gate

A physical realization must derive the freeze-out temperature, domain
independence, CP scale, and bias on a common history. It also needs a calibrated
CP-sensitive detector confusion matrix. Additional source-derived probes are
required to remove the two-dimensional parameter kernel.

Run `uv run --with sympy python
research/flavor/checkers/wp328_cp_domain_preparation_channel.py` to regenerate
the exact audit.
