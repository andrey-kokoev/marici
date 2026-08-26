# Kaon-conditioned pole-width reach: WP461

## Question

Does WP457's formal rank-two mass-plus-width readout remain rank two after a real high-mass resonance resolution is attached?

## Frozen benchmark and transport envelope

This is a conditional reach test, not a source-selected benchmark. Freeze

\[
m_1=g_F\mu=5\ {\rm TeV},
\qquad m_3=\sqrt3m_1.
\]

For the vectorlike SMEFT response, the displayed 5 TeV Atlas coefficients give the physical response factor

\[
F_5=263{,}200{,}000\ {\rm TeV}^2.
\]

The displayed 100 TeV coefficients give

\[
F_{100}=338{,}330{,}000\ {\rm TeV}^2,
\qquad \frac{F_{100}}{F_5}=\frac{33833}{26320}.
\]

WP461 does not interpolate these two points. It declares the hostile envelope

\[
F_5\leq F(m_3)\leq F_{100}
\]

for the unknown quintet-threshold response. This is a robustness assumption motivated by, but not proved by, the published endpoint scale dependence.

Using WP456's pole weights, the total real response is

\[
x=\frac{3F_5-F(m_3)}{24\mu^2}.
\]

At fixed (m_1=5 TeV), the smallest response in the envelope is

\[
x\geq\frac{2{,}256{,}350}{3}g_F^2.
\]

## Conditional kaon constraint

WP460's provisional 1.96-sigma interval has positive endpoint

\[
x_+=-\frac{579}{871}+\frac{49\sqrt{1{,}412{,}509}}{43{,}550}.
\]

For the positive WP447 benchmark response, the conservative envelope therefore gives

\[
g_F<9.46\mathbin{\cdot}10^{-4},
\qquad
\mu>5.29\mathbin{\cdot}10^3\ {\rm TeV},
\qquad
f>1.30\mathbin{\cdot}10^4\ {\rm TeV}.
\]

These are conditional working limits. They inherit WP460's Gaussian treatment of a preliminary lattice systematic and WP461's threshold envelope.

The 5 TeV benchmark itself fixes the readout

\[
\frac{g_Ff}{v}=\frac{5\sqrt6}{0.246}\approx49.79.
\]

This number was chosen by the benchmark pole mass; it is not source-selected.

## Detector convolution

The [ATLAS full Run-2 dijet resonance search](https://arxiv.org/abs/1910.08447) states that its approximate detector-resolution width is 3 percent and treats smaller intrinsic widths as zero-width signal templates.

At the conservative coupling endpoint, WP449 gives

\[
\Gamma_1<3.56\mathbin{\cdot}10^{-4}\ {\rm GeV}.
\]

The 3 percent resolution at 5 TeV is 150 GeV, exceeding this width by more than

\[
4.21\mathbin{\cdot}10^5.
\]

Consequently this detector surface maps the entire allowed intrinsic-width interval to its zero-width template. The mass coordinate may remain measurable if a signal exists, but the width coordinate is deleted and WP457's mass-plus-width Jacobian falls from formal rank two to at most rank one.

Production-rate information could in principle replace the width coordinate, but it requires a separately frozen flavor-changing parton luminosity, acceptance, luminosity covariance, and background likelihood. Algebraic residue span does not supply that executable control.

## Classification and falsifiers

WP461 is a conditional current constraint and a negative detector-width audit. It is neither selector nor rigidifier and adds no reference port.

Smallest falsifiers:

- the envelope-minimum response is nonpositive;
- the provisional positive endpoint fails to bound (g_F);
- the allowed intrinsic width reaches the declared detector resolution;
- the ATLAS zero-width template retains an independently calibrated intrinsic-width coordinate below resolution.

The successor must test a rate-based flavor-tagged channel or a much finer line-shape instrument; it may not continue calling formal pole widths an executable second readout.
