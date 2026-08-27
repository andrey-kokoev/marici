# Boundary Schur recurrence preregistration

Using only even grades through 40, the fixed-size boundary response suggests

\[
\frac{S_{r+1}}{S_r}=
\frac{8(r+1)(r+2)(r+3)(2r+5)^2(4r+5)(4r+11)(2r^2+3r-12)}
{r(r+4)(2r+9)(2r^2-r-13)}.
\]

The quadratic numerator is the next value of the denominator polynomial:
\(2r^2+3r-12=P(r+1)\), where \(P(r)=2r^2-r-13\). Prediction 004 freezes
this recurrence before exact evaluation of the ten ratios at even grades 42
through 60.

## Closed hypergeometric character

Telescoping the recurrence gives the candidate closed form

\[
\begin{aligned}
S_r={}&\frac{70400}{3}\,2^{8(r-1)+1}
\frac{r!(r+1)!(r+2)!}{(r-1)!(r+3)!}
\frac{(\tfrac72)_{r-1}^2(\tfrac94)_{r-1}(\tfrac{15}4)_{r-1}}
{(\tfrac{11}2)_{r-1}}\\
&\times\frac{2r^2-r-13}{-12}.
\end{aligned}
\]

This agrees exactly with every computed boundary Schur determinant through
\(r=30\). It also exposes the complete nonvanishing argument: the Pochhammer
and factorial factors are positive, while \(2r^2-r-13\) has discriminant
105 and therefore no integral root.

This is not yet a theorem because the determinant-to-recurrence step remains
to be derived. The required certificate is now specific: eliminate the
source-ordered triangular core and show that the resulting two boundary
responses at ranks \(r\) and \(r+1\) differ by the displayed rational
character. No determinant interpolation may serve as that certificate.

## Boundary-response shape

Direct Schur elimination reveals a stronger simplification:

\[
S_g=
\begin{pmatrix}
-(2g+7)(4)^{\overline g}&*\\
0&\sigma_g
\end{pmatrix}.
\]

Thus one pivot is the direct endpoint character and is manifestly nonzero.
The lower-left response cancels exactly. The entire invariant-faithfulness
problem is the single scalar \(\sigma_g\). The hypergeometric formula above,
divided by \(-(2g+7)(4)^{\overline g}\), is its candidate closed form.
Symbolically deriving the zero lower-left entry and that last diagonal
response is now the minimal proof certificate.

Dividing the determinant recurrence by the known first pivot gives the cleaner
scalar law, with \(g=2r\) and \(P(r)=2r^2-r-13\):

\[
\sigma_1=\frac{320}{3},\qquad
\frac{\sigma_{r+1}}{\sigma_r}=
\frac{4(r+1)(r+3)(2r+5)(4r+5)(4r+7)P(r+1)}
{r(r+4)(2r+9)P(r)}.
\]

This normalization removes the already understood endpoint factors. The only
nontrivial sign change is carried by the telescoping character
\(P(r+1)/P(r)\). A source proof should therefore construct \(\sigma_r\)
directly as the response of the final boundary observation after eliminating
the triangular interior, rather than re-expand the full determinant.

The recurrence telescopes to

\[
\sigma_r=
-\frac{2240\,4^{3r-3}rP(r)
(9/4)_{r-1}(11/4)_{r-1}}
{(r+3)(2r+5)(2r+7)}.
\]

Every factor other than \(P(r)\) is nonzero for positive integral \(r\).
Moreover, \(P(r)=2r^2-r-13\) has discriminant \(105\), which is not a square.
Thus the candidate closed form has no zero at an admissible integral grade.
The checker compares this expression directly with every independently
eliminated Schur response through even grade \(20\).

## Unbounded first-column certificate

The upper-triangular shape and first pivot do not depend on the finite census.
For the minus endpoint \(a=0\), every source coefficient has the factor

\[
(0)^{\overline{g-j}}.
\]

It therefore vanishes for \(j<g\). Only \(c_g=(4)^{\overline g}\) survives,
and the magnetic path formula places its two output coefficients on target
rows \(0\) and \(1\). The alternate chart retains row \(0\), replaces row
\(1\) by row \(3\), and uses neither endpoint row in the interior core.
Consequently the minus endpoint contributes no interior \(B\)-data and no
row-\(3\) entry. Its Schur column is exactly its raw boundary column:

\[
\begin{pmatrix}
-(2g+7)(4)^{\overline g}\\
0
\end{pmatrix}.
\]

Thus the zero lower-left entry and the first pivot hold for every positive
integral grade directly by support. Only the transverse scalar
\(\sigma_r\) still requires a symbolic elimination theorem.

## Local transverse formula

Row \(3\) meets only the interior plus column at \(a=g+6\). Since \(A_g\)
is upper triangular, the relevant reconstruction coordinate is its boundary
datum divided by its diagonal pivot. Hence the growing Schur solve reduces
identically to one scalar operation \(E-CB/A\). Direct substitution of the
four path coefficients gives

\[
\sigma_g=
-\frac{8(2g+3)(g^2-g-26)(2g+1)!}
{3(g+5)(g+6)(g+7)(g-1)!}.
\]

This is algebraically identical to the \(g=2r\) hypergeometric form above.
Its only possible positive-integral zero would solve \(g^2-g-26=0\), whose
discriminant is \(105\). Therefore \(\sigma_g\ne0\) at every admissible even
grade. Together with the triangular-core theorem and the endpoint-support
certificate, this proves alternate-chart full rank for arbitrary even grade.
