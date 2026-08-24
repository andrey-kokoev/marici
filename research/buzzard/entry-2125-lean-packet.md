# Lean packet: Entries 2125 and 2116

## Formal objects

- Entry 2125's `(α₀, α₁) ↦ α₁ - α₀` is
  `Marici.Buzzard.differenceCharacter`.
- Its kernel is the predicate `differenceCharacter α = 0`.
- The common-phase diagonal is `diagonalCommonPhase α`, defined by
  `α.1 = α.2`.
- `differenceCharacter_mem_kernel_iff_diagonal` proves pointwise equality;
  `differenceCharacter_kernel_eq_diagonal` proves extensional equality of
  the two predicates.
- Entry 2116's finite coordinate carrier is `CoordinateSpace d 𝕜 = Fin d → 𝕜`.
- A finite family of probes is `ProbeFamily d m 𝕜 W`.
- `InJointKernel q v` means `q i v = 0` for every probe `i`.
- `JointlyFaithful q` means every vector in that joint kernel is zero.
- `jointlyFaithful_iff_jointKernel_trivial` and
  `jointlyFaithful_iff_forall_probe_zero` state the requested equivalence.

## Assumptions and coefficient types

Entry 2125 is proved over an arbitrary coefficient type `A` with subtraction
`[Sub A]`, a distinguished zero `[OfNat A 0]`, and the explicit hypothesis
`SubZeroKernelLaw A`, namely `∀ x y, y - x = 0 ↔ y = x`. It assumes no order,
topology, field structure, or phase periodicity. Every additive group supplies
this law, but the dependency-free file records only the exact law it uses.

Entry 2116 uses arbitrary coefficient and codomain types `𝕜` and `W`, with
distinguished zeros `[OfNat 𝕜 0] [OfNat W 0]`. Dimensions and family cardinality are natural
numbers `d` and `m`; the carrier and probe index are `Fin d` and `Fin m`.
The equivalence is set-theoretic and does not require probe linearity, so it
specializes to linear probe families.

## Typing boundary

The ledger calls the map a “character” and its kernel a “line,” but does not
fix whether phases are real/additive coefficients, elements of
`ℝ / 2πℤ`, or circle-valued. The theorem here selects the minimal additive
group reading. For genuinely periodic phases, the diagonal statement must be
made in the chosen quotient group; an equality in real representatives has a
larger periodic preimage and is not the theorem proved here.

Likewise, Entry 2116 does not specify a scalar field, linear-map type, or a
proof that each source-admissible differential `dqᵢ` is linear. The formal
kernel characterization is therefore stated for arbitrary probes on an
explicit finite coordinate carrier. A Mathlib `LinearMap.ker`/submodule
version requires agreement on a project root, Mathlib version, scalar field,
modules, and linearity of every `dqᵢ`.

This formalization does not assume any cosmological activation, legality,
framing, physical distinguishability, or source-generation conclusion.

## Build

Run from `C:/Users/andrey/src/marici`:

```powershell
& "$env:USERPROFILE/.elan/bin/lean.exe" research/buzzard/Entry2125.lean
```

Lean version: `4.33.1` (`x86_64-w64-windows-gnu`).

Result on 2026-08-24: exit code `0`, with no diagnostics.
