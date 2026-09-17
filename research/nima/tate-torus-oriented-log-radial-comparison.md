# Tate-torus versus oriented log-radial carrier

## Carrier map

A finite lattice packet

\[
\mu=\sum_m a_m\delta_m
\]

embeds into distributions on logarithmic space. Applying `exp` places it on the positive oriented radial port:

\[
J\mu=\sum_m a_m\delta_{e^m},
\]

up to the selected density normalization. The multivariable channel lattice uses the coordinatewise map from `R^D` to `(R_+^x)^D`.

This gives an injective map on finite Catalan packets. Weighted completions require a convergence condition because arithmetic log specializations can have dense image.

## Operator comparison

Pontryagin Fourier in logarithmic coordinates has kernel

\[
K_{Tate}(m,u)=e^{-2\pi i m u}.
\]

The oriented log-radial operator is additive Fourier in the physical coordinate, conjugated by `x=e^u`. Its kernel is

\[
K_{or}(m,u)
=e^{-2\pi i e^m e^u}
=e^{-2\pi i e^{m+u}},
\]

multiplied by a nonzero Jacobian or half-density factor.

The phases differ. An amplitude normalization cannot turn one kernel into the other. In particular,

\[
W_{or}J(\delta_m)
\]

is an exponential-of-exponential oscillatory function in `u`, while the Tate transform is the ordinary character `e^{-2 pi i m u}`. The image of the Tate lattice packet space is not invariant under `W_or`.

## Disposition

The requested identification does not hold for the displayed operators. The two constructions use different Fourier transforms:

- Tate torus: Fourier duality for the additive logarithmic lattice;
- oriented radial carrier: physical additive Fourier transformed through a nonlinear logarithmic chart.

They can be placed inside a common strong-dual carrier on logarithmic Euclidean space, where both operators are defined. Their equality cannot be asserted. A future bridge would be an explicit integral transform conjugating the two kernels, not the oriented logarithm itself.

The Catalan quarter theorem retains its combinatorial, Pontryagin, and trace statements. Its chart operator should be called the **log-lattice Pontryagin successor**, rather than identified with the earlier physical oriented Fourier successor.

`check_tate_torus_vs_oriented_log_radial.py` records explicit phase witnesses and the surviving finite-packet carrier embedding.
