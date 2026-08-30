# Two-axis matrix-generation audit

Source packet:
`research/grothendieck/two-nonresonant-primes-generate-the-full-reciprocal-matrix-algebra.md`.

## Formal theorem boundary

`MariciFormal/TwoAxisMatrixGeneration.lean` works over complex `2×2`
matrices. The first reciprocal axis is `sigmaOne`; the second is
`cosine * sigmaOne + sine * sigmaTwo`. If `sine ≠ 0`, Lean constructs explicit
coefficients expressing every target matrix as a linear combination of
identity, the first axis, the second axis, and their ordered product.

At the resonant locus `sine=0`, the hostile parallel-axis fixture proves that
the missing `sigmaTwo` direction cannot be expressed by those four generated
matrices. Nonresonance is therefore a necessary premise of this generation
argument.

Strength: finite complex matrix-generation theorem. This is local algebraic
capability, not a compiler for a norm-ordered prime product, a convergence
theorem, a spectral determinant, or evidence constraining Riemann zeros. The
Lean file treats cosine and sine as typed coefficients and does not formalize
their analytic origin `t log(q/p)` or the exact trigonometric exceptional set.

## Verification

Run from `research/buzzard/marici_formal`:

```powershell
lake env lean MariciFormal/TwoAxisMatrixGeneration.lean
lake build MariciFormal
```

No Git command or Marici site build is part of this audit.

Both commands were executed successfully. The final targeted run exited zero
without output or warnings, and the project build completed with 8797 jobs.
Unused simplifier hints reported by the first targeted run were removed before
the final verification. No placeholder or active-conjecture conclusion is
present.
