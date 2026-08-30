# Higher Laguerre forms are even jet self-transvectants

## Bounded question

What is the correct geometric-algebra object extending the first phase-circle
area form to every generalized Laguerre order?

## Exact jet form

For a real entire function `X`, define

\[
 \mathcal L_n[X](x)
 =\sum_{j=0}^{2n}
 \frac{(-1)^{n+j}}{j!(2n-j)!}
 X^{(j)}(x)X^{(2n-j)}(x).
\]

Equivalently,

\[
 \boxed{
 (2n)!\mathcal L_n[X]
 =\sum_{j=0}^{2n}(-1)^{n+j}
 \binom{2n}{j}X^{(j)}X^{(2n-j)}.}
\]

This is, up to the displayed sign convention, the order-`2n`
self-transvectant of the derivative jet.  The alternating binomial
coefficients are not chosen to fit zeros; they are the canonical invariant
pairing on the `2n`-th symmetric-power representation of a two-dimensional
phase space.

Odd self-transvectants vanish by antisymmetry.  Even orders are symmetric and
produce the scalar hierarchy above.

## First two orders

At order one,

\[
 \mathcal L_1=(X')^2-XX'',
\]

which packet 120 identified with the phase-plane bivector.

At order two,

\[
 \boxed{
 12\mathcal L_2
 =XX^{(4)}-4X'X^{(3)}+3(X'')^2.}
\]

This is not a single ordinary Wronskian or Pluecker coordinate. It is the
invariant quadratic contraction of the fourth derivative jet. Thus the
tentative osculating-flag language in packet 120 must be refined: exterior
orientation is sufficient at first order, while higher orders live in
symmetric-power phase representations.

## Vertical self-comparison

Taylor expansion gives the generating identity

\[
 \boxed{
 |X(x+iy)|^2
 =\sum_{n\ge0}\mathcal L_n[X](x)y^{2n}.}
\]

Hence the complete hierarchy asks whether the vertical self-comparison has
nonnegative coefficients at every real base point.  The phase-circle angular
velocity is only its first nontrivial coefficient.

## Two-copy source representation

If

\[
 X(x)=\int_{\mathbb R}\Phi(u)e^{ixu}\,du,
\]

then binomial expansion gives

\[
 \boxed{
 (2n)!\mathcal L_n[X](x)
 =\iint_{\mathbb R^2}
 (u-v)^{2n}\Phi(u)\Phi(v)e^{ix(u+v)}\,du\,dv.}
\]

Every order is therefore the same two-copy Carrier with a higher even power
of source separation.  The source measure is positive; only the global
sum-coordinate phase remains indefinite.

## Geometric interpretation

The hierarchy is not an unrelated list of inequalities:

\[
 \boxed{
 \text{two-dimensional value--flux phase space}
 \xrightarrow{\operatorname{Sym}^{2n}}
 \text{canonical even invariant}
 \xrightarrow{\text{source readout}}
 \mathcal L_n.}
\]

This supplies the higher-order form of the operator's two-plane intuition.
The two reciprocal sectors generate a basic phase plane; each Laguerre order
tests the orientation induced on one even symmetric power of that plane.

## RH boundary

Under the required real-entire growth and canonical-product hypotheses, the
nonnegativity of the complete hierarchy is the Laguerre--Polya target related
to RH for the completed Xi function. This packet identifies the invariant but
does not prove its sign.

The next gate is functorial: determine whether the all-order source seam-jet
orientation from packet 114 is transported by modular Fourier sewing to the
canonical invariant form on every `Sym^(2n)`. The smallest falsifier is the
first `n` for which the transport fails to intertwine the source Vandermonde
form with the transvectant form.
