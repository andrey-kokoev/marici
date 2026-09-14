# Source-side scout finds rank-two compensation and severe cancellation

## Computation

The rank-two antisymmetric deficit was evaluated directly from the endpoint, digamma-integral, and von Mangoldt terms of the shifted-Gaussian source formula. No zero locations were used.

The scan used

\[
0.005\leq\sigma\leq0.1,
\qquad
0.1\leq d\leq3,
\]

and prime powers through \(1{,}200{,}000\).

## Outcome

No numerically significant negative deficit was found. Before the roundoff-dominated regime, the smallest sampled value was approximately

\[
6.15\times10^{-10}
\]

at \(\sigma=0.05\) and \(d=0.5\).

At \(\sigma=0.1\), separate source contributions have ordinary size while their sum is near machine precision. For example, at \(d=3\), the approximate contributions are

\[
-1.42175,
\quad
-0.36103,
\quad
-0.27042,
\quad
2.05321.
\]

Their residual is about \(-9.3\times10^{-15}\), which is treated as floating cancellation rather than a falsifier.

## Interpretation

The prime sector numerically compensates the combined endpoint and gamma deficit in the sampled region. The compensation becomes extremely ill-conditioned as the width increases. This confirms that separate sector bounds are unlikely to certify rank-two positivity: they discard the cancellation carrying nearly the entire answer.

The scout does not prove positivity. Its digamma asymptotics, numerical quadrature, finite prime cutoff, and floating arithmetic are not interval-certified.

## Next gate

A rigorous rank-two certificate should target the narrow-width cases first and use:

1. interval evaluation of the digamma integral;
2. exact von Mangoldt summation through a certified cutoff;
3. an explicit log-Gaussian prime-tail bound;
4. cancellation-aware accumulation rather than independent coarse sector intervals.

The near-zero wider-width regime will require substantially higher precision or an analytically combined representation.

## Verification

```text
python research/voevodsky/checkers/scout_two_translate_weil_deficit.py
```

Artifact:

- `research/voevodsky/results/two_translate_weil_deficit_scout.json`
