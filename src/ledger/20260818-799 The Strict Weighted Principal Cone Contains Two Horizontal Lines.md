# The Strict Weighted Principal Cone Contains Two Horizontal Lines

## Calculation

Entry 798 supplies a strict morphism of differential modules on the weighted
exceptional chart,

\[
C_E:P\longrightarrow E,
\qquad
C_E=\frac1{2(t^2-1)}
\begin{pmatrix}0&-1\\0&3\end{pmatrix},
\]

where both \(P\) and \(E\) have rank two.  The inherited connections are

\[
A_P=\operatorname{diag}\!\left(0,\frac{2t}{t^2-1}\right),
\qquad A_E=0.
\]

Over \(\mathbb Q(t)\), \(C_E\) has rank one.  Therefore its two-term cone
has

\[
H^{-1}=\ker C_E=\mathbb Q(t)\langle(1,0)^T\rangle
\]

and

\[
H^0=\operatorname{coker}C_E,
\qquad
H^0\xrightarrow{\sim}\mathbb Q(t)
\text{ represented by }(3,1).
\]

Both induced connection actions vanish:

\[
\boxed{
\nabla H^{-1}=0,
\qquad
\nabla H^0=0.
}
\]

Thus the strict local cone does not isolate a unique horizontal line.  It
contains two: an untouched source-kernel line in degree \(-1\), and a target
cokernel line in degree zero.

## Endpoint test

The endpoint residues are

\[
\operatorname{res}_{t=1}C_E=
\begin{pmatrix}0&-\frac14\\0&\frac34\end{pmatrix},
\qquad
\operatorname{res}_{t=-1}C_E=
\begin{pmatrix}0&\frac14\\0&-\frac34\end{pmatrix}.
\]

They have the same rank-one image line.  Hence both endpoints preserve the
same kernel and cokernel objects; the local endpoint residues alone do not
select between the two cone cohomology lines.

## Consequence

The desired physical rank-one object cannot be identified merely as "the
cohomology of the strict principal cone."  A further, independently typed
operation must distinguish cohomological degree or support.  The remaining
candidate is the global supported Čech/Gysin incidence together with the
relative-cycle pairing:

\[
\operatorname{Tot}_{\rm supp}
\bigl[P^\bullet\xrightarrow{C_E}E^\bullet\bigr]
\longrightarrow
H_{\rm rel}^{\rm chain}{}^\vee.
\]

This operation must say whether it pairs with the degree-zero cokernel line,
the degree-minus-one kernel line, or neither.  Selecting one by hand would
repeat the quotient-typing error avoided in Entry 798.

## Evidence and scope

`research/nima/audit_weighted_principal_strict_cone.py` computes the exact
kernel, cokernel, induced connection actions, and endpoint residues.  Its
output is `research/nima/weighted-principal-strict-cone.json`.

The calculation has the same bounded rational-reconstruction scope as
Entries 793 and 798.  It is a local weighted-exceptional result and does not
identify Entry 740's three-support global Čech class with either local line.

Allocator claim: `seqclaim-c25eebe56c7464089f9be45a`.
