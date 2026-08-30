# The order-two Hausdorff corner is strictly positive

A generic interval-series engine now derives the first six quarter-point
moments. It constructs the regular completed logarithmic derivative from the
certified eta jet, forms the squared-coordinate Stieltjes function

\[
 S(x)=\frac{1}{2s-1}\frac{\Xi'}{\Xi}(s),
 \qquad x=(s-1/2)^2,
\]

and substitutes

\[
 e=s-1=h-h^2+2h^3-5h^4+14h^5+O(h^6),
 \qquad h=x-1/4.
\]

The factor `(2s-1)^(-1)` is essential. Omitting it makes the already-known
`A_1` negative; the checker retains `A_1>0` as a normalization regression.

The newly certified moments are approximately

\[
 A_4=3.1938918608673242\,10^{-12},\qquad
 A_5=1.5758900881660590\,10^{-14}.
\]

All three order-two determinants are enclosed strictly above zero:

\[
\begin{aligned}
\det(A_{i+j})_{0\le i,j\le2}
 &\in 2.15414004153198924\,10^{-22}+[0,9]10^{-37},\\
\det(A_{i+j+1})_{0\le i,j\le2}
 &\in 3.08471321584627138\,10^{-31}+[0,4]10^{-59},\\
\det(4A_{i+j}-A_{i+j+1})_{0\le i,j\le2}
 &\in 1.37627228144335546\,10^{-20}+[0,2]10^{-34}.
\end{aligned}
\]

The lower-support determinant is again the narrowest absolute margin, now at
scale `10^-31`, but its interval width is far smaller. This is the second
complete finite Hausdorff corner and the first one produced by the generic
series architecture.

## Scope

This is unconditional finite-order source positivity without zero locations.
It does not prove the infinite hierarchy, construct the full measure, or prove
RH. The physical relative-chain pushforward remains unavailable and separate.

## Durable verification

- Checker: `checkers/quarter_point_order_two_interval.py`
- Result: `results/quarter-point-order-two-interval.json`
- Eta input: `results/eta-order-six-decimal-interval.json`
