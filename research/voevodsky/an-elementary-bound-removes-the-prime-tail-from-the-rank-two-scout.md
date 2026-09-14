# An elementary bound removes the prime tail from the rank-two scout

## Tail to control

After truncating the prime-power sum at \(N\), each omitted crossed-Gaussian component is bounded using

\[
\Lambda(n)\leq\log n.
\]

It is enough to control sums of the form

\[
\sum_{n>N}
\frac{\log n}{\sqrt n}
\exp\left(-\frac{(\log n-d)^2}{8\sigma}\right).
\]

For the parameters in the scout, the summand is decreasing beyond the cutoff. It is therefore bounded by its first omitted value plus the corresponding integral.

## Explicit integral

Set

\[
x_0=\log N,
\qquad
\mu=d+2\sigma.
\]

After substituting \(x=\log y\) and completing the square, the integral becomes

\[
e^{d/2+\sigma/2}
\int_{x_0}^{\infty}
 x\exp\left(-\frac{(x-\mu)^2}{8\sigma}\right)dx.
\]

This has an explicit expression in terms of the complementary error function and a Gaussian endpoint term. Applying it to the \(+d\), \(-d\), and zero-centered components bounds the absolute omitted contribution to the rank-two deficit.

## Result

At cutoff

\[
N=1{,}200{,}000,
\]

the largest computed upper bound over the complete scan was approximately

\[
3.91\times10^{-64}.
\]

For the narrow-width region \(\sigma\leq0.05\), the largest bound was approximately

\[
5.98\times10^{-130}.
\]

These bounds are overwhelmingly smaller than the smallest reported positive narrow-width margin, approximately \(6.15\times10^{-10}\). Prime truncation therefore cannot explain or reverse those sampled margins.

## Scope

The analytic inequality is elementary and does not use the prime number theorem. The printed decimal evaluations use ordinary floating arithmetic rather than directed interval rounding.

This does not yet certify the full deficit. Remaining numerical errors are:

- truncation of the asymptotic digamma expansion;
- quadrature error in the gamma integral;
- floating cancellation among source sectors.

The next certification target is the gamma integral. Unlike the prime tail, it is now the dominant uncontrolled error.

## Verification

```text
python research/voevodsky/checkers/check_two_translate_prime_tail_bound.py
```

Artifacts:

- `research/voevodsky/checkers/check_two_translate_prime_tail_bound.py`
- `research/voevodsky/results/two_translate_prime_tail_bound.json`
