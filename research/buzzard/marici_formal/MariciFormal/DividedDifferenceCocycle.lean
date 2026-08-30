import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite multiplicative core of Grothendieck's Newman divided-difference
entropy cocycle. Logarithms and differentiable root motion are not inputs.
-/

namespace MariciFormal

open Finset
open scoped BigOperators

section PairCocycle

variable {K : Type*} [Field K]

def pairDividedDifference (f : K → K) (x y : K) : K :=
  (f x - f y) / (x - y)

theorem pairDividedDifference_comp
    (f g : K → K) (x y : K) (hxy : x ≠ y) (hf : f x ≠ f y) :
    pairDividedDifference (g ∘ f) x y =
      pairDividedDifference g (f x) (f y) * pairDividedDifference f x y := by
  unfold pairDividedDifference Function.comp
  field_simp [hxy, hf]
  ring

theorem pairDividedDifference_affine
    (slope intercept x y : K) (hxy : x ≠ y) :
    pairDividedDifference (fun t => slope * t + intercept) x y = slope := by
  unfold pairDividedDifference
  field_simp [hxy]
  ring

end PairCocycle

section FiniteProduct

variable {K : Type*} [Field K]
variable {ι : Type*}

noncomputable def finiteDividedDifferenceProduct
    (indices : Finset ι) (left right : ι → K) (f : K → K) : K :=
  ∏ i ∈ indices, pairDividedDifference f (left i) (right i)

theorem finiteDividedDifferenceProduct_comp
    (indices : Finset ι) (left right : ι → K) (f g : K → K)
    (hpair : ∀ i ∈ indices, left i ≠ right i)
    (himage : ∀ i ∈ indices, f (left i) ≠ f (right i)) :
    finiteDividedDifferenceProduct indices left right (g ∘ f) =
      finiteDividedDifferenceProduct indices (fun i => f (left i))
          (fun i => f (right i)) g *
        finiteDividedDifferenceProduct indices left right f := by
  classical
  unfold finiteDividedDifferenceProduct
  rw [← prod_mul_distrib]
  apply prod_congr rfl
  intro i hi
  exact pairDividedDifference_comp f g (left i) (right i)
    (hpair i hi) (himage i hi)

theorem finiteDividedDifferenceProduct_affine
    (indices : Finset ι) (left right : ι → K) (slope intercept : K)
    (hpair : ∀ i ∈ indices, left i ≠ right i) :
    finiteDividedDifferenceProduct indices left right
        (fun t => slope * t + intercept) = slope ^ indices.card := by
  classical
  unfold finiteDividedDifferenceProduct
  calc
    ∏ i ∈ indices,
        pairDividedDifference (fun t => slope * t + intercept) (left i) (right i) =
        ∏ _i ∈ indices, slope := by
          apply prod_congr rfl
          intro i hi
          exact pairDividedDifference_affine slope intercept (left i) (right i)
            (hpair i hi)
    _ = slope ^ indices.card := by simp

end FiniteProduct

/-- A nonlinear coordinate already produces a non-unit pair correction. -/
theorem square_coordinate_nontrivial_cocycle_hostile :
    pairDividedDifference (K := ℚ) (fun t => t ^ 2) 2 1 = 3 ∧
      pairDividedDifference (K := ℚ) (fun t => t) 2 1 = 1 := by
  norm_num [pairDividedDifference]

end MariciFormal
