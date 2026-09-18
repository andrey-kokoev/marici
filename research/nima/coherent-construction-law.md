# The Coherent Construction Law

## Definition

Let `X` be a positive source space, let

\[
\Gamma=\sum_{h\in\mathcal H}\epsilon_h\,\mathcal C_h
\]

be an oriented chain of admissible positive cells in `X`, and let

\[
\Phi:X\longrightarrow Y
\]

be a map to a positive geometry `Y`.

Assume:

1. every cell `C_h` has the dimension of `Y`;
2. the interiors of the pushed-forward cells cover `Y` with total degree one;
3. shared internal facets occur with opposite orientations;
4. canonical-form pushforward commutes with taking residues.

Then

\[
\boxed{
\Omega_Y
=
\sum_{h\in\mathcal H}
\epsilon_h\,\Phi_*\omega_{\mathcal C_h}
}
\]

and

\[
\partial\Gamma=\Gamma_{\mathrm{ext}}.
\]

Equivalently, all internal residues cancel and only the exterior canonical boundary of `Y` remains.

## Resolution independence

If two oriented source chains `Gamma` and `Gamma'` have the same pushforward and differ only by internal boundaries, then

\[
\Phi_*\Omega_\Gamma
=
\Phi_*\Omega_{\Gamma'}.
\]

Thus

\[
\sum_{h\in\mathcal H}
\epsilon_h\,\Phi_*\omega_{\mathcal C_h}
=
\sum_{h'\in\mathcal H'}
\epsilon'_{h'}\,\Phi_*\omega_{\mathcal C_{h'}}.
\]

The global observable is independent of the chosen coherent construction.

## NNMHV realization

For the tree NNMHV amplituhedron,

\[
X=G_+(2,n),
\qquad
Y=\mathcal A_{n,2,4},
\qquad
\Phi_Z(C)=CZ.
\]

The history chain is

\[
\Gamma_n
=
\sum_{h\in\mathcal H_n}\epsilon_h\,\mathcal C_h,
\qquad
\dim\mathcal C_h=8.
\]

For `n>6`, `Gamma_n` is an eight-dimensional chain inside the higher-dimensional space `G_+(2,n)`; it is not a decomposition of the entire positive Grassmannian.

The law becomes

\[
\boxed{
\Omega_{n,2,4}
=
\sum_{h\in\mathcal H_n}
\epsilon_h\,(\Phi_Z)_*\omega_{\mathcal C_h}
}.
\]

Since

\[
\dim G_+(2,n)=2n-4,
\]

each contributing cell has

\[
\operatorname{codim}_{G_+(2,n)}\mathcal C_h
=2n-12.
\]

## Projected construction law

For the selected component, component extraction sends the canonical-form identity to

\[
\widehat C_{23}(n)
=
\sum_{5\le b_2\le b_1\le n-1}T_n(b_1,b_2).
\]

Taking a cutoff difference gives

\[
\Delta S_n
=J_n^{\mathrm{ins}}+J_n^{\mathrm{ref}}.
\]

Thus the scalar two-channel flux law is a projection of the positive-geometric construction law.

## Interpretation

> A global observable is constructed by the orientation-compatible pushforward of an admissible local-cell chain, independently of the chosen coherent construction.

“Construction” denotes mathematical assembly, not temporal evolution.

## Relation to coherent composition

One rung below construction is the coherent composition law

\[
T_{A\to C}=T_{B\to C}\circ T_{A\to B}.
\]

This law may close analytically on a fixed algebra or category of transformations. It does not, by itself, determine which local cells occur, their orientations, their canonical weights, or the global observable they construct.

The NNMHV transport data demonstrate the distinction explicitly. At seven points, histories 2, 3, and 4 have the same rank-one projective transport but correspond to three distinct certified positroid cells. Hence

\[
[T_h]
\not\Rightarrow
\mathcal C_h
\quad\text{or}\quad
\omega_{\mathcal C_h}.
\]

The faithful datum must retain a resolved fiber, minimally at seven points

\[
\left([T_h],(a_2,b_2)\right),
\]

and in the tested general-cutoff range

\[
\left([T_h],(a_1,b_1),(a_2,b_2)\right).
\]

Thus coherent composition governs compatibility among transformations, while coherent construction specifies which resolved pieces, orientations, and weights assemble the global observable:

\[
\left([T_h],h,\omega_h\right)
\longmapsto
\sum_h\Phi_*\omega_h.
\]

In this sense, composition alone is an incomplete physical description: it specifies how relations combine but not what coherent global object they construct.

## Established scope

- At six points, the history chain is the top cell of `G_+(2,6)`.
- At seven points, all six history cells have certified canonical forms, positroid permutations, necklaces, and rank tables.
- At eight points, all twenty histories have been matched coefficientwise to distinct sourced rational positroid cells.
- The arbitrary-`n` history-to-positroid compiler remains open.

## Evidence

- `research/nima/results/seven-point-history-parity-cell-matching.json`
- `research/nima/results/seven-point-cellulation-incidence.json`
- `research/nima/results/seven-point-positroid-compiler.json`
- `research/nima/results/seven-point-positroid-rank-tables.json`
- `research/nima/results/eight-point-history-positroid-matching.json`
- `research/nima/results/decorated-transport-faithfulness-across-n.json`
- `research/nima/nnmhv-positive-geometry-history-equivalence.md`
