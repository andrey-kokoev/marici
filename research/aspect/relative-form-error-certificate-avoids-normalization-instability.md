# Relative-form error certificate avoids normalization instability

## Question

Can a finite physical block approximation certify strict return without separately controlling numerical errors in inverse square roots of its diagonal sectors?

## Form-level certificate

Let

\[
H=\operatorname{diag}(A,D)
\]

be the exact diagonal reference form and let \(G\) be the exact complete coupled form. Suppose finite source-derived forms \(\widehat G,\widehat H\) satisfy

\[
\widehat G\ge\widehat\eta\,\widehat H,
\]

and the omitted terms obey the relative-form bounds

\[
G-\widehat G\ge-\varepsilon_G H,
\qquad
\widehat H\ge(1-\varepsilon_H)H.
\]

Then

\[
G
\ge
\bigl[\widehat\eta(1-\varepsilon_H)-\varepsilon_G\bigr]H.
\]

Thus the exact coercivity constant is certified by

\[
\eta=
\widehat\eta(1-\varepsilon_H)-\varepsilon_G>0.
\]

This yields the return margin

\[
1-\|K\|\ge2\eta-\eta^2.
\]

No approximate inverse square root enters the theorem.

## Why raw entry errors are insufficient

An absolute matrix-entry residual has no invariant meaning near a small eigenvalue of \(A\) or \(D\). Normalization can amplify it without bound. The errors must be measured relative to the exact positive form \(H\), or accompanied by a separately proved uniform lower spectral bound converting absolute errors into relative ones.

## Exact boundary

With \(\widehat\eta=1/4\) and \(\varepsilon_H=1/10\), the admissible form-error budget is strictly below \(9/40\). At \(\varepsilon_G=1/20\), one obtains \(\eta=7/40\). At \(\varepsilon_G=9/40\), the certificate reaches zero exactly; finite positivity of \(\widehat G\) does not prevent terminal cancellation in the omitted form.

## Sector allocation

If omitted physical sectors satisfy

\[
G-\widehat G=\sum_sE_s,
\qquad
E_s\ge-\varepsilon_sH,
\]

then one may take \(\varepsilon_G=\sum_s\varepsilon_s\). This turns wall, history, tail, and PV truncation estimates into a common coercivity budget without asserting orthogonality.

## Uniformity gate

Every constant in the certificate must be uniform over primes on source-derived reduced supports. A finite-prime minimum of \(\widehat\eta_p\), or pointwise relative convergence, does not prove the required global bound.

## Verification

`research/aspect/checkers/check_relative_form_error_certificate.py` verifies strict, exact-boundary, and failed budgets with rational arithmetic.

## Disposition

The finite physical constructor may now return forms and one-sided relative residual bounds rather than normalized operators. The first missing datum is a prime-uniform reference-form comparison for the omitted wall–history–tail/PV contribution.
