# 4121 — Mixed Pole-Grade Relations Supply 530 Essential Attachment Constraints

## Claim

The 31-dimensional lower-block contribution in Entry 4118 is not a detached direct summand of the source presentation.

The residual matrix contains

\[
9{,}027
\]

relations whose support meets both the top block \((3;22222)\) and lower labelled pole blocks.

Removing all such mixed rows leaves 5,539 diagonal-only rows. Over each tested field,

\[
\operatorname{rank}R_{\rm diag}=1{,}664,
\qquad
\dim\operatorname{coker}R_{\rm diag}=614.
\]

Restoring the mixed rows gives

\[
\operatorname{rank}R_{\rm full}=2{,}194,
\qquad
\dim\operatorname{coker}R_{\rm full}=84.
\]

Therefore the mixed rows contribute exactly

\[
2{,}194-1{,}664=530
\]

independent constraints and remove 530 otherwise surviving quotient directions.

## Replication

The diagonal-only rank and pivot set agree at

\[
p=31991, 32003, 32009.
\]

The diagonal pivot hash is

`a764bbb88bb51aca97d29438dbc53ee45cf7e072e9fd12e50fafecc6f429995e`.

## Interpretation

The identity

\[
84=53+31
\]

describes the associated quotient dimensions, but not a source-level direct-sum decomposition. The complete object is assembled by a large off-diagonal attachment: 530 independent mixed constraints reduce the disconnected diagonal presentation from dimension 614 to 84.

This rules out the naive constructor

\[
F_{84}\cong Q_{53}\oplus B_{31}
\]

obtained by simply juxtaposing separately reduced pole grades. Any splitting must instead be a derived triangular gauge or homotopy compatible with the 530-dimensional attachment image.

This result does not yet prove that the resulting extension is nonsplit over a field: finite-dimensional vector-space extensions split noncanonically. It proves that no splitting is present at the frozen source-presentation level after deleting mixed relations.

## Next falsifier

Construct the induced 530-rank off-diagonal attachment map after diagonal reduction. Then quotient by source-authorized triangular homotopies. A nonzero class proves intrinsic filtered nonsplitting; a zero class yields an explicit source-compatible section.

## Durable artifacts

- `research/benincasa/checkers/census_interaction_net_filtered_attachment.cjs`
- `research/benincasa/checkers/export_interaction_net_diagonal_residual.cjs`
- `research/benincasa/results/interaction-net-integral-residual-diagonal-matrix.txt`
- `research/benincasa/results/interaction-net-filtered-residual-attachment-rank.json`

Sequence claim: `seqclaim-76ae5139249b4a8f417d3b3a`.
