# The pre-determinant characteristic lift is the doubled Clark--Grushin border, but its completed Fredholm gates remain open

The existing theta-bordering construction identifies the correct way to lift a
finite output codiagonal before taking determinants.  Let

\[
P_{\rm loc}(z)=P_+(z)\oplus P_-(z)
\]

be the reciprocal direct sum of the local paired history--arithmetic pencils,
and let

\[
W_{01}:\mathbb C^4\to X_{\rm loc}'
\]

be the four source-derived zeroth/first-moment port columns.  The Clark
codiagonal induces the completed two-port column

\[
W_{\rm Cl}:=W_{01}S_{\rm Cl}^*: \mathbb C^2\to X_{\rm loc}'.
\]

The natural pre-determinant characteristic package is the Grushin border

\[
\mathcal G_{\rm Cl}(z)=
\begin{pmatrix}
P_{\rm loc}(z)&-W_{\rm Cl}\\
-W_{\rm Cl}^{\times}&0
\end{pmatrix}
:
X_{\rm loc}\oplus\mathbb C^2
\longrightarrow
X_{\rm loc}'\oplus\mathbb C^2,
\]

where `times` is the canonical rigged transpose, not a metric-fitted adjoint.
This is the characteristic-side analogue of the Green observation cone.  It
retains the bulk state, both Clark ports, and the left/right cofactor data
before determinant scalarization.

On an invertible local chart its Schur complement is

\[
-W_{\rm Cl}^{\times}P_{\rm loc}(z)^{-1}W_{\rm Cl},
\]

so the completed Clark transfer is recovered from the same fixed codiagonal,
while the determinant line of the full border retains the background
characteristic factor.  This provides a source formula for the previously
missing characteristic lift; it is not defined from the Green cone or from Xi
zeros.

The lift is nevertheless conditional at completion.  It requires:

1. one completed closed rigged domain for `P_+ direct-sum P_-`;
2. continuity of all four moment columns and their rigged transposes there;
3. a holomorphic Fredholm family of fixed index zero;
4. the complete graded arithmetic diagonal rather than the raw strict Cayley
   substitute;
5. regularized determinant and cutoff convergence.

The first two are available for the local translation/endpoint system.  The
last three are the previously recorded operator-compiler gates.  Therefore
`G_Cl` is now an explicit source-typed candidate, but not an admitted completed
Fredholm constructor.  The cofiber comparison `beta_CG` can be written at
finite cutoff and on local charts; global promotion remains blocked by these
completion gates.
