# The soft dyadic tower refines the positive triple compression while retaining the sewing cell

## Physical positive contraction

Set

\[
B_\Lambda
=
P_\Lambda Q_\Lambda P_\Lambda.
\]

Since \(P_\Lambda\) and \(Q_\Lambda\) are orthogonal projections,

\[
0\le B_\Lambda\le I.
\]

For an observer operator \(A_g\), the positive triple-compression feature is

\[
\Phi_{\Lambda,0}(g)
=
B_\Lambda^{1/2}A_g.
\]

Its Gram is

\[
\Phi_{\Lambda,0}^*
\Phi_{\Lambda,0}
=
A_g^*B_\Lambda A_g.
\]

## Dyadic feature at depth \(n\)

For \(n\ge1\), define the bulk slot

\[
x_{\Lambda,n}(g)
=
B_\Lambda^{2^{n-1}}A_g
\]

and defect slots

\[
d_{\Lambda,j}(g)
=
\left[
B_\Lambda^{2^j}
\left(
I-B_\Lambda^{2^j}
\right)
\right]^{1/2}A_g,
\qquad
0\le j<n.
\]

The complete depth-\(n\) feature is

\[
\Phi_{\Lambda,n}(g)
=
\left(
x_{\Lambda,n}(g),
d_{\Lambda,n-1}(g),
\ldots,
d_{\Lambda,0}(g)
\right).
\]

## Exact Gram conservation

The scalar polynomial identity

\[
t^{2^n}
+
\sum_{j=0}^{n-1}
t^{2^j}
\left(
1-t^{2^j}
\right)
=t
\]

holds for every \(t\). Functional calculus gives

\[
B_\Lambda^{2^n}
+
\sum_{j=0}^{n-1}
B_\Lambda^{2^j}
\left(
I-B_\Lambda^{2^j}
\right)
=B_\Lambda.
\]

Therefore

\[
\boxed{
\Phi_{\Lambda,n}^*
\Phi_{\Lambda,n}
=
A_g^*B_\Lambda A_g
}
\]

at every depth.

## Strict depth successor

The successor from depth \(n\) to \(n+1\) splits the bulk slot by

\[
W_nx
=
\left(
B_\Lambda^{2^{n-1}}x,
\left(I-B_\Lambda^{2^n}\right)^{1/2}x
\right)
\]

with the existing defect slots carried identically. It is an isometry, and the depth maps compose strictly because all entries are functions of the same contraction \(B_\Lambda\).

## Sewing cell

Let

\[
H_g=A_gA_g^*.
\]

Connes's product trace splits as

\[
\operatorname{Tr}
(P_\Lambda Q_\Lambda H_g)
=
\operatorname{Tr}
(B_\Lambda H_g)
+
\mathcal E_\Lambda(g),
\]

where

\[
\mathcal E_\Lambda(g)
=
\operatorname{Tr}
\left(
P_\Lambda Q_\Lambda
(I-P_\Lambda)H_g
\right).
\]

Since the dyadic refinement preserves

\[
\operatorname{Tr}(B_\Lambda H_g),
\]

the same sewing cell attaches at every depth:

\[
\boxed{
\operatorname{Tr}
(P_\Lambda Q_\Lambda H_g)
=
\|\Phi_{\Lambda,n}(g)\|^2
+
\mathcal E_\Lambda(g).
}
\]

Thus depth refinement changes the internal distribution of positive mass while leaving the physical product comparison fixed.

## Recentered limit problem

The soft tower provides the canonical positive feature at each cutoff and depth. The remaining boundary datum is the recentered sewing pairing

\[
\mathcal E_\Lambda(g)
=
-
\left\langle
P_\Lambda Q_\Lambda(I-P_\Lambda),
(I-P_\Lambda)[P_\Lambda,H_g]P_\Lambda
\right\rangle_{HS}.
\]

Its convergence is independent of dyadic depth. This separates:

- exact positive refinement, governed by functional calculus of \(B_\Lambda\);
- physical boundary sewing, governed by the recentered prolate and observer Hankel blocks.

## Categorical role

The cutoff and depth indices form a bisimplicial filtered object. Depth arrows are exact isometries. Cutoff arrows remain correspondences or pro-arrows. The sewing term is a depth-constant comparison cell from the positive tower to the signed product-trace presentation.
