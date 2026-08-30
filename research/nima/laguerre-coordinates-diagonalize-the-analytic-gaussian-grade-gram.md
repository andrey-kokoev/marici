# Laguerre coordinates diagonalize the analytic Gaussian grade Gram

## Even Gaussian sector

Set
\[
X=\pi x^2.
\]
For an even function of \(x\),
\[
dx
\quad\longmapsto\quad
\frac1{\sqrt\pi}X^{-1/2}\,dX
\]
on the full line.

The polynomial Gaussian sector has functions
\[
e^{-X}p(X).
\]
Its analytic norm is
\[
\|e^{-X}p(X)\|_{L^2(\mathbb R,dx)}^2
=
\frac1{\sqrt\pi}
\int_0^\infty
|p(X)|^2e^{-2X}X^{-1/2}\,dX.
\]

Set
\[
y=2X.
\]
The source weight becomes the generalized Laguerre weight
\[
e^{-y}y^{-1/2}\,dy.
\]

Therefore the canonical orthogonal basis is
\[
E_k(x)
=
c_k^{(+)}
e^{-X}L_k^{-1/2}(2X),
\]
where
\[
\bigl(c_k^{(+)}\bigr)^{-2}
=
\frac1{\sqrt{2\pi}}
\frac{\Gamma(k+\tfrac12)}{k!}.
\]

Then
\[
\langle E_j,E_k\rangle=\delta_{jk}.
\]

## Odd Gaussian sector

Write odd functions as
\[
x e^{-X}p(X).
\]
Their norm is
\[
\|xe^{-X}p(X)\|^2
=
\frac1{\pi\sqrt\pi}
\int_0^\infty
|p(X)|^2e^{-2X}X^{1/2}\,dX.
\]

After \(y=2X\), the weight is
\[
e^{-y}y^{1/2}\,dy.
\]

Hence the canonical odd basis is
\[
O_k(x)
=
c_k^{(-)}
x e^{-X}L_k^{1/2}(2X),
\]
with
\[
\bigl(c_k^{(-)}\bigr)^{-2}
=
\frac1{2^{3/2}\pi\sqrt\pi}
\frac{\Gamma(k+\tfrac32)}{k!}.
\]

Again,
\[
\langle O_j,O_k\rangle=\delta_{jk}.
\]

## Resolution of the Gamma-Gram defect

The monomial grades
\[
X^ke^{-X}
\quad\text{and}\quad
xX^ke^{-X}
\]
have factorial Hankel Gram matrices. The Laguerre change of coordinates is exactly their Gram orthogonalization in the source \(L^2(dx)\) metric.

Thus the correct coefficient carrier is
\[
\ell^2(\mathbb N_0)
\otimes
\left(
\mathbb C_{\mathrm{even}}
\oplus
\mathbb C_{\mathrm{odd}}
\right)
\]
only after the synthesis maps
\[
(a_k)\longmapsto\sum_ka_kE_k,
\qquad
(b_k)\longmapsto\sum_kb_kO_k
\]
are used.

These synthesis maps are unitary onto the closed even and odd Gaussian-polynomial sectors.

## Source authority

This basis is not an arbitrary numerical preconditioner. It is forced by:

- the Gaussian source factor \(e^{-X}\);
- the full-line Jacobian \(X^{-1/2}\);
- the odd derivative factor \(x\), shifting the weight to \(X^{1/2}\);
- the unique orthogonal polynomial systems for those two weights.

The parity shift from Laguerre parameter \(-1/2\) to \(+1/2\) is the metric counterpart of the earlier degree-shifted completion polynomial.

## Completion operator

The analytic operators
\[
A(A+1)
\quad\text{and}\quad
(A-1)A
\]
can now be conjugated by the unitary Laguerre synthesis maps. Their coefficient realizations are source-equivalent to the analytic dilation graph by construction.

They will not equal the raw monomial band matrix \(\mathfrak J\). Laguerre recurrence and differentiation identities instead produce a finite-band Jacobi-type operator with normalization factors inherited from \(c_k^{(\pm)}\).

This is the correct next matrix calculation.

## Compactness boundary

Orthogonalization repairs the metric defect but does not itself create compactness. The Laguerre sectors are closed subspaces of \(L^2\), and the dilation graph can still admit escaping scale packets unless the Gaussian-polynomial closure or an additional source condition supplies confinement.

Therefore:

- unitary coefficient realization: closed;
- compact graph embedding: still unproved.

## Cutoff interpretation

Laguerre grade cutoff
\[
P_{\le K}^{\mathrm{Lag}}
\]
is an orthogonal projection in the analytic source metric. It is preferable to monomial truncation, whose condition number deteriorates rapidly.

Finite packet tests should therefore be expressed in normalized Laguerre coordinates while retaining the exact conversion to the original monomial/Jordan annotations.

## Hostile

Normalize monomial grades individually but ignore their off-diagonal Hankel correlations. The resulting coefficient metric remains wrong even though every basis vector has norm one. Full Laguerre orthogonalization is required.

## Frontier

The Gamma-weighted coefficient realization now exists exactly. The next theorem is the explicit Laguerre-basis band matrix for completion and the proof that its graph domain agrees with the transported analytic second-order dilation domain.
