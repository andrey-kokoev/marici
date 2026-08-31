# The strict Cayley law overcoerces the square source block but remains valid as the three-port complement

> **Seam-kernel qualification.** The successor packet
> `a-strict-same-sign-arithmetic-complement-cannot-create-a-dressed-seam-zero.md`
> proves that, when both boundary imaginary parts have the same passive sign
> and \(\operatorname{Im}D_U\) is strict, every seam kernel has arithmetic
> coordinate zero. The Cayley law remains a complement constructor, but it
> cannot create arithmetic-dressed seam zeros.

## Scope correction

The earlier same-sign Cayley no-go concerned the square arithmetic/history
characteristic

\[
M_U=D_U+B^\dagger R_HB.
\]

With \(D_U=\Theta_{\rm ar}\), this block is uniformly invertible even on the
seam. It therefore cannot itself carry the Xi divisor.

The minimal three-port characteristic contains an additional theta source
coordinate with zero diagonal:

\[
M_{\theta U}
=
\begin{pmatrix}
V^\dagger R_HV&V^\dagger R_HB\\
B^\dagger R_HV&D_U+B^\dagger R_HB
\end{pmatrix}.
\]

Strictness of the lower-right block does not imply invertibility of this full
matrix.

## Full imaginary part

Let

\[
C=(V\;B):
\mathbb C_\theta\oplus U_{\rm ar}\to H.
\]

Then

\[
M_{\theta U}
=C^\dagger R_HC
+
\begin{pmatrix}0&0\\0&D_U\end{pmatrix}.
\]

In the common upper-half-plane sign convention,

\[
\operatorname{Im}M_{\theta U}
=
C^\dagger(\operatorname{Im}R_H)C
+
\begin{pmatrix}0&0\\0&\operatorname{Im}D_U\end{pmatrix}.
\]

The Cayley law gives

\[
\operatorname{Im}D_U
\ge(3-2\sqrt2)I
\]

on the arithmetic coordinate only. The theta coordinate receives no direct
strict diagonal term.

## Off-seam consequence

Off the seam, the resolvent Weyl form has strict sign on nonzero vectors in
the range of \(C\). If

\[
C(c,x)=0
\]

has no nonzero solution compatible with the reduced source quotient, then the
full imaginary part is strict and \(M_{\theta U}\) is invertible.

Thus the strict Cayley law remains useful as arithmetic-complement control,
while the history Weyl form supplies off-seam control of the theta direction.

## Seam consequence

On the seam, the boundary value of \(\operatorname{Im}R_H\) may be only
semidefinite or relational because the history generator meets continuous
spectrum. The strict arithmetic diagonal still controls \(x\), but it does
not eliminate a theta defect carried by \(c\).

After eliminating the invertible arithmetic block, that possible defect is
exactly the dressed scalar

\[
F_\theta
=
V^\dagger R_HV
-
V^\dagger R_HB Q_U^{-1}B^\dagger R_HV.
\]

Therefore the three-port architecture can retain seam zeros even though its
arithmetic complement is uniformly passive.

## Revised status of the Cayley candidate

Rejected:

- treating \(M_U\) alone as the Xi pencil;
- assigning its zero-free determinant to the Xi divisor.

Still admissible:

- using \(D_U=\Theta_{\rm ar}\) in the arithmetic complement \(Q_U\);
- using its strict gap to justify Schur elimination;
- locating the divisor only in \(F_\theta\).

## Remaining tests

To use the Cayley law in G4, prove:

1. common sign convention for \(R_H\) and \(D_U\);
2. absence of a dark source vector in \(\ker C\) off the seam;
3. operator-norm and relative-ideal completion of \(Q_U\);
4. limiting absorption for the seam boundary value;
5. the divisor identity \(F_\theta=E_\theta\tau\).

## Disposition

Independent reread restores the strict prime Cayley law as a viable
arithmetic-complement constructor. Its previous rejection applies only when
the square source block is mistaken for the entire Xi pencil. The theta zero
diagonal supplies the required defect channel in the three-port system. G4
remains open at the dressed-scalar/Xi identity and seam completion. No RH
conclusion is authorized.
