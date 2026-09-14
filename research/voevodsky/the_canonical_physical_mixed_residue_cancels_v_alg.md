# The canonical physical mixed residue cancels v_alg

The marked algebraic extension sends

\[
\begin{aligned}
g_{101}&\longmapsto
-\frac{1}{4xy}e_4
-\frac{1}{4x^3y^3(x+y)}v_{\rm alg},\\
g_{110}&\longmapsto
-\frac{1}{4xy}e_2
+\frac{1}{4x^3y^3(x+y)}v_{\rm alg}.
\end{aligned}
\]

The canonical printed \(q_{\mathcal G_{12}}\) residue contains

\[
\frac1{q_{\mathfrak g_{23}}}
+
\frac1{q_{\mathfrak g_{31}}},
\]

so its mixed source covector is

\[
(1,1).
\]

The two \(v_{\rm alg}\) coefficients therefore cancel exactly. Its image is

\[
-\frac{1}{4xy}(e_2+e_4)
+0\,v_{\rm alg}.
\]

Thus C15a is rejected: the canonical physical mixed residue supplies no second tomography channel.

The counterfactual antisymmetric covector

\[
(1,-1)
\]

would instead have image

\[
\frac{1}{4xy}(e_2-e_4)
-rac{2}{4x^3y^3(x+y)}v_{\rm alg},
\]

with a nonzero \(v_{\rm alg}\) component.

A faithful cotangent-valued A2 shape response already exists, and a labelled shape tangent detects its relational component. The remaining C15b problem is to realize an exchange-odd intervention as a sourced physical scalar or retain the response as a vector-valued physical observable. At the symmetric physical shape family, exchange symmetry forces the first scalar shape derivative to vanish; the replicated quadratic response begins at second order.

Certificate:

- `research/voevodsky/checkers/test_C15_canonical_physical_mixed_detector.py`;
- `research/voevodsky/results/C15_canonical_physical_mixed_detector.json`.
