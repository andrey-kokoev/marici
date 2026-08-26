# The RH defect is supported over parameter space, not inside the Hardy state

## Typing correction

For a Blaschke zero \(a\), the model-space defect is represented by a Hardy reproducing kernel or an equivalent boundary state. That vector is not spatially supported at \(a\). Its boundary values are generally distributed across the entire Hardy boundary.

Therefore the phrase “the defect state is supported off the seam” is misleading. Two different supports must be distinguished:

1. state support in the Hardy boundary variable;
2. parameter support of the kernel or cokernel family over \(z\).

RH concerns the second.

## Operator family

Let \(T(z)\) be a source-derived family of compressed theta/Tate operators over a spectral domain. Associate the two-term complex

\[
\mathcal C_z:
\qquad
\mathcal H_1
\xrightarrow{\,T(z)\,}
\mathcal H_0.
\]

Its cohomology is

\[
H^0(\mathcal C_z)=\ker T(z),
\]

and

\[
H^1(\mathcal C_z)=\operatorname{coker}T(z).
\]

For an isometric inner multiplier, the first group vanishes while the second is the model space.

As \(z\) varies, these groups form a defect family or, with the required analytic structure, a coherent defect sheaf over the spectral base.

## Correct support statement

The meaningful confinement claim is:

> The parameter support of the defect sheaf is contained in the critical seam.

This says that the complex is exact at every parameter in either open half-plane.

It does not say that the boundary vectors representing seam defects have spatial support only at one boundary location.

## Equivalence boundary

If \(T(z)\) is constructed from the completed scalar section so that its cokernel multiplicity equals the zero multiplicity of \(\Xi(z)\), then

\[
\operatorname{Supp}_z H^\bullet(\mathcal C)
\subseteq
\{\operatorname{Re}z=0\}
\]

is exactly RH in the centered coordinate.

Renaming zeros as cokernel support does not explain them.

The statement becomes explanatory only if all of the following are derived before scalar projection:

1. the complex \(\mathcal C_z\) comes from labelled theta/Tate operations;
2. its determinant section is subsequently identified with \(\Xi\) up to a nonvanishing unit;
3. each open half-plane carries a source-derived contracting homotopy;
4. the contraction survives the restricted-product completion;
5. no inverse of \(\Xi\), zero inspection, or fitted inner–outer factorization is used.

## Concrete contraction target

On either open sector, the desired homotopy is a family \(h(z)\) satisfying

\[
T(z)h(z)=I
\]

and

\[
h(z)T(z)=I
\]

on the declared complex domains, or the corresponding graded homotopy equations when boundary components are retained.

This is the concrete version of the earlier canonical-acyclicity proposal. The Toeplitz construction supplies the candidate differential and the Blaschke model space supplies its immediate hostile witness.

## Why ordinary parametrices are insufficient

A Fredholm parametrix gives inverse identities only modulo compact operators. Compact remainders can carry finite-dimensional zero states. Therefore Fredholmness, index zero, or invertibility modulo compacts does not prove exactness.

Likewise, a cutoffwise inverse may diverge or lose its domain during completion. The contraction must be continuous in the source topology and compatible with the arithmetic bonding maps.

## Two-sector form

For a genuine Ubersector, the differential should retain both reciprocal components and the seam carrier. Schematically,

\[
\mathcal C_z^- \longleftrightarrow \mathcal C_z^+
\]

is sewn through a boundary object. Exactness must be proved separately on the two open components. The seam is allowed to carry nontrivial comparison data because it is where the reciprocal charts meet unitarily.

A freely adjoined Julia defect channel is not a source-derived differential. It completes the operator after the defect is known and therefore cannot establish acyclicity.

## Finite falsifier

Use a degree-one Blaschke factor. Its two-term Toeplitz complex has

\[
\ker T_B=0,
\qquad
\dim\operatorname{coker}T_B=1.
\]

Any proposed universal contraction must fail on this complex. The exact failed equation identifies whether the alleged homotopy smuggles in a divisor inverse, drops a model-space state, or changes the domain.

For theta cutoffs, the corresponding falsifier is the first parameter and label packet at which the proposed contraction residual is nonzero or its norm loses completion control.

## Disposition

The defect-support formulation is now correctly typed, but it is not yet an RH advance. An off-seam zero is equivalent to off-seam cohomology of the Toeplitz family.

The only noncircular next move is to derive the Toeplitz family from labelled theta/Tate source operations and construct its open-sector contraction before identifying its determinant with \(\Xi\).
