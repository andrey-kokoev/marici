# Halmos two-projection theory gives the canonical two-by-two prolate colligation behind the semilocal trace

## The cutoff pair

Let

\[
P=P_\Lambda,
\qquad
Q=\widehat P_\Lambda
=FP_\Lambda F^{-1}
\]

on the semilocal Hilbert space. Both are orthogonal projections. Connes's cutoff is the non-self-adjoint product

\[
R_\Lambda=PQ.
\]

Rather than inventing a feature decomposition from its scalar trace, one can use the canonical operator model for a pair of projections.

## Halmos generic-position decomposition

After separating the four intersection spaces

\[
\operatorname{ran}P\cap\operatorname{ran}Q,
\quad
\operatorname{ran}P\cap\ker Q,
\quad
\ker P\cap\operatorname{ran}Q,
\quad
\ker P\cap\ker Q,
\]

the generic part of the Hilbert space is unitarily equivalent to

\[
\mathcal K_\Lambda
\oplus
\mathcal K_\Lambda.
\]

On this part there are commuting positive contractions `C_Lambda,S_Lambda` satisfying

\[
C_\Lambda^2+S_\Lambda^2=I
\]

and

\[
\boxed{
P=
\begin{pmatrix}
I&0\\
0&0
\end{pmatrix},

Q=
\begin{pmatrix}
C_\Lambda^2&C_\Lambda S_\Lambda\\
C_\Lambda S_\Lambda&S_\Lambda^2
\end{pmatrix}.
}
\]

The operator `C_Lambda=cos Theta_Lambda` is the cosine of the principal-angle operator between the physical and Fourier cutoff subspaces.

## Product and positive compression

The product cutoff becomes

\[
\boxed{
PQ=
\begin{pmatrix}
C_\Lambda^2&C_\Lambda S_\Lambda\\
0&0
\end{pmatrix}.
}
\]

The positive triple compression is

\[
\boxed{
PQP=
\begin{pmatrix}
C_\Lambda^2&0\\
0&0
\end{pmatrix}
\succeq0.
}
\]

Thus the sewing remainder is canonically the angle cross block

\[
C_\Lambda S_\Lambda.
\]

No arbitrary inside/outside Hilbert--Schmidt factorization is needed.

## Positive row factorization of Q

Since `C` and `S` commute and satisfy `C^2+S^2=I`, define the row coisometry

\[
W_\Lambda=
\begin{pmatrix}
C_\Lambda&S_\Lambda
\end{pmatrix}.
\]

Then

\[
W_\Lambda W_\Lambda^*=I
\]

and

\[
\boxed{
Q=W_\Lambda^*W_\Lambda
=
\begin{pmatrix}
C^2&CS\\
CS&S^2
\end{pmatrix}.
}
\]

Therefore the complete `2x2` cutoff block is positive by construction, and the Connes trace observes only its first row after multiplication by `P`.

## Trace insertion

Let

\[
A=U_S(g),
\qquad
U_S(g*g^*)=AA^*.
\]

Write the two Halmos components of `A` schematically as

\[
A=
\binom{A_+}{A_-}.
\]

Then the product-cutoff quadratic expression has first-row form

\[
\operatorname{Tr}(PQAA^*)
=
\operatorname{Tr}
\left(
C^2A_+A_+^*
+
CS A_-A_+^*
\right)
\]

whenever the displayed products are trace class.

The complete positive `Q`-trace is

\[
\operatorname{Tr}(QAA^*)
=
\|CA_++SA_-
\|_{HS}^2.
\]

Hence the missing terms are canonically

\[
CS A_+A_-^*,
\qquad
S^2A_-A_-^*.
\]

These are exactly the conjugate cross entry and outside-square entry found formally before, but now they are typed by the bounded angle operators.

## Prolate operator

The nonzero spectral data of

\[
PQP
\]

are the eigenvalues of

\[
C_\Lambda^2.
\]

This is the standard time--band limiting/prolate concentration operator. Eigenvalues near `1` correspond to nearly common physical/Fourier support; eigenvalues near `0` correspond to the Sonin sector.

The complementary operator is

\[
S_\Lambda^2=I-C_\Lambda^2.
\]

Thus the positive/negative prolate decomposition proposed by Connes--Consani--Moscovici is already the spectral decomposition of the Halmos angle operator for the two trace cutoffs.

