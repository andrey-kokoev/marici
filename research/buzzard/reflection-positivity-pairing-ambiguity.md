# Reflection and positivity do not select the pairing

Owner: `marici.Buzzard`

Source locator: `Reflection and positivity still do not select the pairing`
in `research/strominger/distinction-preserving-completion.md`.

## Formal increment

The channel space is `Fin 2 → Rat`, with reflection swapping the two
coordinates. `reflectionPairing alpha beta` is the quadratic form associated
with

`[[alpha,beta],[beta,alpha]]`.

Lean proves every such form is invariant under channel swap. It then verifies
strict positive definiteness for the two exact forms

- `identityPairing`, with parameters `(1,0)`;
- `coupledPairing`, with parameters `(2,1)`.

The second positivity proof uses the exact sum-of-squares decomposition

`2x₀² + 2x₀x₁ + 2x₁² = (x₀+x₁)² + x₀² + x₁²`.

On the same first-channel feature, the two forms give energies one and two.
Lean therefore proves existentially that reflection invariance and positive
definiteness admit distinct pairings with different observed energies.

## Type-system consequence

Covariance restricts a pairing to a commutant cone; positivity restricts that
cone further. Neither condition selects a point. A source flux normalization,
boundary current, or equivalent pairing constructor remains independent data.

This is stronger than the earlier one-dimensional hostile where reflection
alone admitted both positive and negative signs. Here both competing pairings
are already strictly positive and reflection invariant.

## Boundary and missing interfaces

This is a rational two-channel quadratic model. A faithful sector theorem
still needs:

- the four-channel source representation and its parity decomposition;
- real or complex symmetric/Hermitian pairing types;
- the precise reflection or reciprocal-conjugate action;
- the feature rows and source-derived normalization functionals;
- multiplicity spaces and their commutant dimension;
- a proof that supplied flux probes reconstruct the pairing.

The abstraction generalized the nonselection theorem while preserving the
sector-specific need for a source-derived pairing.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/ReflectionPairingAmbiguity.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

The targeted command exited `0` without warnings or diagnostics. No site build
or Git command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/ReflectionPairingAmbiguity.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/reflection-positivity-pairing-ambiguity.md`
