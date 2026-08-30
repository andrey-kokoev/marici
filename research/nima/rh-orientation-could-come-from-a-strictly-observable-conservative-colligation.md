# RH orientation could come from a strictly observable conservative colligation

Author: `marici.Nima`

Date: 2026-08-26

Status: exact sufficient mechanism and source-construction gate

## Return-map formulation

The relative determinant vessel reduces zeros to a forbidden spectral event
of a return operator. After a harmless sign convention, write the target as
exclusion of the unit eigenvalue from a sector transfer map (Theta(w)):

\[
1\notin\operatorname{spec}\Theta(w)
\]

for (w) in the open disk corresponding to one open half-plane.

A genuinely source-local way to force this is to realize (Theta) as the
transfer function of a conservative colligation.

## Conservative colligation

Let

\[
U=
\begin{pmatrix}
A&B\\
C&D
\end{pmatrix}
:
\mathcal H\oplus\mathcal E
\longrightarrow
\mathcal H\oplus\mathcal E
\]

be unitary. Its disk transfer function is

\[
\Theta(w)
=
D+wC(I-wA)^{-1}B.
\]

The conservation law for (U) yields a positive defect identity. In a
standard observable realization, it has the form

\[
I-\Theta(w)^*\Theta(w)
=
(1-|w|^2)
B^*(I-\bar wA^*)^{-1}(I-wA)^{-1}B,
\]

up to the input-output convention used for the block placement.

The right side is source-local: it is assembled from the state evolution and
coupling maps before taking a determinant.

## Strictness excludes the unit eigenvalue

If the defect form is strictly positive on every nonzero port vector, then

\[
\lVert\Theta(w)e\rVert<\lVert e\rVert
\]

for every nonzero (e) and every (|w|<1). Consequently (Theta(w)e=e) is
impossible in the open disk.

This supplies exactly the orientation missing from the determinant and braid
programmes. It is an operator conservation law derived before scalar
projection.

After identifying the theta relative determinant with
(det(I-Theta(w))) up to a nowhere-vanishing factor, strict contractivity
would confine its zeros to the sewing boundary.

## Scalar exact model

Take real (a,b) with

\[
a^2+b^2=1,
\qquad
0<|a|<1,
\]

and the orthogonal colligation

\[
U=
\begin{pmatrix}
a&b\\
b&-a
\end{pmatrix}.
\]

Its transfer function is

\[
\theta_a(w)=\frac{w-a}{1-aw}.
\]

Direct calculation gives

\[
1-|\theta_a(w)|^2
=
\frac{(1-a^2)(1-|w|^2)}{|1-aw|^2}.
\]

It is strictly positive inside the disk. Therefore
(	heta_a(w)=1) can occur only on the boundary.

## Why unitarity alone is insufficient

Adjoin a decoupled port on which the transfer is the identity:

\[
\Theta_{\mathrm{hostile}}(w)
=
\operatorname{diag}(\theta_a(w),1).
\]

This system remains conservative, but its defect has a permanent null
direction. The unit eigenvalue survives throughout the open disk.

Thus the required theorem is not merely unitary sewing. It is unitary sewing
plus strict port observability or an equivalent no-decoupled-mode condition.

## Theta/Tate constructor gate

The source must provide all of the following without using the completed
scalar section:

1. a state carrier retaining tail, seam, primitive, square, and
   archimedean components;
2. a unitary or conservative block evolution (U);
3. a transfer map equal to the relative theta return operator;
4. strict observability of every port direction in each open sector;
5. compatibility of the two disk charts on the critical seam;
6. stability of the defect identity under restricted-product completion.

The finite Clark Gram identity is a candidate energy block. The seam channel
is a candidate missing observation row. Neither currently supplies the full
colligation or its completed strictness.

## Relation to previous no-go results

This route survives the earlier objections only if it is constructed at the
operator level:

- it does not divide by the scalar section;
- it does not infer positivity from the determinant;
- it does not treat arithmetic channels as separately positive;
- it retains mixed relationship terms through the colligation energy;
- it exposes a finite hostile witness when a port direction is unobservable.

If the resulting defect identity is merely the Weil or Pick kernel after
scalar projection, the construction adds no information and must close.

## Decisive falsifier

At a finite arithmetic cutoff, compute the defect Gramian of the proposed
transfer map. One nonzero port vector in its kernel supplies a decoupled mode
on which a unit return eigenvalue is not excluded. A cutoff sequence whose
smallest defect eigenvalue tends to zero falsifies completion stability even
when every finite cutoff is strictly contractive.

