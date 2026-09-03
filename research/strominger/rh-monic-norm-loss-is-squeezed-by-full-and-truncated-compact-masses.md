# Monic-norm loss is squeezed by full and truncated compact masses

## Question

What variational estimates can prove

\[
1-h_n^{\geq X}/h_n=O_X(n^{-2})?
\]

Let \(\pi_n\) minimize the full monic norm and \(q_n\) minimize the truncated monic norm. Write \(C=[0,X]\). Testing \(\pi_n\) in the truncated problem gives

\[
h_n^{\geq X}
\leq h_n-\int_C|\pi_n|^2d\nu,
\]

hence

\[
\frac1{h_n}\int_C|\pi_n|^2d\nu
\leq\ell_n.
\]

Testing \(q_n\) in the full problem gives

\[
h_n
\leq h_n^{\geq X}+\int_C|q_n|^2d\nu,
\]

so

\[
\ell_n
\leq
\frac1{h_n}\int_C|q_n|^2d\nu
\leq
\int_C|Q_n^{\geq X}|^2d\nu,
\]

where \(Q_n^{\geq X}=q_n/\sqrt{h_n^{\geq X}}\), using \(h_n^{\geq X}\leq h_n\).

Thus leverage is squeezed between the compact mass of the full orthonormal polynomial and the exterior continuation mass of the truncated orthonormal polynomial.

## Disposition

Resolve the variational reduction. An \(O(n^{-2})\) upper bound for

\[
\int_0^X|Q_n^{\geq X}(x)|^2d\nu(x)
\]

proves the monic-norm-loss theorem.

The next leaf is `truncated-exterior-polynomial-mass`: control the continuation of polynomials orthonormal on \([X,\infty)\) back across the deleted compact interval.

## Claim boundary

The squeeze is exact and one-sided where stated. It gives no exterior continuation bound by itself.
