import Mathlib.NumberTheory.Prime.Basic
import Mathlib.Tactic

/-!
Finite label-level core of Grothendieck's prime multiplication/division
curvature.  Hilbert completion and Gaussian orbit realization are external.
-/

namespace MariciFormal

def multiplyLabel (p n : ℕ) : ℕ := p * n

def divideLabel (p n : ℕ) : Option ℕ :=
  if p ∣ n then some (n / p) else none

def divisionAfterMultiplication (p n : ℕ) : Option ℕ :=
  divideLabel p (multiplyLabel p n)

def multiplicationAfterDivision (p n : ℕ) : Option ℕ :=
  (divideLabel p n).map (multiplyLabel p)

theorem divisionAfterMultiplication_eq
    (p n : ℕ) (hp : 0 < p) :
    divisionAfterMultiplication p n = some n := by
  simp [divisionAfterMultiplication, divideLabel, multiplyLabel, hp]

theorem multiplicationAfterDivision_eq
    (p n : ℕ) :
    multiplicationAfterDivision p n = if p ∣ n then some n else none := by
  by_cases hdiv : p ∣ n
  · rw [if_pos hdiv]
    simp [multiplicationAfterDivision, divideLabel, hdiv, multiplyLabel,
      Nat.mul_div_cancel' hdiv]
  · rw [if_neg hdiv]
    simp [multiplicationAfterDivision, divideLabel, hdiv]

def PrimeDivisionCurvatureAt (p n : ℕ) : Prop :=
  divisionAfterMultiplication p n ≠ multiplicationAfterDivision p n

/-- The mixed-square residual is supported exactly on labels excluded from
the range of multiplication by `p`. -/
theorem primeDivisionCurvature_iff_not_dvd
    (p n : ℕ) (hp : 0 < p) :
    PrimeDivisionCurvatureAt p n ↔ ¬ p ∣ n := by
  rw [PrimeDivisionCurvatureAt, divisionAfterMultiplication_eq p n hp,
    multiplicationAfterDivision_eq]
  by_cases hdiv : p ∣ n <;> simp [hdiv]

def ExclusionAnnihilated {R : Type*} [Zero R]
    (coefficient : ℕ → R) (p : ℕ) : Prop :=
  ∀ n, ¬ p ∣ n → coefficient n = 0

/-- All prime-exclusion ports are jointly faithful on positive integer labels.
The zero label is deliberately excluded because every prime divides zero. -/
theorem allPrimeExclusions_jointlyFaithful
    {R : Type*} [Zero R] (coefficient : ℕ → R)
    (hannihilated : ∀ p, p.Prime → ExclusionAnnihilated coefficient p) :
    ∀ n, 0 < n → coefficient n = 0 := by
  intro n hn
  obtain ⟨p, hpLower, hpPrime⟩ := Nat.exists_infinite_primes (n + 1)
  apply hannihilated p hpPrime n
  intro hpDvd
  have hpUpper : p ≤ n := Nat.le_of_dvd hn hpDvd
  omega

/-- Every prime exclusion reads the vacuum label `1`. -/
theorem prime_exclusion_reads_vacuum
    (p : ℕ) (hp : p.Prime) : ¬ p ∣ 1 := by
  intro hdiv
  exact hp.ne_one (Nat.dvd_one.mp hdiv)

/-- A packet with nonzero vacuum coefficient cannot be annihilated by even
one prime-exclusion port. -/
theorem nonzero_vacuum_hostile
    {R : Type*} [Zero R] (coefficient : ℕ → R)
    (hvacuum : coefficient 1 ≠ 0) (p : ℕ) (hp : p.Prime) :
    ¬ ExclusionAnnihilated coefficient p := by
  intro hannihilated
  exact hvacuum (hannihilated 1 (prime_exclusion_reads_vacuum p hp))

end MariciFormal
