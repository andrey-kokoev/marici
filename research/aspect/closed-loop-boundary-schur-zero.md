# Closed-loop boundary Schur-zero instrument

## Result

An exact finite optical feedback realization localizes a network zero to the boundary Schur complement while its open two-mode plant remains invertible. This is a calibration and falsification instrument, not a source law excluding zeros.

## Source and ports

One phase-referenced boundary probe drives two internal optical modes. Four ports are calibrated independently: the open plant (A), boundary injection (B), returned readout (C), and direct boundary path (D(q)).

\[
A=\begin{pmatrix}2&0\\0&3\end{pmatrix},\quad
B=\begin{pmatrix}1\\1\end{pmatrix},\quad
C=\begin{pmatrix}2&3\end{pmatrix},\quad
D(q)=2+q.
\]

## Constructor order and calibration frame

The boundary field is injected by (B), propagated through (A^{-1}), returned by (C), and interfered with the direct path (D). A common coherent phase reference fixes the signs of all four block measurements. Closing the loop only after separate calibration gives

\[
S_\partial(q)=D(q)-CA^{-1}B=q.
\]

The loop contribution is exactly (CA^{-1}B=2). At (q=0), neither the open plant nor the direct path is singular: (det A=6) and (D(0)=2). The zero appears only after coherent boundary closure.

## Conserved quantities and detector

The finite transfer coefficients are gain-normalized amplitudes; a physical passive realization may dilate unused norm into monitored environment ports. The detector first estimates the four blocks in open-loop calibration runs, then detects the full closed-network null. At (q=-1/2,0,1/2), the exact full determinants are (-3,0,3).

The null state is

\[
(-1/2,-1/3,1),
\]

which contains a nonzero boundary coordinate. Direct transmission or open-plant spectroscopy alone lies in the detector kernel for this distinction.

## Smallest hostile

The hostile analysis uses the correctly calibrated invertible plant and nonzero direct path but omits their coherent feedback term. It concludes that no zero exists at (q=0). The full Schur calculation rejects that conclusion exactly.

## Small-gain boundary

After normalizing the direct block at (q=0), the loop gain is one. Thus this apparatus is also the smallest equality witness showing why strict small gain would exclude the boundary zero. It does not show that any theta-derived reciprocal loop obeys such a bound, and it does not compare the two causal sector directions.

## Completion boundary

The finite instrument verifies block localization and determinant factorization. It supplies no prime-labelled theta realization, no Fredholm determinant comparison, no continuum feedback limit, no source-authorized norm, and no RH inference.

## Reproduction

Run:

    python research/aspect/checkers/closed_loop_boundary_schur_zero.py
