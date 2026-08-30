# Gaussian Annihilation and Prime Dilation Form a Flat Connection

## Native coupled constructor

Let

\[
A_t=\partial_x+2\pi t x
\]

be the annihilator of the Gaussian

\[
g_t(x)=e^{-\pi t x^2}.
\]

Let prime dilation act by

\[
(D_pf)(x)=f(px).
\]

This combines the archimedean vacuum law with the arithmetic operation that
sends an integer label \(n\) to \(pn\).

## Exact covariance

A direct calculation gives

\[
A_tD_p=pD_pA_{t/p^2}.
\]

Indeed,

\[
A_tD_pf
=
pf'(px)+2\pi txf(px),
\]

which equals \(pD_pA_{t/p^2}f\).

The Gaussian family is compatible with the same transport:

\[
D_pg_t=g_{p^2t},
\qquad
A_{p^2t}g_{p^2t}=0.
\]

Thus prime multiplication, real heat-scale transport, and Gaussian
annihilation form a commuting source square.

## Diagonal sampling

Sampling on the integer comb gives the labelwise Ward identity

\[
g_t'(n)+2\pi tn\,g_t(n)=0
\]

for every integer \(n\). Its adjoint distributional form is

\[
A_t^*\Delta_{\mathbb Z}
=
\sum_{n\in\mathbb Z}
\left(-\delta_n'+2\pi tn\delta_n\right),
\]

whose pairing with \(g_t\) vanishes label by label.

After summing labels, this identity generates the ordinary theta heat
relations. Prime dilation gives the corresponding sublattice rescaling
relations. After Mellin transport, the same covariance becomes the
archimedean gamma recurrence together with the prime character multiplier.

## Discrimination without orientation

This constructor is more selective than the standard Tate comparison cell.
A Fourier-self-dual polynomial--Gaussian hostile does not satisfy the
first-order vacuum equation and therefore produces a nonzero annihilation
current before its zeros are inspected.

But for the physical Gaussian source the connection is flat: its curvature
vanishes identically. The resulting Ward identities constrain the
presentation of theta, yet supply no positive or oriented bulk capable of
excluding a scalar Mellin cancellation.

Squaring the annihilator does not help. Its vacuum energy is zero on every
physical Gaussian atom. It detects deviations from the authorized source but
does not distinguish one spectral parameter from another within that source.

## Consequence

The first nonseparable Gaussian--arithmetic constructor exists, but it is a
source-rigidity certificate rather than an RH law.

The missing operation must compare two different transports of this flat
connection and retain their boundary anomaly. A viable candidate must have:

1. zero interior curvature on the Gaussian source;
2. a nonzero relative boundary curvature after diagonal completion;
3. the factor \(2\operatorname{Re}s-1\) under reciprocal Mellin transport;
4. a faithful boundary energy annihilated by a scalar zero-state.

This points back to a relative holonomy or Green current around the completed
Mellin--Poisson square, not another local annihilation identity.

## Falsifier

A proposed Gaussian--arithmetic curvature fails if it reduces to:

- \(A_tg_t=0\) label by label;
- the theta heat equation after summation;
- the gamma recurrence after Mellin transport;
- or a nonnegative annihilator norm that vanishes identically on the physical
  source.
