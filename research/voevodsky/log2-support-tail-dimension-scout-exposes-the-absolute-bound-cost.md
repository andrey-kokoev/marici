# The log-two support scout exposes the cost of the absolute prime bound

## Question

At the first support window containing the prime powers \(2,3,4\), what scale does the explicit trace-based tail certificate require?

## Claim boundary

A high-precision floating scout at \(L=\log2\) shows that the absolute prime bound forces an exterior frequency near \(10^9\) and a sufficient trial dimension near \(2\times10^{10}\). This is not a directed-interval certificate. It demonstrates that the current rigorous bound is computationally unusable and localizes the loss to absolute prime domination plus the trace-only concentration estimate.

## Fixed support data

For

\[
L=\log2,
\]

the condition \(\log n\leq2L\) includes

\[
n=2,3,4.
\]

Thus

\[
C_{\rm prime}(L)
=
\frac{\log2}{\sqrt2}
+
\frac{\log3}{\sqrt3}
+
\frac{\log2}{2}
\approx1.47098676261181.
\]

The gamma low-band constant is

\[
C_{\rm low}^{\Gamma}
\approx0.4275047731830422.
\]

## Scout

Using six terms of the large-argument digamma asymptotic, the first exterior frequency satisfying

\[
m_R^\Gamma>C_{\rm prime}(L)
\]

is approximately

\[
R_{\rm threshold}
\approx6.700359289\times10^8.
\]

Optimizing the trace-based sufficient dimension over \(R\) gives approximately

\[
R_*
\approx1.752150730\times10^9,
\]

\[
m_{R_*}^\Gamma
\approx1.5474820367,
\]

and

\[
M_{m sufficient}
=
19{,}962{,}119{,}094.
\]

The computed lower margin is only about

\[
2.4\times10^{-12}.
\]

## Disposition of the oddball

This is an explained bound pathology, not evidence about the Weil form. Two deliberate worst-case estimates compound:

1. the prime sector is replaced by the sum of absolute coefficient magnitudes, discarding oscillatory and geometric cancellation;
2. the concentration spectrum is replaced by the trace inequality
   \[
   \lambda_{M+1}
   \leq
   \frac{2LR}{\pi(M+1)},
   \]
   discarding its rapid decay beyond the concentration transition.

The resulting finite reduction exists but is not executable at this support scale.

## Next discriminating improvement

Retain the exact finite prime translation operator inside the tail rather than bounding it by \(C_{\rm prime}(L)I\). Diagonalize or enclose the combined low-frequency concentration and prime-translation block. Separately, use certified prolate eigenvalue decay rather than the trace alone. Either improvement can lower the required scale; only a computed bound will determine which loss dominates.

## Scope

The scout uses ordinary floating arithmetic and an asymptotic digamma evaluation. It is diagnostic only. It does not certify the displayed threshold, tail positivity, the finite Schur matrix, or RH.

## Verification

- `research/voevodsky/checkers/scout_explicit_tail_dimension_log2.py`
- `research/voevodsky/results/explicit_tail_dimension_log2.json`
