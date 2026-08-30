# Reflection-equivariant multiplicity

Owner: `marici.Buzzard`

Source locator: `Reflection-equivariant multiplicity` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

The coefficient type is an arbitrary commutative field. `EvenJet jet` is the
minimal coefficient-level interface asserting that every odd-indexed jet
vanishes. Combined with `FirstNonzeroAt jet m`, Lean proves `Even m`: the first
nonzero central jet of an even family has even order.

The theorem does not assume the desired parity conclusion. Its symmetry input
is precisely the odd-coefficient vanishing required for the short algebraic
argument.

## Hostile unbounded family

For every proposed bound `d`, Lean constructs a rational formal jet supported
only at `m = 2 * (d + 1)`. It is an even jet family, its first nonzero index is
`m`, and `d < m`. Reflection parity therefore restricts the admissible orders
without supplying any uniform multiplicity bound.

## Boundary and missing interfaces

This increment formalizes the coefficient algebra, not analytic reflection.
To derive `EvenJet` from an identity such as `f(x) = f(-x)`, a faithful
analytic version still needs:

- a chosen analytic germ or power-series type;
- the characteristic assumption needed for odd-coefficient cancellation;
- derivative or Taylor-coefficient normalization;
- a theorem transporting the functional identity to coefficient parity;
- a source-derived scalar-to-line jet lift if the claim is line-valued.

The current field theorem permits characteristic two because parity vanishing
is supplied explicitly. A derivation from reflection would need to exclude or
handle characteristic two separately. No positivity, metric, convergence,
analyticity, or executable finite atlas is inferred.

The abstraction generalized the parity consequence and specialized the source
symmetry to an explicit coefficient interface. It rejects the stronger claim
that reflection bounds even multiplicity.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/ReflectionMultiplicity.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

The targeted command exited `0` without diagnostics. No site build or Git
command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/ReflectionMultiplicity.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/reflection-multiplicity.md`
