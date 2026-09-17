# Convolution and product are one monoidal object in two Pontryagin charts

## Exact homeomorphism

For the universal channel lattice

\[
L_n=\mathbb Z^{D_n}
\]

and its compact Pontryagin dual

\[
\mathbb T_n=\operatorname{Hom}(L_n,U(1)),
\]

Plancherel--Pontryagin Fourier transform is a unitary homeomorphism

\[
\mathcal F:\ell^2(L_n)\xrightarrow{\cong}L^2(\mathbb T_n).
\]

On the dense convolution algebra where products are typed,

\[
\mathcal F(f*g)=(\mathcal Ff)(\mathcal Fg).
\]

Hence convolution and pointwise multiplication are not independent structures. They are one monoidal product transported across a homeomorphism:

\[
\mu_{\cdot}
=\mathcal F\,\mu_*\,(\mathcal F^{-1}\times\mathcal F^{-1}).
\]

The correct object is a topological algebra presentation groupoid with two objects

\[
(\ell^2(L_n),*)
\quad\text{and}\quad
(L^2(\mathbb T_n),\cdot)
\]

and Fourier equivalences between them. Strictly, arbitrary `L2` pairs need not have products in `L2`; the algebra statement is made on the declared dense algebra or graph domains, while Fourier remains unitary on the Hilbert completions.

## Four-chart orbit

On incidence atoms,

\[
\delta_v\mapsto\chi_{-v}\mapsto\delta_{-v}
\mapsto\chi_v\mapsto\delta_v.
\]

Thus

\[
\mathcal F^4=1,
\]

and the four chart labels are an orbit of one periodic object rather than four unrelated carriers. Convolution and product alternate around the orbit. Polygon rotation commutes with the Fourier transition, so geometric rotation does not destroy this presentation identification.

## What can be quotiented

The binary label

\[
\text{convolution chart}/\text{product chart}
\]

can be moved from object-state data into the morphisms of the homeomorphism groupoid. One may choose the lattice chart as a base presentation and recover the product chart by transport.

The fourfold phase cannot always be discarded entirely: it records the monodromy `F^2` (reflection) and, after graded lift, the suspension on wrap. But it is presentation/monodromy data, not four independent analytic spaces.

## Boundary: historical physical Fourier

This identification is exact for the canonical channel-lattice/Pontryagin model. It is not an identification with oriented radialized additive Fourier. Their kernels are

\[
e^{-2\pi i\langle m,u\rangle}
\quad\text{and}\quad
e^{-2\pi i e^{m+u}},
\]

respectively. A Jacobian cannot repair that phase mismatch. The carriers have a finite-packet embedding, but the displayed generators are not topologically conjugate.

Therefore the first presentation quotient is accepted canonically and rejected for the direct historical radial comparison.
