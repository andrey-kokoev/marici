# 1579 — The Cubic Statistical Tangent Changes Variance Before Dyson Propagation

## Question

Does Entry 1577's rank-one common-contour statistical direction map to
itself under the first local step of the one-loop cubic correction?

## Exact contour calculation

For ordered times (t_1>t_2), set

\[
G_0^{ab}=(x,y,x,y)
\]

in the basis ((++,+-,-+,--)).  The two cubic contour vertices give

\[
\Sigma^{ab}\propto(ab)(G^{ab})^2,
\qquad
(ab)=(1,-1,-1,1).
\]

Linearizing along

\[
\delta_{\rm stat}G=(1,1,1,1)s
\]

produces

\[
\boxed{
D\Sigma_{G_0}(\delta_{\rm stat}G)
\propto(2x,-2y,-2x,2y)s.
}
\]

The image is not a common-contour line.  It is odd under the first contour
occurrence flip.

## Type correction

This does not falsify the Gaussian splitting.  The cubic local map has type

\[
T_G\mathcal G^{\rm Gauss}
\longrightarrow
T_G^*\mathcal G^{\rm Gauss},
\]

with the contour metric supplied by the two vertex signs.  Comparing its
input and output as though it were an endomorphism would erase variance.

Thus the direct channel-preservation test proposed in Entry 1577 is
withdrawn at the self-energy stage.

## Surviving falsifier

Compose the self-energy variation with the retarded/advanced Dyson kernel,

\[
\delta G
\to\delta\Sigma
\to G_R\delta\Sigma G_A,
\]

and only then project the corrected propagator onto the two Bogoliubov
directions and the statistical line.  Failure of that typed composite to
land in the rank-three Gaussian object is the coefficient obstruction.

## Classification

\[
\boxed{
\text{shared doubled contour carrier}
+\text{variance-sensitive coefficient map};
\quad\text{no new carrier datum}.
}
\]

## Artifacts

- `research/benincasa/cubic-statistical-self-energy-variance.md`
- `research/benincasa/checkers/cubic_statistical_self_energy_variance.rs`
- `research/benincasa/results/cubic-statistical-self-energy-variance.json`

Ledger sequence claim: `seqclaim-197f4639350278911a7190bc`.
