# Clock-spectrum parallelization gate (WP431)

## Candidate repair

WP430 requires one absolute mediator mass or equivalent dimensionful invariant
relative to a physical clock. The Standard Model already supplies measured
clocks such as the electroweak scale (v), the Higgs mass, and quark masses.
The question is whether attaching one of these clocks fixes the conditional
flavor-mediator spectrum.

## Exact free ratio

Let (v>0) be an independently measured clock and write a mediator mass as

$$
M=xi v.
$$

The ratio (xi) is a new dimensionless datum. For a pole with low-energy
coefficient (k=r/M^2) and dimensionless width (q=Gamma/M), every positive
(xi) admits

$$
r=k xi^2v^2,
\qquad
Gamma=q xi v.
$$

All members have the same observed clock (v), infrared coefficient (k),
and dimensionless width (q), while their absolute masses, widths, residues,
and fixed-frequency responses differ. Merely expressing the spectrum in Higgs
units does not select (xi).

The exact hostile pair (xi=1) and (xi=10), with (v=k=1) and (q=1/10),
reproduces WP430's two scale-related spectra. Both are calibrated against the
same clock. The ambiguity is therefore not a units problem.

## Portal relation does not automatically fix the ratio

A Higgs-portal mass relation of the form

$$
M^2=m_0^2+kappa v^2
$$

is a named interface, but (v) alone does not determine (m_0^2) and
(kappa). Unless a source theory fixes them independently, the portal merely
parameterizes the free ratio

$$
xi^2=\frac{m_0^2}{v^2}+kappa.
$$

An observed Higgs clock plus a valid flavor Lagrangian therefore does not imply
a source-calibrated spectrum. The interface constructor must carry independent
parameter authority.

## Disposition

No currently admitted Standard Model clock breaks the WP430 scale orbit because
no source-authorized relation fixes the mediator-to-clock ratio. The first
missing arrow is not clock measurement; it is a derived parallelization map
from the clock-bearing Standard Model sector to the mediator mass packet.

This result does not prohibit using an observed mediator pole as its own clock.
Such an observation would directly fix (M), but the mediator has not been
observed. Nor does it prohibit a UV symmetry, dimensional-transmutation law, or
threshold relation that predicts (xi); those are precisely the reopening
constructors.

The smallest exact falsifier is a source-derived equation fixing (xi) with no
free dimensionless or dimensionful input adjusted to the flavor outcome. It
must descend under the full weak-basis groupoid and retain a separately typed
measurement of the clock.

Run `uv run --with sympy python
research/flavor/checkers/wp431_clock_spectrum_parallelization_gate.py` to
regenerate the JSON result.
