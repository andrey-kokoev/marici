# Correction: the mixed external coefficient is closed; the live residual is the ordered bulk four-block

## Fresh-state correction

The earlier frontier

\[
(m,a_{\rm shape},a_{\rm coeff},a_{\rm sum})=(1,1,0,0)
\]

is stale. Existing completed zero-trace work already proves

\[
\mathfrak b_\partial^+-\mathfrak b_\partial^-+\mathfrak F_B=0.
\]

Thus the external wall/jump/linking flux, including its coefficient and completed summation, is closed. The quotient calculation identifying the relative-cell form with the canonical Krein exchange shape remains correct, but it is explanatory rather than the live gate.

The corrected external coordinate is

\[
(m,a_{\rm shape},a_{\rm coeff},a_{\rm sum})=(1,1,1,1).
\]

## Live bulk kernel

For resolved source histories define the polarized two-height bulk form

\[
\mathcal C(w,z)
=\langle DK_w,zK_z\rangle
+\langle wK_w,DK_z\rangle.
\]

In an ordered two-column frame \((e_1,e_2)\), its complete datum is

\[
C_X(w,z)=
\begin{pmatrix}
\mathcal C(w,z;e_1,e_1)&\mathcal C(w,z;e_1,e_2)\\
\mathcal C(w,z;e_2,e_1)&\mathcal C(w,z;e_2,e_2)
\end{pmatrix}.
\]

The remaining local comparison is the entrywise residual

\[
\mathcal R_X^{\rm bulk}(w,z)
=C_X^{\rm source}(w,z)-C_X^{\rm arith}(w,z).
\]

All four ordered entries must vanish before codiagonalization.

## Why diagonal data are insufficient

For any diagonal unitary

\[
U_\varphi=\operatorname{diag}(1,e^{i\varphi}),
\]

the matrix

\[
C_\varphi=U_\varphi^*CU_\varphi
\]

has the same two diagonal entries, trace, determinant, eigenvalues, and positivity as \(C\), while

\[
(C_\varphi)_{12}=e^{i\varphi}C_{12}.
\]

Therefore no collection of diagonal energies, determinant checks, or positive-shape certificates identifies the ordered bulk polarization.

## Minimal finite tomography

For a Hermitian diagonal specialization \(C(z,z)\), let \(q(v)=v^*Cv\). Besides \(q(e_1)\) and \(q(e_2)\), evaluate

\[
q(e_1+e_2),\qquad q(e_1-ie_2).
\]

Then

\[
\operatorname{Re}C_{12}
=\frac{q(e_1+e_2)-q(e_1)-q(e_2)}2,
\]

\[
\operatorname{Im}C_{12}
=\frac{q(e_1-ie_2)-q(e_1)-q(e_2)}2
\]

for the convention conjugate-linear in the first variable. These four probes reconstruct the complete Hermitian cell and detect every phase hostile.

For the full two-height kernel, diagonal tomography is not enough: one must evaluate the same ordered four entries for arbitrary \((w,z)\), or prove a holomorphic polarization theorem from a source-open diagonal set.

## Radical descent

If \(N_X\) is the radical of the even zero-trace bulk form, the comparison descends only if

\[
C_X(r,v)=C_X(v,r)=0
\]

for all \(r\in N_X\) and admitted \(v\). Checking only \(C_X(r,r)=0\) does not suffice.

## Refined lattice coordinate

Use

- \(b_{\rm diag}=1\): positive/even diagonal bulk data are formed;
- \(b_{\rm ord}=0\): ordered source-to-arithmetic four-block equality is unproved;
- \(b_{\rm rad}=0\): two-sided radical descent is unproved.

The live local coordinate is

\[
(b_{\rm diag},b_{\rm ord},b_{\rm rad})=(1,0,0).
\]

## Claim boundary

This correction accepts the completed external cancellation. It does not infer the ordered bulk identity from it, and it makes no RH claim.
