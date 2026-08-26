import Mathlib.LinearAlgebra.Basic
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

/-!
Coordinate-free linear core of Grothendieck's Betti boundary-commutator
invariance packet. Smith normal form is deliberately left as a separate
integral interface.
-/

namespace MariciFormal

section CoordinateChange

variable {R : Type*} [CommRing R]
variable {A B C D : Type*}
variable [AddCommGroup A] [AddCommGroup B] [AddCommGroup C] [AddCommGroup D]
variable [Module R A] [Module R B] [Module R C] [Module R D]

/-- Coordinate expression `P_out⁻¹ f P_in`, stated using linear
equivalences so invertibility is carried by the type. -/
def coordinateChange (outBasis : B ≃ₗ[R] B) (inBasis : A ≃ₗ[R] A)
    (map : A →ₗ[R] B) : A →ₗ[R] B :=
  outBasis.symm.toLinearMap.comp (map.comp inBasis.toLinearMap)

theorem coordinateChange_eq_zero_iff
    (outBasis : B ≃ₗ[R] B) (inBasis : A ≃ₗ[R] A)
    (map : A →ₗ[R] B) :
    coordinateChange outBasis inBasis map = 0 ↔ map = 0 := by
  constructor
  · intro hchanged
    ext x
    have hpoint := LinearMap.congr_fun hchanged (inBasis.symm x)
    have htransport := congrArg outBasis hpoint
    simpa [coordinateChange] using htransport
  · rintro rfl
    ext x
    simp [coordinateChange]

theorem coordinateChange_ne_zero_iff
    (outBasis : B ≃ₗ[R] B) (inBasis : A ≃ₗ[R] A)
    (map : A →ₗ[R] B) :
    coordinateChange outBasis inBasis map ≠ 0 ↔ map ≠ 0 := by
  exact not_congr (coordinateChange_eq_zero_iff outBasis inBasis map)

/-- The defect of a candidate chain map. -/
def boundaryCommutator (targetBoundary : C →ₗ[R] D)
    (highMap : A →ₗ[R] C) (lowMap : B →ₗ[R] D)
    (sourceBoundary : A →ₗ[R] B) : A →ₗ[R] D :=
  targetBoundary.comp highMap - lowMap.comp sourceBoundary

/-- Changing all four chain-group bases conjugates the boundary defect by
the outer basis changes; the two intermediate changes cancel. -/
theorem boundaryCommutator_coordinateChange
    (sourceHighBasis : A ≃ₗ[R] A) (sourceLowBasis : B ≃ₗ[R] B)
    (targetHighBasis : C ≃ₗ[R] C) (targetLowBasis : D ≃ₗ[R] D)
    (targetBoundary : C →ₗ[R] D)
    (highMap : A →ₗ[R] C) (lowMap : B →ₗ[R] D)
    (sourceBoundary : A →ₗ[R] B) :
    boundaryCommutator
        (coordinateChange targetLowBasis targetHighBasis targetBoundary)
        (coordinateChange targetHighBasis sourceHighBasis highMap)
        (coordinateChange targetLowBasis sourceLowBasis lowMap)
        (coordinateChange sourceLowBasis sourceHighBasis sourceBoundary) =
      coordinateChange targetLowBasis sourceHighBasis
        (boundaryCommutator targetBoundary highMap lowMap sourceBoundary) := by
  ext x
  simp [boundaryCommutator, coordinateChange]

/-- Vanishing of the boundary obstruction is presentation-independent. -/
theorem boundaryCommutator_changed_eq_zero_iff
    (sourceHighBasis : A ≃ₗ[R] A) (sourceLowBasis : B ≃ₗ[R] B)
    (targetHighBasis : C ≃ₗ[R] C) (targetLowBasis : D ≃ₗ[R] D)
    (targetBoundary : C →ₗ[R] D)
    (highMap : A →ₗ[R] C) (lowMap : B →ₗ[R] D)
    (sourceBoundary : A →ₗ[R] B) :
    boundaryCommutator
        (coordinateChange targetLowBasis targetHighBasis targetBoundary)
        (coordinateChange targetHighBasis sourceHighBasis highMap)
        (coordinateChange targetLowBasis sourceLowBasis lowMap)
        (coordinateChange sourceLowBasis sourceHighBasis sourceBoundary) = 0 ↔
      boundaryCommutator targetBoundary highMap lowMap sourceBoundary = 0 := by
  rw [boundaryCommutator_coordinateChange]
  exact coordinateChange_eq_zero_iff _ _ _

end CoordinateChange

/-- Vanishing after one modular reduction is not evidence of integral
vanishing: the nonzero integer `2` disappears modulo `2`. -/
theorem one_prime_vanishing_not_integral_vanishing :
    (2 : ℤ) ≠ 0 ∧ (2 : ZMod 2) = 0 := by
  norm_num

end MariciFormal
