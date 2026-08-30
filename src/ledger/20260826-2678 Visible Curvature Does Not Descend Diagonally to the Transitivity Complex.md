# 2678 — Visible Curvature Does Not Descend Diagonally to the Transitivity Complex

## Frozen descent test

Let

\[
\kappa:R^3\longrightarrow R^4
\]

be Entry 2674's cotangent-transitivity map. For a visible curvature matrix \(F\in\operatorname{End}_{\mathbb F_p}(R)\), the unique untwisted occurrence action is diagonal:

\[
F_3=I_3\otimes F,
\qquad
F_4=I_4\otimes F.
\]

Descent to the kernel and cokernel requires the chain-map identity

\[
F_4\kappa-\kappa F_3=0.
\]

## Exact result

For every labelled component \(F_{12},F_{13},F_{23}\), at every replicated point and prime, and for both curvature-sign conventions,

\[
\operatorname{rank}(F_4\kappa-\kappa F_3)=12.
\]

No tested visible curvature component descends under the frozen diagonal action.

## Narrow result

The rank-four visible curvature is not yet an endomorphism of the finite cotangent-transitivity cohomology. Its direct diagonal extension fails by a stable rank-twelve defect.

A surviving total action would require an independently derived off-diagonal coherence block coupling base-direction and conormal occurrences. This result does not authorize fitting that block. If the source reduction calculus supplies no such map, the observed visible curvature is presentation curvature rather than a derived coefficient class.

## Artifacts

- `research/benincasa/checkers/check_cm_curvature_transitivity_descent.py`
- `research/benincasa/results/cm-curvature-transitivity-descent.json`
- `research/benincasa/results/cm-conormal-kodaira-spencer.json`

## Next falsifier

Inventory the tracked reduction formulas for a source-labelled off-diagonal base-to-conormal action. If one exists, insert it before projection and test cancellation of the rank-twelve defect. If none exists, close this curvature-completion branch rather than solving for a fitted correction.
