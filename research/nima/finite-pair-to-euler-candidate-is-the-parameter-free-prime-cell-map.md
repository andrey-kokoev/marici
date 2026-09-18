# Finite pair-to-Euler candidate is the parameter-free prime-cell map

For each prime shell, the completed theta wall and Wronskian columns fix

$$
w_\theta=\binom{1/2}{1/2},
\qquad
j_\theta=\binom{1/4}{-1/4},
$$

and hence the invertible local comparison

$$
Q_p^{\rm lin}
=\begin{pmatrix}1/2&1/4\\1/2&-1/4\end{pmatrix}
$$

in the declared even/odd and endpoint-polarity bases. There is no free scalar.

The finite-shell pair-to-Euler candidate is the chain

$$
P_{\rm pair,p}
\xrightarrow{T_{{\rm PB},p}}
B_{{\rm full},p}
\xrightarrow{\partial_{\rm Wr}}
W_p
\xrightarrow{Q_p^{\rm lin}}
E_{{\rm cons},p},
$$

with all labelled coordinates retained in its graph. This gives the local linear part of the desired `Q_X`.

Its admission requires the metric Beck–Chevalley identity

$$
G_p^{\rm St}(e_j,e_k)
=G_p^\theta(Q_p^{\rm lin}e_j,Q_p^{\rm lin}e_k),
\qquad j,k\in\{1,2\}.
$$

Quarter-turn covariance and the correct antiunitary reflection law reduce the defect to

$$
\Delta
=a\,\operatorname{diag}(1,1/4)
+b\begin{pmatrix}0&i\\-i&0\end{pmatrix},
\qquad a,b\in\mathbb R.
$$

Thus two independent source comparisons remain:

1. the even-wall diagonal equality, forcing `a=0`;
2. the oriented Stokes/Wronskian equality, forcing `b=0`.

The second comparison cannot be erased by reflection because reflection is antiunitary on the ordered linking channel. Moreover, prior no-go results exclude promotion of `Q_p^lin` to a direct bulk metric intertwiner. The required higher filler is a common boundary triple or matrix Weyl/Calderon function extracting both channels.

Status: finite linear component identified uniquely; its two-scalar boundary-Weyl coherencer remains open.
