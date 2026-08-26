# Reciprocal half-form Gram positivity does not orient the cross-kernel

## Bounded question

Does the reciprocal Gram kernel of the quarter-density-weighted staircase
features supply new theta-specific positivity capable of preventing scalar
cancellation?

## Feature vectors

For an admitted finite prime-power packet \(J\), define

\[
\Phi_+(z)
=\bigl(\eta_jB_j[A](z)\bigr)_{j\in J},
\]

and

\[
\Phi_-(z)
=\bigl(\eta_jB_j[A](-z)\bigr)_{j\in J}.
\]

Here \(\eta_j\) is the canonical square root of the positive arithmetic
weight. The reciprocal cross-kernel is

\[
K_J(z,w)=\langle\Phi_+(z),\Phi_-(w)\rangle.
\]

## Universal Gram positivity

The two-vector Gram matrix

\[
G_J(z,w)=
\begin{pmatrix}
\|\Phi_+(z)\|^2&K_J(z,w)\\
\overline{K_J(z,w)}&\|\Phi_-(w)\|^2
\end{pmatrix}
\]

is positive semidefinite for every source for which the feature vectors are
defined. This is the ordinary Gram theorem. It yields only

\[
|K_J(z,w)|^2
\leq
\|\Phi_+(z)\|^2\|\Phi_-(w)\|^2.
\]

It gives an upper bound, not a nonzero lower bound.

## Smallest orthogonality witness

Take two nonzero feature vectors

\[
u=(1,1),
\qquad
v=(1,-1).
\]

Then

\[
\langle u,v\rangle=0
\]

while both diagonal norms are positive and the Gram matrix remains positive.
Thus full Gram positivity permits complete cross cancellation.

Even reciprocal conjugacy is insufficient. If \(v=\overline u\), then the
cross entry is the bilinear square sum

\[
\langle u,\overline u\rangle=\sum_ju_j^2.
\]

For \(u=(1,i)\), this also vanishes although \(u\ne0\).

## Consequence for the theta packet

The quarter-density lift makes the feature space and its diagonal energy
canonical. It does not prevent the reciprocal feature vectors from becoming
orthogonal after oscillatory phase transport. Positivity of the full Gram
matrix is therefore another universal carrier fact.

To obtain zero confinement one needs a source-derived acute relation such as a
strict lower bound on the normalized cross overlap, or a cone preserved by all
theta constructors. Neither follows from Gram positivity or reciprocal
conjugacy.

## Result

The reciprocal Gram construction adds no RH force at the level of positivity
alone. The only possibly source-specific datum is the actual orientation of
its off-diagonal cross-kernel.

The hostile falsifier is rank two: any proposed theorem admitting the two
vectors above while claiming nonvanishing from diagonal positivity is false.

## Next gate

Compute the source-derived phase evolution of the normalized overlap

\[
\rho_J(z)
=\frac{K_J(z,z)}
{\|\Phi_+(z)\|\,\|\Phi_-(z)\|}.
\]

The required theorem must keep \(\rho_J(z)\) away from zero off seam through a
constructor law absent for hostile sources. Bounding only \(|\rho_J|\leq1\)
is universal and insufficient.
