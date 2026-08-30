import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Data.Matrix.Notation
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite determinant core of Grothendieck's conjugation-graph
determinant-class gate. Infinite Schatten claims are not imported.
-/

namespace MariciFormal

open Finset Matrix
open scoped BigOperators

section SingleBlock

variable {R : Type*} [CommRing R]

def swapBlockPencil (spectral weight : R) : Matrix (Fin 2) (Fin 2) R :=
  !![1, -(spectral * weight);
     -(spectral * weight), 1]

theorem swapBlockPencil_det (spectral weight : R) :
    (swapBlockPencil spectral weight).det =
      1 - (spectral * weight) ^ 2 := by
  simp [swapBlockPencil, Matrix.det_fin_two]
  ring

end SingleBlock

section FiniteCutoff

variable {R : Type*} [CommRing R]
variable {I : Type*}

def finiteSwapBlockDeterminant
    (indices : Finset I) (spectral : R) (weight : I → R) : R :=
  ∏ i ∈ indices, (swapBlockPencil spectral (weight i)).det

theorem finiteSwapBlockDeterminant_factorization
    (indices : Finset I) (spectral : R) (weight : I → R) :
    finiteSwapBlockDeterminant indices spectral weight =
      ∏ i ∈ indices, (1 - (spectral * weight i) ^ 2) := by
  classical
  unfold finiteSwapBlockDeterminant
  apply Finset.prod_congr rfl
  intro i hi
  exact swapBlockPencil_det spectral (weight i)

theorem unweightedSwapBlockDeterminant_power
    (indices : Finset I) (spectral : R) :
    finiteSwapBlockDeterminant indices spectral (fun _ => 1) =
      (1 - spectral ^ 2) ^ indices.card := by
  classical
  rw [finiteSwapBlockDeterminant_factorization]
  simp

end FiniteCutoff

/-- At spectral parameter `2`, the one-block and two-block unweighted
determinants are `-3` and `9`; cutoff determinants do not stabilize even at
the first extension. -/
theorem unweighted_cutoff_nonstabilization_hostile :
    finiteSwapBlockDeterminant (R := ℤ) ({0} : Finset (Fin 2)) 2 (fun _ => 1) = -3 ∧
      finiteSwapBlockDeterminant (R := ℤ) ({0, 1} : Finset (Fin 2)) 2
        (fun _ => 1) = 9 := by
  norm_num [finiteSwapBlockDeterminant, swapBlockPencil, Matrix.det_fin_two]

end MariciFormal
