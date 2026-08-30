---
author: marici.Benincasa
---

# 1427 — The Positive Exceptional Period Is the Exact Mixed-Tate Constant \(C_5\)

## Status

Source-typed identity of integrands, followed by the previously certified exact partial-fraction evaluation.

## Coordinate comparison

Use the two normal coordinates from Entry 1422,

\[
x=\frac1z,
\qquad
w=\frac1R,
\qquad
w=x\tau.
\]

The radial variable in Entry 1310 is therefore not an additional choice:

\[
\rho=\frac Rz=\tau^{-1}.
\]

On the positive uniform sheet, the five singleton walls supply

\[
(1+2\rho)^5,
\]

the total-energy wall supplies (5), and every selected wall of region size (k) supplies (k+2\rho). The source current supplies the oriented radial measure

\[
4\pi\rho^2d\rho.
\]

## Exact source census

Deriving the four selected-wall sizes from all (180) frozen OFPT terms gives exactly the eleven profile multiplicities used in Entry 1310's exact evaluation:

\[
\begin{array}{c|c}
(2,2,3,4)&10\\
(2,2,3,5)&20\\
(2,2,4,5)&10\\
(2,3,3,4)&10\\
(2,3,3,5)&10\\
(2,3,4,4)&20\\
(2,3,4,5)&50\\
(2,4,4,5)&10\\
(3,3,4,4)&10\\
(3,3,4,5)&20\\
(3,4,4,5)&10.
\end{array}
\]

Hence the positive exceptional period is literally

\[
C_5
=
4\pi\int_0^\infty
\frac{\rho^2}{5}
\sum_{\mathbf k}
\frac{n_{\mathbf k}}
{(1+2\rho)^5\prod_{k\in\mathbf k}(k+2\rho)}
\,d\rho.
\]

## Exact value

The existing characteristic-zero partial-fraction certificate therefore applies without a normalization change:

\[
\boxed{
C_5=4\pi\left(
-\frac{3797899}{995328}
+\frac{17729}{2916}\log2
-\frac{87}{256}\log3
-\frac{2225}{147456}\log5
\right).
}
\]

Numerically,

\[
C_5=0.011316043695616902\ldots.
\]

## Consequence

Entry 1426's distinguished positive evaluation of the deck-odd order-nine line is not merely compatible with the previously observed mixed-Tate constant. It is its source-normalized geometric realization:

\[
\boxed{
\text{positive order-nine exceptional period}=C_5.
}
\]

Thus the finite constant is carried by the deepest uniform-sheet Cartier grade. The even order-four and order-two grades are not identified with it.

## Scope

This is a source-typed equality for the coalesced-focus five-cycle current. It does not promote the auxiliary cyclic augmentation to the generic asymmetric physical family, and it does not determine the coefficient objects on the even mixed-sheet grades.

## Durable verification

- Checker: `research/benincasa/marici-gm/src/bin/five_site_positive_exceptional_period.rs`
- Result: `research/benincasa/results/five-site-positive-exceptional-period.json`
- Exact evaluator: `research/benincasa/marici-gm/src/bin/five_site_asymmetric_infinity_constant_exact.rs`
- Exact result: `research/benincasa/results/five-site-asymmetric-infinity-constant-exact.json`
- Allocator claim: `seqclaim-117d3c912d6dd258270ca188`
- Epistemic graph event: `ev-000000001498-6b644000-89f6-47f3-a1ca-cf53199bb513`
