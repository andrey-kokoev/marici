# The naive physical Tate/reference channel Grams miss the ordered cross seam

## Objective

Make the previously symbolic physical Grams explicit and test whether their difference equals the transported centered regulator.

Fix a finite regulator

\[
\alpha=(\Lambda,R,N,n,F).
\]

Suppress the finite angular, depth, and conductor projections in the notation. Put

\[
P=P_\Lambda,
\qquad
A=P_R-P_\Lambda,
\]

so that

\[
PA=AP=0,
\qquad
P+A=P_R.
\]

Let \(Q^T\) be the Tate Fourier cutoff and \(Q^0\) its pure-translation reference on the same transported carrier. Write

\[
\Delta Q=Q^T-Q^0.
\]

For an observer amplitude \(g\), let \(U_g=U_S(g)\).

## Naive positive channel features

The direct two-channel positive features are

\[
\boxed{
X_{diag}^T(g)
=
\begin{pmatrix}
Q^TPU_g\\
Q^TAU_g
\end{pmatrix},
\qquad
X_{diag}^0(g)
=
\begin{pmatrix}
Q^0PU_g\\
Q^0AU_g
\end{pmatrix}.
}
\]

Since \(Q^T,Q^0\) are projections, their polarized Grams are

\[
G_{diag}^T(g,h)
=
\operatorname{Tr}
\left(
U_h^*(P Q^T P+A Q^T A)U_g
\right),
\]

\[
G_{diag}^0(g,h)
=
\operatorname{Tr}
\left(
U_h^*(P Q^0 P+A Q^0 A)U_g
\right).
\]

Therefore

\[
\boxed{
G_{diag}^T-G_{diag}^0
=
U^*(P\Delta QP+A\Delta QA)U.
}
\]

This is the diagonal-channel relative form.

## Ordered Connes relative form

The regulated ordered product uses the first physical row against the complete outer window:

\[
D_{ord}(g,h)
=
\operatorname{Herm}
\operatorname{Tr}
\left(
U_h^*P\Delta Q(P+A)U_g
\right).
\]

Expanding gives

\[
\boxed{
D_{ord}
=
U^*
\left[
P\Delta QP
+
\frac12
(P\Delta QA+A\Delta QP)
\right]
U.
}
\]

The second term is the ordered inside--annular cross seam.

## Exact mismatch

Subtracting the two forms gives

\[
\boxed{
\begin{aligned}
D_{ord}-(G_{diag}^T-G_{diag}^0)
&=
U^*
\left[
\frac12(P\Delta QA+A\Delta QP)
-A\Delta QA
\right]
U.
\end{aligned}
}
\]

There is no general reason for this operator to vanish. Orthogonality \(PA=0\) does not imply

\[
P\Delta QA=0
\]

because the Fourier cutoff difference does not preserve the physical window decomposition.

Thus the natural diagonal two-channel Grams do **not** satisfy

\[
G_{phys}^T-G_{phys}^0=D_{ord}
\]

in general.

## Finite-dimensional hostile

Take two orthogonal window projections \(P,A\) and a self-adjoint \(\Delta Q\) with nonzero off-diagonal block

\[
P\Delta QA\ne0.
\]

Then the ordered form contains that cross block while the diagonal channel-Gram difference does not. This already disproves automatic physical alignment in dimension two.

The obstruction is structural, not asymptotic.

## Correct complete channel feature

The physical feature must retain cross polarization before taking Grams. Introduce the Hadamard window coordinates

\[
W_+=\frac{P+A}{\sqrt2},
\qquad
W_-=\frac{P-A}{\sqrt2}.
\]

Equivalently retain both original channels together with their polarized cross pairing. A complete feature must have enough rows to recover

\[
P\Delta QP,
\qquad
P\Delta QA,
\qquad
A\Delta QP,
\qquad
A\Delta QA
\]

separately.

The eight-leg transported construction has exactly this role: common/difference doubling records the Hermitian ordered cross seam without forcing the two observer placements to commute.

## Revised common-remainder gate

The common-remainder equation must not compare the Krein residual with \(G_{diag}^{T,0}\). It must compare it with complete cross-polarized physical Grams

\[
G_{cross}^{T,0}
=(X_{cross}^{T,0})^*X_{cross}^{T,0}
\]

whose difference has first been verified to equal \(D_{ord}\):

\[
\boxed{
G_{cross}^T-G_{cross}^0=D_{ord}.
}
\]

Only then is the common-bulk question well typed:

\[
\boxed{
G_{cross}^T-
\widehat G^T
=
G_{cross}^0-
\widehat G^0
\succeq0.
}
\]

Equality of the two remainders follows algebraically from equality of their signed differences. Positivity is the remaining substantive condition.

## Consequence

The previously missing definitions of \(X_{phys}^{T,0}\) have two possible meanings:

1. diagonal two-channel features — explicit but incorrectly aligned with the ordered form;
2. complete cross-polarized features — correctly typed, but their positive normalization and comparison with the independently physical regulator must be declared.

Therefore the first step is not to prove positivity of an unnamed remainder. It is to fix \(X_{cross}^{T,0}\) as the authoritative physical positive features and verify their exact Gram difference.

## Disposition

The naive physical choice is falsified:

\[
\boxed{
G_{diag}^T-G_{diag}^0
\ne D_{ord}
}
\]

whenever the inside--annular Fourier cross seam is nonzero.

The full polarity-cube filler must use a cross-polarized physical feature. After that correction, the open metric theorem reduces to positivity of one common remainder.
