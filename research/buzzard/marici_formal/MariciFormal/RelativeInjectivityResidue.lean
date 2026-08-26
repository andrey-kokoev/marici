import Mathlib

/-!
Failure of relative injectivity has an exact ordinary residue: the excess
preimage maps onto the intersection of the codomain-transport kernel with the
realized operator image, and its kernel is the original operator kernel.
-/

namespace MariciFormal

variable {V W U : Type} [AddCommGroup V] [Module Rat V]
  [AddCommGroup W] [Module Rat W] [AddCommGroup U] [Module Rat U]

def ExcessPreimage (sourceMap : V →ₗ[Rat] W) (codomainTransport : W →ₗ[Rat] U) :
    Submodule Rat V :=
  LinearMap.ker (codomainTransport.comp sourceMap)

def ImageKernelOverlap
    (sourceMap : V →ₗ[Rat] W) (codomainTransport : W →ₗ[Rat] U) :
    Submodule Rat W :=
  LinearMap.range sourceMap ⊓ LinearMap.ker codomainTransport

noncomputable def excessResidueMap
    (sourceMap : V →ₗ[Rat] W) (codomainTransport : W →ₗ[Rat] U) :
    ExcessPreimage sourceMap codomainTransport →ₗ[Rat]
      ImageKernelOverlap sourceMap codomainTransport where
  toFun x := ⟨sourceMap x, ⟨⟨x, rfl⟩, by
    have hx := x.property
    simpa [ExcessPreimage, LinearMap.mem_ker] using hx⟩⟩
  map_add' x y := by
    ext
    simp
  map_smul' scalar x := by
    ext
    simp

theorem excessResidueMap_kernel_iff
    (sourceMap : V →ₗ[Rat] W) (codomainTransport : W →ₗ[Rat] U)
    (x : ExcessPreimage sourceMap codomainTransport) :
    excessResidueMap sourceMap codomainTransport x = 0 ↔ sourceMap x = 0 := by
  constructor
  · intro h
    have hValue := congrArg Subtype.val h
    simpa [excessResidueMap] using hValue
  · intro h
    apply Subtype.ext
    simpa [excessResidueMap] using h

theorem excessResidueMap_surjective
    (sourceMap : V →ₗ[Rat] W) (codomainTransport : W →ₗ[Rat] U) :
    Function.Surjective (excessResidueMap sourceMap codomainTransport) := by
  intro overlap
  rcases overlap.property.1 with ⟨x, hx⟩
  have hxExcess : x ∈ ExcessPreimage sourceMap codomainTransport := by
    simp only [ExcessPreimage, LinearMap.mem_ker, LinearMap.comp_apply]
    rw [hx]
    exact overlap.property.2
  refine ⟨⟨x, hxExcess⟩, ?_⟩
  apply Subtype.ext
  exact hx

/-- Exactness at the excess preimage: residue zero is precisely source kernel. -/
theorem relativeInjectivityResidue_exact
    (sourceMap : V →ₗ[Rat] W) (codomainTransport : W →ₗ[Rat] U) :
    Function.Surjective (excessResidueMap sourceMap codomainTransport) ∧
      ∀ x : ExcessPreimage sourceMap codomainTransport,
        excessResidueMap sourceMap codomainTransport x = 0 ↔ sourceMap x = 0 := by
  exact ⟨excessResidueMap_surjective sourceMap codomainTransport,
    excessResidueMap_kernel_iff sourceMap codomainTransport⟩

theorem zeroOverlap_iff_relativeInjectivity
    (sourceMap : V →ₗ[Rat] W) (codomainTransport : W →ₗ[Rat] U) :
    ImageKernelOverlap sourceMap codomainTransport = ⊥ ↔
      ∀ x, codomainTransport (sourceMap x) = 0 → sourceMap x = 0 := by
  constructor
  · intro hOverlap x hx
    have hMember : sourceMap x ∈ ImageKernelOverlap sourceMap codomainTransport :=
      ⟨⟨x, rfl⟩, hx⟩
    rw [hOverlap] at hMember
    simpa using hMember
  · intro hRelative
    apply le_antisymm
    · intro y hy
      have hyZero := hRelative hy.1.choose (by
        rw [hy.1.choose_spec]
        exact hy.2)
      rw [hy.1.choose_spec] at hyZero
      simpa using hyZero
    · exact bot_le

end MariciFormal
