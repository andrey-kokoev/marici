# The angular Bernstein measure is the differentiated Xi heat trace

## Exact transport

Let the squared logarithmic derivative have Stieltjes representation

\[
S(w)=\int_0^\infty\frac{d\rho(a)}{w+a},
\]

and define its heat transform

\[
\Theta_\rho(t)=\int_0^\infty e^{-at}\,d\rho(a).
\]

For `c=1/4` and `H(w)=(w-c)S(w)`, the Bernstein density of `H'` derived previously is

\[
m_H(t)=t\int_0^\infty(a+c)e^{-(a+c)t}\,d\rho(a).
\]

It has the exact compressed form

\[
m_H(t)=-t\frac{d}{dt}\left(e^{-ct}\Theta_\rho(t)\right).
\]

Thus the angular-current Bernstein measure is not a second spectral object. It is the exponentially shifted Xi heat trace followed by one directed heat derivative.

## RH model

Under real squared zero coordinates `a=gamma^2` with multiplicities,

\[
\Theta_\rho(t)=\sum_\gamma m_\gamma e^{-\gamma^2t},
\]

and

\[
m_H(t)=t\sum_\gamma m_\gamma(\gamma^2+1/4)e^{-(\gamma^2+1/4)t}>0.
\]

An off-axis zero quartet instead contributes oscillatory complex-squared exponentials to the heat trace; positivity is no longer automatic.

## Consequence for the proof search

The proposed construction of a Bernstein measure for `H'` and the older construction of a positive Xi heat trace are the same gate under a fixed source-derived transform. Laplace-transform uniqueness prevents choosing a different positive measure to repair a sign failure.

The noncircular arithmetic target can therefore be stated once: derive a positive heat distribution `Theta_rho` from the completed endpoint--gamma--prime source such that its Stieltjes transform equals the exact centered Xi logarithmic derivative. Positivity of `m_H` then follows by the displayed derivative only if the shifted heat trace is decreasing; under a positive spectral measure this is automatic, but proving that premise is RH-strength.

## Disposition

Merge the angular Bernstein branch into the Xi heat-trace/Stieltjes branch. The conditional-spread and Schwarzian consequences require no separate conjectures. The sole missing arrow is source arithmetic to a positive heat/Stieltjes measure without inserting zero locations.
