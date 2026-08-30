# Soft exchange-breaking ratio selector (WP314)

## Minimal broken vacuum

On the fixed radial shell, write $t=v_1/v_2>0$. Add one exchange-odd soft
coefficient $\epsilon$ to the WP312 angular potential:

\[
U(t)=\frac{\kappa(t-1)^2+\epsilon(t^2-1)}{1+t^2},
\qquad \kappa>0.
\]

The positive stationary branch is

\[
t_*=\frac{\sqrt{\epsilon^2+\kappa^2}-\epsilon}{\kappa}.
\]

At $\epsilon=0$, this recovers the symmetric selector $t_*=1$.

## Authority inversion

The selected ratio can be inverted exactly:

\[
\frac{\epsilon}{\kappa}=\frac{1-t_*^2}{2t_*}.
\]

Thus any desired positive ratio can be installed through the soft coefficient.
The exact hostile packets select $t=2$ at $\epsilon/\kappa=-3/4$ and $t=3$
at $\epsilon/\kappa=-4/3$.

Soft breaking repairs WP312's forced equality but restores a rank-one source
ambiguity. It is a genuine tunable selector, not a parameter-independent
prediction.

## Progressive gate

A viable successor must derive $\epsilon/\kappa$ from discrete source data or
a zero-modulus operation before flavor fitting. That value must then survive
vacuum stability, realistic left-right matching, thresholds, and the complete
`physical16` ensemble. Choosing it from the desired hierarchy is exactly the
WP301 target-coding defect.

Run `uv run --with sympy python
research/flavor/checkers/wp314_soft_exchange_breaking_ratio.py` to regenerate
the exact soft-breaking audit.
