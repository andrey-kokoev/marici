# D reflected-product factorization

## Question

What exact algebraic object contains the adjacent even/odd coefficient pairing responsible for imaginary-axis dominance?

## Claim boundary

With `A=H D_n` and `P=R+A`, the exact identity is

\[
P(x)P(-x)-R(x)R(-x)=A(x)P(-x)+R(x)A(-x).
\]

The tempting one-sided factorization `A(x)(P(-x)+R(-x))` is false; exact checking exposed and corrected that missing cross-symmetry term. Odd coefficients of the symmetric identity cancel algebraically. In all 21 bounded cases, its even coefficients have sign `(-1)^k`, equivalent to the established positive coefficients of `|P(i omega)|^2-|R(i omega)|^2`. This remains bounded sign evidence, not a uniform theorem.

## Disposition

Adjacent parity matching is not an isolated Hurwitz minor; it is the symmetric sum of two reflected convolution products. The next proof target is a sign-reversing involution pairing terms between `A(x)P(-x)` and `R(x)A(-x)` while leaving positive even-index residues.
