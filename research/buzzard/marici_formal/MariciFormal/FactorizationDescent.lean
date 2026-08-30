import MariciFormal.Sprint1

/-!
Factorization through an arbitrary presentation map.

Kernel inclusion is sufficient for the canonical quotient map.  For a general
map into a named target, surjectivity (or equivalent presentation data) is an
additional premise.
-/

namespace MariciFormal

section General

variable {R V W D : Type*} [CommRing R]
  [AddCommGroup V] [Module R V]
  [AddCommGroup W] [Module R W]
  [AddCommGroup D] [Module R D]

def FactorsThrough (Q : V →ₗ[R] W) (observation : V →ₗ[R] D) : Prop :=
  ∃ induced : W →ₗ[R] D, induced.comp Q = observation

theorem factorsThrough_implies_ker_le
    {Q : V →ₗ[R] W} {observation : V →ₗ[R] D}
    (factorization : FactorsThrough Q observation) :
    LinearMap.ker Q ≤ LinearMap.ker observation := by
  rintro x hx
  rcases factorization with ⟨induced, hfactor⟩
  change observation x = 0
  rw [← hfactor]
  have hQx : Q x = 0 := hx
  change induced (Q x) = 0
  rw [hQx, map_zero]

/-- Exact factorization criterion for a surjective presentation map. -/
theorem factorsThrough_iff_ker_le_of_surjective
    (Q : V →ₗ[R] W) (observation : V →ₗ[R] D)
    (surjective : Function.Surjective Q) :
    FactorsThrough Q observation ↔
      LinearMap.ker Q ≤ LinearMap.ker observation := by
  constructor
  · exact factorsThrough_implies_ker_le
  · intro hker
    let quotientObservation : (V ⧸ LinearMap.ker Q) →ₗ[R] D :=
      (LinearMap.ker Q).liftQ observation hker
    let presentation : (V ⧸ LinearMap.ker Q) ≃ₗ[R] W :=
      Q.quotKerEquivOfSurjective surjective
    refine ⟨quotientObservation.comp presentation.symm.toLinearMap, ?_⟩
    ext x
    simp [quotientObservation, presentation,
      LinearMap.quotKerEquivOfSurjective_symm_apply]

end General

section HostileIntegers

/-- The nonsurjective integer presentation `x ↦ 2x`. -/
def doubleIntegerMap : ℤ →ₗ[ℤ] ℤ where
  toFun x := 2 * x
  map_add' x y := by ring
  map_smul' a x := by simp [mul_comm, mul_assoc]

theorem doubleIntegerMap_ker_le_identity_ker :
    LinearMap.ker doubleIntegerMap ≤ LinearMap.ker (LinearMap.id : ℤ →ₗ[ℤ] ℤ) := by
  intro x hx
  simp only [LinearMap.mem_ker, LinearMap.id_apply]
  change 2 * x = 0 at hx
  omega

theorem doubleIntegerMap_not_surjective :
    ¬ Function.Surjective doubleIntegerMap := by
  intro h
  rcases h 1 with ⟨x, hx⟩
  change 2 * x = 1 at hx
  omega

/-- Kernel inclusion alone does not give factorization through a nonsurjective module map. -/
theorem kernel_inclusion_without_surjectivity_does_not_factor :
    LinearMap.ker doubleIntegerMap ≤
        LinearMap.ker (LinearMap.id : ℤ →ₗ[ℤ] ℤ) ∧
      ¬ FactorsThrough doubleIntegerMap (LinearMap.id : ℤ →ₗ[ℤ] ℤ) := by
  refine ⟨doubleIntegerMap_ker_le_identity_ker, ?_⟩
  rintro ⟨induced, hfactor⟩
  have hone := LinearMap.congr_fun hfactor 1
  change induced 2 = 1 at hone
  have hlinear := induced.map_smul 2 (1 : ℤ)
  norm_num at hlinear
  omega

end HostileIntegers
end MariciFormal
