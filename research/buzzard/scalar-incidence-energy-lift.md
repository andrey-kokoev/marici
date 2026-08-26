# Scalar incidence does not determine the energy lift

Owner: `marici.Buzzard`

Source locator: `Scalar Poisson incidence does not determine the energy lift`
in `research/strominger/distinction-preserving-completion.md`.

## Formal increment

The state space is `Fin 2 → Rat`. The distinguished state is `e₀`; the hidden
complementary state is `e₁`. The Clark reference form is the identity quadratic
form.

Lean defines two energy lifts:

- `positiveEnergyLift(x) = x₀² + x₁²`, corresponding to `diag(1,1)`;
- `indefiniteEnergyLift(x) = x₀² - x₁²`, corresponding to `diag(1,-1)`.

Lean proves both lifts give scalar observation one on the distinguished state.
The positive lift equals the Clark form and is nonnegative on every state. The
indefinite lift gives value `-1` on the hidden state and is not nonnegative.

The existential hostile theorem therefore shows that equality of the observed
scalar byte is compatible with both coercive and noncoercive global lifts.

## Type-system consequence

A scalar incidence section fixes only its tested matrix coefficient. It does
not select the feature map, pairing matrix, orientation, or generalized
Rayleigh spectrum on the unobserved complement. Those remain separate typed
inputs.

## Boundary and missing interfaces

This is the exact rational two-channel hostile, not a construction of the
Tate--Poisson energy. A faithful sector theorem requires:

- the four typed feature rows in `W_X`;
- a source-derived pairing/orientation matrix `J_X`;
- the factorization `E_X = W_X^* J_X W_X`;
- the Clark form `B_{a,X}` and positivity conventions;
- cutoff covariance and residual block typing;
- generalized eigenvalue/Rayleigh definitions;
- a determinant--kernel bridge for any scalar-divisor conclusion.

This increment overlaps the earlier symmetry-versus-positivity lesson but is
not collapsed into it: here the hostile concerns underdetermination by a
distinguished scalar observation, not reflection symmetry.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/EnergyLiftAmbiguity.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

The targeted command exited `0` without warnings or diagnostics. No site build
or Git command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/EnergyLiftAmbiguity.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/scalar-incidence-energy-lift.md`
