/-!
# Entries 2125 and 2116: relative phase and jointly faithful probes

This dependency-free file uses only Lean's prelude.

For Entry 2125, the coefficient type has subtraction, a distinguished zero,
and the single cancellation law used by the proof.  No division, topology,
or periodicity is assumed.

For Entry 2116, a `d`-dimensional coordinate carrier over a coefficient type
`𝕜` is represented explicitly by `Fin d → 𝕜`.  The theorem is set-theoretic,
so the probes need not be assumed linear: it therefore applies in particular
to every finite family of linear probes once those maps are supplied.
-/

namespace Marici.Buzzard

section RelativePhase

variable {A : Type} [Sub A] [OfNat A 0]

/-- The exact subtraction cancellation assumption needed below. -/
def SubZeroKernelLaw (A : Type) [Sub A] [OfNat A 0] : Prop :=
  ∀ x y : A, y - x = 0 ↔ y = x

/-- Entry 2125's relative-phase character `(α₀, α₁) ↦ α₁ - α₀`. -/
def differenceCharacter (α : A × A) : A := α.2 - α.1

/-- The diagonal common-phase locus. -/
def diagonalCommonPhase (α : A × A) : Prop := α.1 = α.2

/-- Entry 2125: the kernel of the difference character is exactly diagonal. -/
theorem differenceCharacter_mem_kernel_iff_diagonal
    (hsub : SubZeroKernelLaw A) (α : A × A) :
    differenceCharacter α = 0 ↔ diagonalCommonPhase α := by
  rw [differenceCharacter, hsub]
  exact eq_comm

/-- Extensional form: the kernel predicate equals the diagonal predicate. -/
theorem differenceCharacter_kernel_eq_diagonal (hsub : SubZeroKernelLaw A) :
    (fun α : A × A => differenceCharacter α = 0) = diagonalCommonPhase := by
  funext α
  apply propext
  exact differenceCharacter_mem_kernel_iff_diagonal hsub α

end RelativePhase

section JointFaithfulness

variable {𝕜 W : Type} [OfNat W 0]

/-- A coordinate model for a `d`-dimensional coefficient space. -/
abbrev CoordinateSpace (d : Nat) (𝕜 : Type) := Fin d → 𝕜

/-- A finite family of `m` probes on a `d`-coordinate carrier. -/
abbrev ProbeFamily (d m : Nat) (𝕜 W : Type) :=
  Fin m → CoordinateSpace d 𝕜 → W

/-- The intersection of all probe kernels, expressed as a predicate. -/
def InJointKernel {d m : Nat} (q : ProbeFamily d m 𝕜 W)
    (v : CoordinateSpace d 𝕜) : Prop :=
  ∀ i, q i v = 0

/-- A probe family is jointly faithful when only zero lies in every kernel. -/
def JointlyFaithful {d m : Nat} [OfNat 𝕜 0]
    (q : ProbeFamily d m 𝕜 W) : Prop :=
  ∀ v, InJointKernel q v → v = fun _ => 0

/--
Entry 2116's finite-dimensional generalization: joint faithfulness is
precisely triviality of the intersection of the probe kernels.
-/
theorem jointlyFaithful_iff_jointKernel_trivial {d m : Nat} [OfNat 𝕜 0]
    (q : ProbeFamily d m 𝕜 W) :
    JointlyFaithful q ↔ ∀ v, InJointKernel q v → v = fun _ => 0 := by
  rfl

/-- Expanded coefficient-level form of the same characterization. -/
theorem jointlyFaithful_iff_forall_probe_zero {d m : Nat} [OfNat 𝕜 0]
    (q : ProbeFamily d m 𝕜 W) :
    JointlyFaithful q ↔
      ∀ v : Fin d → 𝕜, (∀ i : Fin m, q i v = 0) → v = fun _ => 0 := by
  rfl

end JointFaithfulness

end Marici.Buzzard
