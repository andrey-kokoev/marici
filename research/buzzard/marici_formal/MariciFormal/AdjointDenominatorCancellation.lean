import Mathlib.Data.Rat.Defs
import Mathlib.Tactic

/-!
Rank-one arithmetic core of Grothendieck's adjoint-denominator composition
packet. Pairing lattices and higher-rank Smith data are not inferred here.
-/

namespace MariciFormal

/-- An integer clears a rational scalar when multiplication lands in the
embedded integers. -/
def ClearsRationalDenominator (denominator : ℤ) (scalar : ℚ) : Prop :=
  ∃ integral : ℤ, (denominator : ℚ) * scalar = integral

/-- A least positive clearing denominator, characterized by its universal
divisibility property. -/
structure LeastRationalDenominator (denominator : ℤ) (scalar : ℚ) : Prop where
  positive : 0 < denominator
  clears : ClearsRationalDenominator denominator scalar
  divides_every_clearer : ∀ other : ℤ,
    ClearsRationalDenominator other scalar → denominator ∣ other

/-- Clearing denominators is submultiplicative under scalar composition. -/
theorem clearsRationalDenominator_mul
    {leftDenominator rightDenominator : ℤ} {left right : ℚ}
    (hleft : ClearsRationalDenominator leftDenominator left)
    (hright : ClearsRationalDenominator rightDenominator right) :
    ClearsRationalDenominator (leftDenominator * rightDenominator)
      (left * right) := by
  rcases hleft with ⟨leftIntegral, hleft⟩
  rcases hright with ⟨rightIntegral, hright⟩
  refine ⟨leftIntegral * rightIntegral, ?_⟩
  rw [Int.cast_mul]
  calc
    ((leftDenominator : ℚ) * (rightDenominator : ℚ)) * (left * right) =
        ((leftDenominator : ℚ) * left) *
          ((rightDenominator : ℚ) * right) := by ring
    _ = (leftIntegral : ℚ) * (rightIntegral : ℚ) := by rw [hleft, hright]
    _ = ((leftIntegral * rightIntegral : ℤ) : ℚ) := by norm_num

/-- Therefore the least denominator of a composite divides the product of
the two stage denominators. -/
theorem leastRationalDenominator_mul_dvd
    {leftDenominator rightDenominator compositeDenominator : ℤ}
    {left right : ℚ}
    (hleft : LeastRationalDenominator leftDenominator left)
    (hright : LeastRationalDenominator rightDenominator right)
    (hcomposite : LeastRationalDenominator compositeDenominator (left * right)) :
    compositeDenominator ∣ leftDenominator * rightDenominator := by
  exact hcomposite.divides_every_clearer _
    (clearsRationalDenominator_mul hleft.clears hright.clears)

theorem twoThirds_leastRationalDenominator :
    LeastRationalDenominator 3 (2 / 3 : ℚ) := by
  refine ⟨by norm_num, ⟨2, by norm_num⟩, ?_⟩
  intro other hother
  rcases hother with ⟨integral, hintegral⟩
  have hrational : (2 : ℚ) * (other : ℚ) = 3 * (integral : ℚ) := by
    rw [← hintegral]
    ring
  have hinteger : 2 * other = 3 * integral := by exact_mod_cast hrational
  omega

theorem threeHalves_leastRationalDenominator :
    LeastRationalDenominator 2 (3 / 2 : ℚ) := by
  refine ⟨by norm_num, ⟨3, by norm_num⟩, ?_⟩
  intro other hother
  rcases hother with ⟨integral, hintegral⟩
  have hrational : (3 : ℚ) * (other : ℚ) = 2 * (integral : ℚ) := by
    rw [← hintegral]
    ring
  have hinteger : 3 * other = 2 * integral := by exact_mod_cast hrational
  omega

theorem one_leastRationalDenominator :
    LeastRationalDenominator 1 (1 : ℚ) := by
  refine ⟨by norm_num, ⟨1, by norm_num⟩, ?_⟩
  intro other _
  exact one_dvd other

/-- The rank-one pairing-lattice fixture from the source packet: both stage
adjoints are nonintegral, but their composite is the integral identity. -/
theorem rankOne_adjoint_denominator_cancellation :
    let stageQ : ℚ := 2 / 3
    let stageR : ℚ := 3 / 2
    ClearsRationalDenominator 3 stageQ ∧
      ClearsRationalDenominator 2 stageR ∧
      ¬ ClearsRationalDenominator 1 stageQ ∧
      ¬ ClearsRationalDenominator 1 stageR ∧
      stageR * stageQ = 1 ∧
      LeastRationalDenominator 3 stageQ ∧
      LeastRationalDenominator 2 stageR ∧
      LeastRationalDenominator 1 (stageR * stageQ) := by
  dsimp
  constructor
  · exact ⟨2, by norm_num⟩
  constructor
  · exact ⟨3, by norm_num⟩
  constructor
  · rintro ⟨integral, hintegral⟩
    norm_num only [Int.cast_one, one_mul] at hintegral
    have hrational : (3 : ℚ) * (integral : ℚ) = 2 := by
      rw [← hintegral]
      norm_num
    have hinteger : 3 * integral = 2 := by exact_mod_cast hrational
    omega
  constructor
  · rintro ⟨integral, hintegral⟩
    norm_num only [Int.cast_one, one_mul] at hintegral
    have hrational : (2 : ℚ) * (integral : ℚ) = 3 := by
      rw [← hintegral]
      norm_num
    have hinteger : 2 * integral = 3 := by exact_mod_cast hrational
    omega
  constructor
  · norm_num
  constructor
  · exact twoThirds_leastRationalDenominator
  constructor
  · exact threeHalves_leastRationalDenominator
  · norm_num only
    exact one_leastRationalDenominator

end MariciFormal
