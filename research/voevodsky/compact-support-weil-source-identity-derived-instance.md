# Derived compact-support Weil source identity

## Question

Can the two-variable source formula be transported to the compact zero-extended interval functions used by the certificate, with every normalization explicit?

## Claim boundary

The derivation identifies the coded quadratic form and its closure from smooth compact tests to the logarithmic Fourier-form domain. Its source is the repository packet `research/grothendieck/explicit-two-variable-weil-heat-source-formula.md`; independent comparison with an external edition of the classical explicit formula remains required before calling the instance publication-authoritative.

## Smooth compact test

For \(f\in C_c^\infty(-L,L)\), set

\[
Ff(u)=\int_{\mathbb R}f(x)e^{-iux}\,dx,
\qquad
\mathcal Ff=(2\pi)^{-1/2}Ff,
\]

and use the Hermitian entire test

\[
h_f(z)=Ff(z)\overline{Ff(\overline z)}.
\]

On the real axis, \(h_f(u)=|Ff(u)|^2\). Fourier inversion gives

\[
\frac1{2\pi}\int_{\mathbb R}|Ff(u)|^2e^{iua}\,du
 =\langle f,T_a f\rangle,
\qquad
(T_af)(x)=f(x+a),
\]

with both functions zero-extended outside \([-L,L]\).

## Source-side quadratic identity

Substituting \(h_f\) into the centered half-divisor formula gives

\[
Q_L(f)=E(f)+G(f)+P_L(f),
\]

where

\[
E(f)=\operatorname{Re}\left(
  \int f(x)e^{x/2}\,dx\;
  \overline{\int f(x)e^{-x/2}\,dx}
\right),
\]

\[
G(f)=\frac12\int_{\mathbb R}
\left(\operatorname{Re}\psi(1/4+iu/2)-\log\pi\right)
|\mathcal Ff(u)|^2\,du,
\]

and

\[
P_L(f)=-\sum_{\log n\leq2L}
\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle f,T_{\log n}f\rangle.
\]

Terms with \(\log n>2L\) vanish by disjoint support. In unitary Fourier coordinates, the prime term has multiplier

\[
-\sum_{\log n\leq2L}\frac{\Lambda(n)}{\sqrt n}
\cos(u\log n).
\]

The endpoint matrix for real coordinates is therefore

\[
\frac{a_+a_-^*+a_-a_+^*}{2},
\qquad
(a_\pm)_j=\int p_j(x)e^{\pm x/2}\,dx.
\]

This is the factor missing from the superseded checker.

## Closure to zero-extended polynomial tests

Let \(\mathcal H_{\log,L}\) be the zero-extended functions supported in \([-L,L]\) for which

\[
\int_{\mathbb R}\log(2+|u|)|\mathcal Ff(u)|^2\,du<\infty.
\]

The gamma multiplier is bounded in magnitude by a constant times \(1+\log(2+|u|)\). Translation is unitary on \(L^2(\mathbb R)\), and each endpoint functional is bounded on fixed support by Cauchy--Schwarz. Hence all three terms are continuous in the graph norm of \(\mathcal H_{\log,L}\).

Zero-extended interval polynomials have Fourier decay \(O(|u|^{-1})\), so they lie in this domain. Standard convolution followed by an interior cutoff approximates them by \(C_c^\infty(-L,L)\) in every fractional Sobolev norm \(H^s\) with \(0<s<1/2\); since the logarithmic weight is bounded by a constant times \((1+|u|^2)^s\), convergence also holds in \(\mathcal H_{\log,L}\). The smooth identity therefore extends to the polynomial span used by the checker without adding a boundary term.

## Disposition

The internal source-to-matrix comparison is now explicit and explains the endpoint factor \(1/2\). The coded first-prime certificate applies to the closure of compact smooth tests represented by its polynomial span. The remaining authority gate is external source verification of the centered half-divisor formula and its Schwartz-test hypotheses; this packet does not manufacture that authority.
