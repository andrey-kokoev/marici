# Spectral-scale underdetermination (WP430)

## Question

Can WP429's missing frequency-resolved rival packets be derived from the
already frozen low-energy matching data and conditional mediator Lagrangians?

## Exact hostile dilation

For one damped mediator contribution, write the source response as

$$
\chi(\omega)=\frac{r}{m^2-\omega^2-i m\Gamma}.
$$

Its zero-frequency lossless matching coefficient is

$$
k=\frac{r}{m^2}.
$$

Under the common dilation

$$
m\mapsto sm,
\qquad
\Gamma\mapsto s\Gamma,
\qquad
r\mapsto s^2r,
$$

the coefficient (k) and dimensionless width (Gamma/m) remain fixed. The
pole location, absolute width, residue, and response at a fixed detector
frequency change. Hence the low-energy match and a dimensionless line-shape
ratio do not fix the spectrum in detector units.

The benchmark ((m,\Gamma,r)=(1,1/10,1)) and its (s=10) dilation have the
same exact (k=1). At the fixed command frequency (omega=1), their complex
responses are unequal.

## Relation to the declared flavor portal

WP131 supplies a gauge- and Lorentz-complete version of the same obstruction.
Scaling all flavor-sector dimension-one inputs preserves the dimensionless
low-energy Yukawa packet while moving two poles from ((1,2)) to ((10,20)),
changing their portal residues, and taking the accessible-pole count from two
to zero for a fixed detector reach.

Thus the obstruction is not an artifact of the generic pole notation. The
declared conditional portal contains an exact scale orbit invisible to the
matched low-energy record.

## Disposition

The existing low-energy flavor packet and conditional Lagrangian forms do not
derive WP429's missing spectra in calibrated detector units. Choosing a point
on the scale orbit is an additional boundary datum. RG transport does not
select it, and matching cannot infer it from the infrared coefficient.

The first missing constructor is now sharper: a physical clock or independently
observed mass threshold must break the scale orbit before the WP428 scan can be
evaluated. That observation must be external to the selector-facing four-bin
outcome.

This is still not evidence that the threshold instrument has low rank. It is a
proof that its numerical response matrix cannot be generated from the admitted
low-energy authority.

The smallest exact falsifier is a source law deriving one absolute mediator
mass or equivalent dimensionful invariant relative to an admitted clock while
preserving full weak-basis descent. Once one scale is fixed, the remaining pole
packet still requires widths, residues, continuum density, normalization, and
uncertainties.

Run `uv run --with sympy python
research/flavor/checkers/wp430_spectral_scale_underdetermination.py` to
regenerate the JSON result.
