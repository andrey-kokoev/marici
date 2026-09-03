# Descent from framed to metric-transition Markov objects

## Question

Does the framed GL construction descend canonically after quotienting frame choices by vertexwise orthogonal transformations?

## Claim boundary

This packet treats finite-dimensional positive-definite metrics and typed one-edge covariance blocks. It proves a quotient coordinate for finite framed Markov data. Infinite quotient topology and completion descent require separate uniformity arguments.

## Framed data and equivalence

A framed chain consists of invertible \(R_i\) and normalized contractions \(A_i\). Vertexwise orthogonal matrices \(O_i\) act by

\[
R_i\mapsto R_iO_i,
\qquad
A_i\mapsto O_i^TA_iO_{i+1}.
\]

Define invariants

\[
M_i=R_iR_i^T,
\qquad
C_i=R_iA_iR_{i+1}^T.
\]

Both are unchanged by the orthogonal action.

## Faithful quotient coordinate

The coordinate

\[
[(R_i,A_i)]\longmapsto(M_i,C_i)
\]

is faithful on the orthogonal quotient. Given positive-definite \(M_i\), choose any frames satisfying \(M_i=R_iR_i^T\) and reconstruct

\[
A_i=R_i^{-1}C_iR_{i+1}^{-T}.
\]

Any second frame has the form \(R_iO_i\) with \(O_i\) orthogonal, and its reconstructed transfer is \(O_i^TA_iO_{i+1}\). Thus different frame choices yield exactly one quotient point.

The contraction condition descends as

\[
M_{i+1}-C_i^TM_i^{-1}C_i\succeq0.
\]

## Kernel reconstruction

Long cross blocks are reconstructed without choosing a persistent frame:

\[
K_{ij}=C_iM_{i+1}^{-1}C_{i+1}\cdots M_{j-1}^{-1}C_{j-1}.
\]

Substitution of framed data telescopes to \(R_i(A_i\cdots A_{j-1})R_j^T\). Hence positivity, amalgamation associativity, contiguous Beck–Chevalley, and GL congruence action descend.

## Hostile boundary

Changing \(R_i\) to \(R_iO_i\) while leaving adjacent \(A_i\) fixed generally changes \(C_i\). Frame independence requires the coupled transfer action; frame erasure alone is not descent.

## Disposition

Finite framed data descend to a faithful metric-transition quotient with coordinates \((M_i,C_i)\). The prior metric-only blocker is repaired by retaining typed one-edge covariance blocks. Infinite completion descent remains open.

## Verification

- `research/voevodsky/checkers/check_framed_to_metric_markov_descent.py`
- `research/voevodsky/results/framed_to_metric_markov_descent.json`
