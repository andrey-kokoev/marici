# The k-successor 4-simplex turns positive filling into a base case plus defect-square induction

## Five tetrahedral faces

Adjoin the refinement direction as vertex `5` to the presentation tetrahedron
`1234`. The oriented boundary is

\[
\partial[12345]
=
[2345]-[1345]+[1245]-[1235]+[1234].
\]

Here:

- `[1234]` is the positive pyramid filler at stage `k`;
- `[2345]`, `[1345]`, `[1245]`, and `[1235]` are the four prisms transporting
  its faces through the successor `k -> k+1`;
- the resulting opposite tetrahedron is the filler at stage `k+1`.

Thus the 4-simplex equation compares “fill, then refine” with “refine all four
faces, then fill.”

## Metric form of the fifth-face equation

Let

\[
C_k=X_k^*X_k
\]

be the positive common bulk at stage `k`, and let

\[
B_k=\beta_k^*\beta_k
\]

be the odd-endpoint demand. Define the Schur margin

\[
M_k=C_k-B_k.
\]

Assume the four successor prisms identify the old bulk and endpoint features
inside the next stage through isometries, while the new `k`-layer contributes a
source-defined orthogonal defect feature

\[
Y_k:E_k\longrightarrow\mathcal D_k.
\]

The metric 4-simplex equation is then

\[
\boxed{
C_{k+1}=S_k^*C_kS_k+Y_k^*Y_k,}
\]

\[
\boxed{
B_{k+1}=S_k^*B_kS_k.}
\]

Subtracting gives

\[
\boxed{
M_{k+1}=S_k^*M_kS_k+Y_k^*Y_k.}
\]

This is the higher-dimensional noncircular identity: the fifth face is the
positive defect square left after transporting the four old faces.

## Positive induction theorem

If

\[
M_0\succeq0,
\]

then

\[
M_k\succeq0
\]

for every finite `k`. Indeed, positivity is preserved by pullback along `S_k`,
and \(Y_k^*Y_k\succeq0\). Iteration gives

\[
\boxed{
M_k
=S_{0,k}^*M_0S_{0,k}
+
\sum_{j<k}
S_{j+1,k}^*Y_j^*Y_jS_{j+1,k}
\succeq0.}
\]

Consequently

\[
B_k\preceq C_k,
\]

which is the desired Schur--Douglas estimate at every finite stage.

## Why this can break circularity

The argument does not define \(Y_k\) as \(M_{k+1}^{1/2}\). It requires
\(Y_k\) to be the already source-constructed orthogonal defect row introduced
by one refinement step. In the semilocal positive dilation, the candidate is
the new Halmos/dyadic defect layer. Those refinement maps are isometric and
the new layer is orthogonal by construction.

Therefore the proof becomes noncircular if one verifies directly, before any
Jordan minimalization, that:

1. the four old face features are carried isometrically into depth `k+1`;
2. the completed odd endpoint feature has no new orthogonal component;
3. the new physical common-bulk component is exactly the dyadic defect row
   \(Y_k\);
4. the depth-zero margin is positive.

No global Schur inequality is assumed in these four checks.

## Concrete finite-cutoff target

Write the depth refinement of the physical common feature as

\[
X_{k+1}S_k
=J_kX_k\oplus Y_k,
\]

where \(J_k\) is an isometry. Write endpoint transport as

\[
\beta_{k+1}S_k=R_k\beta_k
\]

with \(R_k\) an isometry. Taking Grams immediately yields the two boxed
4-simplex equations.

Thus the exact calculation to perform on the existing sign-preserving dyadic
Halmos refinement is

\[
\boxed{
X_{k+1}S_k-J_kX_k
	ext{ is the orthogonal new defect row }Y_k,}
\]

and not a direct proof of \(B_k\preceq C_k\).

## Limit passage

Finite-stage positivity passes to the completed form only if the increasing
sum of defect squares is closable and its partial forms Mosco-converge. This is
where the previously isolated uniform observer-tail estimate enters. The
4-simplex induction handles positivity; it does not by itself supply the
completion estimate.

## Resulting programme

The positive tetrahedron problem has been converted into:

- one depth-zero calculation;
- one exact local refinement identity;
- one analytic closure/tail theorem.

This is strictly stronger than stagewise signed coherence and avoids assuming
the desired contraction at every `k` independently.
