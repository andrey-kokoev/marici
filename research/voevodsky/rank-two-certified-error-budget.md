# Certified error budget for the rank-two gate

## Question

How accurately must the four endpoint--gamma--prime samples be enclosed to certify the sign of the first Turán determinant?

## Claim boundary

An exact perturbation budget is derived and verified. The received prime-tail estimate has not been independently recomputed, and gamma interval quadrature remains absent.

## Moment-level bound

Let

\[
D=a_0a_2-a_1^2
\]

and suppose computed centers \(\widehat a_k\) satisfy

\[
|a_k-\widehat a_k|\leq\eta_k.
\]

Writing \(a_k=\widehat a_k+e_k\) gives

\[
D-\widehat D
=
\widehat a_2e_0
+
\widehat a_0e_2
-2\widehat a_1e_1
+e_0e_2-e_1^2.
\]

Therefore

\[
|D-\widehat D|
\leq
|\widehat a_2|\eta_0
+|\widehat a_0|\eta_2
+2|\widehat a_1|\eta_1
+\eta_0\eta_2
+\eta_1^2.
\]

Call the right side \(E_D\). Then:

- \(\widehat D>E_D\) certifies \(D>0\);
- \(\widehat D<-E_D\) certifies \(D<0\);
- otherwise the result is indeterminate.

## Four-sample propagation

For

\[
a_k=X_k-X_{k+1},
\]

suppose

\[
|X_k-\widehat X_k|\leq\varepsilon_k.
\]

Then

\[
\eta_k\leq\varepsilon_k+\varepsilon_{k+1}.
\]

Thus four outward-rounded sample enclosures determine a rigorous interval for \(D_2\) without assuming independent errors.

A sector tail bound \(T(s)\) similarly contributes

\[
\eta_k^{\rm tail}
\leq
T(t+kh)+T(t+(k+1)h).
\]

Endpoint, gamma, prime, and rounding contributions can be added at the \(\eta_k\) level before evaluating \(E_D\).

## Prime-tail consequence

The received prime estimate reports a controlling exponent below \(-459\) for cutoff \(N=200000\) and sampled arguments through \(0.08\). If independently verified with outward rounding, this places the prime truncation far below the observed \(10^{-8}\) determinant margin.

That does not certify the determinant by itself. It reallocates the meaningful error budget to:

- gamma integral or series quadrature;
- gamma-tail control;
- completed gamma normalization;
- interval rounding and cancellation.

## Why direct determinant intervals may be preferable

The slope-curvature coordinates isolate the mechanism but divide by \(a_0,b_0\). If either lower bound approaches zero, interval division can amplify errors. The direct determinant budget avoids division and is therefore the fallback certification chart.

Use the slope chart when sector masses have strong positive lower bounds. Use the direct chart when denominator uncertainty dominates. Agreement of both enclosures is a useful implementation cross-check but not additional mathematical evidence.

## Exact fixtures

The dependency-free checker verifies:

- the determinant perturbation bound at all error-box vertices;
- propagation from four sample errors to three moment errors;
- certified positive and negative cases;
- an indeterminate case whose enclosure crosses zero.

## Disposition

The rank-two numerical claim now has a complete certification interface. Its first missing typed object is four outward-rounded gamma sample enclosures with a proved tail. Once supplied, the determinant sign follows by exact rational error propagation.

## Verification

- `research/voevodsky/rank-two-certified-error-budget-v1.json`
- `research/voevodsky/checkers/check_rank_two_certified_error_budget.py`
- `research/voevodsky/results/rank_two_certified_error_budget.json`
