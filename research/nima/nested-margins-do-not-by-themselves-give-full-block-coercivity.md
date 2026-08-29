# Nested margins do not by themselves give full-block coercivity

## Sheetwise diagonal bounds

Suppose on reduced supports that

\[
S\ge s_0 I,
\qquad
\|K\|\le1-\delta_{\mathrm{aux}}.
\]

Then for both reciprocal sheets,

\[
D_\pm=S^{1/2}(I\pm K)S^{1/2}
\ge
\delta_{\mathrm{aux}}S
\ge
s_0\delta_{\mathrm{aux}}I.
\]

Hence

\[
\|D_\pm^{-1}\|
\le
\frac1{s_0\delta_{\mathrm{aux}}}.
\]

Likewise, if

\[
A\ge a_0I,
\qquad
\|L_\pm\|\le1-\delta_{\mathrm{load}},
\]

then

\[
G_{\mathrm{eff},\pm}
=
A^{1/2}(I-L_\pm^{*}L_\pm)A^{1/2}
\]

satisfies

\[
G_{\mathrm{eff},\pm}
\ge
a_0
\left(1-(1-\delta_{\mathrm{load}})^2\right)I.
\]

Thus the exact endpoint coercivity factor associated with a norm margin is

\[
2\delta_{\mathrm{load}}-\delta_{\mathrm{load}}^2,
\]

not merely \(\delta_{\mathrm{load}}\).

## Exact block factorization

For either sheet, the complete enlarged cell has the triangular factorization

\[
\mathcal G_\pm
=
\begin{pmatrix}
I&CD_\pm^{-1}\\
0&I
\end{pmatrix}
\begin{pmatrix}
G_{\mathrm{eff},\pm}&0\\
0&D_\pm
\end{pmatrix}
\begin{pmatrix}
I&0\\
D_\pm^{-1}C^{*}&I
\end{pmatrix}.
\]

This proves positivity from the two nested gates. But it also shows why their margins do not yield a simple product formula for coercivity of \(\mathcal G_\pm\): the triangular comparison can be badly conditioned.

Let

\[
X_\pm=CD_\pm^{-1}.
\]

For \(T_\pm=\begin{pmatrix}I&X_\pm\\0&I\end{pmatrix}\),

\[
\mathcal G_\pm=T_\pm
\operatorname{diag}(G_{\mathrm{eff},\pm},D_\pm)
T_\pm^{*}.
\]

Therefore a lower bound for the full block also requires control of \(T_\pm^{-1}\), equivalently of \(X_\pm\). A coarse valid estimate is

\[
\mathcal G_\pm
\ge
\frac{
\min\{\lambda_{\min}(G_{\mathrm{eff},\pm}),
\lambda_{\min}(D_\pm)\}
}{
\|T_\pm^{-1}\|^2
}
I.
\]

Since

\[
\|X_\pm\|
\le
\frac{\|C\|}{s_0\delta_{\mathrm{aux}}},
\]

absolute incidence and auxiliary scale bounds are indispensable.

## Three quantitative layers

Completion-stable local assembly therefore needs:

1. auxiliary spectral scale and margin:
   \[
   S\ge s_0I,\qquad\delta_{\mathrm{aux}}>0;
   \]
2. endpoint spectral scale and loading margin:
   \[
   A\ge a_0I,\qquad\delta_{\mathrm{load}}>0;
   \]
3. triangular shear control:
   \[
   \sup_\pm\|CD_\pm^{-1}\|<\infty.
   \]

The third may follow from the first plus a uniform bound on \(C\), but it does not follow from the two dimensionless margins alone.

This is analogous to coherent transport: diagonal positive pieces can each be uniformly controlled while a nonunitary comparison map destroys the completed norm.

## Hostiles

1. Keep \(D=I\), \(G_{\mathrm{eff}}=I\), but let \(C=nI\) and choose \(A=I+C C^{*}\). Both normalized contraction margins are maximal, yet the triangular shear grows with \(n\), and the smallest eigenvalue of the full block tends to zero.
2. Keep both dimensionless margins fixed while \(s_0\to0\). The auxiliary inverse and shear diverge.
3. Keep \(D\) uniformly positive and the loading margin fixed while changing the source normalization of \(A\) so \(a_0\to0\). Endpoint coercivity vanishes.

The first hostile is especially sharp: positivity and both diagonal Schur gaps remain perfect, but full-block coercivity is lost solely through incidence shear.

## Consequence for the global programme

The local constructor certificate should expose the tuple

\[
(\delta_{\mathrm{aux}},
\delta_{\mathrm{load}},
s_0,
a_0,
M_{\mathrm{shear}})
\]

rather than compress it prematurely into one scalar. After the typed Adams edge is assembled, global Green normalization may absorb some absolute scales, but only through a proved uniformly bi-bounded comparison.

## Next theorem

Derive a source-normalized bound for

\[
M_{\mathrm{shear}}
=
\sup_{p,\pm}
\|C_pD_{p,\pm}^{-1}\|
\]

on compact off-seam regions. This is the exact quantitative bridge from the two nested contraction gates to completion-stable coercivity of the full local Adams cell.
