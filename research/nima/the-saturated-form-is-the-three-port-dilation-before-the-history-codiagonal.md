# The saturated form is the three-port dilation before the history codiagonal

## Reconciliation

The source corpus already contains the exact rank-one wall contribution sought
after the counit-preserving shear.  It is not a new adjoined energy:

\[
J_{\mathrm{wall}}:w\longmapsto M_\Phi w
\]

is the typed transport from the retained input wall to the theta output wall.
Its squared Gram is \(M_\Phi^2P_W\).

The remaining distinction between the shifted-history and saturated forms is
therefore a codiagonal question: is the output wall kept as a separate port, or
is it added to the derivative tail before the norm is taken?

## Three-port dilation

Write \(M=M_\Phi\) and \(B=H_KD\).  Define the resolved map

\[
R:f\longmapsto(f,Bf,Mf)
\]

with target

\[
\mathcal H_{\rm in}\oplus
\mathcal H_{\rm tail}\oplus
\mathcal H_{\rm outwall}.
\]

With the direct-sum metric,

\[
R^*R=(1+M^2)I+B^*B.
\]

This is exactly the Fourier-saturated zero-cross-term form.  The required
rank-one repair is the third component \(Mf\), already typed by the wall
transport graph.

Now define the output codiagonal

\[
\nabla(t,o)=t+o
\]

and

\[
A=I_{\rm in}\oplus\nabla.
\]

Then

\[
ARf=(f,Bf+Mf)=(f,H_\Phi f),
\]

so

\[
R^*A^*AR=I+H_\Phi^*H_\Phi.
\]

This is exactly the shifted-history graph form.  Expanding \(A^*A\) on the
resolved tail/output-wall pair gives

\[
A^*A=
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix},
\]

whereas the saturated resolved metric uses the identity matrix.  Their
pullback difference is

\[
R^*(A^*A-I)R=M(B+B^*).
\]

Thus the disputed cross term is precisely the effect of the output
codiagonal.  It is neither a missing wall energy nor a parity error.

## Why the tensor-unit counit is preserved

The input component of \(R\) is exactly \(f\), so the canonical tensor-unit
counit remains unchanged.  No wall rescaling occurs.  The output wall is a
separate typed copy carrying amplitude \(M\), consistent with the established
statement that input and output walls are compared by an arrow but are not
identified as one coordinate.

This resolves the earlier two-port obstruction at the linear-algebra level:
the saturated form is a dilation, not a counit-preserving congruence of the
already codiagonalized two-port history form.

## The exact remaining source square

The first-Adams quadratic question now has a concrete commuting-square form.
One must determine whether the completed relative edge factors through
\(R\) or only through \(AR\):

\[
\begin{array}{ccc}
\mathcal H&\xrightarrow{\ R\ }&
\mathcal H_{\rm in}\oplus\mathcal H_{\rm tail}\oplus
\mathcal H_{\rm outwall}\\
&&\downarrow A\\
&&\mathcal H_{\rm in}\oplus\mathcal H_{\rm out}.
\end{array}
\]

- If the completed Green/Stokes construction retains the output wall until
  after quadratic evaluation, its pullback is the saturated form \(R^*R\).
- If it applies the codiagonal before quadratic evaluation, its pullback is
  the history form \(R^*A^*AR\).

Since \(A\) is not an isometry on the resolved two-port output, these two
orders cannot be exchanged formally.

## Four matrix units

For incidence columns \(q_1,q_2\), the complete resolved target Gram is now
specified without unknown wall/tail terms:

\[
G^{\rm res}_{ij}
=\langle q_i,q_j\rangle
 +\langle Bq_i,Bq_j\rangle
 +M^2\langle q_i,q_j\rangle.
\]

The codiagonalized history Gram is

\[
G^{\rm hist}_{ij}
=G^{\rm res}_{ij}
 +M\langle q_i,Bq_j\rangle
 +M\langle Bq_i,q_j\rangle.
\]

Therefore the four ordered matrix-unit tests reduce to computing the single
polarized matrix

\[
C_{ij}=\langle q_i,Bq_j\rangle.
\]

Its Hermitian part is strictly negative on nonzero causal incidence vectors;
its skew-Hermitian part carries reciprocal orientation.

## Status

The abstract form relation is now explicit and source-typed.  No extra wall
port needs to be invented: the theta output wall supplies exactly
\(M_\Phi^2P_W\).  G1.1 remains open only at the ordering/authority step:
prove from the completed relative Green construction whether quadratic
measurement occurs before or after the tail/output-wall codiagonal, then prove
the corresponding common-domain, radical, cutoff, and uniformity statements.
