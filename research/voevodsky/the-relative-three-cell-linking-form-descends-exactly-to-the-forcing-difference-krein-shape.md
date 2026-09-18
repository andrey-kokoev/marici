# The relative three-cell linking form descends exactly to the forcing-difference Krein shape

## Arithmetic relative-cell form

The source-derived relative cell carries the unique reflection-odd form

\[
\Omega_0=
\begin{pmatrix}
0&1&-1\\
-1&0&1\\
1&-1&0
\end{pmatrix},
\qquad
\ker\Omega_0=\mathbb C(1,1,1)^\top.
\]

For a prime cell, derivative loading gives

\[
P_p=\operatorname{diag}(A_p,B_p,1),
\quad
A_p=-2(\log p)p^{-1/2},
\quad
B_p=2(\log p)p^{-1},
\]

and

\[
\Omega_p=\omega_p P_p\Omega_0P_p.
\]

Its radical is \(P_p^{-1}(1,1,1)^\top\), exactly the previously computed transported overlap relation.

## Quotient calculation

Pass to the two-dimensional quotient by the radical and use the classes of the first two coordinate vectors as a section. The descended skew matrix is

\[
\Omega_p^{\rm quot}
=\omega_p A_pB_p
\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

In the Hermitian lane its oriented form is

\[
H_p^{\rm quot}=i\Omega_p^{\rm quot}.
\]

Let

\[
S=\operatorname{diag}(1,-i).
\]

Then

\[
S^*H_p^{\rm quot}S
=\omega_p A_pB_p
\begin{pmatrix}0&1\\1&0\end{pmatrix}
=\omega_p A_pB_p J_{\rm mix}.
\]

Therefore the arithmetic relative-cell form and the forcing-difference two-port have exactly the same nondegenerate Krein shape after quotient and one fixed phase rotation. No additional matrix-valued degree of freedom remains.

## What remains

Shape compatibility reduces the mixed Green comparison to one scalar coefficient identity in each prime/grade cell:

\[
\omega_p A_pB_p
=\alpha_p^{\rm forcing},
\]

where \(\alpha_p^{\rm forcing}\) is the coefficient obtained by evaluating the causal-odd forcing-difference current in the same normalized quotient frame. Since

\[
A_pB_p=-4(\log p)^2p^{-3/2},
\]

the required normalization is completely fixed once either coefficient is independently computed.

This equality must be established before summing over primes and before Xi specialization. Equality of a scalar total after summation would not prove labelled naturality.

## Refined frontier

The arithmetic mixed coordinate splits as

- \(a_{\rm shape}=1\): quotient form is congruent to the canonical forcing-difference Krein metric;
- \(a_{\rm coeff}=0\): the independently derived coefficient equality has not been shown;
- \(a_{\rm sum}=0\): cutoff-compatible summation has not been justified.

Thus

\[
(m,a_{\rm shape},a_{\rm coeff},a_{\rm sum})=(1,1,0,0).
\]

## Claim boundary

This proves exact matrix-shape compatibility, not the source coefficient identity. It does not choose \(\omega_p\) to force equality and does not establish the global positive Green cycle.
