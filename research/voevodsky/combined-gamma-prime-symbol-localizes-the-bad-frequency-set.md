# The combined gamma--prime symbol localizes the bad frequency set

## Question

Can the unusable absolute prime bound be replaced by the exact finite prime translation operator before constructing the positive tail?

## Claim boundary

Yes. On each fixed support window, the gamma and prime sectors combine into one real Fourier multiplier. Tail construction should concentrate only on the sublevel set where this combined symbol is small, rather than on the entire interval from zero to the absolute-bound threshold. This removes the worst-case prime constant from the tail inequality. The measure and geometry of the sublevel set remain to be certified.

## Combined symbol

For fixed \(L\), define

\[
a_L(u)
=
\frac{\operatorname{Re}\psi(1/4+iu/2)-\log\pi}{4\pi}
-
\sum_{\log n\leq2L}
\frac{\Lambda(n)}{\sqrt n}
\cos(u\log n).
\]

The cosine terms are the Fourier symbols of the symmetric translation pairings. Hence

\[
(\Gamma_L+P_L)(f,f)
=
\int_{\mathbb R}a_L(u)|\widehat f(u)|^2du.
\]

## Bad-frequency sublevel set

Choose \(\delta>0\) and define

\[
\Omega_{L,\delta}
=
\{u\in\mathbb R:a_L(u)<\delta\}.
\]

Because the gamma term tends to positive infinity while the finite trigonometric prime sum is bounded, \(\Omega_{L,\delta}\) is bounded and has finite measure.

Let \(\Pi_{L,\delta}\) project onto this frequency set and define

\[
T_{L,\delta}
=
J_L^*\mathcal F^{-1}\Pi_{L,\delta}\mathcal FJ_L.
\]

Its trace is

\[
\operatorname{Tr}(T_{L,\delta})
=
\frac{L}{\pi}|\Omega_{L,\delta}|.
\]

## Tail inequality

Let

\[
C_-(L,\delta)
=
\sup_{u\in\Omega_{L,\delta}}
\max(0,-a_L(u)).
\]

On the complement of the first \(M\) concentration eigenvectors,

\[
\int_{\Omega_{L,\delta}}|\widehat f|^2
\leq
\lambda_{M+1}\lVert f\rVert_2^2.
\]

Therefore

\[
(\Gamma_L+P_L)(f,f)
\geq
\left[
\delta-(\delta+C_-)\lambda_{M+1}
\right]\lVert f\rVert_2^2.
\]

The trace estimate gives the explicit sufficient condition

\[
M+1
>
\frac{L|\Omega_{L,\delta}|}{\pi}
\frac{\delta+C_-}{\delta}.
\]

Endpoint representers are again adjoined to the finite trial space.

## Improvement over absolute domination

The previous method treated every frequency below roughly \(6.7\times10^8\) as potentially bad at \(L=\log2\). The new method retains cancellation in the finite cosine sum and pays only for the actual sublevel-set measure. Whether this makes the certificate computationally feasible is a quantitative question, not assumed here.

## Disposition

The absolute prime bound is removed from the architecture. The first missing executable object is a directed enclosure of \(\Omega_{L,\delta}\), its measure, and \(C_-(L,\delta)\) for a selected \(L,\delta\). The finite Schur gate remains.

## Verification

- `research/voevodsky/checkers/check_combined_gamma_prime_symbol.py`
- `research/voevodsky/results/combined_gamma_prime_symbol.json`
