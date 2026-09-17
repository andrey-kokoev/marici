# Canonical channel Tate-torus Fourier functor

The arbitrary assignment of channels to rational primes is removed by passing to the universal channel lattice.

For the `n`-gon let `D_n` be its diagonal set and define

\[
L_n=\mathbb Z^{D_n},
\qquad
\mathbb T_n=\operatorname{Hom}(L_n,U(1)).
\]

A triangulation has canonical incidence vector

\[
v_T=\sum_{d\in T}e_d\in L_n.
\]

Define its chart-zero realization by the lattice point mass

\[
R_{0,n}(T)=\delta_{v_T}.
\]

This is injective without tags or choices. Compatible subtree/channel union becomes lattice addition and hence convolution:

\[
\delta_{v_{T_1}}*\delta_{v_{T_2}}
=\delta_{v_{T_1}+v_{T_2}}.
\]

Pontryagin Fourier transform gives

\[
\delta_{v_T}
\xrightarrow{\mathcal F}
\chi_{-v_T}
\xrightarrow{\mathcal F}
\delta_{-v_T}
\xrightarrow{\mathcal F}
\chi_{v_T}
\xrightarrow{\mathcal F}
\delta_{v_T}.
\]

Thus `F^4=1` and the chart products alternate between convolution on `L_n` and pointwise multiplication on `T_n`.

Polygon rotation canonically permutes the basis `e_d`. Its lattice action and contragredient torus action commute with Pontryagin Fourier transform. Consequently the geometric channel rotation and analytic chart successor form a strict commuting/intertwining square, without assigning primes or transporting external tags.

## Exact quarter and asymptotic quarter

The enlarged four-chart carrier contains four copies of the Catalan basis, so each presentation chart has exact normalized weight

\[
\frac{C_{n-2}}{4C_{n-2}}=\frac14
\]

at every degree.

This should be distinguished from the character decomposition of polygon quarter-rotation on one Catalan module. Those four weights differ at finite `n` by the centrally symmetric correction and approach `1/4` asymptotically. The Tate-torus functor explains both statements:

- chart phase has exact weight `1/4` in the enlarged carrier;
- geometric `C4` characters have asymptotic weight `1/4` in one chart.

## Arithmetic specialization

Any homomorphism

\[
L_n\to\mathbb R,
\qquad e_d\mapsto\log p_d,
\]

specializes the universal incidence atom to the earlier Euler monomial

\[
v_T\mapsto\log\prod_{d\in T}p_d.
\]

Distinct-prime specialization is faithful on squarefree incidence vectors by unique factorization. Hence the prime model is a faithful arithmetic point of the canonical multivariable Tate torus, rather than part of its definition.

`check_canonical_tate_torus_realization.py` verifies injectivity, Fourier order four, rotation/Fourier commutation, and exact chart weight `1/4` on every triangulation at `n=4,8,12`.
