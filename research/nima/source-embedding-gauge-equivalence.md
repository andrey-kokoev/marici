# Gauge equivalence for source-embedding candidates

## Question

Which changes of presentation preserve the logarithmic form, and which also preserve a fixed unit-weight scalar amplitude convention?

## Claim boundary

The equivalence preserves labelled affine facet divisors and the logarithmic form. Independent facet rescaling is not gauge for a scalar weighted sum whose coefficients are held fixed.

For an invertible affine change and positive facet rescalings,

\[
x'=Mx+t,\qquad a_i'(x')=\lambda_i a_i(M^{-1}(x'-t)),
\quad \lambda_i>0,
\]

the inequalities, labelled zero loci, and `dlog` form are preserved. Gradients and volume transform as

\[
\nabla'a_i'=\lambda_i M^{-T}\nabla a_i,
\qquad d^dx'=\det(M)d^dx.
\]

A triangulation Jacobian therefore acquires the product of its facet scales and `1/det(M)`. These factors cancel the rescaled denominators in the differential form. The coordinate scalar coefficient correspondingly carries `1/det(M)`.

This does not preserve the unweighted scalar sum

\[
\sum_T\prod_{c\in T}a_c^{-1}
\]

under independent `lambda_c`. To compare a fixed unit-weight amplitude convention, either the facet scales must be fixed by the source channel normalization or each triangulation coefficient must transport by the product of its incident facet scales. An exact five-point checker uses scales `2,3,5,7,11`: the Jacobian-weighted form is unchanged, while the unit-weight scalar has a nonzero rational residual.

If `det(M)<0`, orientation reversal remains explicit. Facet relabelling requires a separate incidence-preserving labelled map and its dihedral sign.

## Disposition

Affine coordinate transport is genuine gauge once its volume determinant is recorded. Positive facet rescaling is gauge for the canonical `dlog` form, but not for a fixed scalar amplitude normalization unless coefficient weights are transported. The source-embedding interface must therefore retain channel scales or an equivalent weight map.
