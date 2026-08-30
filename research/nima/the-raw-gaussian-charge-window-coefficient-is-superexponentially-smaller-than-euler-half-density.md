# The raw Gaussian charge-window coefficient is superexponentially smaller than Euler half-density

## Exact coefficient

The local cross-character coefficient is
\[
\beta_p
=
4\bigl(H(L)-H(2L)\bigr),
\qquad
L=\log p.
\]

Because
\[
H'(x)=-e^{-\pi x^2},
\]
we have the exact integral
\[
\beta_p
=
4\int_L^{2L}e^{-\pi u^2}\,du.
\]

Hence
\[
0<\beta_p
\le
4L e^{-\pi L^2}.
\]

The geometric coefficient therefore decays like a Gaussian in \(\log p\), faster than every power of \(p^{-1}\).

## Comparison with Euler half-density scale

The primitive arithmetic first-order scale is proportional to
\[
a_p
=
(\log p)p^{-1/2}
=
L e^{-L/2},
\]
up to the independently frozen constant and sign convention.

The normalized ratio obeys
\[
0<
\frac{\beta_p}{a_p}
\le
4e^{-\pi L^2+L/2}.
\]
Therefore
\[
\frac{\beta_p}{a_p}
\longrightarrow0
\qquad(p\to\infty).
\]

Consequently no uniformly bounded and boundedly invertible scalar calibration can identify the raw Gaussian window coefficient with the Euler half-density coefficient.

## Exact obstruction

Suppose one seeks source-frame factors \(c_p\) satisfying
\[
a_p=c_p\beta_p.
\]
Then necessarily
\[
|c_p|
\ge
\frac14e^{\pi L^2-L/2},
\]
so
\[
|c_p|\to\infty
\]
superexponentially in \(\log p\).

This violates completion-stable bi-bounded realization. Finite-prime fitting remains possible but is analytically meaningless at the completed edge.

## Interpretation

The exact Stokes cell at event 10376 is a valid local geometric interaction, but it is not yet the arithmetic Adams coefficient. The mismatch is not a small normalization defect. It is an order-of-decay mismatch:

\[
\text{raw window geometry}
\sim
e^{-\pi(\log p)^2},
\]
whereas
\[
\text{Euler half-density}
\sim
p^{-1/2}
=
e^{-(\log p)/2}.
\]

Thus the comparison must pass through the already identified source chain:

\[
\text{Gaussian window path}
\longrightarrow
\text{label shifts and dilations}
\longrightarrow
\text{theta synthesis}
\longrightarrow
\text{completion differential}.
\]

Those operations can convert the geometric \(\log p\) translation into the correct multiplicative arithmetic scale. A direct scalar calibration cannot.

## What remains useful

The raw cross-character cell still proves:

- correct reciprocal orientation;
- exact Stokes sign;
- prime diagonality;
- cutoff naturality;
- absence of mixed-block divergence.

It supplies the local geometric kernel that a source comparison functor must transport. It does not supply the arithmetic coefficient by itself.

## Hostile

At every finite cutoff, define
\[
c_p=a_p/\beta_p.
\]
All scalar coefficients then match exactly. Yet the largest calibration factor below cutoff \(X\) diverges at least like
\[
\exp\!\left(\pi(\log X)^2-\frac12\log X\right).
\]
The completed constructor has no bounded source realization.

## Revised frontier

Arithmetic calibration is closed negative at the raw-window level. The next theorem must act before scalar pairing and retain the three theta-completion Jordan grades:

\[
O\ \widehat{\otimes}\ D(W_{2L}-W_L)
\longrightarrow
\text{label-synthesized three-grade theta cell}
\longrightarrow
\text{Euler-normalized mixed coefficient}.
\]

Only a typed transport through this chain can legitimately bridge the decay orders.
