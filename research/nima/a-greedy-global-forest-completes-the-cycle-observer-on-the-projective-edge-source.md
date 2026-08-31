# A greedy global forest completes the cycle observer on the projective edge source

## Question

Can the finite spanning-forest observer be made cutoff-natural and continuous on a projective exponential completion?

## Claim boundary

Yes after fixing an admissible well-order of each ratio block and using its greedy global forest. Chord projection is contractive in every weighted edge seminorm, initial cutoffs inherit the same forest decomposition, and no nonzero projectively summable divergence-free flow can remain on the forest.

## Projective edge source

For one ratio block \(D\), enumerate translated shell edges

\[
E_D=\{e_1,e_2,\ldots\}
\]

by a source-fixed order refining arithmetic cutoff. Let \(W(e)\ge0\) be a proper edge grade and define

\[
q_\delta(c)
=
\sum_{e\in E_D}|c_e|e^{\delta W(e)},
\qquad
\mathcal C_{D,\exp}
=
\bigcap_{\delta>0}\ell^1(E_D,e^{\delta W}).
\]

Finite initial packets are dense in every seminorm.

## Greedy global forest

Process edges in the fixed order. Admit \(e_j\) to \(T_D\) exactly when its endpoints are not already connected by admitted earlier edges. Otherwise declare \(e_j\) a chord.

This constructs a spanning forest of the countable graph. More importantly, every rejected edge has its fundamental forest path among earlier edges. Therefore each initial cutoff

\[
E_D^{(N)}=\{e_1,\ldots,e_N\}
\]

inherits precisely the finite greedy forest and chord decomposition. No later edge changes an earlier chord coordinate.

## Continuous cycle port

Define

\[
Z_Dc=(c_e)_{e\in E_D\setminus T_D}.
\]

Give the chord target the restricted projective seminorms

\[
z_\delta(Z_Dc)
=
\sum_{e\notin T_D}|c_e|e^{\delta W(e)}.
\]

Then

\[
z_\delta(Z_Dc)\le q_\delta(c).
\]

Thus the global chord port is continuous without loss of exponential order. Initial truncations commute exactly with \(Z_D\).

## Faithfulness on the completed kernel

Suppose both the common history and chord port vanish. Common-history vanishing gives zero interval coverage and hence zero graph boundary:

\[
\partial_Gc=0.
\]

Chord vanishing leaves \(c\) supported on the forest \(T_D\). A nonzero divergence-free \(\ell^1\) flow cannot exist on a forest. To see this, remove any edge carrying nonzero flow. Each resulting component must pass the same net magnitude through every successive finite cut separating that edge from infinity. Summing absolute flow over the disjoint cut levels yields an infinite \(\ell^1\) norm. This contradicts

\[
q_0(c)<\infty.
\]

Hence \(c=0\). Therefore

\[
(B_D,Z_D):
\mathcal C_{D,\exp}
\longrightarrow
\mathcal H_D\oplus\mathcal Z_{D,\exp}
\]

is injective.

## Cutoff naturality

Let \(P_N\) be initial edge truncation and \(Q_N\) the corresponding chord truncation. The greedy construction gives

\[
Z_DP_N=Q_NZ_D.
\]

Since \(P_Nc\to c\) in every \(q_\delta\), continuity gives

\[
Z_DP_Nc\longrightarrow Z_Dc
\]

in every chord seminorm. The projective observer is therefore the strong limit of its finite minimal observers.

## Noncanonicity boundary

The construction depends on the admitted edge order. Different orders produce different forest coordinates related by cycle-space changes of basis. The canonical object is still the cycle space and its projective topology, not one forest.

A G4 claim of canonical recovery must either:

1. source the edge order;
2. retain the invariant cycle-space object rather than chosen coordinates;
3. prove coherence between admissible forest choices.

## Disposition

The cycle observer admits a continuous, cutoff-natural projective completion after a source-fixed greedy ordering. This closes the topological existence problem but not canonicality or G4 authority. The next depth-first task is to identify whether the existing prime/grade order supplies the required forest order and whether reciprocal reflection preserves it. No RH conclusion is authorized.
