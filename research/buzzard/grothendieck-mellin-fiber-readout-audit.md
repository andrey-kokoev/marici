# Finite Mellin-fiber readout audit

Source packet:
`research/grothendieck/mellin-radial-compression-forgets-the-norm-one-idele-class-fiber.md`.

## Formal claim boundary

`MariciFormal/FiniteFiberCompression.lean` formalizes the packet's exact
two-point hostile model over `ℚ`. The source is `Fin 2 → ℚ`; radial
compression is the linear map `(a,b) ↦ a+b`; the angular mode is `(1,-1)`.
Lean proves that this mode is nonzero and belongs to the compression kernel.
It then reuses the cross-sector post-processing kernel theorem to prove that
the mode remains invisible after a scalar post-compression readout. The radial
mode `(1,1)` maps to `2`, so the compressor is not the zero map.

Strength: finite-cutoff theorem and hostile countermodel. This independently
instantiates the same information-loss law as Aspect's finite marginal
readouts. It does not construct the full idele-class source, its norm-one
fiber, a topology or measure, Mellin integration, Fourier–Poisson sewing, or a
completed Green form. The Grothendieck packet explicitly leaves open whether
the distinguished theta state has a nontrivial component in every fiber mode.

## Coefficients and assumptions

- Coefficients are exact rationals `ℚ`.
- The two fiber sites are indexed by `Fin 2`.
- Radial compression is stipulated by the source packet's finite hostile
  model, not claimed to be the analytic adelic pushforward.
- The displayed post-compression readout is the scalar identity; the reusable
  kernel-inclusion theorem applies to arbitrary linear post-processing.

## Verification

Run from `research/buzzard/marici_formal`:

```powershell
lake env lean MariciFormal/FiniteFiberCompression.lean
lake build MariciFormal
```

No Marici site build or Git command is part of this audit.

Both commands were executed. The targeted file exited zero with no output;
the project build completed successfully with 8792 jobs. No source placeholder
or active-conjecture conclusion is used.

## Standard-vacuum finite mode fixture

Source packet:
`research/grothendieck/the-standard-zeta-vacuum-occupies-only-the-trivial-norm-one-fiber-mode.md`.

The same two-point model now has an involutive fiber swap and exact radial and
angular coefficients. Lean proves exact reconstruction of every state from
the constant mode `(1,1)` and angular mode `(1,-1)`, and proves that swap
invariance is equivalent to vanishing angular coefficient. The constant
finite vacuum is invariant and purely radial. The hostile perturbation `(1,0)`
has angular coefficient `1/2` and is not invariant, separating ambient fiber
capacity from activation by the standard vacuum.

This is a finite representation fixture shared with optical common/difference
mode decomposition. It does not formalize the packet's global identification
of the norm-one idele-class fiber, local-unit invariance at every prime, or the
adelic restricted tensor product. Those remain source-side inputs rather than
conclusions of this Lean file.
