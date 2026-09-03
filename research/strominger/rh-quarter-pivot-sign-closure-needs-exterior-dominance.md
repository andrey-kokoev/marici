# Quarter pivot sign closure needs exterior dominance

## Question

Does the sign-skew Schur class preserve itself under one-pivot elimination using signs alone?

## Claim boundary

The exact classification covers 5,376 one-pivot updates across all relevant order-eight principal Schur complements. It does not prove the required magnitude inequality at arbitrary size.

## Disposition

For a Schur matrix \(M\), elimination at \(p\) gives

\[
M'_{ij}=M_{ij}-\frac{M_{ip}M_{pj}}{M_{pp}}.
\]

In all 1,792 cases with \(i<p<j\), the correction has the opposite sign and therefore reinforces \(M_{ij}\) automatically. In all 3,584 exterior-pivot cases, the correction has the same sign; every case satisfies

\[
|M_{ij}|>rac{|M_{ip}M_{pj}|}{M_{pp}}.
\]

Thus sign data close only interior elimination. Exterior closure needs a quantitative multiplicative inequality. The next leaf is `quarter-schur-multiplicative-monge-dominance`, testing whether these inequalities form a coherent Monge-type system on absolute Schur entries that can be preserved inductively.
