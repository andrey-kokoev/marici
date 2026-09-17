# Tate-prime channel realization

The artificial binary supports can be replaced by arithmetic support coordinates from finite places.

Choose a distinct rational prime `p_d` for every polygon channel `d` and place the channel atom at the oriented logarithmic coordinate

\[
x_d=\log p_d.
\]

For a triangulation `T`, convolution gives

\[
*_{d\in T}\delta_{\log p_d}
=\delta_{\sum_{d\in T}\log p_d}
=\delta_{\log N_T},
\qquad
N_T=\prod_{d\in T}p_d.
\]

Unique factorization makes `T -> N_T` injective. Under Mellin/Laplace evaluation this atom is the squarefree Euler monomial

\[
N_T^{-s}=\prod_{d\in T}p_d^{-s}.
\]

The four analytic presentations are

\[
\delta_{\log N_T}
\xrightarrow{\mathcal F}
\chi_{-\log N_T}
\xrightarrow{\mathcal F}
\delta_{-\log N_T}
\xrightarrow{\mathcal F}
\chi_{\log N_T}
\xrightarrow{\mathcal F}
\delta_{\log N_T}.
\]

Thus channel gluing is simultaneously:

- convolution of oriented log atoms;
- multiplication of squarefree Euler monomials;
- pointwise multiplication of Fourier characters in the odd charts.

At `n=12`, the first 54 primes (through 251) distinguish all 16,796 triangulations and all 67,184 chart states without external tags.

## Remaining naturality issue

The assignment `d -> p_d` is faithful but not canonical: polygon rotation permutes chosen finite places, while no corresponding automorphism of `Q` permutes rational primes arbitrarily. Hence this is a Tate-coordinate realization, not yet an intrinsic arithmetic realization.

A genuinely canonical version needs either:

1. a coefficient ring whose named places are functorially indexed by channels, or
2. a proof that the realization is independent, up to admitted place relabelling, of the injection `D_n -> Spec(Z)`.

The first option is naturally provided by a multivariable Euler/Tate torus with one coordinate place per channel. Specialization to distinct rational primes then recovers the concrete model above.

`check_tate_prime_channel_realization.py` verifies unique-factorization injectivity and the exact Fourier cycle at `n=4,8,12`.
