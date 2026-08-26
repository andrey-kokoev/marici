# Shared latent mediator (WP344)

## Conditional preparation

Let one shared binary mediator choose between domain probabilities

\[
p_-=\bar p-d,
\qquad
p_+=\bar p+d
\]

with equal weights. The probability domain is restricted by
\(0<d<\min(\bar p,1-\bar p)\). Conditional on that mediator, all six domains
are iid. If the mediator record is discarded, the marginal moments become

\[
u_1=\bar p,
\qquad
u_2=\bar p^2+d^2,
\qquad
u_3=\bar p^3+3\bar p d^2.
\]

The connected pair coincidence is exactly \(d^2\).

## Factorization obstruction

The product law at probability \(\bar p\) has the same first moment as the
latent mixture. First-order agreement therefore cannot certify WP343's
no-latent clause. Second order separates the models whenever \(d\neq0\).

Even then, the marginal tower initially identifies the mediator variance
\(d^2\), not an absolute sign of \(d\). A branch-resolved mediator port would
define a finer relational experiment.

## Instrument gate

The smallest useful control is a calibrated connected pair coincidence.
Alternatively, an executable mediator readout must establish that the same
mediator branch is shared across the domains and freeze-out history under
test.

Run `uv run --with sympy python
research/flavor/checkers/wp344_shared_latent_mediator.py` to regenerate the
exact common-cause audit.
