# A zero Riesz projection around one is the spectral completion certificate

## Common reduced carrier

Assume the Green radical has been source-reduced, reachable and quotient
presentations are uniformly transverse, and their determinant frames have
been controlled.

Transport every cutoff operator to one fixed reduced carrier \(H_C\) over a
compact spectral set \(C\). Let

\[
K_X(s):H_C\to H_C
\]

be the transported normalized incidence operators, and let \(K(s)\) denote the
candidate limit.

Without this common carrier, resolvents and Riesz projections at different
cutoffs are not comparable.

## Limit gap and contour

Assume the limit family has a compact-local gap

\[
\delta_C
=
\inf_{s\in C}
\operatorname{dist}
\left(
1,\sigma(K(s))
\right)
>0.
\]

Choose

\[
0<r_C<\delta_C
\]

and the common contour

\[
\Gamma_C=\{z:|z-1|=r_C\}.
\]

Then \(\Gamma_C\) lies in the resolvent set of every \(K(s)\), and the interior
disk contains no limit spectrum.

The limit Riesz projection is

\[
P(s)
=
\frac{1}{2\pi i}
\int_{\Gamma_C}
(z-K(s))^{-1}\,dz
=
0.
\]

This is the precise limit zero-exclusion certificate.

## Finite Riesz projections

Whenever \(\Gamma_C\) lies in the finite resolvent set, define

\[
P_X(s)
=
\frac{1}{2\pi i}
\int_{\Gamma_C}
(z-K_X(s))^{-1}\,dz.
\]

The rank of \(P_X(s)\) is the algebraic multiplicity of finite eigenvalues
inside the disk around one.

Thus:

- \(P_X(s)=0\) means no finite defect near one;
- \(P_X(s)\ne0\) records the complete near-one defect space;
- stable rank records stable defect multiplicity.

This remains valid for compact non-normal operators. Positivity is not needed
for the contour definition.

## Norm-resolvent certificate

Suppose

\[
\sup_{s\in C}\sup_{z\in\Gamma_C}
\left\|
(z-K_X(s))^{-1}
-
(z-K(s))^{-1}
\right\|
\longrightarrow0.
\]

Then

\[
\sup_{s\in C}
\lVert P_X(s)-P(s)\rVert
\longrightarrow0.
\]

Since \(P(s)=0\),

\[
\sup_{s\in C}\lVert P_X(s)\rVert\longrightarrow0.
\]

Every nonzero projection has norm at least one. Therefore

\[
P_X(s)=0
\]

for all sufficiently large \(X\), uniformly for \(s\in C\).

This proves eventual finite spectral exclusion and rules out spectral
pollution near one.

## Uniform resolvent bound

Norm-resolvent convergence on \(\Gamma_C\) implies a uniform bound

\[
\sup_{X\ge X_0}
\sup_{s\in C}
\sup_{z\in\Gamma_C}
\lVert(z-K_X(s))^{-1}\rVert
<\infty.
\]

Conversely, a bare uniform resolvent bound without convergence does not
identify the limit projection. Both the limit zero projection and convergence
of the contour resolvents are required.

The finitely many cutoffs below \(X_0\) must be audited directly.

## Collective-compact implementation

Collective compactness plus uniform strong convergence on the common carrier
is one sufficient route to contour-resolvent convergence away from the limit
spectrum.

The required package is:

1. collective compactness of \(K_X(s)\) over \(X\) and \(s\in C\);
2. uniform strong convergence on every fixed vector;
3. the corresponding adjoint condition when non-self-adjoint spectral
   exactness requires it;
4. norm-continuity of the limit family;
5. the positive limit gap \(\delta_C\).

These hypotheses prevent an almost-defect eigenvector from escaping into new
cutoff directions.

## Strong hostile revisited

For

\[
K_n=\left(1-\frac1n\right)P_{e_n}
\]

on \(\ell^2\), one has strong convergence to zero. The limit projection around
one is zero.

