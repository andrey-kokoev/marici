# The oriented Hurwitz--polylogarithm pair closes the source-comb Fourier intertwiner

## Question

Does the newly verified oriented radial Mellin operator carry the actual shifted-support seed through its complete four-port Fourier orbit, including the missing orientation information?

## Claim boundary

Yes on the meromorphic distribution/test-dual rung after separating the zero atom. The shifted comb becomes an ordered Hurwitz-zeta pair, its Fourier image becomes an ordered periodic-polylogarithm pair, and the previously derived Tate gamma matrix is exactly their Fourier functional-equation operator. Hilbert Gram equality with an external G4 carrier remains unproved.

## Shifted comb

Let

$$
a=\frac rq\in(0,1),
\qquad
P_a=\sum_{n\in\mathbb Z}\delta_{n+a}.
$$

Separate positive and negative radii before Mellin transformation. Pairing with \(|x|^{-s}\) gives

$$
\mathcal M_{\rm or}P_a(s)
=
\begin{pmatrix}
\displaystyle\sum_{n\ge0}(n+a)^{-s}\\[2mm]
\displaystyle\sum_{m\ge1}(m-a)^{-s}
\end{pmatrix}
=
\begin{pmatrix}
\zeta(s,a)\\
\zeta(s,1-a)
\end{pmatrix}.
$$

Unlike their symmetric sum, this ordered pair distinguishes \(a\) from \(1-a\).

## Character comb

With the Fourier convention

$$
\widehat f(y)=\int f(x)e^{-2\pi ixy}\,dx,
$$

Poisson summation gives

$$
\mathcal FP_a
=
C_{-a}
=
\sum_{k\in\mathbb Z}e^{-2\pi iak}\delta_k.
$$

Retain the atom at \(k=0\) as a separate endpoint port. The nonzero oriented Mellin image is

$$
\mathcal M_{\rm or}^{\times}C_{-a}(s)
=
\begin{pmatrix}
\displaystyle\sum_{k\ge1}e^{-2\pi iak}k^{-s}\\[2mm]
\displaystyle\sum_{k\ge1}e^{+2\pi iak}k^{-s}
\end{pmatrix}
=
\begin{pmatrix}
\operatorname{Li}_s(e^{-2\pi ia})\\
\operatorname{Li}_s(e^{+2\pi ia})
\end{pmatrix}.
$$

The zero atom is not hidden in either convergent Dirichlet series.

## Fourier functional equation

The exact oriented radial kernel

$$
K_{\epsilon',\epsilon}(v,u)
=e^{(u+v)/2}
 e^{-2\pi i\epsilon\epsilon'e^{u+v}}
$$

has logarithmic Mellin multiplier

$$
G(t)=
\begin{pmatrix}
m_+(t)&m_-(t)\\
m_-(t)&m_+(t)
\end{pmatrix},
$$

$$
m_\sigma(t)
=(2\pi)^{-1/2+it}
\Gamma\left(\frac12-it\right)
 e^{-i\sigma\pi(1/2-it)/2}.
$$

Applying this operator distributionally to the ordered Hurwitz pair gives the ordered periodic pair with spectral reflection. In parity coordinates, the sum is the cosine/even functional equation and the difference is the sine/odd functional equation. Thus both the \(\pm1\) and \(\pm i\) branches are retained.

## Orbit closure

Reflection sends

$$
P_a\longmapsto P_{1-a}
$$

and exchanges the two Hurwitz components. A further Fourier step gives the conjugate periodic pair. Therefore the source map

$$
P_a
\longmapsto
(\zeta(s,a),\zeta(s,1-a))
$$

and the gamma-matrix transport determine all four ports of the cyclic comb orbit without fitted phase choices.

## External boundary

This proves the finite sewing comparison on the common meromorphic distribution rung whenever external sewing means the additive Fourier action on the declared comb orbit. It does not prove:

- membership in the external weighted Green Hilbert carrier;
- equality of orbit Gram matrices in that carrier;
- acceptance by the current three-port G4 contract;
- absorption of the zero atom into a bulk Mellin channel.

## Disposition

The missing source-derived support-port image and its complete order-four radial transport are explicit: shifted support gives the ordered Hurwitz pair, character support gives the ordered polylogarithm pair, and the Tate gamma matrix is their sewing operator. External G4 identification is now reduced purely to topology/Gram acceptance and contract typing, not to an unknown analytic kernel or phase.