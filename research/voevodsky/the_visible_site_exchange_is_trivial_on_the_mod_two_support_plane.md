# The visible site exchange is trivial on the mod-two support plane

## Question

Does the explicit exchange of the two loop coordinates induce the nontrivial parity involution needed by the conditional symmetry selector?

## Rank-nine basis action

The source scalar basis contains

\[
\begin{aligned}
e_1&=y_{23}y_{31}\varphi_{001},&
e_2&=y_{23}\varphi_{001},&
e_3&=y_{23}\varphi_{002},\\
e_4&=y_{31}\varphi_{001},&
e_5&=y_{31}\varphi_{002},&
e_6&=\varphi_{002},\\
e_7&=\varphi_{001},&
e_8&=y_{23}^2\varphi_{001},&
e_9&=y_{31}^2\varphi_{001}.
\end{aligned}
\]

The visible coordinate exchange

\[
\chi:y_{23}\longleftrightarrow y_{31}
\]

acts by

\[
e_2\leftrightarrow e_4,
\qquad
e_3\leftrightarrow e_5,
\qquad
e_8\leftrightarrow e_9,
\]

and fixes \(e_1,e_6,e_7\).

## Action on the supported plane

The final-block frame for the source-supported plane is

\[
e_6=(1,0,0,0),
\qquad
v_{\rm alg}=(0,\alpha,\beta,\gamma)
\]

in coordinates \((e_6,e_7,e_8,e_9)\). Modulo two,

\[
\beta\equiv\gamma\equiv0,
\]

so

\[
v_{\rm alg}\equiv(0,\bar\alpha,0,0).
\]

The exchange \(e_8\leftrightarrow e_9\) therefore fixes both supported generators modulo two. On the parity plane visible from this frame, its matrix is

\[
\chi_K=I_2.
\]

## Scope

This computes the action of the explicit loop-coordinate transposition on the displayed support frame. It does not prove that projective reciprocity

\[
(x,y,t)\mapsto(y,x,t^{-1})
\]

lifts to exactly this coordinate transposition on the compactified del Pezzo model. Such an identification requires the missing coordinate-origin map.

It also does not compute the action of the node involution \(t\mapsto-t\) on the ambient Picard lattice.

## Consequence

The visible site exchange cannot provide the nontrivial involution required by the conditional parity selector. Even if it is identified with reciprocity, its displayed mod-two action fixes all three nonzero parity candidates rather than selecting one.

The remaining symmetry target is the ambient lift of \(t\mapsto-t\), or another involution whose action mixes \(e_6\) and \(v_{\rm alg}\) modulo two.

## Disposition

One candidate symmetry action is now computed and is trivial on the two-bit support plane. The torsion theorem still excludes \((0,0)\), but visible site exchange does not distinguish \((1,0),(0,1),(1,1)\).
