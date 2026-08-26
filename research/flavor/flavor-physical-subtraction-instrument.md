# Physical-subtraction instrument audit (WP383)

## Bounded question

Can a physically calibrated vertex remove WP382's finite-counterterm
ambiguity, and does doing so create source-derived selector authority?

## Calibrated response

Use the invariant two-residual vertex

\[
\Gamma(p^2;\mu)=c(\mu)+\alpha\log\frac{M^2+p^2}{\mu^2}.
\]

Declare a physical subtraction measurement at $p_0^2$,

\[
\Gamma(p_0^2)=C_0.
\]

Eliminating the scheme coefficient gives

\[
\Gamma(p^2)=C_0+
\alpha\log\frac{M^2+p^2}{M^2+p_0^2}.
\]

This expression is exactly invariant under a compensating finite scale and
counterterm change. One calibrated value therefore repairs WP382's scheme
ambiguity and makes momentum transport predictive.

## Calibration is not selection

The derivative with respect to the calibrated boundary value is exactly one.
Two packets with the same
source spectrum and running but opposite measured values of $C_0$ retain
opposite curvature at the subtraction point. The instrument identifies which
finite-boundary class nature occupies; it does not explain or predict that
class. Positivity becomes an empirical condition, not a source-generated
numerical selector.

This is the same logical separation emphasized by the cross-sector work:
a readout can repair a nonfaithful projection without uniquely identifying or
selecting its constructor.

## Executability gate

The formal vertex is weak-basis invariant because both insertions are the
WP378 residual $F$. But $F$ has bifundamental field degree 24, hence the
local $F^2$ contact has field degree 48. Calling $\Gamma$ a physical
subtraction observable does not by itself provide an experiment capable of
preparing and resolving that composite channel.

An admitted instrument must specify external states or a lower-point mixing
channel, kinematic support, detector resolution, backgrounds, and an
uncertainty model. If a reference channel supplies the measurement, it defines
a relational experiment over its stabilizer groupoid; it does not expose an
absolute coefficient of the original unreferenced experiment.

## Disposition

WP383 constructs a scheme-faithful calibration map. It is a physical readout
conditional on an executable vertex instrument, not a source selector. It
fixes $C_0$ empirically and then predicts transport away from $p_0$.

The smallest exact falsifier is the pair $C_0=1$ and $C_0=-1$ at fixed
spectrum and running. The remaining gate is an executable, source-generated
probe sensitive to the degree-48 invariant contact, or a derived lower-point
channel with a named matching map.

Run `uv run --with sympy python
research/flavor/checkers/wp383_physical_subtraction_instrument.py` to
regenerate the result.
