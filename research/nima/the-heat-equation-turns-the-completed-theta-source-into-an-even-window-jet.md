# The heat equation turns the completed theta source into an even window jet

The Jacobi carrier supplies an exact differential comparison between the
window and completed-theta slices.

## Jacobi heat equation

For

\[
\Theta(z,r)
=
\sum_{n\in\mathbb Z}e^{-\pi r(n+z)^2},
\]

termwise differentiation on every compact set with \(r>0\) gives

\[
\partial_r\Theta
=
\frac1{4\pi}\partial_z^2\Theta.
\]

Consequently,

\[
\partial_r^2\Theta
=
\frac1{16\pi^2}\partial_z^4\Theta.
\]

This is the source connection relating Gaussian scale to the even additive
jet.

## Completion in the heat coordinate

Set

\[
r=e^{2u},
\qquad
h(u)=e^{u/2}\Theta(0,r).
\]

Conjugating the completion differential gives

\[
e^{-u/2}
\left(\partial_u^2-\frac14\right)
e^{u/2}
=
4r^2\partial_r^2+6r\partial_r.
\]

Therefore the completed theta source is

\[
\Phi(u)
=
e^{u/2}
\left(
4r^2\partial_r^2+6r\partial_r
\right)\Theta(0,r).
\]

Using the heat equation,

\[
\Phi(u)
=
e^{u/2}
\left[
\frac{r^2}{4\pi^2}\partial_z^4
+
\frac{3r}{2\pi}\partial_z^2
\right]
\Theta(z,r)\bigg|_{z=0}.
\]

Thus completion is an exact even spatial-jet observer on the Jacobi carrier.
No fitted three-grade map is needed to obtain its linear source formula.

## Relation to the window slice

The lattice-sampled window path satisfies

\[
\mathcal W'(t)=-2\Theta(t,1).
\]

Hence its second and fourth path derivatives at the seam give

\[
\partial_t^2\Theta(t,1)\big|_{t=0},
\qquad
\partial_t^4\Theta(t,1)\big|_{t=0}.
\]

At \(r=1\),

\[
\Phi(0)
=
\left[
\frac1{4\pi^2}\partial_t^4
+
\frac3{2\pi}\partial_t^2
\right]\Theta(t,1)\bigg|_{t=0}.
\]

Equivalently,

\[
\Phi(0)
=
-\frac12
\left[
\frac1{4\pi^2}\partial_t^4
+
\frac3{2\pi}\partial_t^2
\right]\mathcal W'(t)\bigg|_{t=0}.
\]

This is the first exact window-to-completed-theta comparison formula.

## Why the odd front is absent here

The completed source \(\Phi\) is reflection-even, so only even \(z\)-jets
appear. The reciprocal-odd companion is obtained by the scale derivative
\(\Phi'\), not by inserting an odd window coefficient into this formula.

Odd \(z\)-jets belong to the differentiated-comb or oriented-front channel.
They must remain separately typed. Scalar symmetrization of the two fronts
would erase them.

## Global scale propagation

For \(r\ge1\), the heat semigroup propagates the \(r=1\) window slice forward:

\[
\Theta(\cdot,r)
=
e^{\frac{r-1}{4\pi}\partial_z^2}
\Theta(\cdot,1).
\]

This propagation is smoothing and contractive on the standard periodic
Hilbert scales.

For \(0<r<1\), backward heat evolution from \(r=1\) is not uniformly bounded.
The source must instead use Poisson reciprocity,

\[
\Theta(z,r)
=
r^{-1/2}
\sum_k e^{-\pi k^2/r}e^{2\pi ikz},
\]

and propagate forward in the reciprocal variable \(1/r\). This gives the
direct and reciprocal sectors their correct analytic roles.

## Zero-mode compatibility

The \(z\)-constant Fourier mode is annihilated by both
\(\partial_z^2\) and \(\partial_z^4\). Therefore the even-jet completion
formula kills the wall exactly, in agreement with

\[
\left(\partial_u^2-\frac14\right)h_0=0.
\]

The wall must still be retained through the Wronskian connecting morphism.

## Constructor status

The linear comparison is now explicit:

1. comb-pair and differentiate the window path to obtain \(\Theta(z,1)\);
2. propagate by the heat semigroup in the direct sector or by Poisson-dual
   heat flow in the reciprocal sector;
3. apply the fixed even jet
   \[
   \frac{r^2}{4\pi^2}\partial_z^4
   +
   \frac{3r}{2\pi}\partial_z^2;
   \]
4. attach the half-density \(e^{u/2}\);
5. retain the zero mode relatively.

This closes the linear source formula relating the two branches.

## Remaining gate

The Green-polarized comparison remains open. One must prove that the heat
propagator, even-jet observer, endpoint traces, and Wronskian connecting map
form one closable relative Green square. In particular:

- derivative evaluation at \(z=0\) needs a declared Sobolev/analytic rigging;
- direct and reciprocal heat flows need compatible metrics;
- the oriented odd front must be retained;
- radical descent must precede quadratic block congruence.

No mixed Green form, Adams edge, or boundary pencil is yet promoted.

## Source locators

- research/nima/the-jacobi-heat-kernel-is-the-first-common-carrier-for-window-shift-and-theta-scale.md
- research/nima/the-wronskian-lagrange-boundary-map-is-the-relative-connecting-morphism-for-the-killed-wall.md
- research/nima/the-completion-differential-annihilates-the-wall-so-the-common-carrier-must-be-relative.md
- research/nima/theta-exact-modular-lattice-weight-rigidity.md
