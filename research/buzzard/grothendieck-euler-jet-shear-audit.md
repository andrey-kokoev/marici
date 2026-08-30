# Euler-jet shear audit

Source packet:
`research/grothendieck/primitive-and-square-euler-jet-currents-have-flat-triangle-transport.md`.

## Formal theorem boundary

`MariciFormal/EulerJetShear.lean` defines the normalized rational lower shear

```text
[[1, 0], [a, 1]].
```

Lean proves that two such shears multiply by adding slopes, commute, and have
determinant one. A chart potential induces comparison slope `a_q-a_p`; these
comparisons compose exactly and every triangle product is the identity.

The hostile upper shear supplies a second nilpotent direction. At unit slopes,
the lower and upper shears do not commute. Thus flatness follows from the
source packet's one-generator premise; arbitrary two-generator enlargement
would not inherit it.

This exact matrix fixture is shared with optical transfer shears. It does not
formalize the analytic Euler factor, logarithmic series, prime-depth
convergence, or identify primitive and square coefficients from a completed
source. Those remain packet-side inputs.

## Verification

Run from `research/buzzard/marici_formal`:

```powershell
lake env lean MariciFormal/EulerJetShear.lean
lake build MariciFormal
```

No Git command or Marici site build is part of this audit.

Both commands were executed successfully. The targeted file exited zero with
no output, and the project build completed with 8796 jobs. The first targeted
run exposed only proof-order and normalization defects in the triangle proof;
those were repaired without changing the theorem statements. No placeholder
or active-conjecture conclusion remains.
