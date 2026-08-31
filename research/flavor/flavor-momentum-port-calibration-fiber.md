# Momentum-port calibration fiber: WP1041

## Question

Can finite-response readout close WP1040 without an independently calibrated
momentum port?

## Ratio collision

Keep the WP1040 repaired domain: \(k=2\), \(C=23\), fixed zero-momentum
coefficient, and one degenerate positive pole. The normalized response is

\[
\frac{R(p^2)}{R(0)}=\frac{M^2}{M^2+p^2}.
\]

It depends only on the dimensionless ratio \(p^2/M^2\). The exact packets

\[
(M^2,p^2)=(1,1),
\qquad
(M^2,p^2)=(2,2)
\]

share the response \(1/2\) and all zero-momentum source data. A finite-response
record without a momentum standard therefore cannot select an absolute pole
mass.

## Calibrated-port separation

If the same physical port \(p^2=1\) is independently calibrated, then the
WP1040 hostile pair is separated:

\[
M^2=1:\quad \frac12,
\qquad
M^2=2:\quad \frac23,
\qquad
\Delta=\frac16.
\]

This is readout faithfulness to the ratio on the degenerate one-pole domain,
not source selection of that ratio.

## Classification

The first nonfaithful arrow is

\[
\{\text{finite threshold response}\}
\longrightarrow
\{\text{absolute pole mass without a momentum standard}\}.
\]

A threshold instrument must carry a calibrated physical momentum port in the
same frame as the pole mass and `physical16` detector. It still would not
derive the source value of \(p^2/M^2\).

## Disposition

Negative for readout-only repair of the WP1040 mass-clock fiber. Reopening
requires a source-calibrated momentum port and an independent source law fixing
the dimensionless threshold ratio, after WP1038 and WP1039's integer-label and
pole-spectrum gates have been closed.

Checker: `research/flavor/checkers/wp1041_momentum_port_calibration_fiber.py`

Result: `results/wp1041_momentum_port_calibration_fiber.json`
