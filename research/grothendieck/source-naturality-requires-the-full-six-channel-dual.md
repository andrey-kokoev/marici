# Source Naturality Requires the Full Six-Channel Dual

## Surprise

The five-channel lift is sufficient to make adjacent degree comparisons orthogonal. It is not sufficient to make the resulting metric natural under changes of source presentation.

The issue is categorical, not numerical. Let the original carrier have the source coflag

\[
0\longrightarrow T\longrightarrow V\longrightarrow W\longrightarrow0,
\]

where (T) is the two-dimensional tail plane and (W) is the one-dimensional wall quotient. The five-channel construction adjoins

\[
(\det T)^*\oplus W^*.
\]

The wall dual really does linearly dualize (W). But the determinant dual is a covector on the area line (\det T), not a linear covector on (T). It cannot supply a nondegenerate bilinear evaluation pairing with the two tail coordinates.

## Scaling falsifier

Apply a scalar change of tail presentation (t\mapsto\lambda t). On

\[
T\oplus W\oplus(\det T)^*\oplus W^*,
\]

the five coordinate weights are

\[
(1,1,0,-2,0).
\]

A presentation-natural bilinear coefficient between coordinates of weights (r_i,r_j) can survive only when (r_i+r_j=0). Neither tail weight (1) has a partner of weight (-1). Both tail rows of every invariant bilinear form therefore vanish, making the form degenerate.

This does not contradict the seven-parameter degree-global form. That form is invariant under the narrow adjacent-degree comparison family, which supplies a preferred flag and shear. It is not natural under the larger source automorphism group.

## Canonical repair

The linear dual demanded by source naturality is the full dual carrier:

\[
V\oplus V^*
=
T\oplus W\oplus T^*\oplus W^*.
\]

Its dimension is six. It carries the canonical split evaluation form

\[
Q_{\mathrm{ev}}
=
\begin{pmatrix}
0&I_3\\
I_3&0
\end{pmatrix}.
\]

For every invertible source transfer (A), the functorial lift

\[
A\oplus A^{-T}
\]

preserves (Q_{\mathrm{ev}}) exactly. No fitted metric parameters remain. The signature is ((3,3)).

## Meaning of the sixth channel

The sixth coordinate is not a new physical wall or another categorical rung. It is the missing second component of the tail covector. Replacing (T^*) by the one-dimensional line ((\det T)^*) preserved oriented area while erasing directional linear comparison.

Thus two different closures must not be conflated:

- five channels close exterior orientation under the degree subgroup;
- six channels close a presentation-natural linear Clifford pairing.

The determinant line remains useful as the top exterior readout of the six-channel object, but it cannot substitute for the full dual before linear pairing.

## Consequence for the analytic strip

The next source construction is no longer to invent germs for two abstract determinant channels. It is to derive the adjoint Mellin/Pearson action on (V^*), including the wall evaluation covector. If the analytic strip supplies that contragredient action continuously, its canonical evaluation metric is already fixed. If it does not, the Clifford route fails at a precise source-lift gate.

## Verification

The dependency-free checker `research/grothendieck/checkers/full_tail_dual_requires_six_channels.py` verifies the five-channel scaling radical and exact preservation of the six-channel evaluation form by a nontrivial rational transfer and its contragredient.
