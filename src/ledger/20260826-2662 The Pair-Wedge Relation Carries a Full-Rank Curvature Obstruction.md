# 2662 — The Pair-Wedge Relation Carries a Full-Rank Curvature Obstruction

## Frozen construction

Let

\[
c_{12}(\kappa_1\wedge\kappa_2)+
c_{13}(\kappa_1\wedge\kappa_3)+
c_{23}(\kappa_2\wedge\kappa_3)=0
\]

be the unique normalized relation in the tested Kodaira–Spencer pair-wedge packet. Evaluate the visible curvature triple on those same labelled coefficients:

\[
\mathfrak o_c
=c_{12}F_{12}+c_{13}F_{13}+c_{23}F_{23}.
\]

If curvature descended through the pair-wedge quotient, this contraction would vanish. A nonzero result is the canonical obstruction to descent along the frozen relation.

## Result

At A, B, and HOMA, over primes 32003 and 65521, and for both curvature-sign conventions,

\[
\mathfrak o_c\ne0,
\qquad
\operatorname{rank}(\mathfrak o_c)=4.
\]

The obstruction is confined to the visible four-dimensional block but is full rank there.

## Interpretation

The missing coherence is not a scalar correction and not an optional presentation choice. The unique conormal relation is sent to a full visible endomorphism. Any source-derived derived completion must therefore provide a labelled homotopy whose boundary is exactly \(\mathfrak o_c\).

This does not authorize adjoining such a homotopy after observing the defect. It supplies its acceptance equation. If the frozen principal/Koszul/Gauss–Manin construction contains no cell with this boundary, the proposed conormal completion fails.

## Artifacts

- `research/benincasa/checkers/check_cm_curvature_relation_obstruction.py`
- `research/benincasa/results/cm-curvature-relation-obstruction.json`

## Next falsifier

Construct the source-labelled principal/Koszul differential before quotienting and test whether one of its existing degree-two coherence cells maps to \(\mathfrak o_c\), with the correct base-two-form labels and both curvature-sign conventions. Do not fit a homotopy matrix to the observed obstruction.
