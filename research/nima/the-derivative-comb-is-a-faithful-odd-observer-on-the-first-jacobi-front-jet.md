# The derivative comb is a faithful odd observer on the first Jacobi front jet

## Scope

The full Jacobi comb is reflection-even and therefore annihilates the oriented front. This note identifies the smallest source-native repair: retain the distributional derivative of the comb and do not evaluate away the first elliptic jet.

This closes a finite observer-rank question. It does **not** identify the elliptic odd jet with the scale-odd completed-theta current, and it does not yet construct the mixed Adams Green form.

## Conventions

Use the Fourier transform

\[
\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx
\]

and the integer Dirac comb

\[
\Delta=\sum_{n\in\mathbb Z}\delta_n.
\]

Poisson summation gives \(\widehat\Delta=\Delta\). Distributional differentiation gives

\[
\widehat{\Delta'}(\xi)
=
2\pi i\,\xi\,\Delta(\xi)
=
2\pi i\sum_{k\in\mathbb Z}k\,\delta_k.
\]

Thus the odd observer is preserved by Poisson transport, but changes type from a derivative comb to a weighted comb. This is an ordered, positive-distribution-order port; it is not covered by any rigidity statement restricted to order-zero modular measures.

For \(r>0\), put

\[
g_{z,r}(x)=e^{-\pi r(x+z)^2},
\qquad
\Theta(z,r)=\langle\Delta,g_{z,r}\rangle
=\sum_{n\in\mathbb Z}e^{-\pi r(n+z)^2}.
\]

## Exact odd pairing

By the definition of the distributional derivative,

\[
\begin{aligned}
\langle\Delta',g_{z,r}\rangle
&=
-\sum_{n\in\mathbb Z}\partial_x g_{z,r}(n)\\
&=
2\pi r\sum_{n\in\mathbb Z}(n+z)e^{-\pi r(n+z)^2}\\
&=
-\partial_z\Theta(z,r).
\end{aligned}
\]

The sign is fixed by the source orientation of \(\Delta'\). Reflection sends \(z\mapsto-z\) and \(\Delta'\mapsto-\Delta'\), so this port has exactly the reciprocal-odd character missing from the scalar comb.

At the symmetric seam,

\[
\langle\Delta',g_{0,r}\rangle=0.
\]

This is not observer failure. It says that an odd functional vanishes on an even state. The retained datum is its action on the first oriented front jet:

\[
\left.
\partial_z\langle\Delta',g_{z,r}\rangle
\right|_{z=0}
=
-\partial_z^2\Theta(0,r).
\]

## Strict faithfulness on the first front jet

Consider the two-dimensional first-jet plane

\[
J_r=\operatorname{span}\{g_{0,r},\,\dot g_{0,r}\},
\qquad
\dot g_{0,r}=
\left.\partial_zg_{z,r}\right|_{z=0}.
\]

Use the even and odd observers

\[
E(F)=\langle\Delta,F\rangle,
\qquad
O(F)=\langle\Delta',F\rangle.
\]

Parity gives

\[
E(\dot g_{0,r})=0,
\qquad
O(g_{0,r})=0.
\]

The remaining diagonal entries are

\[
E(g_{0,r})=\Theta(0,r)>0
\]

and

\[
O(\dot g_{0,r})
=
-\partial_z^2\Theta(0,r).
\]

The Jacobi heat equation

\[
\partial_r\Theta=\frac1{4\pi}\partial_z^2\Theta
\]

therefore yields

\[
O(\dot g_{0,r})
=
-4\pi\,\partial_r\Theta(0,r).
\]

Since

\[
\partial_r\Theta(0,r)
=
-2\pi\sum_{n\ge1}n^2e^{-\pi rn^2}<0,
\]

we obtain the exact positive value

\[
O(\dot g_{0,r})
=
8\pi^2\sum_{n\ge1}n^2e^{-\pi rn^2}>0.
\]

Hence the observer matrix in the ordered basis \((g_{0,r},\dot g_{0,r})\) is diagonal:

\[
\begin{pmatrix}
\Theta(0,r)&0\\
0&-\partial_z^2\Theta(0,r)
\end{pmatrix},
\]

and has rank two for every finite \(r>0\).

This proves that the value comb together with the derivative comb is jointly faithful on the first Jacobi front jet. The full-comb cancellation found previously is exactly a rank-one scalar projection, not a loss in the unevaluated jet packet.

## Quantitative range

Both diagonal observer entries are continuous and strictly positive for \(r>0\). Therefore every compact interval

\[
0<r_-\le r\le r_+<\infty
\]

has a positive lower frame bound.

There is no unnormalized global lower bound as \(r\to\infty\), because

\[
-\partial_z^2\Theta(0,r)
=
8\pi^2e^{-\pi r}+O(e^{-4\pi r}).
\]

Thus completion claims must either remain on compact scale regions, pass through reciprocal sewing, or introduce a source-authorized intensive normalization. Finite faithfulness alone does not authorize a uniform end margin.

## Constructor consequence

The smallest odd Jacobi packet is

\[
(\Delta,\Delta')
\quad\longleftrightarrow\quad
\left(\Delta,\,2\pi i\,\xi\Delta\right)
\]

under Poisson transport. Its value and first-jet ports separate the even front state from its oriented tangent.

The next unresolved comparison is narrower:

> Construct a source-authorized map from this elliptic odd jet to the scale-odd completed-theta/Wronskian port, preserving reflection, prime labels, wall routing, and compact-region frame bounds.

Until that comparison exists, the derivative comb is an exact odd observer for the Jacobi cell, but not yet the arithmetic Adams orientation itself.
