# Site exchange is D4 triality and fixes the diagonal pairing

Label the four conductor marks by their signs

\[
p_{\sigma\tau}=(\sigma y,\tau x).
\]

The three nonzero classes of the \(D_4\) discriminant group are the three perfect matchings:

\[
\begin{aligned}
A&=(++,+-)\mid(-+,--),\\
B&=(++,-+)\mid(+- ,--),\\
C&=(++,--)\mid(+-, -+).
\end{aligned}
\]

Here \(A\) pairs points with equal \(a\)-sign, \(B\) pairs points with equal \(b\)-sign, and \(C\) pairs points with equal sign product.

The genuine site exchange acts simultaneously by

\[
x\leftrightarrow y,
\qquad a\leftrightarrow b,
\qquad(\sigma,	au)\longmapsto(\tau,
\sigma).
\]

Therefore

\[
A\leftrightarrow B,
\qquad C\longmapsto C.
\]

In coordinates \(A=(1,0)\), \(B=(0,1)\), \(C=(1,1)\), its matrix is

\[
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

This is a nontrivial \(D_4\) triality action. Its fixed classes are zero and the unique nonzero diagonal matching

\[
C=(++,--)\mid(+-, -+).
\]

This corrects the interpretation of the earlier visible-frame computation. Swapping \(e_8,e_9\) in a rational de Rham frame did not prove that site exchange was trivial on the integral discriminant group; the missing Betti comparison was exactly where triality could act. The conductor geometry now computes that action without choosing such a comparison.

The positive physical mark \(p_{++}\) is itself fixed by site exchange. Hence an equivariantly defined physical thimble can represent only

\[
0\quad\text{or}\quad C.
\]

No fitting has selected between them. The remaining theorem is conceptual: prove whether the oriented physical thimble has nonzero image in \(D_4^\vee/D_4\). If it is nonzero, site symmetry forces the diagonal pairing automatically.

Certificate:

- `research/voevodsky/checkers/conductor_triality_site_exchange.py`;
- `research/voevodsky/results/conductor_triality_site_exchange.json`.
