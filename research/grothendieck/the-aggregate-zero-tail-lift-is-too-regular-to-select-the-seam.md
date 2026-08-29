# The Aggregate Zero-Tail Lift Is Too Regular to Select the Seam

## Aggregate transform

Let the completed even theta source be \(\Phi\), and define

\[
X(z)
=
\int_{\mathbb R}
\Phi(v)e^{zv}\,dv.
\]

Because \(\Phi\) decays superexponentially at both ends, \(X\) is entire.

Define the full-line tail state

\[
G_z(q)
=
e^{-zq}
\int_q^\infty
\Phi(v)e^{zv}\,dv.
\]

It satisfies the source-derived equation

\[
G_z'(q)=-zG_z(q)-\Phi(q).
\]

## Positive-end decay

As \(q\) tends to positive infinity, the integral is a tail of a
superexponentially decaying function. Multiplication by \(e^{-zq}\) does not
alter that decay class. Hence \(G_z\) and all its derivatives decay faster
than every fixed exponential at the positive end.

## Zero closes the negative endpoint

Assume

\[
X(z)=0.
\]

Then

\[
\int_q^\infty\Phi(v)e^{zv}\,dv
=
-\int_{-\infty}^q\Phi(v)e^{zv}\,dv.
\]

The right side is a negative-end tail of the same superexponentially decaying
source. Therefore \(G_z\) and its derivatives also decay faster than every
fixed exponential as \(q\) tends to negative infinity.

Thus every scalar zero produces a nonzero aggregate tail state lying in all
of the opposite exponential Sobolev riggings:

\[
G_z
\in
\bigcap_{\varepsilon>0}
\left(
\mathcal H_{+,\varepsilon}
\cap
\mathcal H_{-,\varepsilon}
\right).
\]

This conclusion is independent of \(\Re z\).

## Why this does not transmit seam selection

The primitive all-prime currents have a common regulator domain collapsing to
\(\Re z=0\). The aggregate tail state does not: source completion has already
summed all labels and erased the primitive comb divergence.

Therefore a zero always produces a common aggregate tail state. That
implication cannot prove RH: it holds just as well for a hypothetical
off-seam zero.

The missing implication is stronger. A zero must produce a common labelled
tail state compatible with every primitive comb current.

Only the labelled lift retains the arithmetic completion threshold that
selects the seam.

## Structural lesson

Aggregation changes admissibility. It can turn a source packet lacking common
labelwise meaning into a perfectly regular scalar tail state. This is another
instance of a quotient becoming smoother than its fibers.

The zero-to-kernel bridge must therefore be formulated before vacuum
compression and label summation.

## Falsifier

The result fails if a scalar zero-tail state does not decay at one endpoint or
if its membership depends on \(\Re z\). The zero identity and
superexponential source decay exclude both.
