import MariciFormal.JetAtlas

/-!
Parity constraints on central jets under an explicit evenness interface.
-/

namespace MariciFormal

section Parity

variable {K : Type*} [Field K]

/-- Coefficient-level content of evenness around a reflection-fixed point. -/
def EvenJet (jet : Nat → K) : Prop :=
  ∀ n, Odd n → jet n = 0

/-- The first nonzero coefficient of an even jet family has even index. -/
theorem firstNonzeroAt_even_of_evenJet
    {jet : Nat → K} {m : Nat}
    (symmetric : EvenJet jet) (first : FirstNonzeroAt jet m) :
    Even m := by
  rcases Nat.even_or_odd m with hm | hm
  · exact hm
  · exact False.elim (first.2 (symmetric m hm))

end Parity

section UnboundedEvenOrder

/-- A formal central jet with exactly one nonzero coefficient. -/
def centralMonomialJet (m : Nat) : Nat → Rat := fun n =>
  if n = m then 1 else 0

theorem centralMonomialJet_first_nonzero (m : Nat) :
    FirstNonzeroAt (centralMonomialJet m) m := by
  constructor
  · intro n hn
    simp [centralMonomialJet, Nat.ne_of_lt hn]
  · simp [centralMonomialJet]

theorem centralMonomialJet_even (m : Nat) (hm : Even m) :
    EvenJet (centralMonomialJet m) := by
  intro n hn
  have hne : n ≠ m := by
    rintro rfl
    rcases hm with ⟨a, ha⟩
    rcases hn with ⟨b, hb⟩
    omega
  simp [centralMonomialJet, hne]

/-- Reflection parity constrains order but supplies no uniform even-order bound. -/
theorem evenFirstNonzeroOrdersAreUnbounded :
    ∀ d : Nat, ∃ jet : Nat → Rat, ∃ m : Nat,
      d < m ∧ EvenJet jet ∧ FirstNonzeroAt jet m := by
  intro d
  let m := 2 * (d + 1)
  refine ⟨centralMonomialJet m, m, ?_, ?_, centralMonomialJet_first_nonzero m⟩
  · dsimp [m]
    omega
  · apply centralMonomialJet_even
    exact ⟨d + 1, by simp [m, two_mul]⟩

end UnboundedEvenOrder

end MariciFormal
