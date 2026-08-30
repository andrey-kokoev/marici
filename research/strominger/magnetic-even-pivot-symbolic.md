# The stable even Schur pivot is a two-column collision identity

Let `q=2w`.  Index the old minus columns in the collision window by

\[
b_e=a-q+2e,qquad e=0,\ldots,w-1,
\]

and the boundary-covector rows by

\[
R_d=r_+-(2d-1),qquad d=1,\ldots,w.
\]

The entry of column `b_e` on row `R_d` is the path coefficient with index

\[
R_d-(-b_e-g)=2(e-d+1).
\]

It vanishes when `d>e+1`.  The collision-chain matrix is therefore upper
triangular, with `B0` on its diagonal.  Stable depth `a-q>=4` makes every
diagonal entry nonzero.

The new plus observation row meets old column `b_e` at index `2e+1`.  The first
triangular equation consequently gives

\[
\lambda_1=-\frac{B_1^{\mathrm{old}}}{B_0^{\mathrm{old}}},
\qquad b_0=a-q.
\]

Although the full covector has `w` entries, the new plus column begins one row
below the observation row.  It meets `R_d` at path index

\[
2-2d.
\]

Only `d=1` is supported.  Hence all later covector coefficients are necessary
to annihilate the old block but irrelevant to the new pivot evaluation.  The
effective pivot is exactly

\[
v_{mathrm{eff}}
=-B_1^{\mathrm{new}}
+\frac{B_1^{\mathrm{old}}}{B_0^{\mathrm{old}}}B_0^{\mathrm{new}}.
\]

Remove the common factor `(-1)^g a rising (g-1)`.  Direct simplification gives

\[
\boxed{
-B_1^{\mathrm{new}}
+\frac{B_1^{\mathrm{old}}}{B_0^{\mathrm{old}}}B_0^{\mathrm{new}}
=qg(g+h-1).
}
\]

Restoring the common factor proves

\[
\boxed{
v_{mathrm{eff}}
=(-1)^gqg(g+h-1)a^{\overline{g-1}}.
}

At the rigid offset `h=4`, this is the required

\[
(-1)^gqg(g+3)a^{\overline{g-1}}.
\]

This is an all-parameter stable proof.  It uses only support arithmetic,
triangular collision-chain elimination, and the two endpoint coefficients.  No
growing determinant, fitted recurrence, or matrix inverse remains in the even
pivot derivation.
