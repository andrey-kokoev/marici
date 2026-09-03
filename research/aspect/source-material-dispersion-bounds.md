# Source material-dispersion bounds

## Question

Can phase slope and curvature bounds be derived from a source transfer model with uncertain material parameters, while excluding resonance poles from the admitted frequency band?

## Claim boundary

This packet treats a one-pole rational phase model with positive parameter intervals. It is a source-model prototype, not a fit to a named optical material or evidence for a laboratory component.

## One-pole phase model

Declare the phase transfer function

\[
\phi(\omega)=L\left(
 n_0\omega+a\frac{\omega}{\Omega^2-\omega^2}
\right),
\]

where \(L,n_0,a>0\), and the admitted band lies below the resonance \(\Omega\). The rational pole term represents a dispersive correction; its source and units must be specified in any physical use.

The exact derivatives are

\[
\phi'(\omega)=L\left[
 n_0+a\frac{\Omega^2+\omega^2}
 {(\Omega^2-\omega^2)^2}
\right]
\]

and

\[
\phi''(\omega)=
La\frac{2\omega(3\Omega^2+\omega^2)}
{(\Omega^2-\omega^2)^3}.
\]

## Interval source data

Use the rational source intervals

\[
L\in[1/100,1/90],
\quad n_0\in[3/2,8/5],
\]

\[
a\in[1/10,1/8],
\quad\Omega\in[2,5/2],
\]

on the band

\[
\omega\in[2/5,3/5].
\]

The band center is \(\omega_0=1/2\) and radius \(\Delta=1/10\).

All factors are positive. Below resonance, the derivative and curvature bounds increase with \(L,n_0,a,\omega\) and decrease with \(\Omega\). Hence outward bounds use the upper coefficients, upper frequency where appropriate, and lower resonance.

Define

\[
B=L_{\max}\left[
 n_{0,\max}+a_{\max}
 \frac{\Omega_{\min}^2+\omega_0^2}
 {(\Omega_{\min}^2-\omega_0^2)^2}
\right]
\]

and

\[
K=L_{\max}a_{\max}
\frac{2\omega_{\max}(3\Omega_{\min}^2+\omega_{\max}^2)}
{(\Omega_{\min}^2-\omega_{\max}^2)^3}.
\]

Then every admitted parameter choice obeys

\[
|\phi'(\omega_0)|\le B,
\qquad
\sup_{\rm band}|\phi''|\le K.
\]

## Pole exclusion

The lower resonance satisfies

\[
\Omega_{\min}-\omega_{\max}=7/5>0.
\]

Thus every denominator is separated from zero on the full parameter box and band. If a resonance interval intersects the band, derivative bounds are undefined; subdivision cannot repair a genuine pole crossing without a different absorptive transfer model.

## Continuous-mode margin

The phase radius supplied to the continuous-mode attachment certificate is

\[
r_\phi=B\Delta+K\Delta^2/2.
\]

The corresponding effect perturbation is at most \(2r_\phi\). Exact rational evaluation leaves a positive residual against nominal margin \(1/20\).

## Hostile fixture

Changing the resonance lower bound to \(1/2\) places a possible pole inside \([2/5,3/5]\). The checker rejects the parameter box before evaluating derivatives. This failure is a source-model domain violation, not a numerical-margin failure.

## Disposition

A declared rational dispersion model and parameter intervals generate exact phase slope and curvature bounds once the band is proved pole-free. Those bounds feed directly into the essential-supremum attachment margin. Physical application still requires sourced material parameters and a transfer model valid near every admitted frequency.
