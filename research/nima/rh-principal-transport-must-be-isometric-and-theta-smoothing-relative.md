# RH principal transport must be isometric and theta smoothing relative

Author: `marici.Nima`

Date: 2026-08-26

Status: exact infinite-dimensional no-go and architectural correction

## Smoothing cannot preserve a uniform angle

The proposed theta bridge was typed as a smoothing map

\[
K_\Phi:E'\longrightarrow E.
\]

On a Hilbert realization, a nuclear smoothing map is compact. An injective
compact operator of infinite rank cannot be bounded below. Otherwise its
inverse on its range would be bounded, the image of the unit ball would be
compact, and the infinite-dimensional unit ball would itself be compact.

Therefore no estimate of the form

\[
\|K_\Phi x\|\ge c\|x\|,
\qquad c>0,
\]

can hold on an unrestricted infinite-dimensional carrier.

This is not a defect in a particular theta estimate. It is a categorical
conflict between smoothing and strict transversality in one fixed Hilbert
topology.

## Native diffusion exhibits the obstruction exactly

The source-derived theta diffusion has compact resolvent. If its eigenvalues
are

\[
0=\lambda_0<\lambda_1\le\lambda_2\le\cdots,
\qquad \lambda_n\longrightarrow\infty,
\]

then for positive time its smoothing semigroup has singular values

\[
e^{-t\lambda_n}\longrightarrow0.
\]

It is contractive and may remain injective, but it has no cutoff-independent
lower bound. Contraction is therefore the wrong one-sided property for
protecting distance from the Maslov divisor.

The same mechanism appears in the tail--seam synthesis multiplier
\(|\widehat\Phi(\xi)|\to0\): high-frequency packets retain coefficient norm
while their observed source energy tends to zero.

## Corrected factorization

The principal correspondence must carry the nonvanishing geometry before
smoothing is applied. The theta/Tate source already provides a candidate:
the complete tail--seam cut

\[
U_qf=(g_q,h_q).
\]

It is an exact isometry and retains all energy that migrates across the moving
seam. Prime composition is interval concatenation, so this principal
transport is coherent under arithmetic resegmentation.

Theta smoothing should therefore enter only as a relative perturbation of an
isometric or Fredholm principal transport:

\[
T_z=U_z+K_z
\]

or, after a typed identification of domains,

\[
T_z=U_z(I+C_z).
\]

Here \(U_z\) carries the complete boundary state and \(C_z\) is compact,
trace-class, or rigged-nuclear in the source-authorized topology.

The determinant section belongs to the relative factor \(I+C_z\), not to the
smoothing map by itself.

## New Maslov formulation

The isometric principal part keeps the reference Lagrangian pair at a fixed
angle. The compact relative factor may create isolated Fredholm crossings.
A scalar zero is then a failure of invertibility of \(I+C_z\), equivalently
an eigenvalue \(-1\) of \(C_z\), with its determinant-line multiplicity.

RH becomes a sectorial exclusion theorem:

\[
-1\notin\operatorname{Spec}(C_z)
\]

throughout both open half-planes, while reciprocal sewing relates the two
relative families.

This does not solve the problem, but it removes an impossible demand. One no
longer asks a nuclear bridge to be uniformly bounded below. One asks the
identity-relative Fredholm factor to avoid one distinguished spectral value.

## Source typing

The proposed decomposition is admissible only if all parts are derived before
the scalar determinant:

1. \(U_z\) must be the complete source transport, including seam history;
2. \(C_z\) must contain the Clark, primitive, square, connected, and
   archimedean defects with their declared types;
3. \(C_z\) must be compact or determinant-class in one fixed
   constructor-generated topology;
4. reciprocal reflection must transport the full pair \((U_z,C_z)\);
5. the relative determinant must reproduce every finite source cutoff;
6. no division by \(\Xi\) or zero-location data may enter the construction.

## Why scalar diffusion remains insufficient

The completed scalar diffusion preserves reflection and the constant endpoint
mode, but hostile symmetric multipliers leave that diffusion unchanged while
altering the divisor. It cannot determine \(C_z\) uniquely.

The relative defect must retain labelled arithmetic and boundary incidence.
Otherwise the corrected Fredholm architecture merely relocates the same
scalar circularity.

## Finite falsifier

The checker uses the exact rational smoothing spectrum \(2^{-n}\). Every
finite cutoff is injective, but its smallest singular value is \(2^{-N}\)
and tends to zero. It then adjoins the identity and verifies that
\(I+K_N\) has a uniform lower bound, while a signed rank-one relative defect
with eigenvalue \(-1\) produces an isolated determinant zero.

This separates three notions exactly:

- smoothing injectivity;
- uniform principal transversality;
- isolated relative Fredholm crossing.

