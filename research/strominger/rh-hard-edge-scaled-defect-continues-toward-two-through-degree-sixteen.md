# The hard-edge scaled defect continues toward two through degree sixteen

## Question

Does a higher-degree precision grid falsify

\[
n^2\frac{a_n+a_{n+1}-b_n}{a_{n+1}}\to2?
\]

A 320-versus-520-digit incomplete-gamma Gram--Schmidt calculation extends the truncated recurrence through degree sixteen. The scaled defects increase monotonically. For \(n=10,\ldots,16\), they are

\[
1.5085,
1.5456,
1.5774,
1.6051,
1.6295,
1.6510,
1.6701.
\]

All remain below two, and the two precision runs agree beyond 250 digits.

## Disposition

Complete the extended defect diagnostic. It strengthens compatibility with the limit two but does not prove convergence or exclude a larger-degree turn.

The next leaf is `hard-edge-defect-correction-model`: determine whether \(2-n^2\varepsilon_n\) follows a stable inverse-power law and identify the asymptotic input needed for proof.

## Claim boundary

Monotone finite approach is not a bound by two for all degrees and is not a convergence theorem.
