# Truncation Jacobi relative errors show an n-minus-three grid

## Question

How do shifted/unshifted recurrence differences depend on degree and tail start?

Exact incomplete-gamma moments were evaluated with independent 90- and 150-digit Gram--Schmidt runs for \(q=3,12,48\) and degrees one through eight. The runs agree beyond the reported precision threshold.

At degree eight, the relative off-diagonal errors are

\[
9.61\times10^{-5},\quad1.74\times10^{-4},\quad2.40\times10^{-4},
\]

and relative diagonal errors are

\[
7.90\times10^{-5},\quad1.43\times10^{-4},\quad1.97\times10^{-4}.
\]

For fixed \(q\), the off-diagonal late-degree values are consistent with an \(n^{-3}\) decay. For example, at \(q=12\), multiplying the off-diagonal relative errors by \(n^3\) gives approximately \(0.0902\) at \(n=4\) and \(0.0892\) at \(n=8\). A subsequent log--log fit gives diagonal slopes near \(-2.72\), so the grid does not support assigning the same exponent to \(b_n\).

## Disposition

Complete the relative-grid diagnostic. Promote only the conjectures

\[
\frac{a_n^{(X)}}{a_n}-1=O_X(n^{-3}),
\qquad
\frac{b_n^{(X)}}{b_n}-1=O_X(n^{-\gamma})
\quad\text{for some }\gamma>1.
\]

The fitted diagonal exponent is diagnostic, not a theorem or a selected exact value. The next leaf is `truncation-relative-asymptotic-proof`. Summable relative perturbations in both coefficients would provide the natural input for asymptotic comparison of Jacobi transfer products.

## Claim boundary

The exponent \(-3\) is inferred from a short exact-input grid, not proved. The constants increase with \(q\), so no uniform moving-start estimate follows.
