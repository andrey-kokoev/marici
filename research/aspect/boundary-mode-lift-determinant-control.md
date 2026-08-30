# Boundary-mode lift determinant-control instrument

## Result

A two-port optical lift realizes the exact determinant-control trilemma. Decoupled and one-way auxiliary modes preserve the original scalar zero but cannot supply two-way feedback. Two-way coupling moves the zero unless an explicit compensating direct term is supplied.

## Source and ports

The source provides one distinguished boundary mode with scalar response (x(q)=q) and one generic auxiliary optical mode with calibrated response (E=1). The auxiliary mode is deliberately not identified with a prime-power grade: arithmetic prime powers are cyclic returns of one primitive loop, not independent state ports.

The lifted response is

\[
\widetilde S(q)=
\begin{pmatrix}
x(q)&b\\
c&E
\end{pmatrix}.
\]

## Constructor order and calibration frame

Coherent transfer tomography separately measures (x,b,c,E) in one phase frame before determinant and null scans. Elimination of the auxiliary mode gives

\[
\det\widetilde S=E\left(x-bE^{-1}c\right)=x-bc.
\]

With (b=c=1/2), the old zero at (q=0) is removed because the determinant is (-1/4). The new zero occurs at (q=1/4).

## Four calibrated lifts

- Decoupled: (b=c=0), so the determinant remains (q).
- Forward triangular: (b=1/2,c=0), so the determinant remains (q).
- Reverse triangular: (b=0,c=1/2), so the determinant remains (q).
- Two-way coupled: (b=c=1/2), so the determinant becomes (q-1/4).

A compensated two-way lift replaces the direct scalar block by (x(q)=q+1/4), restoring determinant (q). The apparatus records that compensation as a separate source input; it cannot be inferred or fitted from the desired determinant.

## Conserved quantities and detector

The ideal response is an amplitude model. A passive physical realization conserves total norm only after unused splitter and loss ports are retained. Mode-resolved coherent tomography detects one-way and two-way incidence even when scalar determinants agree. Determinant scans alone have an (SL(2))-type realization kernel and do not identify the ordered optical network.

## Smallest hostile

The hostile lift keeps the visible compression (x(q)=q), adds symmetric coupling (b=c=1/2), and claims that the original zero is preserved because the scalar coordinate is unchanged. Exact determinant measurement rejects it: the zero moves from 0 to (1/4).

## Completion and authority boundary

This finite instrument tests whether an added boundary mode is inert, triangular, determinant-changing, or explicitly compensated. It supplies no source law for the compensation, no arithmetic interpretation of the auxiliary port, no prime-power direct sum, no infinite-dimensional determinant comparison, and no RH inference.

## Reproduction

Run:

    python research/aspect/checkers/boundary_mode_lift_determinant_control.py
