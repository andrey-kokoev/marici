# Gap leverage retains n-minus-two scaling through degree seventeen

## Question

Does a higher-degree, independently precision-checked grid falsify \(\ell_n=O(n^{-2})\)?

Using exact incomplete-gamma moments, Gram--Schmidt was run at 320 and 520 decimal digits through degree eighteen. The resulting leverages agree beyond 250 digits.

The scaled values increase slowly:

\[
n^2\ell_n=0.08205,0.08259,0.08306,0.08346,0.08382,0.08414
\]

for \(n=12,\ldots,17\). Their late spread is below five percent and remains below the determinant coefficient near \(0.09\).

## Disposition

Complete the extended leverage diagnostic. It does not falsify \(n^{-2}\) decay and narrows the likely coefficient, but finite stabilization is not a theorem.

The next leaf is `leverage-recurrence-representation`: express \(\ell_n\) through the endpoint-selected Jacobi solution or a Schur complement in a form amenable to analytic decay bounds.

## Claim boundary

Precision agreement controls numerical cancellation only. It supplies no uniform bound beyond degree seventeen.
