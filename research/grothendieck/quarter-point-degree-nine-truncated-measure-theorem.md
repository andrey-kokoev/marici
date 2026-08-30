# The degree-nine source jet has a positive compact representing measure

For `A_0,...,A_9`, the odd-degree Hausdorff criterion on `[0,4]` is positivity
of

\[
 (A_{i+j+1})_{0\le i,j\le4},\qquad
 (4A_{i+j}-A_{i+j+1})_{0\le i,j\le4}.
\]

All leading minors of both matrices are interval-certified strictly positive.
Sylvester's criterion and the truncated Hausdorff theorem therefore give a
positive Borel measure `mu_9` on `[0,4]` with

\[
 A_k=\int_0^4u^k\,d\mu_9(u),\qquad0\le k\le9.
\]

The five-node Gaussian measure is one positive atomic realization. This is the
first finite positive spectral model produced entirely from the completed
source jet rather than from zero locations.

The result is finite and nonunique: many measures can share ten moments. Only
the all-order hierarchy gives a unique compact measure and global resolvent.

## Scope

This is not a full spectral measure, a physical relative-chain assertion, or
RH.

## Durable verification

- Checker: `checkers/quarter_point_truncated_measure_certificate.py`
- Result: `results/quarter-point-truncated-measure-certificate.json`
