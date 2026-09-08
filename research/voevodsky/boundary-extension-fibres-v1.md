# Boundary extension fibres: bounded Cubical interface

## Question

Can the Cubical interface distinguish unique extension of fixed boundary data from selection of a normalized boundary marking, without changing the analytic evaluator?

## Claim boundary

`agda/BoundaryExtensionFibres.agda` defines the dependent extension fibre, unique-extension predicate, and path-valued pairwise overlap assembly. The identity restriction has a proposed constructive contraction of each fibre. A two-constructor marking type mapping to a singleton supplies regressions: a split readout need not be invertible, its normalized fibre need not be contractible, and unique identity-extension fibres do not select one normalized boundary marking. `FaithfulReadout` deliberately demands contractible fibres (full equivalence, stronger than mere injectivity).

These are abstract regressions, not a formalization of the octagon, polynomial coefficients, chain contractions, or its source comparison. Pairwise overlap data alone do not certify arbitrary higher-dimensional descent. No conversion from a marking-space certificate to an acyclic derived-complex certificate is supplied. The analytic completion and Dirichlet interfaces are unchanged.

## Disposition

Implemented and successfully typechecked as an isolated safe Cubical module, using Agda 2.8.0.1 and Cubical 0.9. All counterexample proofs and the identity-fibre contraction passed; no holes or postulates were authored. No aggregate or analytic rebuild was performed.

Structured-command initially refused Agda (`executed: false`, `command_not_allowed`). The operator subsequently explicitly authorized shell execution for Agda commands. The first shell attempt found no Agda on PATH; the existing checker configuration supplied the installed executable below. Its first typecheck reported an infective-import flag mismatch. Adding `--guardedness`, required by Cubical.Foundations.Prelude, repaired it without weakening `--safe`. The repeated command exited 0:

```
pwsh -NoProfile -Command "& 'C:/Users/andrey/tools/agda-2.8.0.1/agda.exe' --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/BoundaryExtensionFibres.agda"
```

Compiler output: `Checking BoundaryExtensionFibres`. The acceptance test is now satisfied for this module. No dependency or toolchain installation was performed. Shell fallback was confined to the authorized Agda executions; source and packet mutations used filesystem MCP.

Operator prohibited all Git operations; none performed. New owned files: this packet and `research/voevodsky/agda/BoundaryExtensionFibres.agda`. No existing source was edited. No commit or push was performed.
