# A common graph presentation generates all opposite edges at fixed realization dimension

## Objective

Construct bidirectional comparison among the four semilocal presentations at one fixed realization dimension without separately guessing 28 reverse segment formulas.

## Common object

Let \(D_{0,k}\) be the finite-support source core at realization dimension \(k\). Let

\[
q_{i,k}:D_{0,k}\longrightarrow Y_{i,k},
\qquad i=1,2,3,4,
\]

collect the already retained coordinates of presentation \(i\): source/geometric, dual, spectral, and completed observer coordinates respectively. Define the joint graph map

\[
\Gamma_kx=(x,q_{1,k}x,q_{2,k}x,q_{3,k}x,q_{4,k}x).
\]

The common graph presentation is the completion

\[
M_k:=\overline{\Gamma_k(D_{0,k})}
\]

in the declared product graph topology. The source coordinate is retained; therefore \(\Gamma_k\) is faithful. Prior joint-closability results justify this construction for the retained history, grade, trace, sewing, and current coordinates. External \(G_4\) identification is not included.

## Four complete presentations

For each \(i\), define the complete presentation to be the graph image

\[
\widetilde V_{i,k}:=
\{(x,q_{i,k}x):x\in M_k\}.
\]

Let

\[
e_{i,k}:M_k\longrightarrow\widetilde V_{i,k},
\qquad e_{i,k}(x)=(x,q_{i,k}x).
\]

Because the source anchor \(x\) is retained, \(e_{i,k}\) has the exact inverse

\[
e_{i,k}^{-1}(x,q_{i,k}x)=x.
\]

Thus the comparison from presentation \(i\) to presentation \(j\) is

\[
E_{ij,k}=e_{j,k}e_{i,k}^{-1},
\]

with component formula

\[
E_{ij,k}(x,q_{i,k}x)=(x,q_{j,k}x).
\]

Its opposite arrow is automatic:

\[
E_{ji,k}(x,q_{j,k}x)=(x,q_{i,k}x),
\]

and the inverse equations hold strictly:

\[
E_{ji,k}E_{ij,k}=\mathrm{id}_{\widetilde V_{i,k}},
\qquad
E_{ij,k}E_{ji,k}=\mathrm{id}_{\widetilde V_{j,k}}.
\]

All triangle and tetrahedral equations reduce to cancellation of the graph charts. For example,

\[
E_{j\ell,k}E_{ij,k}=E_{i\ell,k}.
\]

No cross-dimension map is used.

## Fine segments

For a seven-segment presentation path, let \(q_{i,k}^{[r]}\) denote the coordinates retained after fine stage \(r\), where \(r=0,\ldots,7\). Replace every fine node by its anchored graph

\[
\widetilde V_{i,k}^{[r]}
=
\{(x,q_{i,k}^{[r]}x):x\in M_k\}.
\]

The forward segment changes only the displayed coordinate while preserving \(x\):

\[
(x,q_{i,k}^{[r]}x)
\longmapsto
(x,q_{i,k}^{[r+1]}x).
\]

The opposite segment is the same rule with \(r\) and \(r+1\) exchanged. Hence every typed fine segment becomes strictly reversible on the anchored graph, even when its unanchored shadow is polarization, projection, or trace and is noninjective.

## Meaning of the construction

This does not claim that a scalar trace can recover its source. Reconstruction uses the retained source anchor in the complete graph presentation. Forgetting that anchor recovers the original lossy presentation and destroys invertibility. The construction therefore distinguishes:

- complete graph presentations, which form a fixed-\(k\) groupoid;
- unanchored physical shadows, which remain directed and possibly noninvertible.

## Analytic boundary

Algebraic reversal is immediate on graph images. Topological reversal is continuous when each graph image carries the transported topology from \(M_k\); identifying that topology with an independently prescribed topology on an unanchored target requires closed-range estimates. Positivity of a shadow is not implied by graph invertibility and retains the previously stated relative-feature qualifications.

## Disposition

At fixed realization dimension, the common anchored graph replaces separate reversal proofs for every admitted fine map by construction of one jointly closable master object and four graph charts. It supplies an algebraic opposite only after a forward fine node has been typed and included as a graph coordinate. Presently only 14 of the proposed 28 forward segment positions have standalone eight-node factorizations; the other fourteen positions are not yet defined reverse-arrow rows. The remaining work is to extend the coordinate ledger, construct or reject the two missing standalone edge factorizations, and compare graph-chart topology with any pre-existing target topology.