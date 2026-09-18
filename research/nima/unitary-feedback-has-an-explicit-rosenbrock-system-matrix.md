# Unitary feedback has an explicit Rosenbrock system matrix

Let the passive colligation be

$$
\mathfrak U=
\begin{pmatrix}A&B\\C_0&D\end{pmatrix}
$$

with transfer

$$
G(\lambda)
=D+\lambda C_0(I-\lambda A)^{-1}B.
$$

Let `C` be the reciprocal boundary sewing unitary. Introduce the feedback Rosenbrock matrix

$$
\mathcal R_{\rm fb}(\lambda)
=
\begin{pmatrix}
I-\lambda A&-\lambda B\\
-CC_0&I-CD
\end{pmatrix}.
$$

On a chart where `I-lambda A` is invertible, left multiplication by

$$
L(\lambda)=
\begin{pmatrix}
I&0\\
CC_0(I-\lambda A)^{-1}&I
\end{pmatrix}
$$

gives

$$
L(\lambda)\mathcal R_{\rm fb}(\lambda)
=
\begin{pmatrix}
I-\lambda A&-\lambda B\\
0&I-CG(\lambda)
\end{pmatrix}.
$$

A subsequent invertible upper-triangular column operation removes the upper-right block. Hence

$$
\mathcal R_{\rm fb}(\lambda)
\sim_{m hol}
(I-\lambda A)\oplus(I-CG(\lambda)).
$$

Therefore feedback resonances are exactly the Rosenbrock kernel states after removing the invertible internal factor. The reduction preserves local multiplicity.

The final source comparison is now

$$
\mathcal R_\Xi(z)
\sim_{\rm hol}
\mathcal R_{\rm fb}(\lambda(z))
$$

up to an invertible auxiliary block. All blocks on the feedback side are determined by the one-sided sum/difference colligation and reciprocal sewing.

Status: feedback matrix and Schur reduction explicit; source identification with the two-stable-history Xi matrix remains open.
