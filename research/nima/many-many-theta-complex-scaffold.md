# Many-many completed theta-complex scaffold

Use a graded source object

$$
E_\theta^\bullet
=E_{\rm prim}\oplus E_{\rm sq}\oplus E_{\rm conn}
\oplus E_{\rm seam}\oplus E_{\rm end}\oplus E_{\infty}.
$$

The differential is assembled as a block operator

$$
 d_\theta(s)=
\begin{pmatrix}
 d_{\rm prim}&0&0&0&0&0\\
 a_{\rm prim,sq}&d_{\rm sq}&0&0&0&0\\
 0&a_{\rm sq,conn}&d_{\rm conn}&0&0&0\\
 0&0&a_{\rm conn,seam}&d_{\rm seam}&0&0\\
 0&0&0&a_{\rm seam,end}&d_{\rm end}&0\\
 0&0&0&0&a_{\rm end,\infty}&d_\infty
\end{pmatrix}.
$$

The source construction must choose the adjacent arrows so that

$$
 d_\theta(s)^2=0.
$$

Each block receives a common dense graph domain. Reciprocal transport and cutoff bonding maps must commute with `d_theta`. The determinant functor must identify the resulting complex with the existing theta–Poisson Xi line.

Status: graded theta-complex scaffold fixed; source arrows, signs, domains, and determinant identification remain open.
