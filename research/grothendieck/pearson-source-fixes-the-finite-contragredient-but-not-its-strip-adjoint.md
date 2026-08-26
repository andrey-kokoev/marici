# The Pearson Source Fixes the Finite Contragredient but Not Its Strip Adjoint

## Finite source transfer

At degree (j), write the primal Gamma-wall transfer as

\[
M_j=
\begin{pmatrix}
A_j&-B_j&1\\
1&0&0\\
0&0&c
\end{pmatrix},
\qquad
A_j=j+\frac{19}{4},
\qquad
B_j=\frac32\left(j+\frac54\right).
\]

On the full six-channel carrier (V\oplus V^*), functoriality forces the dual transfer to be (M_j^{-T}). Direct inversion gives

\[
M_j^{-T}=
\begin{pmatrix}
0&-B_j^{-1}&0\\
1&A_jB_j^{-1}&0\\
0&(B_jc)^{-1}&c^{-1}
\end{pmatrix}.
\]

There are no free metric parameters.

## The source incidence recovered by the adjoint

The entry ((B_jc)^{-1}) sends the second tail covector into the wall covector. It is the contragredient of the primal wall-to-tail shear. Thus retaining the full dual does more than repair a reciprocal eigenvalue: it restores the direction of the boundary incidence erased by the determinant-line compression.

For all primal vectors (v) and covectors (\lambda),

\[
\langle M_jv,M_j^{-T}\lambda\rangle
=
\langle v,\lambda\rangle.
\]

Consequently the canonical split form on (V\oplus V^*) is preserved at every finite degree.

## Where the analytic lift stops

The value-level transfer is not yet the complete Pearson operator. Mellin pushforward contains the exponent translation

\[
K_j(q)\longmapsto K_j(q-1).
\]

Its adjoint cannot be inferred from the finite matrix. It depends on the pairing between the regular strip and its continuous dual:

- a vertical-line (L^2) pairing moves the contour and needs growth control;
- a residue pairing sees polar Laurent data but not the entire regular strip;
- the compact-open topology has a large distributional dual and unbounded prime translations are not equicontinuous;
- a fitted weighted norm could manufacture continuity and is therefore unauthorized.

The source has fixed the algebraic contragredient and the wall evaluation covector, but it has not yet selected a continuous duality for the function-valued base strip. This is the first real obstacle in lifting the six-channel Clifford carrier from finite values to continuous exponent response.

## Exact next theorem

Construct a source-derived pairing between the analytic base strip and a dual strip such that:

1. Mellin translation has a densely defined adjoint;
2. the adjoint boundary term is exactly the wall residue covector;
3. the Pearson transfer and its contragredient preserve the evaluation form;
4. logarithmic prime translations act covariantly on both sides;
5. no terminal-jet projector enters the physical boundary.

Failure of any one condition closes the six-channel analytic-lift route. Success would replace the seven-parameter metric search by one canonical dual-pairing theorem.

## Verification

The dependency-free checker `research/grothendieck/checkers/pearson_full_contragredient.py` verifies the exact inverse-transpose formula, evaluation invariance, and nonzero tail-covector-to-wall-covector incidence through eight rational degree samples.
