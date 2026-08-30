# Spanning-tree reduction turns global Adams-seam coherence into one base-metric system

## Finite theorem

Let \(K\) be a finite typed parameter cell complex with 1-skeleton
\[
K^{(1)}=(V,E).
\]
Each oriented edge \(e:v\to w\) carries an authorized invertible transport
\[
T_e:H_v\to H_w,
\]
with
\[
T_{\bar e}=T_e^{-1}
\]
only when reverse transport is explicitly authorized.

Choose one spanning tree in each connected component and one base vertex \(v_0\).

Tree transport identifies all vertex metrics with one base metric:
\[
G_v=(T_{P_v}^{-1})^*G_0T_{P_v}^{-1},
\]
where \(P_v\) is the unique tree path from \(v_0\) to \(v\).

## Fundamental non-tree holonomies

Every non-tree edge \(e:v\to w\) defines a based loop
\[
\gamma_e=P_v\,e\,P_w^{-1}
\]
and ordered holonomy
\[
H_e=T_{P_w}^{-1}T_eT_{P_v}
\]
under the corresponding path-composition convention.

Global metric compatibility is equivalent to
\[
H_e^*G_0H_e=G_0
\]
for every non-tree edge, before imposing 2-cell relations.

The number of independent graph cycles is
\[
b_1^{\mathrm{graph}}
=
|E|-|V|+c,
\]
where \(c\) is the number of connected components.

This count is for the 1-skeleton only. Plaquettes and higher cells can kill or relate these generators.

## Cell relations

Each authorized 2-cell supplies a word relation
\[
r_j(H_{e_1},\ldots,H_{e_b})=I
\]
or an authorized higher intertwiner when the boundary closes only weakly.

Relevant cells include:

- elementary Adams-seam plaquettes;
- reciprocal-sheet sewing;
- Real/reciprocal mixed squares;
- associator and unitor coherence cells;
- endpoint and archimedean clutching cells;
- any admitted cutoff comparison cells.

After quotienting the free graph group by these relations, the surviving based loops present the residual fundamental group or groupoid.

The metric equations need only be imposed on a generating set of the represented residual holonomy group, but all equations use the same \(G_0\).

## Exact equivalence

Assume all tree arrows are invertible and typed in one component.

Then these statements are equivalent:

1. there is a compatible positive metric field \(G_v\) on every vertex and every edge;
2. there is one \(G_0>0\) invariant under every fundamental non-tree holonomy;
3. there is one \(G_0>0\) invariant under the full represented based holonomy group.

Proof direction:

- a metric field restricts to \(G_0\) and makes every loop unitary;
- an invariant \(G_0\) transports along the tree;
- non-tree invariance makes the transported metrics independent of the added edge;
- invariance composes to all words.

Cell relations reduce the generator list but do not change the equivalence.

## Ordered probes before characters

The primary Wilson probe is
\[
H_\gamma
\]
itself, modulo authorized base-frame conjugation:
\[
H_\gamma\sim SH_\gamma S^{-1}.
\]

A scalar trace
\[
\operatorname{tr}H_\gamma
\]
is not generally faithful on noncommutative holonomy data. Distinct nonconjugate matrices can share a trace, determinant, or even characteristic polynomial when Jordan structure differs.

Therefore scalar characters may replace ordered probes only after proving that the declared character family separates the relevant conjugacy classes of the represented holonomy group.

## Minimal trace hostile

Take
\[
H_1=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix},
\qquad
H_2=I.
\]
Both satisfy
\[
\operatorname{tr}H_1=\operatorname{tr}H_2=2,
\qquad
\det H_1=\det H_2=1.
\]
But \(H_1\) is nontrivial unipotent and not similar to \(H_2\). It is not unitarizable in a positive metric.

Trace and determinant lenses identify them incorrectly; the ordered lens separates them.

## Character-separation authorization

A family of characters \(\{\chi_\lambda\}\) is sufficient only if the theorem proves:
\[
\chi_\lambda(H)=\chi_\lambda(H')
\ \forall\lambda
\quad\Longrightarrow\quad
H,H'\text{ are conjugate in the authorized class}.
\]

For compact unitary groups, sufficiently rich irreducible characters separate conjugacy classes. Before compactness/unitarizability is established, this theorem cannot be imported automatically.

Thus ordered holonomies must be retained during the unitarization audit.

## Typed complex output

The source calculation must produce:

1. vertex records with fiber type, grade, sheet, and source-energy version;
2. edge records with transport operator, orientation, authority, and inverse status;
3. two-cell records with boundary word and strict/higher relation status;
4. one spanning forest;
5. non-tree edges and their based loop words;
6. the graph cycle rank;
7. the residual group presentation after cell relations;
8. ordered matrices for surviving holonomy generators.

This is a finite, falsifiable constructor artifact.

## Common metric solve

For surviving generators \(H_1,\ldots,H_m\), solve
\[
H_i^*G_0H_i=G_0,
\qquad i=1,\ldots,m,
\]
for one Hermitian \(G_0>0\).

The linear fixed space is
\[
\mathcal F=
\bigcap_i\ker(G\mapsto H_i^*GH-H).
\]
The system passes exactly when \(\mathcal F\) intersects the positive-definite cone.

If it fails, report:

- determinant character witness;
- spectrum/Jordan witness for a short word;
- or positive-cone infeasibility of the joint fixed space.

## Completion control

For cutoff \(X\), the spanning tree may change. To compare metrics, freeze a compatible tree policy or prove tree-choice independence with uniformly bounded coherence transports.

Normalize \(G_{0,X}\) by a source-authorized rule and require
\[
m_CI\le G_{0,X}(s)\le M_CI
\]
uniformly for \(s\) in compact off-seam \(C\).

Transported vertex metrics must satisfy the same kind of uniform bound:
\[
m_C'I\le G_{v,X}(s)\le M_C'I.
\]

A uniformly controlled base metric is insufficient if tree transports amplify with graph depth.

## Toric-code correspondence

The reduction has the same logical structure as a toric-code pilot:

- the 1-skeleton supplies candidate cycles;
- plaquette relations kill contractible cycles;
- residual fundamental cycles label logical sectors;
- ordered holonomies are logical operators;
- the common positive metric selects the unitary transport representation;
- completion asks whether this logical-sector geometry remains uniformly controlled.

The coefficient lens differs, but the cellular reduction is the same.

## Next executable theorem

> Given a finite typed Adams-seam cell complex, the checker constructs a spanning forest, presents the residual holonomy group after declared cell relations, computes ordered generator holonomies, and decides whether one positive base metric induces a compatible metric field on the entire complex.

The completion extension then tracks base and transported metric spectra under cutoff.

This theorem is the finite bridge from local plaquette data to global simultaneous unitarization.
