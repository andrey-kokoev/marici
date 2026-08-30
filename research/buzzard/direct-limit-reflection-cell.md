# Direct-limit reflection cell

Owner: `marici.Buzzard`

Source locator: `Direct-limit reflection cell` and the repeated-dilation
counterexample in `research/strominger/distinction-preserving-completion.md`.

## Formal increment

For a complex scalar transition `u`, Lean proves that the explicit unitary
premise `‖u‖ = 1` implies

`u⁻¹ = conj u`.

Thus, at the scalar level, the dual transition and conjugate transition agree
on the unit circle. This is the finite comparison cell used by the seam
construction.

The off-seam hostile family is the real metric sequence

`dilatedMetric n = (1/4)^n`.

Lean proves its initial value is one, each step divides the metric coefficient
by four, every finite coefficient is positive, and the sequence converges to
zero. It follows that there is no positive constant uniformly bounded below by
all transported metrics.

## Exact distinction

Every finite dilation admits exact metric transport. This does not establish
uniform equivalence to the original ambient metric. Finite compatibility and
uniform comparison are therefore different theorem fields.

Likewise, the scalar equality between inverse and conjugate transitions does
not by itself construct a Hilbert direct limit, a Riesz map, or a line-valued
reflection cell.

## Assumptions and limits

The unitary theorem uses complex scalars and their standard norm and
conjugation. The hostile sequence uses real coefficients and ordinary
topological convergence. `dilatedMetric` is marked noncomputable because
Lean's real division instance is noncomputable; this has no effect on its
propositional theorems.

A faithful line-level upgrade still needs:

- an indexed family of one-dimensional Hilbert spaces;
- directed bonding maps and their cocycle law;
- unitarity at every admitted seam transition;
- the direct-limit constructor;
- compatible dual, conjugate, and Riesz comparison maps;
- an independently sourced ambient comparison for any off-seam uniformity
  claim.

The abstraction generalized the unitary scalar identity and specialized the
nonuniformity obstruction to the exact repeated-dilation model.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/DirectLimitReflection.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

The targeted command exited `0` without diagnostics. No site build or Git
command was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/DirectLimitReflection.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/direct-limit-reflection-cell.md`
