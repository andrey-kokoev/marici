# Gap leverage is relative optimal monic-norm loss

## Question

Can rank-one gap leverage be represented without a Fredholm resolvent?

Let \(h_n\) be the squared norm of the degree-\(n\) monic orthogonal polynomial for the full Weibull measure, and \(h_n^{\geq X}\) the corresponding optimal monic norm after restriction to \([X,\infty)\). Since

\[
D_{n+1}=h_nD_n,
\qquad
D_{n+1}^{\geq X}=h_n^{\geq X}D_n^{\geq X},
\]

the gap ratio satisfies

\[
\frac{G_{n+1}}{G_n}
=
\frac{h_n^{\geq X}}{h_n},
\qquad
G_n=\frac{D_n^{\geq X}}{D_n}.
\]

Combining with the rank-one determinant lemma gives the exact identity

\[
\ell_n=1-rac{h_n^{\geq X}}{h_n}.
\]

Thus leverage is the relative loss of the optimal monic norm caused by deleting the compact interval.

Both norms are Schur complements. If \(H_n=(\mu_{i+j})_{i,j<n}\) and \(v_n=(\mu_{n+i})_{i<n}\), then

\[
h_n=
\mu_{2n}-v_n^*H_n^{-1}v_n,
\]

with the identical formula for truncated moments. This moves the decay problem from a restricted Fredholm resolvent to a ratio of two explicit moment Schur complements.

## Disposition

Resolve the leverage representation. The next leaf is `monic-norm-loss-asymptotic`: prove

\[
1-h_n^{\geq X}/h_n=O_X(n^{-2})
\]

using incomplete-gamma moment structure while respecting Hankel conditioning.

## Claim boundary

The identity is exact. Entrywise moment closeness still does not control either Schur complement, so no decay bound follows without a stable large-Hankel argument.
