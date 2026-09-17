# Regulator-independent quarter trace

The normalized quarter does not depend on identifying the channel heat operator with the historical rotor weight.

## Four-chart theorem

Let `R` be any positive trace-class operator on one chart carrier. Transport it around the Fourier helix:

\[
R_i=W^iRW^{-i}.
\]

Unitary invariance gives

\[
\operatorname{Tr}(R_i)=\operatorname{Tr}(R).
\]

On the four-chart sum set

\[
R_{tot}=R_0\oplus R_1\oplus R_2\oplus R_3.
\]

For the chart projection `P_i`,

\[
\frac{\operatorname{Tr}(P_iR_{tot})}
{\operatorname{Tr}(R_{tot})}
=\frac{\operatorname{Tr}(R)}{4\operatorname{Tr}(R)}
=\frac14.
\]

This applies to the channel heat operator, resolvent powers, and the historical weighted rotor operator whenever each is transported by the chart equivalence. Their unnormalized traces may differ.

## Catalan theorem

Let `N` be the channel number operator. Every triangulation incidence vector has norm squared `n-3`, so for any radial regulator `f(N)`,

\[
f(N)|_{H_n}=f(n-3)I.
\]

For every projection `P` on `H_n`,

\[
\frac{\operatorname{Tr}(P f(N))}
{\operatorname{Tr}(f(N)|_{H_n})}
=\frac{\operatorname{rank}P}{\dim H_n}.
\]

The forced-channel ratio remains

\[
\frac{C_{n-3}}{C_{n-2}}
\longrightarrow\frac14,
\]

and the polygon-rotation character ratios retain their central-symmetry correction and the same limit.

## Historical rotor comparison

The prior rotor completion uses

\[
w_s(t)=(1+t^2)^{-s}.
\]

Its translation-covariant centered family and the Fourier-chart transport provide equal chart traces by conjugacy. This proves agreement of the normalized quarter with the channel heat model. A spectral identification between rotor coordinate `t` and channel norm `|m|` is unnecessary for that conclusion.

`check_quarter_trace_regulator_independence.py` tests heat, resolvent, and polynomial weights and verifies both the exact chart quarter and the regulator-independent Catalan ratios through `n=100`.
