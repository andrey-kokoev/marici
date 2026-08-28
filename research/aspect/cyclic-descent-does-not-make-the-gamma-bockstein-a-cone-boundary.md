# Cyclic descent does not make the gamma-Bockstein a cone boundary

## New lowest obstruction

The gamma-Bockstein is now normalized and strictly descended across the complete cyclic chart atlas. That proves it is a globally defined class. It does not prove that the class vanishes in specialization-cone cohomology.

For consecutive cone differentials

\[
C^{k-1}\mathop{\longrightarrow}^{d_{k-1}}C^k
\mathop{\longrightarrow}^{d_k}C^{k+1},
\]

the Bockstein vector (eta\in C^k) must pass two independent gates:

1. cycle: (d_k\beta=0);
2. boundary: there exists (h\in C^{k-1}) with (d_{k-1}h=\beta).

In finite matrices, the boundary gate is exact:

\[
\operatorname{rank}(d_{k-1})
=
\operatorname{rank}([d_{k-1}\mid\beta]).
\]

## Minimal hostile

Take a one-dimensional middle cone group, zero differentials, and (eta=1). The class is closed. Give every atlas transition unit one, so descent and triangle holonomy are perfect. Yet the preceding differential has zero image, while augmenting it by (eta) raises rank from zero to one. The class is not a boundary.

The boundary control replaces the preceding differential by the identity. The same (eta) then has primitive (h=1).

Thus no amount of additional prime checking or chart coherence can substitute for construction of the relative cone differential and primitive.

## Admission gate

The next source packet must export:

1. the finite source-derived specialization-cone groups in the relevant grades;
2. both adjacent differentials;
3. the embedded gamma-Bockstein vector;
4. the cycle residual;
5. the augmented boundary rank;
6. an explicit primitive if the class vanishes;
7. transport of that primitive across the cyclic atlas.

If the augmented rank rises by one, the proposed repair remains a nonzero cohomology class and the Deutsch explanation fails at the final causal step.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_specialization_cone_nonboundary_hostile.py
```
