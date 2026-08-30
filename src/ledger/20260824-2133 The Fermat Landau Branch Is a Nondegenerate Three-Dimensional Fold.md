# 2133 — The Fermat Landau Branch Is a Nondegenerate Three-Dimensional Fold

> **Superseded by Entry 2135.** The Morse calculation is mathematically
> correct for the sum-of-three-distances function, but that function is not a
> denominator of the all-deleted source integrand.

## Hard-to-vary claim

At a generic interior Fermat point, the grade-three Landau critical point is a positive nondegenerate Morse point in the full three-dimensional loop space. Its local singularity is a simple fold with square-root character.

## Hessian

Let `u_i` be the three unit vectors from the Fermat point to the external triangle vertices and let `r_i>0` be their lengths. For

\[
S(\ell)=\sum_{i=1}^3|\ell-v_i|,
\]

the Hessian is

\[
H=\sum_{i=1}^3\frac{I-u_iu_i^T}{r_i}.
\]

The `u_i` lie in the external momentum plane, have pairwise angles `120 degrees`, and sum to zero.

The eigenvalue normal to the plane is

\[
\lambda_\perp=\sum_i\frac1{r_i}>0.
\]

The planar determinant is

\[
\det H_\parallel
=\frac34\sum_{i<j}\frac1{r_ir_j}>0.
\]

Therefore

\[
\boxed{
\det H
=\frac34
\left(\sum_i\frac1{r_i}\right)
\left(\sum_{i<j}\frac1{r_ir_j}\right)>0,
\qquad
\operatorname{index}H=0.
}
\]

## Why the third direction matters

In edge-length coordinates the Fermat point lies on the Cayley--Menger boundary and the measure contains a square-root Jacobian. On the physical loop-vector cover, that boundary normal is the ordinary out-of-plane displacement. Retaining it gives a three-dimensional Morse point.

Discarding the cover normal would incorrectly type the singularity as a two-dimensional logarithmic critical point.

## Local coefficient character

For the simple translated total-energy denominator, the local model is

\[
\int_{\mathbb R^3}
\frac{d^3\xi}{\delta+\xi^TH\xi}.
\]

After subtraction of analytic terms, its first nonanalytic contribution is proportional to

\[
\delta^{1/2}.
\]

Hence a loop around the generic Fermat discriminant acts by

\[
\boxed{T_{\mathcal F_3}=-1}
\]

on the rank-one local vanishing coefficient.

## Verification

`research/benincasa/checkers/fermat_hessian_fold.rs` checks the exact determinant formula and positivity at three independent positive rational-weight packets. The displayed determinant identity proves the general result.

## Classification

The grade-three port therefore carries a genuine sector-specific Kummer/fold coefficient along `\mathcal F_3=0`, over the unchanged Cayley--Menger Carrier.

This establishes coefficient monodromy. It does not establish physical activation by the source Bunch--Davies relative cycle.

## Next falsifier

Continue the normalized positive loop cycle using the source `i\epsilon` prescription toward a generic smooth point of `\mathcal F_3=0`. Compute the oriented intersection with the Morse thimble.

Because the coefficient monodromy is nontrivial, the remaining decision is binary:

- zero intersection: physically invisible coefficient branch;
- nonzero intersection: genuine correlator threshold on the existing Carrier.
