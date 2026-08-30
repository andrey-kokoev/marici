# Prime-seam factorization audit

Source packet:
`research/grothendieck/poisson-sewing-does-not-factor-through-prime-seam-sampling.md`.

## Formal theorem boundary

`MariciFormal/FiniteSamplingFactorization.lean` proves over an arbitrary field
that if a source variation lies in the kernel of a sampling map but not in the
kernel of a richer readout, then no linear interpolation can factor the richer
readout through sampling.

The packet's exact hostile model is instantiated over `ℚ` on `Fin 2 → ℚ`.
`seamSampling` reads coordinate zero, `gapSensitiveReadout` reads coordinate
one, and `gapVariation=(0,1)` is sampling-invisible but readout-visible. Lean
therefore rejects every factorization
`gapSensitiveReadout = interpolation.comp seamSampling`.

This is a finite source-typed factorization obstruction shared with optical
sampling aliasing. It does not construct Schwartz or adelic test spaces,
prime-power evaluation, Fourier–Poisson correspondence, Mellin readout, or a
continuous between-primes bump. Formalizing the analytic packet verbatim
still requires those source spaces, maps, topology, and normalization.

## Verification

Run from `research/buzzard/marici_formal`:

```powershell
lake env lean MariciFormal/FiniteSamplingFactorization.lean
lake build MariciFormal
```

No Git command or Marici site build is part of this audit.

Both commands were executed successfully. The targeted file exited zero with
no output, and the project build completed with 8794 jobs. No placeholder or
active-conjecture conclusion is present.
