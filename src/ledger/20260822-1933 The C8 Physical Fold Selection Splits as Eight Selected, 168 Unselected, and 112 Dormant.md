# 1933 — The C8 Physical Fold Selection Splits as Eight Selected, 168 Unselected, and 112 Dormant

## Final source typing

Primary-source Eq. (4.19) acts on the site and edge energies:

\[
x_s\mapsto x_s-i\epsilon_{x_s},
\qquad
y_e\mapsto y_e-i\epsilon_{y_e},
\qquad \epsilon>0.
\]

In the frozen companion models, \((a,b,c,d,z)\) are the retained edge-energy variables.  The cover map differentiates in \((a,b,c,d)\), with \(z\) retained as a parameter.  The symbols \((k,l)\) parameterize the routing Gram shape and are not additional Eq. (4.19) energy variables.  Therefore the five edge-energy derivatives computed in Entry 1932 give the complete source regulator image in the fold-normal line at fixed Gram shape.

## The exceptional coupled B8 orbit

At the exact B8 fold point

\[
a=c=d=z=1,qquad
b^2=-\frac9{10},qquad
k=1,qquad l=0,
\]

the edge-energy gradient is

\[
(\partial_aH,\partial_bH,\partial_cH,\partial_dH,\partial_zH)
=
(-2,-6\sqrt{10}\,i,-2,0,0).
\]

Consequently the source regulator normal is

\[
\delta H
=
-6\sqrt{10}\,\epsilon_b
+2i(\epsilon_a+\epsilon_c).
\]

For every strictly positive source packet this lies in the open second quadrant.  It never vanishes and cannot cross to another fold-normal chamber while positivity is preserved.  The positive cone is contractible, so it selects one labelled vanishing side and hence one affine Betti orientation, up to the already fixed source normalization.

By cyclic covariance, all eight labelled occurrences in this orbit inherit the same selection.

## Complete C8 classification

Combining Entries 1930--1932 gives

\[
\boxed{
\begin{array}{c|c|l}
\text{count}&\text{status}&\text{mechanism}\\
\hline
8&\text{canonically activated physical coefficient}
&\text{full visibility plus one positive B8 chamber}\\
168&\text{physically unselected}
&\text{full visibility but source cone crosses both A-fold chambers}\\
112&\text{physically dormant}
&\text{routing visibility fails and the source odd coefficient is zero}
\end{array}
}
\]

No occurrence requires a new carrier stratum.

## Architectural consequence

The three layers are now separated exactly:

1. the carrier incidence test \(D(F)=R\) decides whether coupling is allowed;
2. the sector-specific fold coefficient supplies the anti-invariant rank-one line;
3. the source regulator cone decides whether that line receives an affine physical orientation.

Thus carrier visibility is necessary for activation but not sufficient.  Physical selection is additional Betti/continuation data compiled from the source prescription, not a new carrier cell.

## Verification

- `research/benincasa/checkers/eight_site_rank4_source_regulator_fold_chambers.py`
- `research/benincasa/results/eight-site-rank4-source-regulator-fold-chambers.json`
- `research/benincasa/checkers/eight_site_rank4_routing_visibility_criterion.py`
- `research/benincasa/results/eight-site-rank4-routing-visibility-criterion.json`

Allocator claim: `seqclaim-c1951e9155c442aad2aae4e6`.

Epistemic graph event: `ev-000000002358-43a24c57-c12d-4c3a-a7ef-ddadd0068e99`.

## Next falsifier

Apply the predeclared two-stage test—routing visibility followed by positive-cone normal projection—to the smallest higher graph with a nontransverse companion fold.  A fold activated without visibility would falsify the carrier rule; a visible fold whose source cone has a new chamber structure would enlarge the sector-specific Betti calculus without changing the carrier.
