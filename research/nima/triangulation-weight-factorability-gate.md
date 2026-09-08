# Triangulation-weight factorability gate

## Question

When can a non-unit triangulation coefficient system be absorbed into channel-facet rescalings?

## Claim boundary

The criterion is algebraic. It does not assert that source coefficients are positive, factorable, or geometrically authorized.

Let `A` be the triangulation-channel incidence matrix and let positive triangulation weights satisfy

\[
w_T=\prod_{c\in T}\lambda_c.
\]

Taking logarithms gives

\[
\log w=A\log\lambda.
\]

Thus facet scales exist exactly when `log w` lies in the column image of `A`. Equivalently, every integer relation `z` in the left kernel satisfies the binomial constraint

\[
\prod_T w_T^{z_T}=1.
\]

Exact polygon census gives full column rank at `n=4..7`. At four and five points, the numbers of triangulations equal the numbers of channels, so there are no independent weight invariants: every positive coefficient system can be absorbed uniquely at logarithmic level. At six points there are fourteen triangulations and nine channels, leaving five independent binomial relations. At seven points there are forty-two triangulations and fourteen channels, leaving twenty-eight.

The checker records an explicit integer six-point kernel relation. Changing one participating triangulation weight from one to two while keeping all others one makes its binomial ratio a nontrivial power of two, so no facet rescaling can absorb that deformation.

## Disposition

Five-point agreement cannot distinguish source coefficient normalization from facet scale choice. Six points are the first tested stage with scale-invariant coefficient constraints. An owner-supplied embedding and weighted amplitude comparison must satisfy the five explicit six-point binomials before coefficient differences may be called gauge.
