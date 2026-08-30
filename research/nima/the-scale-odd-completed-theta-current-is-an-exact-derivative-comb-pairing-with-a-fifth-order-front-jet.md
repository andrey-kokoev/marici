# The scale-odd completed-theta current is an exact derivative-comb pairing with a fifth-order front jet

## Result

The missing comparison between the elliptic odd Jacobi port and the scale-odd completed-theta port is not an identification of their one-dimensional representations. It is a bilinear contraction:

- the derivative comb supplies an odd observer;
- an odd elliptic front jet supplies an odd state;
- their pairing is an even Jacobi derivative;
- source coefficients and reciprocal scale sewing assemble those derivatives into the scale-odd current \(\Phi'(u)\).

This gives an exact source formula before any Green completion.

## Jacobi and completion conventions

Let

\[
\Theta(z,r)=\sum_{n\in\mathbb Z}e^{-\pi r(n+z)^2},
\qquad
r=e^{2u},
\]

and

\[
H(u)=e^{u/2}\Theta(0,e^{2u}),
\qquad
\Phi(u)=\left(\partial_u^2-\frac14\right)H(u).
\]

The previously established heat-jet formula is

\[
\Phi(u)
=
e^{u/2}
\left[
\frac{r^2}{4\pi^2}\partial_z^4
+
\frac{3r}{2\pi}\partial_z^2
\right]\Theta(z,r)\bigg|_{z=0}.
\]

The heat equation is

\[
\partial_r\Theta=\frac1{4\pi}\partial_z^2\Theta.
\]

## Exact scale derivative

Differentiate the heat-jet formula with respect to \(u\). Since

\[
\partial_u r=2r,
\qquad
\partial_u\partial_z^k\Theta
=
\frac{r}{2\pi}\partial_z^{k+2}\Theta,
\]

one obtains

\[
\Phi'(u)
=
e^{u/2}
\left[
\frac{r^3}{8\pi^3}\partial_z^6
+
\frac{15r^2}{8\pi^2}\partial_z^4
+
\frac{15r}{4\pi}\partial_z^2
\right]\Theta(z,r)\bigg|_{z=0}.
\]

The coefficients follow independently:

\[
\frac{r^2}{4\pi^2}
\longmapsto
\left(\frac12+4\right)\frac{r^2}{4\pi^2},
\]

and the derivative of the fourth jet contributes an additional

\[
\frac{3r^2}{4\pi^2},
\]

giving \(15r^2/(8\pi^2)\). The second-jet coefficient becomes

\[
\left(\frac12+2\right)\frac{3r}{2\pi}
=
\frac{15r}{4\pi}.
\]

## Derivative-comb realization

Let

\[
\Delta'=\sum_{n\in\mathbb Z}\delta_n'
\]

and

\[
g_{z,r}(x)=e^{-\pi r(x+z)^2}.
\]

For every \(k\ge0\),

\[
\left\langle
\Delta',
\left.\partial_z^k g_{z,r}\right|_{z=0}
\right\rangle
=
-\partial_z^{k+1}\Theta(0,r).
\]

Define the source-derived odd front jet

\[
J_{\mathrm{odd}}(u)
=
e^{u/2}
\left[
\frac{r^3}{8\pi^3}\partial_z^5
+
\frac{15r^2}{8\pi^2}\partial_z^3
+
\frac{15r}{4\pi}\partial_z
\right]g_{z,r}\bigg|_{z=0}.
\]

Then the scale-odd completed-theta current has the exact pairing formula

\[
\Phi'(u)
=
-\langle\Delta',J_{\mathrm{odd}}(u)\rangle.
\]

No fitted phase, imaginary Gram entry, or auxiliary Fourier quarter-turn is used. The observer orientation is the distributional orientation of \(\Delta'\); the state is the fifth-order odd Jacobi front jet forced by differentiating the completed source.

## Typing

Both factors are elliptic-odd:

\[
R\Delta'=-\Delta',
\qquad
RJ_{\mathrm{odd}}(u)=-J_{\mathrm{odd}}(u)
\]

for front reflection \(z\mapsto-z\). Their scalar contraction is elliptic-even, as required for evaluation at \(z=0\).

Its scale character is separate. The completed source satisfies the reciprocal symmetry

\[
\Phi(-u)=\Phi(u),
\]

and hence

\[
\Phi'(-u)=-\Phi'(u).
\]

Therefore the odd arithmetic seam character is not the bare elliptic character of either factor. It is the reciprocal-scale character of their source-weighted contraction. This resolves the earlier representation mismatch without identifying elliptic reflection with scale reflection.

Under Poisson transport,

\[
\widehat{\Delta'}=2\pi i\,\xi\Delta.
\]

Consequently the same contraction may be represented by the weighted dual comb, provided the fifth-order front jet is Fourier transported with the matching convention. This is a representation theorem, not a new source of phase.

## Domain and quantitative scope

For every \(r>0\), all Gaussian derivatives in \(J_{\mathrm{odd}}(u)\) are Schwartz functions, so the derivative-comb pairing is absolutely defined. On compact scale intervals

\[
0<r_-\le r\le r_+<\infty,
\]

the map into the Schwartz space and the pairing with \(\Delta'\) are uniformly continuous at every fixed Schwartz seminorm order needed here.

This proves local and compact-region continuity. It does not yet prove:

- a cutoff-uniform prime-labelled direct-sum bound;
- compatibility with the adjacent-window Green radical;
- preservation by endpoint loading and Schur elimination;
- a lower frame bound for the assembled odd arithmetic observer.

## Constructor consequence

The first odd comparison arrow is now explicit:

\[
\text{fifth-order odd Jacobi front jet}
\;\xrightarrow{\ \langle\Delta',-\rangle\ }\;
\Phi'(u).
\]

The next gate is no longer the existence of an elliptic-to-scale odd comparison. It is its integration into the prime-labelled Adams cell:

> Prove that the derivative-comb contraction commutes with prime idempotents, reciprocal sewing, cutoff restriction, and the relative Green/Stokes quotient, with a uniform assembled observer bound on compact off-seam regions.

Until that theorem is proved, the scale-odd current has a source-native Jacobi realization, but the global mixed Adams edge remains incomplete.
