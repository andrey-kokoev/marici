# The Normalized Ramanujan Packet Has a Prime-Square Hilbert Anomaly

## Mean-one sieve state

Let \(Q\) be squarefree and work on the probability space
\(\mathbb Z/Q\mathbb Z\) with uniform measure. Define

\[
f_Q(a)=\mathbf 1_{(a,Q)=1},
\qquad
\delta_Q=\frac{\varphi(Q)}{Q}.
\]

The density-normalized survivor state is

\[
w_Q=\delta_Q^{-1}f_Q.
\]

It has mean one. Since \(f_Q^2=f_Q\),

\[
\mathbb E|w_Q|^2
=
\delta_Q^{-2}\mathbb E f_Q
=
\delta_Q^{-1}.
\]

Therefore its centered energy is exactly

\[
\|w_Q-1\|_2^2
=
\frac{Q}{\varphi(Q)}-1.
\]

## Fourier form

With normalized Fourier coefficients,

\[
\widehat{w_Q}(k)=\frac{c_Q(k)}{\varphi(Q)}.
\]

The zero mode is one. Parseval gives

\[
\sum_{k\ne0}
\left|
\frac{c_Q(k)}{\varphi(Q)}
\right|^2
=
\frac{Q}{\varphi(Q)}-1.
\]

Thus the divergence belongs to the complete mixed-prime Ramanujan packet, not
to a Fourier coordinate omitted from the model.

## Primorial growth

For the primorial cutoff

\[
Q_y=\prod_{p\le y}p,
\]

one has

\[
\frac{Q_y}{\varphi(Q_y)}
=
\prod_{p\le y}(1-p^{-1})^{-1}.
\]

Mertens' product theorem gives

\[
\frac{Q_y}{\varphi(Q_y)}
\sim
e^\gamma\log y.
\]

Hence the mean-one Ramanujan packet has no cutoff-uniform Hilbert bound:

\[
\|w_{Q_y}-1\|_2^2
\sim
e^\gamma\log y.
\]

## Identification of the anomaly grade

The logarithm of the divergent factor is

\[
\log\frac{Q}{\varphi(Q)}
=
\sum_{p\mid Q}\sum_{k\ge1}\frac{p^{-k}}{k}.
\]

At the critical half-density, the primitive local amplitude is
\(p^{-1/2}\). Therefore \(p^{-1}\) is its square. The leading divergent
term is precisely the prime-square determinant current, while
\(k\ge2\) in the displayed \(p^{-k}\) expansion is summable.

This recovers the previously identified square boundary anomaly from the
exact Fourier energy of the full residue packet.

## Consequences

Three statements must be kept separate:

1. all mixed Ramanujan modes are retained;
2. the packet has a faithful finite-cutoff Hilbert norm;
3. that Hilbert norm is uniform under primorial completion.

The first two hold. The third fails logarithmically. Poisson unitarity cannot
repair the failure because Parseval is the identity exposing it.

This does not falsify RH or tempered boundary realization. Temperedness is
weaker than a cutoff-uniform \(L^2\) bound, and logarithmic conductor growth
may be admissible in a rigged topology. It does falsify every proof that
silently treats the completed Ramanujan carrier as an ordinary bounded
Hilbert vector.

## Revised completion target

The full comparison needs three layers:

1. the mean/common mode;
2. the square-current relative covariance line;
3. the centered Ramanujan fluctuation packet.

The square current must renormalize the covariance while remaining explicit
boundary data. After that relative normalization, one must prove continuity
in a source-derived tempered seminorm rather than demand a uniform raw
Hilbert norm.

## Falsifier

A proposed completion fails if it:

- asserts a uniform \(L^2\) bound for \(w_Q-1\);
- omits any Ramanujan mode;
- subtracts the logarithmic divergence without retaining a square boundary
  line;
- or changes the mean-one normalization to conceal the variance growth.

