# Ward common-scale commuting square

Work package: WP553  
Owner: marici.Figueiredo

## Question

Do WP550's pole calibration and WP552's operator parallelization compose into
the WP535 Ward rows when the quark masses and pole masses are calibrated by
different scale chains?

## Common-frame requirement

The scalar Ward coefficients contain

\[
{m_b^2\over\mu_i^2},\qquad
{m_s^2\over\mu_i^2},\qquad
{m_bm_s\over\mu_i^2}.
\]

If the quark and pole coordinates share one lattice energy unit, every common
unit rescaling cancels. The coefficients are dimensionless and the Omega
transfer commutes with the operator-scheme transport of WP552.

If quark masses use a scale factor \(k_q\) and pole masses use \(k_p\), all
three scalar coefficients acquire the relative factor

\[
\left({k_q\over k_p}\right)^2.
\]

In log coordinates their scale row is \((2,-2)\). It has rank one and kernel
\((1,1)^T\): only common scale motion cancels. A separately named interface
equating \(k_q\) and \(k_p\) is therefore necessary before the Ward row is a
common-frame physical object.

## Commuting square

Let \(Z\) be the common four-channel operator map. There are two legal paths:

1. form the dimensionless Ward ratios in the shared lattice frame and then
   apply \(Z\);
2. apply the common Omega scale to every mass, form the same ratios, and then
   apply \(Z\).

The checker proves that the resulting six amplitudes agree exactly. A hostile
split-scale path with \(k_q=2k_p\) multiplies every scalar Ward coefficient by
four while leaving the vector coefficient fixed, so it fails the square.

## Authority boundary

WP550 currently names same-ensemble Omega calibration for the six pole
kernels. WP553 adds the requirement that the renormalized quark masses used in
the Ward identity be obtained in the same ensemble, action, tuning, scale,
and continuum scheme, or be joined by an independently derived matching
constructor with covariance.

This is not the WP431 selector problem. Establishing a common measurement unit
identifies a realized amplitude; it does not derive the mediator-to-Standard-
Model mass ratio from the source.

The smallest exact falsifier is a relative quark/pole scale shift. It preserves
each internally calibrated packet but changes the scalar Ward response.

## Status

WP553 is an exact interface and descent theorem, not an executed instrument.
The remaining physical gate is a joint quark-mass, Omega, pole-kernel, and
operator-renormalization analysis with one covariance and declared matching
scheme.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp553_ward_common_scale_commuting_square.py

The generated result is
research/flavor/results/wp553_ward_common_scale_commuting_square.json.
