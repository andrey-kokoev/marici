# Reciprocal ratio selector (WP309)

## Parameter-free duality fixed point

Let $r>0$ be a dimensionless weak-basis-invariant flavor ratio and admit the
reciprocal duality

\[
r\longmapsto\frac1r.
\]

The invariant nonnegative potential

\[
V(r)=\left(r-\frac1r\right)^2
\]

has the unique positive stationary point and global minimum $r_*=1$, with
positive Hessian 8. No continuous source parameter remains, so the
source-response rank is zero on this declared ratio domain.

This is a genuine mathematical dimensionless selector, not merely a
rigidifier, if reciprocal duality is an admitted source operation.

## Scaled hostile family

The generalized involution

\[
r\longmapsto\frac{\kappa^2}{r}
\]

has fixed point $r_*=\kappa$ and response $dr_*/d\kappa=1$. Thus a hidden
duality scale restores the WP308 center-authority problem. The canonical value
1 is predictive only when the dimensionless normalization of $r$ is fixed
independently of flavor data.

## Classification and gate

The reciprocal construction selects a dimensionless ratio on its changed
duality groupoid. It does not select absolute masses or a full `physical16`
point. Physical progress requires a flavor source deriving the duality, an
executable operation or probe, anomaly and breaking control, and a covariant
map from the selected ratio into the faithful quotient.

Run `uv run --with sympy python
research/flavor/checkers/wp309_reciprocal_ratio_selector.py` to regenerate the
exact duality audit.
