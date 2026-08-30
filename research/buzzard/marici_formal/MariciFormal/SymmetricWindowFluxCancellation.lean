import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite algebraic core of Grothendieck's symmetric-window exterior-flux
cancellation. The analytic fourth-moment estimate is deliberately separate.
-/

namespace MariciFormal

open Finset
open scoped BigOperators

section PairRemainder

variable {K : Type*} [Field K]

def symmetricPairForce (root exterior : K) : K :=
  2 / (root - exterior) + 2 / (root + exterior)

def fourthMomentRemainder (root exterior : K) : K :=
  -4 * root ^ 3 / (exterior ^ 2 * (exterior ^ 2 - root ^ 2))

theorem symmetricPairForce_formula
    (root exterior : K) (hminus : root ≠ exterior)
    (hplus : root ≠ -exterior) :
    symmetricPairForce root exterior = 4 * root / (root ^ 2 - exterior ^ 2) := by
  unfold symmetricPairForce
  field_simp [hminus, hplus]
  ring

theorem symmetricPairForce_secondMoment_remainder
    (root exterior : K) (hexterior : exterior ≠ 0)
    (hgap : root ^ 2 ≠ exterior ^ 2) :
    4 * root / (root ^ 2 - exterior ^ 2) =
      -4 * (1 / exterior ^ 2) * root + fourthMomentRemainder root exterior := by
  unfold fourthMomentRemainder
  field_simp [hexterior, hgap]
  ring

end PairRemainder

section ExactCancellation

variable {K : Type*} [CommRing K]
variable {I : Type*}

/-- Finite coordinate pairing, kept explicit to avoid importing a norm. -/
def finitePairing (indices : Finset I) (u v : I → K) : K :=
  ∑ i ∈ indices, u i * v i

/-- The leading exterior field is a scalar multiple of the centered roots. -/
def leadingExteriorField (moment2 : K) (roots : I → K) (i : I) : K :=
  -4 * moment2 * roots i

theorem leadingExterior_cancels_of_scaleOrthogonal
    (indices : Finset I) (roots defect : I → K) (moment2 : K)
    (hscale : finitePairing indices roots defect = 0) :
    finitePairing indices (leadingExteriorField moment2 roots) defect = 0 := by
  unfold finitePairing leadingExteriorField at *
  calc
    ∑ i ∈ indices, (-4 * moment2 * roots i) * defect i =
        (-4 * moment2) * ∑ i ∈ indices, roots i * defect i := by
          rw [Finset.mul_sum]
          apply Finset.sum_congr rfl
          intro i hi
          ring
    _ = 0 := by rw [hscale, mul_zero]

theorem exteriorFlux_reduces_to_remainder
    (indices : Finset I) (roots defect remainder : I → K) (moment2 : K)
    (hscale : finitePairing indices roots defect = 0) :
    finitePairing indices
        (fun i => leadingExteriorField moment2 roots i + remainder i) defect =
      finitePairing indices remainder defect := by
  calc
    finitePairing indices
          (fun i => leadingExteriorField moment2 roots i + remainder i) defect =
        finitePairing indices (leadingExteriorField moment2 roots) defect +
          finitePairing indices remainder defect := by
            unfold finitePairing
            simp_rw [add_mul, sum_add_distrib]
    _ = finitePairing indices remainder defect := by
      rw [leadingExterior_cancels_of_scaleOrthogonal indices roots defect moment2 hscale,
        zero_add]

end ExactCancellation

/-- Without scale orthogonality, the leading second-moment field survives. -/
theorem missing_scaleOrthogonality_hostile :
    let indices : Finset (Fin 1) := Finset.univ
    let roots : Fin 1 → ℚ := fun _ => 1
    let defect : Fin 1 → ℚ := fun _ => 1
    finitePairing indices roots defect = 1 ∧
      finitePairing indices (leadingExteriorField 1 roots) defect = -4 := by
  norm_num [finitePairing, leadingExteriorField]

end MariciFormal
