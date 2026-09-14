# The full nonlocal reciprocal commutant splits over the two parity sectors

## Question

What is the full commutant and anti-commutant of the reciprocal wall operator when radial nonlocality is allowed, and how does stable observation decompose across reciprocal parity?

## Claim boundary

The classification concerns all bounded operators on the doubled Hilbert carrier. It is no longer restricted to multiplication operators. Real covariance is stated relative to a declared conjugation on the undoubled carrier. Local-mass criteria do not extend to arbitrary nonlocal operators; their replacement is the parity-sector Gramian or Calkin condition.

## Carrier and reciprocal involution

Let \(H_0\) be any complex Hilbert space. It may be

\[
H_0=L^2(\mathbb R_+,K)
\]

with arbitrary multiplicity space \(K\), but no radial decomposition is needed. Set

\[
\mathcal H=H_0\oplus H_0.
\]

For \(u\in U(1)\), define

\[
W_u=
\begin{pmatrix}
0&u^{-1}I\\
u I&0
\end{pmatrix}.
\]

This is a self-adjoint unitary involution. Its spectral projections are

\[
P_\pm=\frac{I\pm W_u}{2}.
\]

The corresponding eigenspaces are

\[
\mathcal H_+
=
\{(x,ux):x\in H_0\},
\qquad
\mathcal H_-
=
\{(x,-ux):x\in H_0\}.
\]

## Full commutant

For \(T\in B(\mathcal H)\), the following are equivalent:

1. \(TW_u=W_uT\);
2. \(T\) preserves \(\mathcal H_+\) and \(\mathcal H_-\);
3. \(P_+TP_-=P_-TP_+=0\);
4. relative to \(\mathcal H=\mathcal H_+\oplus\mathcal H_-\),

   \[
   T=T_+\oplus T_-
   \]

   for arbitrary \(T_\pm\in B(H_0)\).

Therefore

\[
\{W_u\}'
\cong
B(H_0)\oplus B(H_0).
\]

In the original channel coordinates, write

\[
A=\frac{T_++T_-}{2},
\qquad
C=\frac{T_+-T_-}{2u}.
\]

Then every commuting operator has the block form

\[
T_+(A,C)=
\begin{pmatrix}
A&C\\
u^2C&A
\end{pmatrix},
\]

where \(A,C\in B(H_0)\) may be fully nonlocal in the radial coordinate. The earlier multiplier classification is the decomposable subalgebra in which \(A\) and \(C\) are operator-valued multiplication fields.

## Full anti-commutant

The relation

\[
TW_u=-W_uT
\]

is equivalent to

\[
P_+TP_+=P_-TP_-=0.
\]

Thus \(T\) exchanges reciprocal parity sectors and has the form

\[
T=
\begin{pmatrix}
0&S_{+-}\\
S_{-+}&0
\end{pmatrix}
\]

in parity coordinates, with arbitrary bounded

\[
S_{+-}:\mathcal H_-\to\mathcal H_+,
\qquad
S_{-+}:\mathcal H_+\to\mathcal H_-.
\]

In original channel coordinates this is exactly

\[
T_-(A,C)=
\begin{pmatrix}
A&C\\
-u^2C&-A
\end{pmatrix},
\]

with arbitrary \(A,C\in B(H_0)\). The two parity-transition blocks are

\[
S_{-+}=A+uC,
\qquad
S_{+-}=A-uC.
\]

## Equality of even and odd observation strength

Let

\[
S=\operatorname{diag}(I,-I).
\]

Then

\[
T_-(A,C)=S T_+(A,C).
\]

Since \(S\) is unitary,

\[
T_-^*T_-=T_+^*T_+.
\]

This equality is valid for arbitrary bounded nonlocal \(A,C\), not only multipliers. Reciprocal parity changes the variance of the observer but not its ungraded Gramian.

## Parity-sector Gramian criterion

Under the unitary identifications

\[
H_0\longrightarrow\mathcal H_\pm,
\qquad
x\longmapsto2^{-1/2}(x,\pm ux),
\]

a commuting observer becomes

\[
(A+uC)\oplus(A-uC).
\]

