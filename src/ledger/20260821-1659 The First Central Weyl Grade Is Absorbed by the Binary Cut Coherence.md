# 1659 — The First Central Weyl Grade Is Absorbed by the Binary Cut Coherence

## Falsifier

Entry 1658 identifies the first normal-ordering correction \(2\hbar^2\) in \(D(p^3)\). Compute its co-Leibniz defect in the correctly typed occurrence-resolved CCR coalgebra.

## Homogenized two-occurrence algebra

Use

\[
\Delta q=q_L+q_R,
\qquad
\Delta p=p_L+p_R,
\qquad
\Delta\hbar=\hbar_L+\hbar_R.
\]

Define

\[
\Theta_D(p^3)
=
\Delta D(p^3)
-(D_L+D_R)\Delta(p^3).
\]

The checker performs exact normal ordering in both Weyl factors. The resulting defect has eight nonzero terms.

## Central grade

The only term containing no \(q\) or \(p\) is

\[
\boxed{4\hbar_L\hbar_R.}
\]

It is exactly the mixed part of the primitive central coproduct:

\[
2(\hbar_L+\hbar_R)^2
-2\hbar_L^2
-2\hbar_R^2
=
4\hbar_L\hbar_R.
\]

There is no scalar residual independent of \(\hbar_L,\hbar_R\).

## Narrow result

\[
\boxed{
\text{The first quantum central moment grade is absorbed coherently into the existing binary co-Leibniz defect.}
}
\]

Quantum ordering enriches \(\Theta_D\), but does not create a new support class or independent anomaly. Occurrence-resolved central data is precisely what makes the correction typed.

This strongly validates Entry 1657's resolved-before-specialized rule. If one fixed a single scalar \(\hbar\) before sewing, the cross term would be mistyped or lost.

This result does not yet verify the ternary co-Hochschild identity for the complete eight-term quantum defect.

## Durable artifacts

- research/benincasa/checkers/weyl_p3_coleibniz_defect.rs
- research/benincasa/results/weyl-p3-coleibniz-defect.json
- research/benincasa/weyl-p3-coleibniz-defect.md

## Next falsifier

Extend the exact Weyl normal-order engine to three occurrence factors and verify the co-Hochschild identity for the complete \(\Theta_D(p^3)\). A nonzero residual would be the first genuine ternary quantum coherence; closure would show that primitive \(\hbar\) resolves the quantum correction completely.
