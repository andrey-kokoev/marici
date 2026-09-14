# The global reflection is fiberwise inversion on a four-split-fiber pencil

Project the Cayley--Menger double cover away from the fixed base point \([1:0:0]\):

\[
[a:b:h:W]\longmapsto[b:h].
\]

After resolving the two points above the projection center, this is an elliptic pencil. On the affine base \(q=b/h\), its fiber is

\[
W^2=G(a,q,1),
\]

where \(G\) is quadratic in \(A=a^2\). The global reflection \(a\mapsto-a\) acts fiberwise as elliptic inversion.

The discriminant of this quadratic in \(A\) factors exactly as

\[
\begin{aligned}
\operatorname{disc}_A G={}&(x-y-z)(x-y+z)(x+y-z)(x+y+z)\\
&\cdot(q-y-z)(q+y+z)\\
&\cdot(q-2x-y-z)(q+2x+y+z).
\end{aligned}
\]

Away from the external triangle discriminant, the pencil therefore has four distinguished critical fibers:

\[
q=\pm(y+z),
\qquad
q=\pm(2x+y+z).
\]

At every one of these values the quartic becomes a perfect square,

\[
G(a,q,1)=Q_q(a^2)^2,
\]

so the fiber splits into two rational components

\[
W=+Q_q(a^2),
\qquad
W=-Q_q(a^2).
\]

The two signs within each \(q\)-pair yield the same square polynomial. Thus the global surface recovers geometrically the previously observed pattern of two repeated collision types.

Each component is preserved by \(a\mapsto-a\). The differences of the two components in the four split fibers are therefore invariant algebraic roots. Their single fiber relation leaves rank three, explaining the previously derived invariant multiplicity

\[
\dim(E_7^+)=3
\]

without appealing merely to a Weyl-group classification.

This identifies what the invariant algebraic classes mean: they are differences of components of the four split fibers of the reflection-adapted elliptic pencil. The next comparison is now geometric and localizable: match the known source node-to-\(e_6\) Gysin center to one such component difference, and then identify the component combination represented by \(v_{\rm alg}\).

Executable certificate:

- `research/voevodsky/checkers/analyze_reflection_elliptic_pencil.py`;
- `research/voevodsky/results/reflection_elliptic_pencil.json`.
