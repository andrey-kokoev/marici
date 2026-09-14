# A reciprocal-parity observer must control both infinite sectors

## Question

What does the essential-margin theorem become for the reciprocal involution in the doubled Green carrier?

## Claim boundary

An observer equivariant under a self-adjoint reciprocal involution decomposes into parity blocks. Stable joint observation with a compact analytic channel requires an essential lower margin on every infinite-dimensional parity sector. Reading only the wall-compatible positive sector cannot suffice when the negative sector is infinite-dimensional.

## Problem

Let \(X\) carry a self-adjoint unitary involution

\[
W=W^*=W^{-1}.
\]

Then

\[
X=X_+\oplus X_-,
\qquad
X_\pm=\ker(W\mp I).
\]

Let \(A:X\to Y\) be compact and let \(D:X\to Z\) be a proposed complementary observer compatible with reciprocal parity.

## Bold conjecture

Because the Green wall lies in one reciprocal eigenspace, observing that eigenspace together with a compact analytic channel suffices to reconstruct the full doubled carrier.

## Named rivals

1. Every infinite-dimensional parity sector requires its own essential lower margin.
2. A compact analytic channel can repair the omitted opposite-parity sector.
3. Cross-parity mixing in \(D\) can replace blockwise control while retaining equivariance.
4. Boundary-wall maximal isotropy implies carrier-level completeness.

## Equivariant block decomposition

Assume \(Z\) carries a self-adjoint involution \(W_Z\) and

\[
DW=W_ZD.
\]

Then \(D\) maps \(X_\pm\) into \(Z_\pm\), so

\[
D=D_+\oplus D_-.
\]

Consequently

\[
D^*D=D_+^*D_+\oplus D_-^*D_-.
\]

Equivariance excludes cross-parity compensation. Rival 3 fails under the declared symmetry.

## Parity essential-margin theorem

The following are equivalent:

1. \(D\) is upper semi-Fredholm;
2. each \(D_\pm\) is upper semi-Fredholm;
3. there exist finite-dimensional \(K_\pm\subset X_\pm\) and \(\delta_\pm>0\) such that

   \[
   \|D_\pm x\|
   \ge
   \delta_\pm\|x\|
   \qquad
   (x\in K_\pm^\perp\cap X_\pm).
   \]

Because there are only two sectors, the combined essential margin is

\[
\delta_{\rm ess}=\min(\delta_+,\delta_-)>0.
\]

For compact \(A\), the joint observer

\[
T=\binom AD
\]

is bounded below exactly when the two block conditions hold and

\[
\ker A\cap(\ker D_+\oplus\ker D_-)=0.
\]

Thus \(A\) may repair only the finite-dimensional residual kernels in the two sectors.

## One-sector no-go

Suppose \(D\) observes only positive parity:

\[
D|_{X_-}=0.
\]

If \(X_-\) is infinite-dimensional, choose an orthonormal sequence \((x_n)\subset X_-\). Then

\[
Dx_n=0,
\qquad
Ax_n\to0
\]

by compactness. Hence

\[
Tx_n\to0.
\]

No stable lower bound exists. This rejects rivals 1 and 2 in favor of mandatory two-sector control.

## Radial reciprocal eigenspaces

For

\[
W_u=
\begin{pmatrix}
0&u^{-1}\\
u&0
\end{pmatrix},
\qquad |u|=1,
\]

we have \(W_u=W_u^*\) and \(W_u^2=I\). Its eigenspaces are

\[
X_+
=
\{(f,uf):f\in L^2(\mathbb R_+)\},
\]

and

\[
X_-
=
\{(f,-uf):f\in L^2(\mathbb R_+)\}.
\]

Both are infinite-dimensional.

At the boundary fiber, the Green wall relation is

\[
\Lambda_u=\{(c,uc):c\in\mathbb C\},
\]

which is the positive eigenspace of the boundary action. But \(\Lambda_u\) is a boundary domain condition, not a census of the entire carrier. Maximal isotropy of \(\Lambda_u\) does not eliminate the negative-parity bulk sector.

## Correction of notation

The matrix entry in \(W_u\) is \(u\), not an independent symbol. Explicitly,

\[
W_u(f_+,f_-)
=
(u^{-1}f_-,uf_+).
\]

This gives the stated eigenspaces and keeps the phase-decorated fold relation

\[
C_uF^2=W_uC_u.
\]

## Real compatibility

Coefficientwise conjugation need not preserve a fixed \(u\)-wall unless it also conjugates the phase parameter. The correct Real object therefore records the pair

\[
(u,W_u)\longmapsto(\bar u,W_{\bar u}).
\]

When the chosen Real structure fixes the wall phase, the parity subspaces are Real reducing subspaces and the transpose--adjoint comparison decomposes blockwise. Otherwise the Real comparison exchanges the \(u\) and \(\bar u\) fibers rather than acting within one fiber.

This is a further typing condition on any `real_reciprocal_observer`.

## Constructor-role consequences

A `boundary_condition` selects the maximal-isotropic trace relation \(\Lambda_u\). A `carrier_observer` acts on \(X_+\oplus X_-\). A `reciprocal_parity_complement` must declare essential bounds on both infinite sectors. These roles cannot be inferred from one another.

The required signature fields are:

- carrier parity decomposition;
- target parity decomposition;
- block observers \(D_+,D_-\);
- essential margins \(\delta_+,\delta_-\);
- finite residual kernels;
- Real action on the phase parameter \(u\).

## Strongest falsification attempt

The wall graph is maximal isotropic and determines a self-adjoint first-order domain. That is the strongest reason to suspect positive-parity sufficiency. It fails because self-adjoint domain closure is a statement about boundary flux, while stable carrier observation is a lower-frame statement on bulk states. An orthonormal sequence in \(X_-\) has no contradiction with maximal isotropy at the wall.

## Disposition

The bold conjecture is rejected. Reciprocal symmetry splits the doubled carrier into two infinite sectors, and a stable complement must control both essentially. The positive wall relation determines the conservative domain but cannot serve as the sole carrier observer. Real compatibility additionally requires explicit transport of the phase parameter unless \(u\) lies on a fixed Real locus.
