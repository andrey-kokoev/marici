# Atomic log moments have gamma comparators with unimodal error

## Question

Can every entry of the infinite atomic Gram matrix be bounded without enumerating labels through its moment saddle?

## Atomic entry and integral comparator

For integer \(r\geq0\), define

\[
G_r=\sum_{n\ge2}
\frac{(\log n)^r}{n e^{2a(\log n)^\beta}}.
\]

Set

\[
g_r(t)=\frac{(\log t)^r}{t e^{2a(\log t)^\beta}},
\qquad t\ge1.
\]

Its full integral is exact:

\[
I_r=\int_1^\infty g_r(t)dt
=
\int_0^\infty x^r e^{-2ax^\beta}dx
=
\frac1\beta(2a)^{-(r+1)/\beta}
\Gamma\!\left(\frac{r+1}{\beta}\right).
\]

## Unimodal error lemma

The logarithmic derivative of \(g_r(e^x)\) is

\[
\frac r x-1-2a\beta x^{\beta-1}.
\]

For \(r>0\), it crosses zero once; for \(r=0\), the summand is decreasing. Hence \(g_r\) is nonnegative and unimodal on \([1,\infty)\).

Partition the sum and integral at an integer adjacent to the mode. On each monotone side, the integral test brackets every unit interval by its endpoint values. Only the two intervals adjacent to the mode remain unmatched. Therefore

\[
|G_r-I_r|\leq2\sup_{t\ge1}g_r(t).
\]

Finite removal of the anchor labels is exact, so the tail Gram entries used by the constrained correction problem inherit the same error after subtracting their known atoms.

## Scope of the bound

This estimate replaces inaccessible label enumeration by a gamma value and a local mode calculation. It is entrywise. If

\[
H_K=(G_{j+k})_{0\leq j,k\leq K},
\]

then bounds on each \(G_r\) do not imply

\[
H_K^-\preceq H_K\preceq H_K^+
\]

for matrices formed by independently choosing entry endpoints. Hankel inversion can amplify correlated errors, so a Christoffel or quadratic-form bound remains necessary.

## Disposition

The infinite atomic Gram matrix is now controlled entrywise without direct enumeration. This closes the scalar tail problem but not the matrix inverse problem governing anchored minimum norms.

## Claim boundary

No polynomial-density, indeterminacy, or weak-limit conclusion is drawn from the entrywise estimate. Matrix positivity must be retained in the next step.
