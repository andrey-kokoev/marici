# The alternate magnetic chart reduces to one transverse scalar

Companion to `checkers/magnetic_alternate_schur_checks.py` (7/7, exit 0) and
`results/magnetic_alternate_schur.json`.

At the even chart divisor (q=2g+8, k=g/2+4), replace target row (1) by
row (3).  Separate the two reflected endpoint columns

\[
(a,m)=(0,-3g-7),qquad(g+8,1)
\]

and target rows (0,3) from all interior rows and columns.  In this ordering,

\[
M_{\mathrm{alt}}=
\begin{pmatrix}
A_g&B_g\\
C_g&E_g
\end{pmatrix}.
\]

Exact elimination through even grade (30) gives an invertible interior core
(A_g) and the upper-triangular Schur block

\[
S_g=E_g-C_gA_g^{-1}B_g
=
\begin{pmatrix}
-(2g+7)(4)^{\overline g}&-(g+8)^{\overline g}\\
0&\tau_g
\end{pmatrix}.
\]

Consequently,

\[
\det M_{\mathrm{alt}}
=\varepsilon_g\det(A_g)
\bigl(-(2g+7)(4)^{\overline g}\bigr)\tau_g,
\]

where \(\varepsilon_g\) is the explicitly tracked row/column permutation sign.
The first endpoint factor is automatically nonzero for \(g\ge2\).

The growing alternate determinant has therefore compressed to two statements:

\[
\det A_g\ne0,\qquad \tau_g\ne0.
\]

Both hold exactly for all even (2\le g\le30).  The lower-left Schur entry is
identically zero throughout the range, showing that the minus endpoint cannot
feed the transverse row-(3) response after interior elimination.  The entire
chart repair is carried by the scalar \(\tau_g\).

This is the discrete counterpart of the fixed-sector/transverse-jet
decomposition: the row-(0) endpoint supplies the fixed observation energy,
while \(\tau_g\) measures whether row \(3\) detects the direction missed by the
failed (0,1) chart.

## Scope

This is an exact finite fixed-width reduction through grade \(30\), not yet
an unbounded derivation of the closed formula for \(\tau_g\). The interior-core
nonvanishing is proved separately by the triangular-core theorem. The remaining
target is a symbolic boundary-elimination derivation of the scalar response.
