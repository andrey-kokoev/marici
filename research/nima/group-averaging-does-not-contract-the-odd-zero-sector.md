# Group Averaging Does Not Contract the Odd Zero Sector

## Two different complexes

The phrase "odd-sector acyclicity" can refer to two inequivalent objects:

1. the group-cohomology resolution of the reciprocal \(C_2\)-action;
2. the source-derived zero complex after projection to the odd character.

Only the second can carry RH content.

## Semisimplicity trap

Over \(\mathbb C\), the order of \(C_2\) is invertible. The averaging
idempotents

\[
P_+=\frac{1+J}{2},
\qquad
P_-=\frac{1-J}{2}
\]

split every representation into even and odd parts. Higher group cohomology
vanishes for every complex representation, including the one-dimensional
sign representation.

Therefore a group-cohomology contraction can exist while \(V^-\) is
nonzero. It does not exclude a free reciprocal zero orbit.

## Correct target

Let \((K^\bullet,d)\) be a source-derived equivariant complex whose
cohomology is the zero module. The required statement is

\[
H^\bullet(P_-K)=0.
\]

Its contracting homotopy must satisfy

\[
d h^-+h^-d=P_-
\]

on the source complex. The differential \(d\), not the group action alone,
must remove the odd state.

Applying the averaging projector and observing that the representation
splits proves no such statement.

## Positive trace formulation

On a finite reciprocal zero module,

\[
\operatorname{tr}P_-=\dim V^-.
\]

This is nonnegative and vanishes exactly when no free reciprocal orbit is
present. Equivalently,

\[
m_{\rm total}-m_{\rm fixed}=2\operatorname{tr}P_-.
\]

The clean source objective is therefore a trace or index formula for the odd
projector on zero cohomology, followed by a source proof that this trace
vanishes.

## Finite hostile model

Take the sign representation \(V=\mathbb C\) with \(J=-1\). Averaging gives
\(P_+=0\) and \(P_-=1\). Its higher group cohomology vanishes, but its odd
dimension and odd-projector trace are both one.

Any proposed theorem that reports "acyclic" on this fixture while claiming
that the odd state is absent has confused the two complexes.

## Revised three-part gate

1. Construct the zero complex from labelled source operations, not from the
   completed scalar function.
2. Prove its cohomology transfers to the divisor module with multiplicity and
   reciprocal action.
3. Construct a homotopy involving the source differential that contracts
   only the odd projection through completion.

Without all three parts, odd-sector language is another representation of
the RH criterion rather than a mechanism.

