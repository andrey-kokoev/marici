# Wilson history-dilation gate: WP1087

## Question

Can a unitary Wilson evolution admit a minimal nondestructive three-grade
history bundle?

## Conditional bundle

Suppose the missing WP1085 Wilson boundary condition is supplied and the
evolution \(U\) is unitary with simple spectrum. Define the three-grade bundle

\[
V x=\frac{1}{\sqrt3}(x,Ux,U^2x).
\]

Because \(U\) is unitary,

\[
\sum_{k=0}^{2}U^{-k}U^k=3I,
\]

so \(V^\dagger V=I\). The bundle stores all three composition grades without
losing norm.

The checker uses the order-three cyclic permutation
\(e_1\mapsto e_2\mapsto e_3\mapsto e_1\), whose eigenvalues are the three
distinct cube roots of unity. For \(x=(1,2,3)\), the three grade norms sum to
\(42=3\cdot14\), verifying the isometry identity.

## Boundary

This is only a mathematical conditional constructor. The current source still
does not supply:

- the source-fixed unitary Wilson evolution;
- a physical grade register;
- typed readout ports;
- a cyclic ray \(x\);
- the WP1081 reference \(\rho\).

Thus the bundle must not be promoted to a sourced physical history instrument.

## Classification

Conditional history constructor. If the Wilson flag and unitary evolution are
later sourced, an exact three-grade isometric bundle exists. The remaining
physical gates are the source-derived grade register, readout ports, coherent
cyclic ray, and volume reference.

Checker: `research/flavor/checkers/wp1087_wilson_history_dilation_gate.py`

Result: `results/wp1087_wilson_history_dilation_gate.json`
