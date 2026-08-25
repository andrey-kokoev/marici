# Completion-kernel typing — cycle 4

## Sources

- Strominger, `generic-completion-kernel-comparison-theorem.md`.
- `contracts/magnetic-generic-completion.v1.json`.
- `contracts/grothendieck-theta-completion-test.v1.json`.

## Increment

`CompletionKernel.lean` formalizes the algebraic layer common to both frozen
contracts: injective source and target embeddings, source and completed linear
operators, a named canonical-extension mechanism, and the commuting square.
The square restricts to an injective map between kernels. The ordinary
completion-only kernel is the quotient by its range. A derived/Tor obstruction
is a separately evidenced type.

The hostile theorem `completion_does_not_manufacture_operator` exhibits
completion data while the corresponding operator-extension type is empty.

Finite executable models reproduce the magnetic `0 → 21` and theta `0 → 1`
kernel-dimension patterns. They are algebraic models only; they do not prove
the analytic sector claims.

## Disposition

**Generalized algebraically, specialized analytically.** The kernel comparison
and quotient are shared. Density, topology, graph limits, and uniqueness of
the analytic extension are not erased into the common structure.

## Missing convention-fixed inputs

1. Concrete topological vector-space structures and the chosen Hausdorff
   topologies.
2. Formal density proofs for atomic measures and `C_c^∞` respectively.
3. Continuity/closability and uniqueness evidence for the declared extension
   mechanisms.
4. Formal elliptic-regularity and Friedrichs-generator results establishing
   the actual sector kernels.
5. Graph-limit representatives for every completion-only class.
6. A concrete derived category/Tor library before any derived obstruction can
   be constructed rather than merely kept type-distinct.

## Build

From `research/buzzard/marici_formal`, run `lake build`.

Result: `Build completed successfully (8714 jobs).` Lean/mathlib version:
`v4.33.1`.
