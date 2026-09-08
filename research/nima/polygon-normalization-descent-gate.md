# Polygon normalization descent gate

## Question

Which finite source-normalization data would determine the single oriented point scalar propagated by residue factorization?

## Claim boundary

The theorem converts admitted polygon normalizations into a constraint on the base scalar. It does not promote presented unit coefficients into source data.

From residue recursion, the `n`-point normalization is

\[
c_n=s^{n-2}.
\]

If a source-to-volume comparison proves `c_n=1` for sizes in a set `S`, then

\[
s^g=1,\qquad g=\gcd\{n-2:n\in S\}.
\]

This follows from Bezout relations among the exponents when `s` is invertible. One even exponent leaves at least the sign ambiguity `s=+1` or `s=-1`. One odd exponent fixes the real oriented scalar to one but can leave non-real roots if the coefficient field is not restricted.

Unit normalization at any two adjacent sizes removes all root ambiguity over every field: their exponents are consecutive and

\[
\frac{s^{n-1}}{s^{n-2}}=s=1.
\]

In particular, source-authorized unit comparisons at four and five points would fix `s=1`. The existing five-point reference slice has unit Jacobian coefficients only relative to its declared coordinate volume. Without the missing source-to-volume map, that presentation cannot be used as the premise `c_5=1`.

## Disposition

The normalization acceptance request can be finite: one source-authorized odd-exponent normalization with a real orientation convention, or unit normalizations at two adjacent polygon sizes, determines the entire tower. Provenance of those comparisons remains the blocker.
