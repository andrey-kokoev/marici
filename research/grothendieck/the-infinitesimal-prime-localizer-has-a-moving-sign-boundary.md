# The infinitesimal prime localizer has a moving sign boundary

## Question

Does passing from finite differences to the infinitesimal localizer make the prime source term positive?

## Exact derivative

For `a=log n`, the prime heat summand is

\[
P_n(t)
=-\frac{\Lambda(n)}{2\sqrt{\pi n}}
 t^{-1/2}e^{-a^2/(4t)}.
\]

Its contribution to the infinitesimal localizer `-P'(t)` is

\[
- P_n'(t)
=
\frac{\Lambda(n)}{8\sqrt{\pi n}}
 t^{-5/2}e^{-a^2/(4t)}
(a^2-2t).
\]

Therefore its sign changes exactly at

\[
t=\frac{(\log n)^2}{2}.
\]

At fixed `t`, prime powers with

\[
\log n<\sqrt{2t}
\]

contribute negatively, while those beyond the threshold contribute positively.

## Consequence

The infinitesimal identity

\[
Q_{t,h}(F)=\int_0^h E_{t+s}(F)\,ds
\]

localizes the finite-mesh cone but does not produce a positive prime density. The source sign split moves with heat scale and cuts across prime powers. Any positive factor must couple the negative low-prime region to the positive tail and archimedean term before taking a norm square.

This is a source-specific obstruction, not generic GNS circularity. A multiplication-square factor using the individual differentiated prime weights is impossible once the threshold passes a prime power.

## Relation to sampled calculations

For the current numerical boxes, `t<=0.08` and

\[
(\log2)^2/2\approx0.2402,
\]

so every prime-power derivative term is still positive. The observed rank-two sector failure there therefore comes from correlations among shifted samples and gamma coupling, not from negative infinitesimal prime weights.

At larger heat, prime sign-indefiniteness appears already at the scalar infinitesimal level, beginning with `n=2`, then crossing successive prime powers.

## Moving saddle distinction

The derivative sign boundary occurs at `log n` of order `sqrt(t)`, while the continuum prime saddle occurs at `log n` of order `t`. These are distinct scales. The dominant saddle may remain in the positive derivative region even though finitely many low-prime channels have become negative.

## Falsifier

Any proposed infinitesimal source Gram factor that assigns independent positive squared features to each prime-power derivative coefficient fails for `t>(log2)^2/2`. A viable factor must include an explicit nonlocal compression or cancellation identity and cannot be obtained by merely differentiating the prime heat sum.

## Disposition

Retain the infinitesimal cone as an equivalent localization only. Use the moving sign boundary as a required test for any concrete pre-positivity factor.