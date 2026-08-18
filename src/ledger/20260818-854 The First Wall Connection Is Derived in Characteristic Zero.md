# 20260818-854 The First Wall Connection Is Derived in Characteristic Zero

## Setup

Restrict the frozen Cayley--Menger polynomial to

\[
W_1:\qquad L_1=b+1-u=0,
\qquad b=u-1,
\]

and retain the oriented residue basis

\[
t_1=\frac{da}{L_2\sqrt{K|_{W_1}}},
\qquad
g_1=\frac{da}{\sqrt{K|_{W_1}}}.
\]

For each base derivative, reduce against the exact ansatz

\[
d\left(\frac{S(a)}{L_2\sqrt{K|_{W_1}}}\right),
\qquad \deg S\leq6.
\]

After clearing \(L_2^2K^{3/2}\), the coefficient identity has fiber degree at most ten.  Eleven exact fiber evaluations therefore determine the polynomial identity over \(\mathbb Q(u,v)\).  The solve retains one free exact-primitive coefficient, but every connection coefficient is independent of it.

## Result

Define

\[
D=-4+12u-6uv+4v-9u^2+4u^2v-v^2.
\]

In the ordered basis \((t_1,g_1)\), with columns denoting differentiated source classes,

\[
\boxed{
A_{W_1,u}=
\begin{pmatrix}
-\dfrac{2(u-1)}{u(u-2)}&0\\[2mm]
-\dfrac{2(2-3u+uv-v)}{u(u-2)D}&
-\dfrac{6-9u+4uv-3v}{D}
\end{pmatrix}.
}
\]

Similarly,

\[
\boxed{
A_{W_1,v}=
\begin{pmatrix}
-\dfrac1{v-2}&0\\[2mm]
-\dfrac{-2+u+v}{(v-2)(-D)}&
-\dfrac{2-3u-v+2u^2}{D}
\end{pmatrix}.
}
\]

The primitive wall line is preserved, while the top line can extend it.  This derives the first half of Entry 853's sparse pattern directly from the wall forms, without selecting a rank-twelve nullspace.

## Scope and next gate

This entry determines only the \(W_1\) connection.  It does not yet define the rank-three quotient connection because the oriented \(W_2\) reduction and the same-sheet top gluing remain to be computed.  No \(B_\mu\), flatness, infinity-Gysin, or \(\mathcal Q\)-support claim is made.

## Durable artifacts

- `research/benincasa/marici-gm/src/bin/marked_wall_laurent_reduction.rs`
- `research/benincasa/marked-wall-one-laurent-connection.json`
- Epistemic event `ev-000000000469-a95ab8bf-cac1-4db6-b664-b40d71b2253c`
