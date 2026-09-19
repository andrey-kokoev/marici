# The source-selected saturated branch places sigma-z in direct diagonal loadings, not mixed Schur covariance

## Branch selection

The resolved source ordering selects the Fourier-saturated joint comparison
form. On its wall/tail sector,

\[
G_{\rm joint,res}
=(1+M_\Phi^2)I+B^*B,
\]

with exact zero wall--tail cross block. The Adams grade ray preserves this
branch with cutoff-compatible contractive control.

Consequently the mixed even/odd Schur model is not the authoritative source of
the first-Adams `sigma_z` coordinate on this branch:

\[
\alpha_p=0
\]

whenever the remaining seam/endpoint comparisons preserve the saturated
character splitting.

## Direct diagonal channel

Orthogonality of wall and tail does not mean equal diagonal energies. A direct
resolved block

\[
G_{\rm dir}
=
\begin{pmatrix}
r_p&0\\
0&s_p
\end{pmatrix}
\]

has Pauli decomposition

\[
G_{\rm dir}
=
\frac{r_p+s_p}{2}I
+
\frac{r_p-s_p}{2}\sigma_z.
\]

Thus the missing directed energy coordinate can arise from unequal direct
wall/tail loadings while the cross block remains exactly zero.

## Complete target ledger

The selected target has the additive form

\[
G_\theta
=G_{\rm sat}
+G_{\rm jump}
+G_{\rm Wr}
+G_{\rm window}
+G_{f_3},
\]

on one common closed relative domain. Its total Pauli coordinates must equal

\[
(a+4b,\ a-4b,\ 4v,\ 4u).
\]

In particular, the exact diagonal test is

\[
\sum_R
\left((G_R)_{11}-(G_R)_{22}\right)
=8u,
\]

where `R` runs over saturated, jump, Wronskian, window, and fourth-grade
contributions.

The exact off-diagonal test is

\[
\sum_R(G_R)_{12}
=a-4b-4iv.
\]

## Current earliest gate

Before these entries can be added, seam transport composed with endpoint
attachment must be proved to:

- preserve the resolved saturated comparison graph;
- carry radicals into radicals;
- have closed range in the full source pushout;
- retain the prime-labelled two-column incidence.

Only after this domain theorem is it legitimate to combine the component
Green tables.

## Disposition

Direction 1 has selected its authoritative quadratic branch. The mixed Schur
covariance is a hostile alternative unless a later comparison explicitly
breaks saturated character preservation. The productive calculation is now
the direct component ledger and its `8u` diagonal-balance test.