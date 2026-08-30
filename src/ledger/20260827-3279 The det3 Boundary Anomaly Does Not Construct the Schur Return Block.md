# 3279 — The det3 Boundary Anomaly Does Not Construct the Schur Return Block

The exact order-three prime anomaly lives on a determinant line. It constrains
how overlapping prime transfers compose, but it does not reconstruct the
operator-level incidence and return blocks of the reciprocal Evans
colligation.

Even with the bulk scalar fixed, the two symmetric matrices

\[
\begin{pmatrix}2&0\\0&3/2\end{pmatrix},
\qquad
\begin{pmatrix}2&1\\1&2\end{pmatrix}
\]

have the same determinant and Schur section while carrying different
incidence and return blocks. The determinant functor has forgotten the lift.

Therefore the next construction is a common operator refinement with two
independent shadows: its determinant composition must reproduce the det3
shared-corner cocycle, and its Schur complement must reproduce the endpoint
Evans section up to a source-derived nowhere-zero unit. Neither scalar shadow
constructs that refinement alone.

- Research packet: research/grothendieck/det3-boundary-anomaly-does-not-construct-the-schur-return-block.md
- Checker: research/grothendieck/checkers/check_det3_does_not_construct_schur_block.py
- Sequence claim: seqclaim-53d659b2475608bb4d798909
- Graph event: 6942
