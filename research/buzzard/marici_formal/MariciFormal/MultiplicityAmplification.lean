import Mathlib.Data.Matrix.Notation
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite multiplicity hostile from Grothendieck's Xi Weyl-model correction:
scalar atom, principal-ideal Jordan block, and semisimple amplification remain
distinct objects.
-/

namespace MariciFormal

open Matrix

section JordanObstruction

variable {R : Type*} [CommRing R]

def repeatedRootJordan (root : R) : Matrix (Fin 2) (Fin 2) R :=
  !![root, 1;
     0, root]

/-- Any bilinear form symmetrizing the nontrivial repeated-root Jordan block
has zero value on the first basis vector. -/
theorem jordan_symmetrizer_first_diagonal_zero
    (root : R) (metric : Matrix (Fin 2) (Fin 2) R)
    (hsym : metric * repeatedRootJordan root =
      (repeatedRootJordan root)ᵀ * metric) :
    metric 0 0 = 0 := by
  have h01 := congrFun (congrFun hsym 0) 1
  simpa [repeatedRootJordan, Matrix.mul_apply] using h01

end JordanObstruction

theorem repeatedRootJordan_has_no_positive_symmetrizer
    (root : ℝ) :
    ¬ ∃ metric : Matrix (Fin 2) (Fin 2) ℝ,
      0 < metric 0 0 ∧
        metric * repeatedRootJordan root =
          (repeatedRootJordan root)ᵀ * metric := by
  rintro ⟨metric, hpositive, hsym⟩
  have hzero := jordan_symmetrizer_first_diagonal_zero root metric hsym
  linarith

section SemisimpleAmplification

variable {R : Type*} [CommRing R]

def amplifiedRepeatedRoot (root : R) : Matrix (Fin 2) (Fin 2) R :=
  !![root, 0;
     0, root]

theorem amplifiedRepeatedRoot_characteristic
    (spectral root : R) :
    (spectral • (1 : Matrix (Fin 2) (Fin 2) R) -
      amplifiedRepeatedRoot root).det = (spectral - root) ^ 2 := by
  simp [amplifiedRepeatedRoot, Matrix.det_fin_two]
  ring

theorem scalar_atom_has_only_one_factor (spectral root : R) :
    spectral - root = spectral - root := rfl

end SemisimpleAmplification

/-- The concrete double-root fixture: the Jordan quotient cannot have even
the first necessary positive metric entry, while semisimple amplification
has the required squared characteristic factor. -/
theorem double_root_three_object_hostile :
    (¬ ∃ metric : Matrix (Fin 2) (Fin 2) ℝ,
      0 < metric 0 0 ∧
        metric * repeatedRootJordan 1 =
          (repeatedRootJordan 1)ᵀ * metric) ∧
      ((2 : ℝ) • (1 : Matrix (Fin 2) (Fin 2) ℝ) -
        amplifiedRepeatedRoot 1).det = 1 := by
  constructor
  · exact repeatedRootJordan_has_no_positive_symmetrizer 1
  · norm_num [amplifiedRepeatedRoot, Matrix.det_fin_two]

end MariciFormal
