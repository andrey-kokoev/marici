# Correction: the image rank-one term is positive in the required comparison

The principal whole-line logarithmic kernel is negative off the diagonal:

\[
h(t)=-\frac1{|t|}
\]

in the declared cosine-transform normalization. The spectral Dirichlet kernel
is the odd periodization

\[
K_D=\sum_k[h(x-y+2k\ell)-h(x+y+2k\ell)].
\]

The lower-bound comparison uses `K_zero-K_D`, not `K_D-K_zero`. Therefore its
image remainder is

\[
-\sum_{k\ne0}h(x-y+2k\ell)
+\sum_k h(x+y+2k\ell).
\]

Under the paired regularization, the telescoping constant `1/(2ell)` found in
the unsigned image audit enters `K_zero-K_D` with positive sign. Its
half-normalized rank-one form is positive semidefinite and may be discarded in
a lower bound. It must not be charged as a negative budget.

Thus the safe lower-bound budget reverts to

\[
C_\partial\le\frac\pi{\sqrt3}+\log2-\frac38,
\]

while the rank-one term remains recorded explicitly as favorable. The
`M=22134` threshold is valid but nonsharp; the earlier `M=13425` threshold is
the applicable bound after orientation is included.
