import Mathlib

/-!
Exact coupling algebra for the degree-two Li jet.

The endpoint, gamma, and Abel-renormalized prime germs are inputs.  This file
proves their polarization identity but does not derive those germs from xi or
claim that any self-piece or cross-piece is separately positive.
-/

namespace MariciFormal

section DegreeTwoJet

variable {K : Type*} [Field K] [CharZero K]

abbrev LiThreeJet (K : Type*) := Fin 3 → K

def liOddChannelFromJet (a : LiThreeJet K) : K :=
  a 0 - a 1 - 3 * a 2 / 2

def liCoupledDeterminantFromJet (a : LiThreeJet K) : K :=
  a 0 ^ 2 + a 0 * a 1 + 3 * a 0 * a 2 / 2 - 2 * a 1 ^ 2

def liCouplingPolarization (x y : LiThreeJet K) : K :=
  2 * x 0 * y 0 + x 0 * y 1 + x 1 * y 0 +
    3 * (x 0 * y 2 + x 2 * y 0) / 2 - 4 * x 1 * y 1

theorem liCoupledDeterminant_add
    (x y : LiThreeJet K) :
    liCoupledDeterminantFromJet (x + y) =
      liCoupledDeterminantFromJet x + liCoupledDeterminantFromJet y +
        liCouplingPolarization x y := by
  simp [liCoupledDeterminantFromJet, liCouplingPolarization]
  ring

theorem liCoupledDeterminant_threeSector
    (endpoint gamma prime : LiThreeJet K) :
    liCoupledDeterminantFromJet (endpoint + gamma + prime) =
      liCoupledDeterminantFromJet endpoint +
      liCoupledDeterminantFromJet gamma +
      liCoupledDeterminantFromJet prime +
      liCouplingPolarization endpoint gamma +
      liCouplingPolarization endpoint prime +
      liCouplingPolarization gamma prime := by
  simp [liCoupledDeterminantFromJet, liCouplingPolarization]
  ring

/-- A sector can have negative self-energy while the completed coupled jet is
positive; separate sectorwise positivity is not necessary. -/
theorem liCoupling_hostile_mixedSigns :
    let endpoint : LiThreeJet Rat := ![1, 0, 0]
    let prime : LiThreeJet Rat := ![0, 1, 0]
    liCoupledDeterminantFromJet endpoint = 1 ∧
      liCoupledDeterminantFromJet prime = -2 ∧
      liCoupledDeterminantFromJet (endpoint + prime) = 0 := by
  norm_num [liCoupledDeterminantFromJet]

/-- The paired Li contribution factors algebraically.  Interpreting the
second factor as a conjugate, hence the product as a squared norm, requires
the additional unitary-phase condition. -/
theorem liPairEnergy_factorization
    (u : K) (hu : u ≠ 0) (n : Nat) :
    2 - u ^ n - (u⁻¹) ^ n =
      (1 - u ^ n) * (1 - (u⁻¹) ^ n) := by
  have hunit : u ^ n * (u⁻¹) ^ n = 1 := by
    rw [← mul_pow, mul_inv_cancel₀ hu, one_pow]
  calc
    2 - u ^ n - (u⁻¹) ^ n =
        1 - u ^ n - (u⁻¹) ^ n + u ^ n * (u⁻¹) ^ n := by rw [hunit]; ring
    _ = (1 - u ^ n) * (1 - (u⁻¹) ^ n) := by ring

end DegreeTwoJet

end MariciFormal
