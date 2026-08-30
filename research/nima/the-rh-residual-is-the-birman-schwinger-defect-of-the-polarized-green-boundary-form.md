# The RH residual is the Birman--Schwinger defect of the polarized Green boundary form

## Analytic boundary operator

Let \(H_X\) be the finite typed analytic carrier. Suppose the full two-height
Green identity has been derived before scalar projection:

\[
\mathcal B_X(\eta,\zeta)
=
(\zeta+\bar\eta)
G_X(\eta)^*G_X(\zeta).
\]

The boundary pairing \(\mathcal B_X\) includes the endpoint, primitive, square,
connected, seam, and archimedean currents.

On the right half-plane diagonal, define the positive boundary operator

\[
B_X(\zeta)
=
\mathcal B_X(\zeta,\zeta)
=
2\operatorname{Re}\zeta\,
G_X(\zeta)^*G_X(\zeta).
\]

This is the source candidate for the analytic block left open by the graph
Schur reduction. It is not arbitrary: it is fixed by the polarized Green
identity and the complete boundary factorization.

## Residual operator

Let \(U_X\) be weighted arithmetic synthesis and set

\[
F_X=U_XU_X^*.
\]

The graph-augmented residual is

\[
R_X(\zeta)=B_X(\zeta)-F_X.
\]

Assume first that \(B_X(\zeta)>0\) on the finite carrier. Define the normalized
frame interaction

\[
K_X(\zeta)
=
B_X(\zeta)^{-1/2}
F_X
B_X(\zeta)^{-1/2}.
\]

Then

\[
R_X(\zeta)
=
B_X(\zeta)^{1/2}
\left(I-K_X(\zeta)\right)
B_X(\zeta)^{1/2}.
\]

Thus

\[
\ker R_X(\zeta)
\cong
\ker\!\left(I-K_X(\zeta)\right).
\]

An RH-sensitive residual zero is exactly an eigenvalue-one state of the
Birman--Schwinger operator \(K_X(\zeta)\).

## Strict contraction criterion

Because \(F_X\ge0\), one has \(K_X\ge0\). If the source proves

\[
\lVert K_X(\zeta)\rVert\le\rho_K<1
\]

uniformly over cutoffs and over every compact subset of the open right
half-plane, then

\[
R_X(\zeta)
\ge
(1-\rho_K)B_X(\zeta)>0.
\]

Consequently \(R_X(\zeta)\) is invertible and its determinant is nonzero.

This is the exact strict relative bound sought by the observer-comparison
programme. Non-strict domination

\[
F_X\le B_X
\]

is insufficient because equality on one state produces a residual zero.

## Equality case

If \(K_Xh=h\), put

\[
g=B_X^{-1/2}h.
\]

Then

\[
F_Xg=B_Xg.
\]

The analytic boundary energy of \(g\) is exactly saturated by the
source-generated frame energy. This state lifts to the graph kernel

\[
(-U_X^*g,g).
\]

Therefore an off-seam zero corresponds to a source-generated state saturating
the Green boundary supply. The RH-bearing theorem must exclude such saturation
in both open sectors.

## Polarized rather than diagonal authority

The diagonal identity only defines \(B_X(\zeta)\) pointwise. It does not prove
that the family is holomorphic, reciprocal, or compatible with the determinant
line.

The source must first derive the two-height kernel
\(\mathcal B_X(\eta,\zeta)\). Its positivity and factorization provide the
reproducing-kernel or colligation structure that transports the strict bound
between spectral points.

A diagonal estimate fitted separately at each \(\zeta\) can hide incompatible
phases and does not define a categorical section.

## Boundary factorization

After Cayley transformation, the polarized identity has the form

\[
\mathcal B_X(v,w)
=
I-\Theta_X(v)^*\Theta_X(w)
=
(1-w\bar v)\mathcal G_X(v)^*\mathcal G_X(w).
\]

This supplies the conservative analytic boundary block only if every typed
current is present in the input/output spaces.

