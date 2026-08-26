import Mathlib.Algebra.Field.GeomSum
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.NormNum

/-!
Scalar geometric-sum mechanism behind Grothendieck's cyclic and finite
monodromy Adams-spectrum theorems.
-/

namespace MariciFormal

open Finset
open scoped BigOperators

def scalarGeometricSum {R : Type*} [Semiring R] (eigenvalue : R) (index : ℕ) : R :=
  ∑ k ∈ Finset.range index, eigenvalue ^ k

section RingIdentities

variable {R : Type*} [CommRing R]

theorem scalarGeometricSum_mul_sub_one
    (eigenvalue : R) (index : ℕ) :
    scalarGeometricSum eigenvalue index * (eigenvalue - 1) =
      eigenvalue ^ index - 1 := by
  exact geom_sum_mul eigenvalue index

theorem scalarGeometricSum_at_one (index : ℕ) :
    scalarGeometricSum (1 : R) index = index := by
  simp [scalarGeometricSum]

theorem scalarGeometricSum_zero_implies_pow_eq_one
    (eigenvalue : R) (index : ℕ)
    (hzero : scalarGeometricSum eigenvalue index = 0) :
    eigenvalue ^ index = 1 := by
  have h := scalarGeometricSum_mul_sub_one eigenvalue index
  rw [hzero, zero_mul] at h
  exact sub_eq_zero.mp h.symm

end RingIdentities

section FieldClassification

variable {K : Type*} [Field K]

theorem nontrivial_rootOfUnity_geometricSum_zero
    (eigenvalue : K) (index : ℕ)
    (hnontrivial : eigenvalue ≠ 1) (hroot : eigenvalue ^ index = 1) :
    scalarGeometricSum eigenvalue index = 0 := by
  have h := scalarGeometricSum_mul_sub_one eigenvalue index
  rw [hroot, sub_self] at h
  exact (mul_eq_zero.mp h).resolve_right (sub_ne_zero.mpr hnontrivial)

theorem scalarGeometricSum_zero_iff_characteristic_or_root
    (eigenvalue : K) (index : ℕ) :
    scalarGeometricSum eigenvalue index = 0 ↔
      (eigenvalue = 1 ∧ (index : K) = 0) ∨
        (eigenvalue ≠ 1 ∧ eigenvalue ^ index = 1) := by
  by_cases hone : eigenvalue = 1
  · subst eigenvalue
    simp [scalarGeometricSum_at_one]
  · constructor
    · intro hzero
      exact Or.inr ⟨hone,
        scalarGeometricSum_zero_implies_pow_eq_one eigenvalue index hzero⟩
    · rintro (⟨hfalse, _⟩ | ⟨_, hroot⟩)
      · exact (hone hfalse).elim
      · exact nontrivial_rootOfUnity_geometricSum_zero eigenvalue index hone hroot

end FieldClassification

theorem characteristic_and_rootOfUnity_hostiles :
    scalarGeometricSum (1 : ZMod 2) 2 = 0 ∧
      scalarGeometricSum (-1 : ZMod 5) 2 = 0 ∧
      (-1 : ZMod 5) ≠ 1 := by
  norm_num [scalarGeometricSum]

end MariciFormal
