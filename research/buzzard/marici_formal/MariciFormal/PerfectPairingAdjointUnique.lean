/-!
Minimal type-theoretic core of Grothendieck's theorem that a perfect target
pairing forces at most one Betti pushforward adjoint to a supplied coefficient
pullback. Linearity, chain compatibility, and physical realization are
separate interfaces.
-/

namespace MariciFormal

/-- Right nondegeneracy is the exact property needed to distinguish target
Betti vectors by all coefficient probes. -/
def RightNondegenerate {Coefficient Betti Scalar : Type*}
    (pairing : Coefficient → Betti → Scalar) : Prop :=
  ∀ left right,
    (∀ coefficient, pairing coefficient left = pairing coefficient right) →
      left = right

/-- Two Betti maps adjoint to the same coefficient pullback coincide when
the target pairing is right-nondegenerate. -/
theorem adjoint_betti_map_unique
    {CoefficientSource CoefficientTarget BettiSource BettiTarget Scalar : Type*}
    (sourcePairing : CoefficientSource → BettiSource → Scalar)
    (targetPairing : CoefficientTarget → BettiTarget → Scalar)
    (coefficientPullback : CoefficientTarget → CoefficientSource)
    (left right : BettiSource → BettiTarget)
    (hnondegenerate : RightNondegenerate targetPairing)
    (hleft : ∀ coefficient betti,
      sourcePairing (coefficientPullback coefficient) betti =
        targetPairing coefficient (left betti))
    (hright : ∀ coefficient betti,
      sourcePairing (coefficientPullback coefficient) betti =
        targetPairing coefficient (right betti)) :
    left = right := by
  funext betti
  apply hnondegenerate
  intro coefficient
  exact (hleft coefficient betti).symm.trans (hright coefficient betti)

/-- Adjoint assignments compose contravariantly on coefficient maps and
covariantly on Betti maps, purely by substitution. -/
theorem composed_adjoint_identity
    {C₁ C₂ C₃ B₁ B₂ B₃ R : Type*}
    (pair₁ : C₁ → B₁ → R) (pair₂ : C₂ → B₂ → R)
    (pair₃ : C₃ → B₃ → R)
    (pull₁₂ : C₂ → C₁) (pull₂₃ : C₃ → C₂)
    (push₁₂ : B₁ → B₂) (push₂₃ : B₂ → B₃)
    (hadjoint₁₂ : ∀ c b,
      pair₁ (pull₁₂ c) b = pair₂ c (push₁₂ b))
    (hadjoint₂₃ : ∀ c b,
      pair₂ (pull₂₃ c) b = pair₃ c (push₂₃ b)) :
    ∀ c b,
      pair₁ (pull₁₂ (pull₂₃ c)) b =
        pair₃ c (push₂₃ (push₁₂ b)) := by
  intro c b
  exact (hadjoint₁₂ (pull₂₃ c) b).trans
    (hadjoint₂₃ c (push₁₂ b))

end MariciFormal
