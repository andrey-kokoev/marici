# Minimal optical transfer-identifiability instrument

## Result

A two-mode coherent optical instrument distinguishes aggregate determinant data from a full scalar transfer. The full transfer identifies a controllable and observable finite realization up to similarity and port gauge, while determinant-only observation misses input-output incidence and dark modes.

## Source, ports, and constructor order

One calibrated coherent source drives the input port (B), propagates through the ordered internal plant (A), and exits through the phase-referenced readout (C). The base realization is

\[
A=\begin{pmatrix}0&1\\-2&-3\end{pmatrix},\quad
B=\begin{pmatrix}0\\1\end{pmatrix},\quad
C=\begin{pmatrix}1&0\end{pmatrix},\quad D=0.
\]

Its transfer is

\[
G(s)=C(sI-A)^{-1}B=\frac{1}{s^2+3s+2}.
\]

Both the controllability and observability determinants are nonzero, so every internal mode belongs to the input-output cyclic subspace.

## Calibration frame and detector

Coherent impulse tomography or swept heterodyne spectroscopy records signed amplitude and phase, not intensity alone. The exact Markov sequence begins

\[
0,1,-3,7,-15,31,-63,127.
\]

This retains pole residues and port incidence. Measuring only (det(sI-A)=s^2+3s+2) retains the internal characteristic polynomial but discards how the source and detector attach.

## Similarity and port gauge

The shear

\[
T=\begin{pmatrix}1&1\\0&1\end{pmatrix}
\]

changes all three blocks to (TAT^{-1},TB,CT^{-1}) while preserving the complete transfer. This is a state-coordinate change, not a distinct input-output experiment. Likewise, (B\mapsto2B) and (C\mapsto C/2) preserve the transfer and expose the constant input-output port gauge.

## Conserved quantities and detector kernel

A passive dilation preserves total optical norm only after unused environment ports are included. Transfer tomography observes the driven cyclic subspace. Appending a mode of eigenvalue 7 with zero input and output incidence changes the internal spectrum but leaves every measured Markov parameter unchanged. Minimality is therefore an experimental gate, not a consequence of transfer agreement.

## Smallest hostile

Keep the same internal matrix (A), hence the same determinant, but change the input incidence to (B=(1,0)^T). The transfer and Markov sequence change. This exactly rejects any inference from determinant equality to full characteristic transfer equality.

The converse hostile appends an unreachable and unobservable mode. It preserves the full measured transfer but changes the nonminimal internal realization.

## Completion and authority boundary

The instrument verifies the finite control theorem physically: a minimal full transfer is richer than a determinant and fixes a realization only up to admitted gauges. It does not prove that the completed theta section is a full characteristic transfer, supply source-authorized defect ports, establish infinite-dimensional simplicity, or constrain any zero.

## Reproduction

Run:

    python research/aspect/checkers/minimal_optical_transfer_identifiability.py
