# Finite operator-valued Markov Green associator

## Question

Does analytic coherence extend beyond scalar Green chains when edge transfers do not commute?

## Claim boundary

This packet treats finite-dimensional real contraction matrices on a fixed fiber dimension. It proves finite chain amalgamation, positivity, strict associativity, pentagon, and orthogonal vertex-gauge interchange. It does not prove infinite completion, varying-fiber correspondences, or general operator-valued pullback Beck–Chevalley.

## Construction

Let every vertex carry \(\mathbb R^d\), and let edge transfers \(A_i\in M_d(\mathbb R)\) satisfy

\[
I-A_i^TA_i\succeq0.
\]

Define the block kernel by

\[
K_{ii}=I,
\qquad
K_{ij}=A_iA_{i+1}\cdots A_{j-1}\quad(i<j),
\qquad
K_{ji}=K_{ij}^T.
\]

It is the covariance kernel of the recursion with transition \(A_i^T\) and innovation covariance \(I-A_i^TA_i\), so \(K\succeq0\).

## Amalgamation and associator

Contiguous chains amalgamate by concatenating their ordered transfer lists. Every cross-seam block is the uniquely ordered product along the path. Matrix multiplication is associative, so all parenthesizations yield the same full block kernel. The associator is the identity isometry, and the four-edge pentagon commutes strictly.

No commutativity of distinct \(A_i\) is used.

## Orthogonal vertex gauges

For orthogonal \(U_i\), transform

\[
A_i' = U_iA_iU_{i+1}^T.
\]

Internal factors telescope, giving

\[
A_i'\cdots A_{j-1}'
=U_i(A_i\cdots A_{j-1})U_j^T.
\]

Thus gauge transformation commutes with amalgamation when the same \(U_i\) is used at every shared vertex. A mismatched seam gauge leaves an uncancelled factor and is rejected.

## Hostile fixtures

The checker uses noncommuting rational \(2\times2\) transfers. It also verifies that reversing a path-product order changes the cross block and that a shared-seam gauge mismatch breaks the telescoping square.

## Disposition

Finite analytic associator, pentagon, positivity, and compatible-gauge interchange extend from scalar chains to noncommuting matrix-valued Markov transfers. Completion and general Beck–Chevalley remain open.

## Verification

- `research/voevodsky/checkers/check_operator_valued_markov_green.py`
- `research/voevodsky/results/operator_valued_markov_green.json`
