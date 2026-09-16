# Cofinal finite-packet minimalization constructs the regular physical positive pro-completion

Let

$$
E_1\subset E_2\subset\cdots\subset\mathscr E_S
$$

be the finite-dimensional target-adapted observer packets with dense union. Write \(j_{n}:E_n\hookrightarrow\mathscr E_S\) and

$$
A_n=j_n^*\mathcal A_Sj_n.
$$

At finite physical regulator \(\alpha\), exact eight-leg transport gives aligned positive Grams

$$
G_{\alpha,n}^T-G_{\alpha,n}^0=D_{\alpha,n}
$$

on \(E_n\). The signed physical comparison gives, for fixed \(n\),

$$
D_{\alpha,n}\longrightarrow A_n
$$

entrywise. Finite dimensionality upgrades this to operator-norm convergence.

The exact reference mismatch strip is coercive on \(E_n\) for sufficiently large radial cutoff. Hence the forced common remainder

$$
C_{\alpha,n}
=
G_{\alpha,n}^T-(D_{\alpha,n})_+
=
G_{\alpha,n}^0-(D_{\alpha,n})_-
$$

is positive after moving sufficiently far in the admissible regulator direction. Douglas factorization identifies the two realizations of \(C_{\alpha,n}\) as one common physical feature.

Removing it leaves the minimal physical residual

$$
F_{\alpha,n}u
=
\left(
(D_{\alpha,n})_+^{1/2}u,
(D_{\alpha,n})_-^{1/2}u
\right).
$$

Continuous finite-dimensional functional calculus gives

$$
(D_{\alpha,n})_\pm
\longrightarrow
(A_n)_\pm,
$$

and therefore

$$
F_{\alpha,n}^*F_{\alpha,n}
=
|D_{\alpha,n}|
\longrightarrow
|A_n|.
$$

Choose recursively a cofinal regulator sequence \(\alpha_k\) such that for every \(n\le k\),

$$
\left\|
|D_{\alpha_k,n}|-|A_n|
\right\|<2^{-k}
$$

and the common remainder \(C_{\alpha_k,n}\) is positive. This is possible because each stage imposes only finitely many finite-packet conditions.

For \(m\ge n\), retain the source-labelled correspondence

$$
\mathcal R_{m n}^{(k)}
=
\overline{
\left\{
(F_{\alpha_k,n}u,F_{\alpha_k,m}u):u\in E_n
\right\}}.
$$

The resulting cofinal family is a positive pro-Hilbert object. Its packetwise Gram limit is the target system

$$
\left(E_n,|A_n|\right)_{n\ge1}.
$$

Thus the regular physical boundary is analytically connected to the internal Tate chart as a cofinal positive pro-completion. Promotion of this pro-object to one ordinary Hilbert-space limit is exactly the additional uniform tail/Mosco problem; it is not needed for the pro-Hilbert realization itself.
