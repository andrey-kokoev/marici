# Finite-width complementary threshold (WP369)

## Bounded correction

Replace WP368's real heavy propagator by the finite-width pole packet

\[
\frac{1}{L(\epsilon)-i\Omega},
\qquad
L(\epsilon)=L+k\epsilon,
\qquad L,\Omega>0.
\]

Here \(\Omega\) has mass-squared units, for example a pole mass times a width.
The complex threshold correction to the quartic coefficient is

\[
\Delta U
=-\frac{\mu^2}{2[L(\epsilon)-i\Omega]}.
\]

Its dispersive and absorptive parts are

\[
\Delta U_R=-\frac{\mu^2L(\epsilon)}{2[L(\epsilon)^2+\Omega^2]},
\qquad
\Delta U_I=-\frac{\mu^2\Omega}{2[L(\epsilon)^2+\Omega^2]}.
\]

The imaginary part is an open-channel response, not a Hermitian static
potential coefficient. It must be typed through a width or line-shape
instrument.

## Blind point and complementary repair

At \(\epsilon=0\), mass control gives

\[
R_R=\frac{\mu^2k(L^2-\Omega^2)}{2(L^2+\Omega^2)^2},
\qquad
R_I=\frac{\mu^2kL\Omega}{(L^2+\Omega^2)^2}.
\]

The dispersive response vanishes exactly at \(L=\Omega\). The absorptive
response there is

\[
R_I=\frac{\mu^2k}{4\Omega^2},
\]

which is nonzero on the admitted domain. The source-derived complementary
channel therefore removes the finite-width blind point of the ordinary
quartic projection.

The two threshold coordinates are also locally faithful for \((L,\Omega)\)
when \(\mu\) is known: their two-by-two Jacobian has nonzero determinant away
from the deleted coupling. This identification does not add a second control
direction; the mass intervention still traces one response vector.

## Limits and authority

As \(\Omega\) tends to zero, the dispersive matching and response reduce to
WP368 and the absorptive channel vanishes. As \(L\) tends to infinity, both
threshold coordinates and both response components decouple.

This packet upgrades the threshold instrument grammar, not selector authority.
The flavor response still depends on the portal coefficient and still factors
through \(J^2\). A physical realization must derive the width, calibrate the
line shape, include detector resolution and backgrounds, and verify that the
same control changes the complex pole without introducing untracked channels.

The smallest exact falsifier of dispersive-only faithfulness is \(L=\Omega\):
the ordinary response is zero while the absorptive response is nonzero.

Run `uv run --with sympy python
research/flavor/checkers/wp369_finite_width_complementary_threshold.py` to
regenerate the exact result.
