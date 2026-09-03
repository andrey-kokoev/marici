# Near-null polynomial is a high-difference observer

## Question

Does the coefficientwise \(4^m\) prime bound on the near-null polynomial reflect the exact quadratic form, or does observer coherence expose cancellations before estimation?

## Claim boundary

The exact quadratic form is a single high finite difference. Therefore the \(4^m\) coefficientwise cost is not intrinsic; it results from taking absolute values before binomial cancellation. No sign or rank-uniform prime bound is proved.

## Near-null probe

Take

\[
p_m(y)=(1-y)^m
=
\sum_{i=0}^m(-1)^i\binom mi y^i.
\]

For a kernel sampled at \(t+kh\), write

\[
H_k=H(t+kh)
\]

and

\[
b_k=H_k-H_{k+1}.
\]

The Hankel quadratic form is

\[
Q_H(p_m)
=
\sum_{i,j=0}^m
(-1)^{i+j}
\binom mi\binom mj
b_{i+j}.
\]

Vandermonde convolution gives

\[
\sum_{i+j=k}
\binom mi\binom mj
=
\binom{2m}{k}.
\]

Hence

\[
Q_H(p_m)
=
\sum_{k=0}^{2m}
(-1)^k\binom{2m}{k}(H_k-H_{k+1}),
\]

which telescopes to

\[
Q_H(p_m)
=
\sum_{k=0}^{2m+1}
(-1)^k\binom{2m+1}{k}H_k.
\]

With

\[
\Delta_hH(t)=H(t)-H(t+h),
\]

this is exactly

\[
Q_H(p_m)=\Delta_h^{2m+1}H(t).
\]

## Why the old bound is lossy

The coefficient norm used by a termwise absolute estimate is

\[
\left(
\sum_{i=0}^m\binom mi
\right)^2
=4^m.
\]

But the exact functional annihilates every sampled polynomial in \(k\) of degree below \(2m+1\). In particular, a constant kernel contributes zero although the coefficientwise bound assigns it cost \(4^m\).

Thus the exponential factor is an artifact unless the prime kernel oscillates at the full finite-difference scale.

## Integral derivative form

For a sufficiently differentiable scalar kernel \(F\),

\[
\Delta_h^qF(t)
=
(-1)^q
\int_{[0,h]^q}
F^{(q)}(t+u_1+\cdots+u_q)
\,du_1\cdots du_q.
\]

For the near-null direction, \(q=2m+1\). This converts the prime problem from a coefficientwise sum into a high-derivative or finite-difference estimate for each log-Gaussian prime atom.

The derivative estimate may still grow rapidly with \(m\); that growth must be calculated rather than replaced by \(4^m\) a priori.

## Observer interpretation

The polynomial observer and the translation observer are not independent. The special polynomial \((1-y)^m\) is precisely the \((2m+1)\)-fold difference observer acting on \(H\). This is another observer--observer relation, and its coherencer is the Vandermonde identity.

Its algebraic coherence residue is zero. The remaining quantitative residue is the ratio

\[
\frac{|\Delta_h^{2m+1}K_{\mathrm{prime}}(t)|}
     {\Delta_h^{2m+1}K_{\Gamma,\mathrm{leading}}(t)}.
\]

## Disposition

The previously identified \(4^m\) prime obstruction is not yet established as intrinsic. The next discriminating calculation is an exact or saddle-point bound for the high finite difference of

\[
t^{-1/2}
\exp\left(-\frac{(\log n)^2}{4t}\right)
\]

summed with \(\Lambda(n)n^{-1/2}\), compared in the same high-difference norm to the leading gamma energy.

## Verification

- `research/voevodsky/checkers/check_near_null_high_difference_observer.py`
- `research/voevodsky/results/near_null_high_difference_observer.json`
