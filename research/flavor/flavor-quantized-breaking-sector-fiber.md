# Quantized breaking-sector fiber (WP315)

## Discrete soft breaking

Replace WP314's continuous coefficient ratio by an integer source sector,

\[
\frac{\epsilon}{\kappa}=n,
\qquad n\in\mathbb Z.
\]

The selected vacuum ratio becomes

\[
t_n=\sqrt{n^2+1}-n.
\]

There is no continuous tuning inside a fixed sector. Opposite sectors obey
$t_nt_{-n}=1$, as required by exchange. For example,
$t_{-1}=1+\sqrt2$ and $t_{-2}=2+\sqrt5$.

## Discrete fiber obstruction

Quantization produces a discrete prediction family, not a unique prediction.
The exact five-sector audit gives five distinct ratios. This is the same
durable obstruction in a new guise: finite fiber is not singleton fiber.

The simplest parameter-free positive sector energy, $E(n)=n^2$, uniquely
selects $n=0$. It therefore returns $t=1$, the symmetric prediction already
falsified by WP313. A linear flux bias could select nonzero $n$, but its
coefficient would restore the WP314 authority problem.

## Classification

Quantized breaking is a finite-family selector architecture. It is not yet a
sector selector or a numerical `physical16` prediction. A progressive source
must derive both the flux domain and a unique nonzero sector-selection law
without answer-coded bias coefficients.

Run `uv run --with sympy python
research/flavor/checkers/wp315_quantized_breaking_sector_fiber.py` to
regenerate the exact sector audit.
