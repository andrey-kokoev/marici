# Additive even–odd incidence does not imply return triangularity

## Question

Does the source-derived additive differentiation square force reverse triangularity of the enlarged Green return?

## Typed source boundary

The established identity

\[
K_-P=2\pi i\,M_{e^q}K_+
\]

types the archimedean incidence from the even additive Tate port to the odd port. It fixes parity and phase. Its source packet explicitly states that it does not construct the corresponding prime-seam operation or prove exclusion of unit eigenvalues in the complete Schur return.

Thus the bold conjecture crosses from an archimedean parity square to a finite arithmetic Green-return claim without a comparison map.

## Exact independence hostile

Absorb the typed scalar \(2\pi i\) into the coordinate multiplier and take a two-dimensional normalized model

\[
K_+=K_-=P=M=I.
\]

Then the normalized incidence square closes exactly:

\[
K_-P-MK_+=0.
\]

Independently take forward and reverse projectors

\[
P_+=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
P_-=\begin{pmatrix}0&0\\0&1\end{pmatrix}
\]

and return

\[
R=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

The return is a unitary involution, but

\[
P_-RP_+
=\begin{pmatrix}0&0\\1&0\end{pmatrix}
\ne0.
\]

Therefore exact additive even–odd covariance places no constraint on reverse triangularity of an independently typed return.

## What is falsified

The implication

\[
\text{additive differentiation coherence}
\Longrightarrow
\text{reverse-triangular Green return}
\]

is false. Additive differentiation remains a valid source incidence, but it cannot be promoted to the missing label-sensitive return law.

## First missing object

A finite prime-seam operator \(P_{\rm fin}\) must be independently constructed, together with a comparison to the wall–history–tail/PV return. Matching scalar phase or parity is insufficient. The acceptance test is a commuting square whose target includes the actual return \(R_p\), followed by a direct calculation of \(P_-R_pP_+\).

## Verification

`research/aspect/checkers/check_additive_incidence_vs_return_triangularity.py` verifies exact closure of the normalized incidence square and a simultaneous nonzero reverse block using rational matrices.

## Disposition

Reject the bold conjecture. The archimedean additive derivative does not supply reverse triangularity. Strong confinement now requires a new finite label-sensitive source operation or must be withdrawn; existing parity coherence cannot be repurposed.
