# Common scalar mode-factor audit

Source packet:
`research/grothendieck/eisenstein-fourier-modes-repeat-rather-than-constrain-the-scattering-divisor.md`.

## Formal theorem boundary

`MariciFormal/CommonScalarModeFactor.lean` works over an arbitrary field `F`
and channel type `ι`. A finite or infinite family is represented pointwise as
`scaledModes scalar profile i = scalar * profile i`.

Lean proves:

- if at least one profile channel is nonzero, all channels vanish exactly when
  the common scalar vanishes;
- a channel whose profile coefficient is one recovers the scalar exactly;
- division by a nonzero anchor channel cancels the common scalar;
- if every profile channel is zero, the nonzero scalar one is undetectable.

The same algebraic structure occurs in Grothendieck's common Eisenstein
denominator and Aspect's common calibration factors. The theorem therefore
formalizes repetition versus cancellation of one scalar datum. It does not
define completed zeta, Bessel profiles, meromorphic orders, scattering poles,
Maass–Selberg forms, or any resonance-confinement condition.

## Assumptions

- Coefficients form a field `F`.
- The channel profile is an arbitrary function `ι → F`.
- Detection requires an explicit witness that some profile coefficient is
  nonzero.
- Ratio cancellation requires both the common scalar and anchor profile to be
  nonzero.

## Verification

Run from `research/buzzard/marici_formal`:

```powershell
lake env lean MariciFormal/CommonScalarModeFactor.lean
lake build MariciFormal
```

No Git command or Marici site build is part of this audit.

Both commands were executed successfully. The targeted file exited zero with
no output, and the project build completed with 8793 jobs. The file contains
no placeholders and assumes no active-conjecture conclusion.
