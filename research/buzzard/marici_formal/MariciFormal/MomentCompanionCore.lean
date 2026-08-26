import Mathlib.RingTheory.Polynomial.Basic
import Mathlib.Tactic.Ring

/-!
Arbitrary-degree algebraic core of Grothendieck's Hermite companion symmetry.
A coefficient moment functional makes polynomial multiplication symmetric.
Descent to a finite companion quotient additionally requires annihilation of
the defining ideal.
-/

namespace MariciFormal

open Polynomial

section MomentSymmetry

variable {R : Type*} [CommRing R]

def polynomialMomentForm
    (moment : Polynomial R →+ R) (p q : Polynomial R) : R :=
  moment (p * q)

/-- Multiplication by any polynomial, hence in particular by `X`, is symmetric
for a moment form before quotienting. -/
theorem polynomialMultiplication_symmetric_for_momentForm
    (moment : Polynomial R →+ R) (multiplier p q : Polynomial R) :
    polynomialMomentForm moment p (multiplier * q) =
      polynomialMomentForm moment (multiplier * p) q := by
  simp [polynomialMomentForm, mul_assoc, mul_left_comm]

theorem multiplicationByX_symmetric_for_momentForm
    (moment : Polynomial R →+ R) (p q : Polynomial R) :
    polynomialMomentForm moment p (X * q) =
      polynomialMomentForm moment (X * p) q :=
  polynomialMultiplication_symmetric_for_momentForm moment X p q

def CongruentMod (generator p q : Polynomial R) : Prop :=
  ∃ r, p - q = generator * r

def AnnihilatesPrincipalIdeal
    (moment : Polynomial R →+ R) (generator : Polynomial R) : Prop :=
  ∀ r, moment (generator * r) = 0

/-- Ideal annihilation is the exact extra condition needed for a moment
functional to be independent of representatives modulo the companion
polynomial. -/
theorem moment_eq_of_congruentMod
    (moment : Polynomial R →+ R) (generator p q : Polynomial R)
    (hannihilates : AnnihilatesPrincipalIdeal moment generator)
    (hcongruent : CongruentMod generator p q) :
    moment p = moment q := by
  obtain ⟨r, hr⟩ := hcongruent
  have hzero : moment (p - q) = 0 := by
    rw [hr]
    exact hannihilates r
  apply sub_eq_zero.mp
  simpa using hzero

end MomentSymmetry

section QuotientDescentHostile

def hostileQuadratic : Polynomial ℤ := X ^ 2 + 1

theorem hostileQuadratic_congruent_zero :
    CongruentMod hostileQuadratic hostileQuadratic 0 := by
  refine ⟨1, ?_⟩
  simp [hostileQuadratic]

/-- Constant-coefficient readout does not descend modulo `X²+1`: congruent
representatives can have different readout. -/
theorem constantCoefficient_does_not_respect_hostileCongruence :
    hostileQuadratic.coeff 0 ≠ (0 : Polynomial ℤ).coeff 0 := by
  norm_num [hostileQuadratic]

end QuotientDescentHostile

end MariciFormal
