import Mathlib.Tactic

/-!
Finite exponent-classification core of Grothendieck's higher-contact Hermite
profile theorem. Backward heat asymptotics and Hermite sign intervals are external.
-/

namespace MariciFormal

def evenContactOrder (multiplicity : ℕ) : ℕ := 2 * multiplicity

def hermiteNegativeMassExponent (multiplicity : ℕ) : ℚ :=
  multiplicity + 1 / 2

def exponentFromContactOrder (order : ℕ) : ℚ :=
  (order + 1) / 2

theorem exponentFrom_evenContactOrder (multiplicity : ℕ) :
    exponentFromContactOrder (evenContactOrder multiplicity) =
      hermiteNegativeMassExponent multiplicity := by
  simp [exponentFromContactOrder, evenContactOrder,
    hermiteNegativeMassExponent]
  ring

/-- The scaling exponent faithfully records the even contact multiplicity. -/
theorem hermiteNegativeMassExponent_injective :
    Function.Injective hermiteNegativeMassExponent := by
  intro first second heq
  simp only [hermiteNegativeMassExponent] at heq
  have hrat : (first : ℚ) = second := by linarith
  exact_mod_cast hrat

theorem generic_quadratic_contact_exponent :
    hermiteNegativeMassExponent 1 = 3 / 2 := by
  norm_num [hermiteNegativeMassExponent]

theorem quartic_contact_exponent :
    hermiteNegativeMassExponent 2 = 5 / 2 := by
  norm_num [hermiteNegativeMassExponent]

theorem sextic_contact_exponent :
    hermiteNegativeMassExponent 3 = 7 / 2 := by
  norm_num [hermiteNegativeMassExponent]

/-- The universal exponent is not sector authority: distinct sectors with
the same contact multiplicity receive the same classifier value. -/
def boolSectorMultiplicity (_ : Bool) : ℕ := 1

theorem distinctSectors_same_contactExponent_hostile :
    false ≠ true ∧
      hermiteNegativeMassExponent (boolSectorMultiplicity false) =
        hermiteNegativeMassExponent (boolSectorMultiplicity true) := by
  decide

end MariciFormal