The operator \(B_X\) used in the Schur residual must be the Gram operator of
this complete boundary factorization. A scalar flux difference or endpoint
projection is not enough.

## Left sector

On the left half-plane, reverse the sign of the Green polarization so that the
sector boundary form is positive:

\[
B_{-,X}(\zeta)
=
-2\operatorname{Re}\zeta\,
G_{-,X}(\zeta)^*G_{-,X}(\zeta).
\]

Define

\[
K_{-,X}
=
B_{-,X}^{-1/2}
U_{-,X}U_{-,X}^*
B_{-,X}^{-1/2}.
\]

Reciprocal sewing must identify \(K_{-,X}(\zeta)\) with the appropriately
daggered \(K_{+,X}(-\zeta)\) or \(K_{+,X}(1-s)\), according to the chosen
coordinate.

A strict contraction in one sector transfers to the other only after this
operator comparison is source-derived.

## Seam behavior

As \(\operatorname{Re}\zeta\to0\), the diagonal Green factor
\(2|\operatorname{Re}\zeta|\) vanishes. Hence \(B_X^{-1/2}\) can become
singular and the strict contraction margin may close.

This is compatible with the seam being the allowed zero locus. The theorem
requires compact-local bounds in the open sectors, not a uniform bound across
the seam.

The rate at which \(B_X\) degenerates must match the seam and archimedean
boundary channels; otherwise the normalization creates a spurious singularity.

## Determinant factorization

At finite cutoff,

\[
\det R_X
=
\det B_X\,
\det(I-K_X).
\]

Where \(B_X\) is positive definite, \(\det B_X\) is a nonzero boundary unit.
All nontrivial zeros lie in

\[
\det(I-K_X).
\]

At completion, the corresponding formula must use relative determinant lines.
Primitive and square anomalies belong to \(\det B_X\) and the normalization of
\(\det_3(I-K_X)\); they cannot be discarded.

The desired \(\Xi\) bridge is therefore

\[
\det_{\mathrm{rel}}(I-K(s))
=
v(s)\Xi(s)
\]

after the nonzero Green boundary line has been separated.

## Completion gate

Euler weighting makes \(F_X\) compact in the higher grades, but
\(B_X^{-1/2}\) can amplify weak boundary directions. Completion requires:

1. a closed positive boundary form \(B(s)\);
2. relative compactness of \(F(s)\) with respect to \(B(s)\);
3. convergence of \(K_X(s)\) in the determinant ideal;
4. a compact-local strict bound \(\sup_X\lVert K_X(s)\rVert<1\);
5. exactness of the limit kernel comparison.

The fourth item is the quantitative RH gate. The first three only make the
question well-posed.

## Hostile tests

1. Positivity \(K_X\le I\) without strictness allows eigenvalue one.
2. A diagonal Green identity without polarization supplies no coherent
   spectral family.
3. Omitting one boundary channel changes \(B_X\) and can manufacture a strict
   bound.
4. Choosing \(B_X=F_X+\epsilon I\) is circular fitting.
5. Finite \(\rho_X<1\) with \(\rho_X\to1\) permits a completion zero.
6. Reciprocal scalar equality without comparison of \(K_+\) and \(K_-\) does
   not transfer the bound.
7. Uniformity across the seam imposes the wrong target.

## Consequence for categorical RH

The unknown analytic block is no longer featureless. If the complete polarized
Green identity is constructed, it supplies \(B_X\), and graph Schur reduction
turns RH into the strict relative frame inequality

\[
U_XU_X^*
<
B_X
\]

on every compact subset of both open sectors.

Equivalently, the normalized Birman--Schwinger operator must have norm strictly
below one. This is a concrete operator inequality with finite falsifiers and a
clear completion margin.

## Verdict

The categorical RH residual is the defect between the polarized Green boundary
form and the arithmetic synthesis frame. After normalization, off-seam zeros
are exactly eigenvalue-one states of a positive Birman--Schwinger operator.
The remaining RH theorem is the source-derived strict contraction bound,
together with its reciprocal and completion stability.
