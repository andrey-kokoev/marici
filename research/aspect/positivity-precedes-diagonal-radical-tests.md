# Positivity precedes diagonal radical tests

## Question

What is the minimal valid computation for testing whether the seven q_G12 lift-torsor directions lie in the radical of the complete physical joint form?

## Positive-form shortcut

Let \(Q\ge0\) be the complete physical form and let \(v_1,\ldots,v_7\) span the lift-torsor direction space \(V\). For a positive semidefinite form,

\[
Q(v_i,v_i)=0
\quad\Longrightarrow\quad
Qv_i=0.
\]

Therefore, after full joint positivity has been proved, the seven scalar diagonal tests

\[
Q(v_i,v_i)=0
\qquad(i=1,\ldots,7)
\]

are sufficient to establish \(V\subseteq\operatorname{rad}(Q)\). Positivity then forces every cross-pairing with the ambient space to vanish. A complete ambient pairing table is unnecessary.

## Indefinite hostile

The shortcut is invalid before positivity. For

\[
Q=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad
v=\begin{pmatrix}1\\0\end{pmatrix},
\]

one has

\[
Q(v,v)=0
\]

but

\[
Qv=\begin{pmatrix}0\\1\end{pmatrix}\ne0.
\]

Thus an isotropic direction need not be radical for an indefinite joint form. Since pair and triple restrictions can all be positive while a four-sector joint form is indefinite, restricted positivity cannot authorize the diagonal shortcut.

## Valid test order

The source audit must use one of two routes:

1. prove the complete joint form is positive semidefinite, then test the seven diagonal values;
2. without positivity, compute \(Qv_i\) and require exact zero for every torsor basis vector.

A zero \(7\times7\) restricted Gram matrix \((Q(v_i,v_j))\) is also insufficient in the indefinite case because it tests only pairings inside \(V\), not pairings with the ambient complement.

## Consequences

If complete joint positivity holds and one diagonal value is positive, norm descent fails immediately. If every diagonal vanishes, the norm descends through the torsor, but strict return still requires evaluation of the resulting quotient norm. If joint positivity fails, the proposed physical Green form itself is defective before confinement is considered.

## Verification

`research/aspect/checkers/check_psd_radical_test.py` verifies a positive-semidefinite zero direction that is radical and an indefinite isotropic direction with nonzero ambient pairing using exact rationals.

## Disposition

The rank-seven handoff is reduced to a finite exact audit, conditional on full joint positivity. The first executable request is the complete joint-form positivity certificate plus seven torsor diagonal values; absent positivity, seven full operator images are required instead.
