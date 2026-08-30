import Mathlib

/-!
The algebraic consequence of Strominger's native first-order energy identity.
The identity itself remains explicit certificate data.
-/

namespace MariciFormal

/-- Nonnegative terms in the native first-order identity at fixed strip parameter. -/
structure FirstOrderEnergyCertificate where
  a : Real
  derivativeSq : Real
  bulkSq : Real
  endpointSq : Real
  energy : Real
  a_pos : 0 < a
  derivativeSq_nonneg : 0 ≤ derivativeSq
  bulkSq_nonneg : 0 ≤ bulkSq
  endpointSq_nonneg : 0 ≤ endpointSq
  identity : energy = derivativeSq + a ^ 2 * bulkSq + a * endpointSq

/-- The energy controls the boundary contribution with its exact coefficient. -/
theorem endpoint_term_le_energy (certificate : FirstOrderEnergyCertificate) :
    certificate.a * certificate.endpointSq ≤ certificate.energy := by
  rw [certificate.identity]
  have hbulkTerm : 0 ≤ certificate.a ^ 2 * certificate.bulkSq :=
    mul_nonneg (sq_nonneg certificate.a) certificate.bulkSq_nonneg
  linarith [certificate.derivativeSq_nonneg]

/-- At a fixed positive parameter, the endpoint square is controlled by `a⁻¹`. -/
theorem endpointSq_le_energy_div (certificate : FirstOrderEnergyCertificate) :
    certificate.endpointSq ≤ certificate.energy / certificate.a := by
  apply (le_div_iff₀ certificate.a_pos).2
  simpa [mul_comm] using endpoint_term_le_energy certificate

/-- On a region `a ≥ delta > 0`, one uniform constant `delta⁻¹` suffices. -/
theorem endpointSq_le_energy_div_delta
    (certificate : FirstOrderEnergyCertificate)
    {delta : Real} (delta_pos : 0 < delta) (region : delta ≤ certificate.a) :
    certificate.endpointSq ≤ certificate.energy / delta := by
  apply (le_div_iff₀ delta_pos).2
  have endpointScaled : delta * certificate.endpointSq ≤
      certificate.a * certificate.endpointSq := by
    exact mul_le_mul_of_nonneg_right region certificate.endpointSq_nonneg
  simpa [mul_comm] using
    endpointScaled.trans (endpoint_term_le_energy certificate)

/-- Boundary-degeneration fixture: all energy is the endpoint term. -/
def boundaryCertificate (a : Real) (ha : 0 < a) : FirstOrderEnergyCertificate where
  a := a
  derivativeSq := 0
  bulkSq := 0
  endpointSq := 1
  energy := a
  a_pos := ha
  derivativeSq_nonneg := by norm_num
  bulkSq_nonneg := by norm_num
  endpointSq_nonneg := by norm_num
  identity := by ring

/-- Without a positive lower bound on `a`, no finite uniform endpoint constant follows. -/
theorem no_uniform_endpoint_constant_at_boundary :
    ∀ K : Real, 0 ≤ K →
      ∃ certificate : FirstOrderEnergyCertificate,
        K * certificate.energy < certificate.endpointSq := by
  intro K hK
  have hdenom : 0 < K + 1 := by linarith
  let a : Real := 1 / (K + 1)
  have ha : 0 < a := by
    dsimp [a]
    positivity
  refine ⟨boundaryCertificate a ha, ?_⟩
  change K * a < 1
  dsimp [a]
  have hquot : K / (K + 1) < 1 :=
    (div_lt_one hdenom).2 (by linarith)
  simpa [div_eq_mul_inv] using hquot

end MariciFormal
