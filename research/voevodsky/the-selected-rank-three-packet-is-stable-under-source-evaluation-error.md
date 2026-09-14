# The selected rank-three packet is stable under source evaluation error

## Error model

For the selected equally spaced packet, assign error at most \(10^{-6}\) to the directly evaluated diagonal value and at most \(2\times10^{-6}\) to kernel entries formed using a diagonal value and one computed deficit.

These allowances are much larger than the prime-tail, gamma-tail, quadrature-convergence, and standard floating accumulation estimates already recorded. They retain the explicit qualification concerning platform elementary-function evaluation.

## Matrix perturbation

Let \(G\) be the computed Gram matrix and \(E\) its unknown evaluation error. The maximum absolute row sum of \(E\) is at most

\[
5\times10^{-6}.
\]

Therefore

\[
\lVert E\rVert_2
\leq
5\times10^{-6}.
\]

The smallest numerical eigenvalue of \(G\) is approximately

\[
0.0238115187.
\]

Weyl's eigenvalue perturbation inequality then gives

\[
\lambda_{\min}(G+E)
\geq
0.0238115187-0.000005
>0.0238065.
\]

Thus the rank-three packet remains positive definite throughout the declared source-evaluation error box.

## Scope

This is a conditional perturbation certificate, not a directed interval certificate. It establishes that numerical conditioning is not the obstacle at this packet: the positivity gap exceeds the declared evaluation uncertainty by more than three orders of magnitude.

## Verification

```text
python research/voevodsky/checkers/check_rank_three_perturbation_certificate.py
```

Artifacts:

- `research/voevodsky/checkers/check_rank_three_perturbation_certificate.py`
- `research/voevodsky/results/rank_three_perturbation_certificate.json`