But every contour radius \(r>0\) eventually encloses
\(1-1/n\), so

\[
P_n\ne0.
\]

Contour resolvents cannot converge uniformly, and collective compactness
fails. The Riesz certificate detects exactly what strong convergence misses.

## Generalized-pencil version

Before square-root normalization, let the reduced pencil be

\[
\mathcal P_X(s,\lambda)
=
F_X(s)-\lambda B_X(s).
\]

On a carrier where \(B_X\) is positive invertible, this pencil is equivalent to
\(K_X-\lambda I\).

A contour projection may be written directly from the pencil resolvent and its
\(\lambda\)-derivative. This formulation is natural under source congruence and
does not require independently chosen square-root frames.

The pencil contour certificate is preferable when reciprocal transport is
given as

\[
J_X^*F_{-,X}J_X=F_{+,X},
\qquad
J_X^*B_{-,X}J_X=B_{+,X}.
\]

## Reciprocal transfer

If reciprocal congruence acts on the common reduced carriers and transports
the contour-resolvent family, then

\[
P_{-,X}(1-s)
\]

is conjugate to the corresponding positive-sector projection.

Hence zero projection in one open sector transfers to the reciprocal sector.
Scalar determinant reciprocity alone does not transport defect spaces or their
multiplicity.

## Holomorphic parameter dependence

If \(K_X(s)\) and \(K(s)\) are holomorphic operator families, the contour
projections vary holomorphically as long as \(\Gamma_C\) remains in the
resolvent set.

Since a projection-valued holomorphic map has locally constant finite rank,
defect multiplicity cannot change inside a connected parameter region without
spectrum crossing the contour.

This provides a categorical wall-crossing interpretation: a defect token enters
or leaves only through failure of the common resolvent contour.

## Relation to determinant zeros

For determinant-class \(K_X\), a nonzero Riesz projection around one means the characteristic determinant in the eigenvalue variable has a zero inside \(\Gamma_C\). It does not imply \(\det(I-K_X)=0\) unless one itself is an eigenvalue.

When one is an eigenvalue, the order of the zero of \(\det(I-K_X)\) is its algebraic multiplicity, recorded by the corresponding Riesz projection.

At completion, determinant convergence still requires the separate Schatten
cell. The Riesz projection certifies spectral multiplicity, not normalization
of the determinant line.

## Minimal certificate record

For every compact \(C\) in an open sector, record:

1. the fixed reduced carrier and transport maps;
2. the limit gap \(\delta_C\);
3. the chosen contour \(\Gamma_C\);
4. the uniform contour-resolvent convergence bound;
5. the identity \(P(s)=0\);
6. eventual identities \(P_X(s)=0\);
7. the finite audit for earlier cutoffs;
8. reciprocal transport of the contour data.

This is a finite, falsifiable completion certificate.

## Hostile tests

1. A contour chosen before proving a limit gap may cross limit spectrum.
2. Uniform resolvent bounds without convergence do not identify Riesz
   projections.
3. Strong convergence permits nonzero finite projections to escape.
4. Parameter-pointwise contours permit moving collisions.
5. Reciprocal scalar equality does not carry projection rank.
6. Zero Riesz projection does not supply determinant-line normalization.
7. Projections on unstable cutoff carriers cannot be compared.

## Consequence for categorical RH

Spectral exactness near one is now represented by an actual idempotent. The RH
completion claim on a compact open-sector set is that the defect idempotent is
zero in the limit and eventually zero at every cutoff under contour-resolvent
transport.

This is stronger and cleaner than saying vaguely that no invisible state
appears at completion: the possible defect space, its multiplicity, and its
transport are all explicit.

## Verdict

A common contour around one with zero limit Riesz projection and uniform
norm-resolvent convergence is the direct spectral completion certificate.
Collective compactness is one implementation. The certificate excludes
escaping almost-defects while keeping spectral multiplicity separate from
determinant-line normalization.
