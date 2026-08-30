# The Jacobi heat kernel is the first common carrier for window shift and theta scale

The affine no-go does not force an arbitrary bridge. The source Poisson grammar
already supplies a two-parameter common carrier: the Jacobi heat kernel.

## Two-parameter carrier

Define

\[
\Theta(z,r)
=
\sum_{n\in\mathbb Z}
e^{-\pi r(n+z)^2},
\qquad r>0.
\]

The variable \(z\) is additive lattice displacement. The variable \(r\) is
Gaussian scale. These must remain distinct.

Poisson summation gives the exact source identity

\[
\Theta(z,r)
=
r^{-1/2}
\sum_{k\in\mathbb Z}
e^{-\pi k^2/r}e^{2\pi ikz}.
\]

Thus the carrier simultaneously retains:

- additive translation in \(z\);
- Fourier modulation in the dual label \(k\);
- multiplicative scale in \(r\);
- the zero Fourier mode;
- primal–dual lattice sewing.

## Adjacent-window slice

Let

\[
W_t(q)=H(q+t)-H(q-t),
\qquad
H'(q)=-e^{-\pi q^2}.
\]

Comb-pair the window with the integer lattice:

\[
\mathcal W(t)
=
\sum_{n\in\mathbb Z}W_t(n).
\]

The sum is understood through the differentiated Schwartz family. Then

\[
\mathcal W'(t)
=
-\sum_n e^{-\pi(n+t)^2}
-
\sum_n e^{-\pi(n-t)^2}.
\]

Since \(\Theta(-t,1)=\Theta(t,1)\),

\[
\mathcal W'(t)=-2\Theta(t,1).
\]

Therefore the two-front Gaussian window cell lands exactly on the elliptic
slice

\[
(z,r)=(t,1)
\]

of the Jacobi carrier.

## Completed-theta slice

The multiplicative theta precursor uses

\[
\vartheta(e^{2u})
=
\sum_{n\in\mathbb Z}
e^{-\pi n^2e^{2u}}.
\]

Hence

\[
\vartheta(e^{2u})
=
\Theta(0,e^{2u}).
\]

The completed source is obtained from the modular slice \(z=0\) by attaching
the half-density and applying

\[
\partial_u^2-\frac14.
\]

Thus the completed theta history and the lattice-sampled window history are
not images of one another. They are two boundary slices of one
two-parameter Poisson object:

\[
\text{window front}:\quad r=1,\ z=t,
\]

\[
\text{theta scale}:\quad z=0,\ r=e^{2u}.
\]

## Resolution of the affine no-go

The forbidden direct map tried to identify \(z\) with \(\log r\). The Jacobi
carrier does not do that. It embeds additive translation and multiplicative
scale as independent commuting coordinates of a larger object.

Consequently there is no contradiction with

\[
D_aT_bD_a^{-1}=T_{b/a}.
\]

The semidirect action is represented on the full \((z,r)\)-plane before either
boundary slice is taken.

## Wall typing

In the Poisson representation, the dual zero mode is

\[
r^{-1/2}.
\]

After the source half-density is attached, this becomes the universal wall
solution killed by the completion differential. Therefore the wall is visible
on the Jacobi carrier, maps to zero under completion, and returns through the
Wronskian connecting morphism. The three previous facts now belong to one
source object.

## First comparison square

The lawful comparison is not a map from a window front to a theta label. It is
the square

\[
\begin{array}{ccc}
\Theta(z,r)&\xrightarrow{\text{restrict }r=1}&\Theta(z,1)\\
\downarrow{\text{restrict }z=0}&&\downarrow{\text{comb window derivative}}\\
\Theta(0,r)&\xrightarrow{\text{half-density completion}}&\text{relative boundary data}.
\end{array}
\]

The lower-right corner must be interpreted as a relative/mapping-cone object
because completion kills the zero mode.

## Remaining analytic gates

This identifies the source carrier and the two restriction maps. It does not
yet prove that Green polarization commutes around the square. The next theorem
must establish:

1. a rigged Jacobi heat space supporting both restrictions;
2. continuity of \(r=1\) and \(z=0\) traces;
3. compatibility of the heat equation with both source connections;
4. retention of the zero mode in the relative domain;
5. the endpoint-jet image of the window path;
6. radical descent and quadratic Green congruence;
7. prime/grade attachment after the Jacobi comparison.

The smallest hostile is a function with correct two boundary slices but a
different interior Jacobi/heat extension. Therefore the heat equation and
Poisson law are essential authority, not optional interpolation.

## Consequence

The earliest missing representation-changing constructor is now concretely
identified:

\[
\text{Jacobi heat-kernel correspondence}
\]

rather than an unspecified affine-to-Mellin transform. It joins the additive
window and multiplicative theta lanes without conflating their parameters.

No mixed Green form, Adams edge, boundary pencil, or coercivity claim follows
until the Jacobi Green square is proved.

## Source locators

- research/nima/theta-exact-modular-lattice-weight-rigidity.md
- research/nima/theta-global-fourier-action-exists-boundary-observer-lift-is-missing.md
- research/nima/theta-gaussian-vacuum-selection-produces-a-lattice-ward-current-not-yet-rh-orientation.md
- research/nima/no-nonzero-affine-equivariant-map-can-relabel-window-translations-as-theta-dilations.md
- research/nima/the-wronskian-lagrange-boundary-map-is-the-relative-connecting-morphism-for-the-killed-wall.md
