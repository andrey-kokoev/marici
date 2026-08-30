import MariciFormal.FiniteInstrumentReadout

/-!
Finite source-typing obstruction to reconstructing a richer readout from a
coarser sampling map.  The theorem is shared by Grothendieck's prime-seam
projection and finite optical sampling aliases.
-/

namespace MariciFormal.FiniteSamplingFactorization

variable {F V W R : Type*}
  [Field F] [AddCommGroup V] [Module F V]
  [AddCommGroup W] [Module F W]
  [AddCommGroup R] [Module F R]

/-- A source variation killed by sampling but detected by the richer readout
rules out every linear factorization of that readout through sampling. -/
theorem no_factorization_of_kernel_witness
    (sampling : V →ₗ[F] W) (readout : V →ₗ[F] R) (variation : V)
    (samplingInvisible : sampling variation = 0)
    (readoutVisible : readout variation ≠ 0) :
    ¬ ∃ interpolation : W →ₗ[F] R,
      readout = interpolation.comp sampling := by
  rintro ⟨interpolation, factorization⟩
  have detected := LinearMap.congr_fun factorization variation
  simp [samplingInvisible] at detected
  exact readoutVisible detected

/-- Exact two-coordinate sampling projection. -/
def seamSampling : (Fin 2 → ℚ) →ₗ[ℚ] ℚ where
  toFun source := source 0
  map_add' := by intros; simp
  map_smul' := by intros; simp

/-- Exact two-coordinate readout sensitive to the unsampled gap. -/
def gapSensitiveReadout : (Fin 2 → ℚ) →ₗ[ℚ] ℚ where
  toFun source := source 1
  map_add' := by intros; simp
  map_smul' := by intros; simp

def gapVariation : Fin 2 → ℚ
  | 0 => 0
  | 1 => 1

theorem gapVariation_samplingInvisible : seamSampling gapVariation = 0 := by
  rfl

theorem gapVariation_readoutVisible : gapSensitiveReadout gapVariation ≠ 0 := by
  norm_num [gapSensitiveReadout, gapVariation]

/-- Grothendieck's finite hostile fixture: the gap-sensitive source readout
cannot be reconstructed from the seam sample. -/
theorem gapSensitiveReadout_not_factor_through_seamSampling :
    ¬ ∃ interpolation : ℚ →ₗ[ℚ] ℚ,
      gapSensitiveReadout = interpolation.comp seamSampling :=
  no_factorization_of_kernel_witness seamSampling gapSensitiveReadout
    gapVariation gapVariation_samplingInvisible gapVariation_readoutVisible

end MariciFormal.FiniteSamplingFactorization
