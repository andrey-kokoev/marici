import Mathlib.LinearAlgebra.Basic
import Mathlib.Tactic.NormNum

/-!
Minimal algebraic interface behind Grothendieck's integral two-periodic norm
complex. The group-ring realization and its homology remain separate data.
-/

namespace MariciFormal

section AbstractNormRelation

variable {R M : Type*} [CommRing R] [AddCommGroup M] [Module R M]

def normComplement (degree : R) (normMap : M →ₗ[R] M) : M →ₗ[R] M :=
  degree • LinearMap.id - normMap

def SatisfiesNormRelation (degree : R) (normMap : M →ₗ[R] M) : Prop :=
  normMap.comp normMap = degree • normMap

theorem normMap_comp_complement_eq_zero
    (degree : R) (normMap : M →ₗ[R] M)
    (hrelation : SatisfiesNormRelation degree normMap) :
    normMap.comp (normComplement degree normMap) = 0 := by
  ext x
  have hx : normMap (normMap x) = degree • normMap x := by
    have := LinearMap.congr_fun hrelation x
    simpa [SatisfiesNormRelation, LinearMap.comp_apply,
      LinearMap.smul_apply] using this
  simp [normComplement, LinearMap.comp_apply, hx]

theorem complement_comp_normMap_eq_zero
    (degree : R) (normMap : M →ₗ[R] M)
    (hrelation : SatisfiesNormRelation degree normMap) :
    (normComplement degree normMap).comp normMap = 0 := by
  ext x
  have hx : normMap (normMap x) = degree • normMap x := by
    have := LinearMap.congr_fun hrelation x
    simpa [SatisfiesNormRelation, LinearMap.comp_apply,
      LinearMap.smul_apply] using this
  simp [normComplement, LinearMap.comp_apply, hx]

theorem normRelation_defines_twoPeriodicComplex
    (degree : R) (normMap : M →ₗ[R] M)
    (hrelation : SatisfiesNormRelation degree normMap) :
    normMap.comp (normComplement degree normMap) = 0 ∧
      (normComplement degree normMap).comp normMap = 0 :=
  ⟨normMap_comp_complement_eq_zero degree normMap hrelation,
    complement_comp_normMap_eq_zero degree normMap hrelation⟩

end AbstractNormRelation

/-- Omitting `T²=dT` allows both adjacent composites to be nonzero. -/
theorem missing_normRelation_hostile :
    let normMap : ℤ →ₗ[ℤ] ℤ := LinearMap.id
    ¬ SatisfiesNormRelation 2 normMap ∧
      normMap (normComplement 2 normMap 1) = 1 ∧
      normComplement 2 normMap (normMap 1) = 1 := by
  dsimp
  constructor
  · intro h
    have := LinearMap.congr_fun h 1
    norm_num [SatisfiesNormRelation, LinearMap.comp_apply,
      LinearMap.smul_apply] at this
  · norm_num [normComplement, LinearMap.smul_apply]

end MariciFormal
