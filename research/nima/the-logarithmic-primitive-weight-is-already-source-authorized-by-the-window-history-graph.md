# The logarithmic primitive weight is already source-authorized by the window history graph

## Reconciliation

The \(k\log p\) weight needed to compare primitive windows with constant-norm
cut atoms is not an arbitrary repair.  It is already present in the declared
window-history graph.

For one prime, with \(L=\log p\), the source history is

\[
\mathcal H_p\psi:t\longmapsto M_{W_t}\psi,
\qquad t\in[L,2L].
\]

The established graph estimate is

\[
\|\mathcal H_p\psi\|_{H^1_tL^2_q}^2
\le5L\|\psi\|_2^2.
\]

The canonical affine endpoint right inverse similarly satisfies

\[
\|R_L(x,y)\|_{\mathcal G_L}^2
\le
\left(\frac L2+\frac2L\right)
(\|x\|^2+\|y\|^2).
\]

Thus the source graph assigns endpoint lifting a squared norm of order \(L\),
that is, norm growth of order \(\sqrt L\).

## Agreement with the primitive window scale

The ordinary window vector obeys

\[
\|W_L\|_2^2
=2L-\frac{\sqrt2}{\pi}+O(e^{-2\pi L^2}).
\]

Hence its squared Hilbert energy is also of order \(L\).  The same logarithmic
scale appears independently in:

1. the source history interval length;
2. the affine trace right inverse;
3. the ordinary primitive-window norm;
4. the resolved primitive-window norm, which dominates the ordinary norm.

Therefore the required primitive weight

\[
\omega_{p,1}^2\asymp\log p
\]

has source provenance.  It need not be inserted after observing a failed
comparison.

For grade \(k\), the same translated construction over its natural scale cell
gives

\[
\omega_{p,k}^2\asymp k\log p.
\]

## What is still missing

Matching growth orders is weaker than identifying metrics.  The source
history uses operator-valued multipliers and an \(H^1\) path norm, while the
resolved window form uses

\[
(1+M_\Phi^2)\|W_t\|_2^2+\|BW_t\|_2^2
\]

on an \(L^2(q)\) vector carrier.  These are differently typed objects.

The exact remaining comparison is not “find a logarithmic weight”; it is:

> Prove that endpoint attachment from the source history graph to the resolved
> window-vector graph transports the source \(L\)-weight to the frozen
> resolved Green form, with uniform two-sided constants and the declared
> wall/jump ports retained.

This is the seam-transport/endpoint-attachment metric identification already
listed in the source-authorized joint-graph packet.

## Global grade consequence

The source history also explains why primitive and square grades complete
differently.  With Euler weights,

\[
p^{-1}\log p
\]

is not prime-summable, whereas

\[
p^{-2}\log p
\]

is.  Therefore:

- the primitive history belongs to the rigged/distributional grade;
- the square history can lie in a Hilbert grade;
- a common unweighted Hilbert sum is not source-authorized.

This anisotropy must survive the endpoint-to-resolved comparison.  A
bi-bounded theorem on an unweighted all-grade Hilbert direct sum would erase
known source topology.

## Revised frontier

The logarithmic primitive weight is closed at the source-history level.  The
earliest open implication is the typed metric identification between:

\[
\text{operator-valued window history graph}
\quad\text{and}\quad
\text{resolved window-vector Green graph}.
\]

After that identification, one may combine the wall-extended cut atom and
ordered linking ports and address radical descent.  Full rigged pushout closed
range remains open.  No RH conclusion is authorized.
