# Correction: the three-moment flux matrix is a first-order jet, not the Euler-grade carrier

The explicit matrices on `(M_1,M_2,M_3)` are valid for the first ordered derivative of

$$
\Phi=4M_2-6M_1.
$$

They do not define a closed finite-dimensional spectral observer. Repeated differentiation raises `M_3` to `M_4` and continues through the entire moment ladder. The completed invariant carrier is therefore

$$
\mathcal M=\operatorname{span}\{M_1,M_2,M_3,\ldots\}
$$

with its reciprocal doubling and seam-jet completion.

A second typing correction is essential: theta moment order and Euler prime-power grade are different indices.

- `M_j` records Gaussian/dilation moment order;
- `e_(p,k)` records arithmetic prime-power grade.

Primitive, square, and connected grades must not be identified with `M_1,M_2,M_3`. The correct source carrier is a labelled tensor or joint graph

$$
E_{\rm Euler}\widehat\otimes\mathcal M,
$$

with prime translation/evaluation acting on the Euler-label factor and the raising operator acting on the moment factor.

At first derivative order, the moment-side tensors remain

$$
S_\theta=dc^T+cd^T,
\qquad
A_\theta=dc^T-cd^T,
$$

where

$$
c=(-6,4,0)^T,
\qquad d=(-15,30,-8)^T.
$$

But the arithmetic incidence acts by labelled evaluation

$$
e_{p,k}\otimes M_j
\longmapsto
p^{-k/2}M_j(k\log p)
$$

with the declared derivative and `1/k` factors, rather than by sending Euler grades `k=1,2,3` to moment basis vectors `M_1,M_2,M_3`.

The correct first-order naturality test is therefore a tensor identity:

$$
\mathcal I_{p,k}^{*}
\bigl(S_\theta+iA_\theta\bigr)
\mathcal I_{p,k}
=
\mathcal B_{p,k}^{\rm ordered},
$$

with `I_(p,k)` retaining the complete three-moment evaluation column. Cross-grade terms may be formed only by the source-declared within-prime codiagonal after this evaluation.

For full spectral covariance, replace the three-moment matrices by the infinite raising operator `A` satisfying

$$
CAC=-A
$$

on the reciprocal doubled moment module. No finite truncation is invariant because its top moment produces the next rung.

Status: first-order flux matrices retained as finite witnesses; erroneous moment/Euler-grade identification retracted; full target is an Euler-labelled, reciprocally doubled infinite moment observer.