## Sonin harmonic sectors

The nongeneric intersections have direct interpretations:

- `ran P intersect ker Q`: physically supported but Fourier-vanishing sector;
- `ker P intersect ran Q`: Fourier-supported but physically vanishing sector;
- their Fourier exchange gives the two orientations of the Sonin condition.

The semilocal Sonin space is built from simultaneous gaps in physical and Fourier support, so it belongs naturally to the extreme-angle/harmonic boundary of this two-projection complex.

This gives a concrete bridge between the cutoff trace and the semilocal prolate/Sonin construction without identifying it with Suzuki's cokernel.

## Finite-part issue in angle coordinates

Connes's theorem determines

\[
\operatorname*{FP}_{\Lambda\to\infty}
\operatorname{Tr}
\left(
C_\Lambda^2A_+A_+^*
+
C_\Lambda S_\Lambda A_-A_+^*
\right).
\]

It does not determine separately the finite parts of

\[
C_\Lambda^2,
\qquad
C_\Lambda S_\Lambda,
\qquad
S_\Lambda^2.
\]

However, all three are now functions of the single angle operator. Their correlations are exact:

\[
(CS)^2=C^2(I-C^2).
\]

This is much stronger than unrelated Cauchy bounds and preserves the decisive prolate cancellation.

## Canonical transition modes

Diagonalizing `C_Lambda^2` with eigenvalues `lambda_n in [0,1]`, each generic mode contributes the positive rank-one matrix

\[
\boxed{
\begin{pmatrix}
\lambda_n&
\sqrt{\lambda_n(1-\lambda_n)}\\
\sqrt{\lambda_n(1-\lambda_n)}&
1-\lambda_n
\end{pmatrix}
=
\binom{\sqrt{\lambda_n}}
      {\sqrt{1-\lambda_n}}
\begin{pmatrix}
\sqrt{\lambda_n}&
\sqrt{1-\lambda_n}
\end{pmatrix}.
}
\]

Thus the full sewing problem decomposes into canonical prolate transition modes, not prime-labelled channels.

## What positivity would require

For each mode, the Connes trace retains

\[
\lambda_n|a_{+,n}|^2
+
\sqrt{\lambda_n(1-\lambda_n)}
a_{-,n}\overline{a_{+,n}},
\]

while the complete positive square is

\[
\left|
\sqrt{\lambda_n}a_{+,n}
+
\sqrt{1-\lambda_n}a_{-,n}
\right|^2.
\]

The missing completion is therefore explicit mode by mode. To identify it with endpoint--gamma terms, one must prove that the omitted second-row contribution has the source-prescribed finite part.

## Prime dependence

Finite places enter through the semilocal Hilbert space, Fourier transform, and scaling operator `A=U_S(g)`. Consequently both the angle operator `C_Lambda,S` and the observer components `A_plus,A_minus` are semilocal and prime-dependent.

The primes are not diagonalized independently. They modify the common prolate angle spectrum and its mode amplitudes.

## Candidate positive completion

The canonical positive completion at finite cutoff is

\[
\boxed{
\mathcal P_{\Lambda,S}(g)
=
\operatorname{Tr}
\left(
Q_\Lambda
U_S(g)U_S(g)^*

ight)
=
\|W_\Lambda U_S(g)
\|_{HS}^2,
}
\]

when trace class. On the noncompact space this generally has an additional volume divergence, so it cannot simply replace Connes's trace.

The source question is whether conditioning by the semilocal prolate/Sonin negative sector produces a relative version of this positive trace whose finite part equals the completed Weil form.

## Disposition

The cutoff pair itself supplies the sought `2x2` colligation:

\[
\boxed{
Q_\Lambda
=
\begin{pmatrix}
C_\Lambda^2&C_\Lambda S_\Lambda\\
C_\Lambda S_\Lambda&S_\Lambda^2
\end{pmatrix}
=W_\Lambda^*W_\Lambda
\succeq0.
}
\]

Connes's trace uses its first row through `P_Lambda Q_Lambda`. The semilocal prolate operator is the angle operator `C_Lambda^2`, and the missing positive completion is its second row. The next exact comparison is between the finite part of that second row and the endpoint--gamma correction selected by Sonin/prolate conditioning.
