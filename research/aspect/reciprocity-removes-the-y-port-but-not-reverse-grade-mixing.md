# Reciprocity removes the Y port but not reverse-grade mixing

## Question

Can an optical reciprocity law on the strict primitive-square Pauli frame constrain the Green return without the unavailable global completion constructor?

## Reciprocity action

On the ordered primitive-square basis, use

\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
Y=\begin{pmatrix}0&i\\-i&0\end{pmatrix}.
\]

Let the reciprocity involution be entrywise conjugation \(J\). Then

\[
JXJ=X,
\qquad
JYJ=-Y.
\]

Thus a Hermitian two-port operator

\[
K=aI+xX+yY
\]

is reciprocity-even only if \(y=0\). Reciprocity distinguishes the real symmetric mixing channel from the quadrature-odd channel.

## Grade hostile

The reciprocity-even operator \(R=X\) still has

\[
P_-RP_+\ne0
\]

for the primitive and square grade projectors. Therefore reciprocity does not imply grade preservation, reverse triangularity, or scalar-null confinement. It removes the \(Y\) coefficient but leaves the \(X\) route unconstrained.

## Physical distinction

Reciprocity is a relation between exchanged source and detector routes in a declared target pairing. Grade confinement is invariance of the primitive-square filtration. These are different symmetries. Their matrix formulas coexist on the Pauli plane, but no implication exists without an additional theorem identifying grade exchange with reciprocal route exchange.

## Executable consequence

Once a physical return is constructed on this plane, reciprocity supplies one exact audit:

1. decompose its Hermitian part in \(I,X,Y,Z\);
2. require the reciprocity-odd \(Y\) coefficient to vanish under the declared conjugation convention;
3. test the surviving \(X\) coefficient independently for cross-grade return.

A nonzero \(Y\) coefficient falsifies this reciprocity convention. A zero \(Y\) coefficient does not certify confinement.

## Verification

`research/aspect/checkers/check_reciprocity_grade_mixing.py` verifies with Gaussian-integer pairs that \(X\) is reciprocity-even, \(Y\) is reciprocity-odd, and reciprocal \(X\) has a nonzero reverse-grade block.

## Disposition

This executable optics branch is independent of the missing global completion. Reciprocity yields a real constraint on any future physical return, but it cannot replace the source-derived return or its strict norm bound.