Consequently it is bounded below if and only if both parity blocks are bounded below. Its exact lower modulus is

\[
m(T_+)=
\min\bigl(m(A+uC),m(A-uC)\bigr).
\]

Its Gramian is positive in the Calkin algebra if and only if both

\[
(A+uC)^*(A+uC)
\]

and

\[
(A-uC)^*(A-uC)
\]

have positive invertible Calkin classes on \(H_0\).

The same criterion holds for the anti-commuting observer because its Gramian is equal. In parity coordinates the anti-commuting observer exchanges the sectors, but the two transition blocks must still both carry the required margin.

## Compact and finite-defect decomposition

A commuting \(T\) is compact if and only if both parity blocks \(T_+\) and \(T_-\) are compact. It is upper semi-Fredholm if and only if both parity blocks are upper semi-Fredholm. Its kernel is

\[
\ker T
\cong
\ker(A+uC)\oplus\ker(A-uC).
\]

Finite repair must therefore be injective on the actual direct sum of parity defects. Checking only one sector is insufficient unless a Real or other comparison cell proves equivalence of the defects.

## Fixed-fiber Real structure

Let \(\kappa_0:H_0\to H_0\) be a conjugation. Define

\[
J_u=
\operatorname{diag}(I,u^2I)(\kappa_0\oplus\kappa_0).
\]

It preserves each reciprocal parity eigenspace and induces \(\kappa_0\) under the identifications above.

For either the commuting or anti-commuting block family, fixed-fiber Real covariance is equivalent to

\[
\overline A=A,
\qquad
\overline C=u^2C,
\]

where

\[
\overline A=\kappa_0A\kappa_0,
\qquad
\overline C=\kappa_0C\kappa_0.
\]

Equivalently, both parity blocks \(A\pm uC\) commute with \(\kappa_0\). This remains valid for nonlocal operators.

## Why local mass stops here

Uniform local mass is a criterion for decomposable multiplication observers because the observer Gramian can be tested interval by interval. A general element of \(B(H_0)\) may mix disjoint radial regions. It has no pointwise field \(W(r)^*W(r)\), so the expression

\[
\int_IW(r)^*W(r)\,dr
\]

is undefined.

For the full commutant, the correct operational criteria are instead:

- lower moduli of \(A+uC\) and \(A-uC\);
- their Calkin Gramian classes;
- finite residual kernels;
- explicit localization estimates only when an additional propagation or integral-kernel structure is declared.

Nonlocality is not a defect, but it removes the local-mass constructor.

## Integral-kernel subcase

If \(A\) and \(C\) are integral operators with declared kernels, reciprocal classification still uses the same block formulas. Coercivity, however, depends on the global singular values of

\[
A\pm uC.
\]

Kernel support, decay, or off-diagonal bounds may produce sufficient estimates, but none follows from reciprocal covariance. A compact integral kernel cannot provide an essential margin on an infinite-dimensional parity sector.

## Green--Real role assignment

- \(P_\pm\): reciprocal parity selectors;
- \(T_+\in\{W_u\}'\): parity-preserving observer;
- \(T_-\): parity-exchanging observer;
- \(J_u\): Real comparison preserving both parity sectors;
- sector Calkin Gramians: essential-observation tests;
- multiplier local mass: additional criterion only in the decomposable subalgebra.

## Deliberate failures

1. The full commutant is not the multiplier algebra.
2. Commutation with \(W_u\) does not imply locality in the radial coordinate.
3. Reciprocal covariance does not supply a local-mass field.
4. Stability on one parity sector does not imply stability on the other.
5. Equal even/odd Gramians do not identify their reciprocal variance.
6. A compact nonlocal kernel does not supply an essential Calkin margin.

## Disposition

The full bounded reciprocal commutant and anti-commutant are classified. Both retain the same original-channel block formulas as the multiplier families, but \(A\) and \(C\) are now arbitrary bounded operators on the undoubled carrier. Parity diagonalization reduces stable and essential observation to the two operators \(A\pm uC\). Uniform local mass remains valid only in the decomposable multiplier subalgebra; the full nonlocal theory is governed by sector Gramians and Calkin margins.
