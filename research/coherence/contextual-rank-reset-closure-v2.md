# Contextual rank-reset closure v2

The current theory passes one integrated replay of twenty exact Python checkers and four Cubical Agda modules.

## Accepted realization hierarchy

```text
ordered/reversal protocol
  two jointly faithful residual charges

finite labelled context set S
  Green span E_S, dimension |S|

complete dense context set
  H1(R) massive Green RKHS

endpoint-only protocol
  two-moment hyperbolic quotient
```

## Accepted coefficient hierarchy

```text
commutative ring
  polynomial Pfaffian/cofactor laws
  integral torsion module
  presented refinement correspondence

selected-gap localization
  adjacent hyperbolic contraction
  invertible Pfaffian transitions

two invertible
  normalized value/flux Green intertwiner
```

## Formal replay

The checked Agda modules are:

- `BoundaryPfaffianFiniteChain.agda`;
- `BoundaryPfaffianResidualFold.agda`;
- `BoundaryPfaffianResidualRankResetInstance.agda`;
- `BoundaryPfaffianFluxMomentQuotient.agda`.

They cover full Pfaffian triangles through size six, arbitrary alternating residual folds, arbitrary finite context programs, joint faithfulness, labelled-flux symmetry, moment kernels, and split endpoint sections.

## Remaining boundary

The main formal extension is equality between the arbitrary coordinate fold and a general matrix-Pfaffian definition in Agda. The universal higher constructor functor and any physical realization remain separate projects. Neither is needed for the accepted minimal-realization classification.

Machine-readable certificate: `contextual-rank-reset-closure.v2.json`.
