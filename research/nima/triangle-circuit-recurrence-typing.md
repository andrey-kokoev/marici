# The recurring \((1,-1,1)\) vector is shared incidence calculus, not yet a shared class

The same coordinate row appears in three nearby calculations:

1. the disappearing triple incidence of Entry 712;
2. the resolved principal Čech cokernel of Entries 738--743;
3. the generic physical triple-wall logarithmic circuit.

The recurrence has a universal explanation.  For an ordered triangle, the
vertex-to-edge incidence matrix

\[
\delta=
\begin{pmatrix}
0&1&0\\
0&0&1\\
0&-1&1
\end{pmatrix}
\]

has rank two and left cokernel represented by

\[
\lambda=(1,-1,1).
\]

Equivalently, \((1,-1,1)\) is the standard alternating boundary sign of an
ordered two-simplex.  Its recurrence is therefore evidence that all three
constructions use the same **incidence calculus**.

It does not identify their coefficient objects.  Rescaling the three edge
generators changes the displayed row contragrediently, while leaving the
cokernel line invariant.  More importantly, identical incidence complexes
can carry different deck characters, Kummer covers, support conditions, and
connections.

Entry 712 is the internal negative control: its primitive incidence vector is
exactly \((1,-1,1)\), yet its image under the signed-pair discriminant symbol
is generically nonzero.  The vector therefore does not itself provide the
required lift.

The strongest current conclusion is

\[
\boxed{
\text{common oriented-triangle calculus}
\; + \;
\text{separately typed coefficient lines}.
}
\]

A stronger identification requires a source-labelled chain map preserving
support, deck character, internal differential, and Gauss--Manin transport.
Matching a coordinate row or a one-dimensional cokernel is insufficient.

## Reproducibility

- `research/nima/checkers/check_triangle_circuit_recurrence_typing.py`
- `research/nima/results/triangle_circuit_recurrence_typing.json`
- ledger Entries 712, 738, 740, and 743
