# Stieltjes atoms force the fiber-spread bound

## Question

Is convolution-fiber spread an independent assumption once a positive Stieltjes representation exists?

## Claim boundary

The reduction starts from a positive source-derived Stieltjes measure. It does not construct that measure.

## Stieltjes to Bernstein atoms

After the quarter shift, a Stieltjes atom with \(\lambda=a+1/4\) contributes

\[
\frac{\lambda}{(x+\lambda)^2}
=
\int_0^\infty \lambda t e^{-(x+\lambda)t}\,dt.
\]

Thus each derivative atom is a Gamma shape-2 density up to normalization.

## Equal-rate fibers

For two equal-rate atoms, conditioning on \(T+U=v\) cancels the exponential factor and leaves density proportional to

\[
t(v-t),\qquad 0<t<v.
\]

Therefore \(T/v\) has the Beta\((2,2)\) law, with

\[
\mathbb E[T\mid V=v]=\frac v2,
\qquad
\operatorname{Var}(T\mid V=v)=\frac{v^2}{20}.
\]

## Unequal exchange pairs

Pairing rates \((\lambda,\mu)\) with \((\mu,\lambda)\) gives conditional density proportional to

\[
t(v-t)
\cosh\left((\lambda-\mu)(t-v/2)\right).
\]

This tilt is midpoint-even and increases with \(|t-v/2|\). Its covariance with \((t-v/2)^2\) is nonnegative, so it cannot reduce the Beta\((2,2)\) variance. Positive mixtures preserve the common conditional mean \(v/2\) and the lower variance bound.

The checker verifies the Stieltjes–Gamma identity, exact Beta moments, midpoint symmetry, and nine exact even-moment covariance inequalities. It also verifies that an unpaired unequal-rate tilt loses midpoint symmetry.

## Disposition

The fiber-spread condition is automatic from a positive exchange-symmetric Stieltjes measure. It is not an additional RH-strength premise. The sole remaining source gate is construction of that positive Stieltjes measure from completed arithmetic data without importing zero locations.

## Verification

- `research/voevodsky/stieltjes-atoms-force-fiber-spread-v1.json`
- `research/voevodsky/checkers/check_stieltjes_atoms_force_fiber_spread.py`
- `research/voevodsky/results/stieltjes_atoms_force_fiber_spread.json`
