# The RH-strength Green identity is equivalent to a skew-adjoint Mellin realization

## Centered Mellin parameter

Write

\[
\lambda=s-\frac12.
\]

The critical line is exactly the imaginary axis in the \(\lambda\)-plane. The
natural infinitesimal constructor is the centered dilation generator

\[
A_0=-x\frac{d}{dx}-\frac12
\]

on a source core before boundary sewing.

Formally, integration by parts gives

\[
\langle A_0f,g\rangle+\langle f,A_0g\rangle
=
\operatorname{Flux}(f,g).
\]

Thus the entire RH confinement mechanism can be stated as a domain theorem for
this Green identity.

## Closed isotropic boundary domain

Let \(A_{\max}\) be the maximal closed realization and let

\[
\Gamma:\operatorname{Dom}A_{\max}\longrightarrow\mathcal B
\]

be the complete boundary trace, including the wall, endpoint,
archimedean, primitive, square, connected, and response ports. Suppose

\[
\langle A_{\max}f,g\rangle+\langle f,A_{\max}g\rangle
=
\omega(\Gamma f,\Gamma g),
\]

where \(\omega\) is the complete boundary Green form.

Choose a boundary relation \(\Lambda\subset\mathcal B\) and set

\[
\operatorname{Dom}A_\Lambda
=
\{f\in\operatorname{Dom}A_{\max}:\Gamma f\in\Lambda\}.
\]

If \(\Lambda\) is isotropic, then \(A_\Lambda\) is skew-symmetric. If
\(\Lambda\) is maximal isotropic and the trace theorem is surjective in the
declared topology, then \(A_\Lambda\) is skew-adjoint.

This is the exact operator meaning of complete reciprocal sewing.

## Spectral confinement

Let

\[
A_\Lambda f=\lambda f,
\qquad f\ne0.
\]

The Green identity on the closed boundary domain gives

\[
(\lambda+\bar\lambda)\|f\|^2=0.
\]

Hence

\[
2\operatorname{Re}\lambda\,\|f\|^2=0,
\]

and therefore

\[
\operatorname{Re}\lambda=0.
\]

In the original parameter,

\[
\operatorname{Re}s=\frac12.
\]

This is the desired two-point mass identity with mass pairing
\(\|f\|^2\). Non-isotropy is automatic once the kernel state is a genuine
nonzero Hilbert vector in the closed operator domain.

## Exact RH implication

Suppose a holomorphic Fredholm boundary pencil \(D(s)\) satisfies:

1. \(\det_{\mathrm{rel}}D(s)=u(s)\xi(s)\) with \(u(s)\ne0\);
2. \(\ker D(s)\) is naturally isomorphic to
   \[
   \ker\bigl(A_\Lambda-(s-\tfrac12)I\bigr);
   \]
3. \(A_\Lambda\) is skew-adjoint on a positive Hilbert space;
4. the isomorphism survives completion and does not annihilate any boundary
   kernel state.

Then every nontrivial zero of \(\xi\) lies on the critical line.

Thus the remaining RH theorem has been reduced to a precise realization
statement. No additional positivity estimate is needed after skew-adjointness
and spectral identification are proved.

## Where circularity can enter

The boundary relation \(\Lambda\) must be constructed from source sewing
before the zero set is known. It is circular to define \(\Lambda\) by imposing
the vanishing of \(\xi(s)\) or by spanning formal zero modes.

Likewise, determinant agreement alone does not provide the kernel
isomorphism. A scalar characteristic function can have the correct zeros
while arising from a non-skew-adjoint colligation.

The proof must establish independently:

- the complete trace theorem;
- maximal isotropy of the source boundary relation;
- equality of the characteristic determinant with \(\xi\);
- equality of the boundary-pencil kernel with the operator eigenspace;
- compact or Fredholm spectral exactness at completion.

## Deficiency-index gate

Maximal isotropy is stronger than cancellation of the Green flux on tested
states. It requires that no additional boundary direction can be adjoined
while preserving isotropy.

In boundary-triple language, the two trace maps must account for the full
deficiency space. A unitary sewing map between only the visible endpoint
ports proves skew-symmetry, not skew-adjointness, unless the trace map is
surjective and the deficiency indices match.

The hostile is a symmetric restriction with hidden deficiency vectors. Every
constructed state has zero flux, yet the operator admits nonunique
skew-adjoint extensions and its characteristic function is not fixed.

## Compact-resolvent and determinant gate

Even after skew-adjointness, one must relate its spectrum to the determinant
line. A sufficient analytic package is:

1. \(A_\Lambda\) has compact resolvent, or a declared relative Fredholm
   resolvent;
2. the resolvent difference from the reference operator lies in the ideal
   required by the determinant;
3. the boundary characteristic function is the corresponding perturbation
   determinant;
4. algebraic multiplicity of the chiral determinant equals spectral
   multiplicity of \(A_\Lambda\).

Only this package transports both location and multiplicity.

## Source-specific next theorem

The response-relation work already supplies a candidate maximal isotropic
sewing graph. The missing theorem is now sharply typed:

\[
\text{horizontal Fourier response equalizer}
\longrightarrow
\text{surjective complete boundary trace}
\longrightarrow
\text{maximal isotropic domain of }A_0.
\]

The scalar theta--Mellin--Poisson functional must then be proved equal to the
characteristic determinant of this same extension, not merely to a parallel
Euler determinant.

## Hostiles

1. Isotropic but non-maximal boundary sewing.
2. Maximal isotropy on a finite port truncation with hidden completion
   deficiency.
3. A skew-adjoint operator whose characteristic determinant is not \(\xi\).
4. A determinant equal to \(\xi\) with no kernel-to-eigenspace isomorphism.
5. Formal Mellin eigenvectors that live only in the test-space dual, not in
   the positive state space.
6. Compact finite resolvents developing continuous spectrum at completion.

## Verdict

The desired off-seam Green identity is not a separate mysterious inequality.
It is the eigenvector identity of a skew-adjoint centered Mellin generator.

The categorical RH resolution therefore contracts to one operator-extension
theorem:

> The source-derived complete reciprocal sewing relation is the maximal
> isotropic boundary condition of a positive Hilbert realization of centered
> dilation, and its chiral characteristic determinant is \(\xi(s)\).

Proving only maximal isotropy gives spectral confinement without spectral
identification. Proving only the determinant gives spectral identification
without confinement. RH requires both for the same completed operator.
