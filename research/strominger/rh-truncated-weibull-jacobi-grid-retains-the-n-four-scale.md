# The truncated Weibull Jacobi grid retains the n-four scale

## Question

Does compact deletion at \(X=\log12\) immediately falsify the unshifted \(n^4\) Jacobi scaling diagnostic?

For \(\beta=1/4\), truncated moments have an integer-shape incomplete-gamma formula. With \(u_0=X^{1/4}\), their common exponential factor cancels from Gram--Schmidt:

\[
\mu_r^{\geq X}
\propto
4\frac{(4r+3)!}{2^{4r+4}}
\sum_{k=0}^{4r+3}\frac{(2u_0)^k}{k!}.
\]

A 100-digit Decimal Gram--Schmidt computation followed by translation \(y=x-X\) gives, at degree six,

\[
\frac{a_6^{(X)}}{6^4}=188.16436,
\qquad
\frac{b_6^{(X)}}{6^4}=524.86071.
\]

The unshifted values are \(188.08652\) and \(524.69367\). Thus compact deletion does not falsify the candidate scale through degree six.

## Disposition

Complete the finite shifted-grid diagnostic. The close degree-six values motivate, but do not prove, compact-truncation Jacobi stability. The next leaf is `truncation-coefficient-relative-grid`: extend exact incomplete-gamma computations in degree and tail start while monitoring precision and Hankel conditioning.

## Claim boundary

Finite agreement is not a two-sided asymptotic bound. Decimal precision is computational control, not a proof that cancellation remains controlled at untested degrees.
