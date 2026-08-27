# A one-scale Wilson potential selects an angle but cannot select its clock: WP789

## Question

Can a finite Hosotani potential lift WP788's Coulomb modulus without adding an
independent soft scale?

Gauge--Higgs compactifications can generate a radiative Wilson-line potential
and dynamically select its phase; explicit orbifold examples were computed by
[Haba, Hosotani, Kawamura, and Yamashita](https://arxiv.org/abs/hep-ph/0401183).
Models that stabilize both the Wilson line and radion require a complete
radion potential, as illustrated by
[Sakamura](https://arxiv.org/abs/1009.5353).

## General one-scale theorem

Let the four-dimensional effective potential have the single homogeneous
form

\[
V(\theta,R)=\frac{C}{R^4}F(\theta),
\qquad R>0.
\]

Joint stationarity requires

\[
F'(\theta_*)=0,
\qquad
F(\theta_*)=0.
\]

At every such point the mixed and radial Hessian entries vanish:

\[
V_{\theta R}=0,
\qquad
V_{RR}=0.
\]

Therefore no single \(R^{-4}\) Casimir term can have a strict joint minimum in
the Wilson angle and radius.

## Maximally favorable oriented selector

Even grant the oriented periodic shape

\[
F(\theta)=1-\cos(\theta-\phi),
\]

where \(\phi\) is assumed to come from the chiral source. It uniquely selects
\(\theta=\phi\) modulo the period and has positive angular curvature
\(C/R^4\). Nevertheless, the potential vanishes there for every \(R>0\).

The hostile pair

\[
(\theta,R)=(\phi,R_0),
\qquad
(\theta,R)=(\phi,2R_0)
\]

has identical source energy and angular selection. An absolute threshold
\(\lvert q\phi\rvert/R\) differs by a factor two.

## Minimal second-homogeneity repair

Add one genuinely different radius scaling:

\[
V(R)=\frac{Af}{R^4}+\frac{Bg}{R^6}.
\]

The nonzero stationary radius obeys

\[
R_*^2=-\frac{3Bg}{2Af},
\]

and its radial Hessian is

\[
V''(R_*)=-\frac{8Af}{R_*^6}.
\]

Thus stabilization requires a signed balance and fixes the clock through the
ratio \(Bg/(Af)\). Unless both coefficients and their relative sign descend
from the same source operation, the repair merely replaces the radius modulus
by a coefficient-ratio fiber.

## Classification

One-scale Hosotani dynamics is a genuine dimensionless angle selector and
local angular rigidifier. It does not fix:

- the compactification radius;
- the absolute portal magnitude or threshold;
- a complete joint vacuum or RG basin;
- absolute detector calibration;
- the sign instrument required beyond scalar spectroscopy.

The next source must generate two different radius homogeneities with a fixed
relative coefficient and sign, while retaining the oriented Wilson minimum.
This is the first architecture in the current branch capable in principle of
fixing both the dimensionless portal pattern and its physical clock.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp789_wilson_line_angle_radius_homogeneity_no_go.py

Generated result:
research/flavor/results/wp789_wilson_line_angle_radius_homogeneity_no_go.json
