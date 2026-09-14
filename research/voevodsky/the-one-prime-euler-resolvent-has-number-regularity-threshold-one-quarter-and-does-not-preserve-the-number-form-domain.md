# The one-prime Euler resolvent has number regularity threshold one quarter and does not preserve the number-form domain

## Prime-resolvent vacuum

Let

\[
B_p=(I-p^{-1/2}e^{i(\log p)X})^{-1}
\]

and let `e_0` be the degree-zero polynomial vector. The exact lowest-weight `SU(1,1)` coefficient is

\[
M_{m0}(x)
=
i^m
\sqrt{\frac{(1/2)_m}{m!}}
(\tanh x)^m(\operatorname{sech}x)^{1/2}.
\]

The `k`-th Euler term is evaluated at

\[
x=k\log p,
\qquad y=e^{-x}=p^{-k}.
\]

For large `m,x`, its magnitude is comparable to

\[
m^{-1/4}y\exp(-2my^2).
\]

## The geometric grid still covers every degree scale

For every sufficiently large `m`, choose `k=k(m)` so that

\[
p^{-k}
\asymp_p
m^{-1/2}.
\]

The ratio between adjacent allowed values of `y` is the fixed number `p`, so such a choice exists with constants depending only on `p`. Consequently

\[
y\exp(-2my^2)
\asymp_p
m^{-1/2}.
\]

All one-sided Neumann terms in a fixed row have the same phase `i^m` and nonnegative remaining factors. Hence there is no cancellation. Comparison of the geometric sum with its maximal term gives the two-sided estimate

\[
\boxed{
|(B_pe_0)_m|
\asymp_p
m^{-3/4}
}
\]

for the allowed parity, with the other parity determined by the Fourier convention. This holds across all sufficiently large degrees of that parity, not merely a sparse subsequence.

## Correct fractional-domain threshold

For `alpha>=0`, membership in `Dom N^alpha` requires

\[
\sum_m
m^{2\alpha}|(B_pe_0)_m|^2
<\infty.
\]

Using the full-degree estimate,

\[
m^{2\alpha}|(B_pe_0)_m|^2
\asymp
m^{2\alpha-3/2}.
\]

The series converges exactly when

\[
2\alpha-
\frac32<-1,
\]

i.e.

\[
\boxed{
\alpha<\frac14.
}
\]

Therefore

\[
\boxed{
B_pe_0\in\operatorname{Dom}N^\alpha
\quad(\alpha<1/4),
}
\]

but

\[
\boxed{
B_pe_0\notin\operatorname{Dom}N^{1/4}.
}
\]

## Number-form failure

The quadratic-form domain of `N` is

\[
\operatorname{Dom}N^{1/2}.
\]

Since `1/2>1/4`,

\[
\boxed{
B_pe_0
\notin
\operatorname{Dom}N^{1/2}.
}
\]

Thus the Euler resolvent fails to preserve not only the operator domain of `N`, but even its quadratic-form domain.

This corrects the earlier sparse-subsequence count, which incorrectly gave threshold `3/4`. A sparse geometric subsequence tests only whether its selected terms are summable; the optimizing prime-power grid remains within a fixed multiplicative factor of every degree scale and therefore yields the `m^(-3/4)` tail throughout the parity subsequence.

## Consequence for a common polynomial form core

The vacuum `e_0` lies in every power domain of the archimedean number operator, but its Euler transform does not lie in the semilocal number-form domain under the naive common-carrier identification. Hence the archimedean polynomial core cannot be a common form core for the two number operators.

The proposed form difference

\[
q_{N,S}-q_N
\]

is not defined on `e_0` after this identification.

A different source-derived domain or additional smoothing must be inserted before the forms can be compared.

## Minimal smoothing order on the source

If one applies a source smoothing operator with degree decay

\[
(1+N)^{-\sigma},
\]

the vacuum itself is unchanged, so smoothing only on the input side does not repair this particular vector. The smoothing must act after the Euler transform or be incorporated symmetrically into the comparison map.

A candidate is

\[
(1+N)^{-r/2}
B_p
(1+N)^{-r/2}.
\]

The left factor supplies degree decay `m^(-r/2)` to the transformed vacuum. Form-domain membership then requires

\[
\sum_m
m
m^{-r}
m^{-3/2}<\infty,
\]

or

\[
-r-
\frac12<-1.
\]

Thus

\[
\boxed{
r>\frac12}
\]

is necessary and sufficient for this ground-column form test.

This does not prove a global operator bound, but it gives the first unavoidable smoothing threshold.

## Implication for prolate smoothing

If the archimedean prolate operator has degree growth of order `N^beta` in the relevant sector, then a sandwich

\[
(1+|W_{\lambda,\infty}|)^{-s/2}
B_p
(1+|W_{\lambda,\infty}|)^{-s/2}
\]

supplies approximate degree decay `N^(-beta s/2)` on the output. The ground-column test requires

\[
\boxed{
\beta s>\frac12.
}
\]

The actual value of `beta` and cancellations in the prolate operator must be established from its spectral asymptotics before choosing `s`.

## Revised domain strategy

A viable comparison must proceed as follows:

1. choose a two-sided smoothing scale exceeding the ground-column threshold;
2. prove the smoothed Euler transform maps a dense domain into `Dom N^(1/2)`;
3. define the difference of smoothed closed forms;
4. only then test compactness or Schatten membership;
5. remove smoothing, if possible, through a controlled distributional limit.

## Disposition

The correct one-prime regularity threshold is

\[
\boxed{
B_pe_0\in\operatorname{Dom}N^\alpha
\iff
\alpha<\frac14
}
\]

at the ground-column level. In particular the unsmoothed Euler map does not preserve the number-form domain. Any prolate scattering comparison requires genuine two-sided smoothing of at least the corresponding relative order.
