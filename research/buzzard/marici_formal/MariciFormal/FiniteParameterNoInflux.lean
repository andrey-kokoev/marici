import Mathlib.Tactic

/-!
Logical interface extracted from Grothendieck's finite-theta sine-type
theorem. Analytic endpoint/Rouché estimates are external evidence for the
remote-control premise, not encoded as assumptions about theta zeros.
-/

namespace MariciFormal

section SimpleZeroVelocity

variable {K : Type*} [Field K]

/-- Algebraic implicit-velocity law once the differentiated zero equation is
supplied and the spectral derivative is nonzero. -/
theorem simpleZero_velocity_eq
    (parameterDerivative spectralDerivative velocity : K)
    (hsimple : spectralDerivative ≠ 0)
    (hchain : parameterDerivative + spectralDerivative * velocity = 0) :
    velocity = -parameterDerivative / spectralDerivative := by
  apply (eq_div_iff hsimple).2
  linear_combination hchain

/-- At a multiple zero, the zero chain equation can leave velocity
undetermined. -/
theorem missing_simpleZero_hostile :
    let parameterDerivative : ℚ := 0
    let spectralDerivative : ℚ := 0
    let velocity₀ : ℚ := 0
    let velocity₁ : ℚ := 1
    parameterDerivative + spectralDerivative * velocity₀ = 0 ∧
      parameterDerivative + spectralDerivative * velocity₁ = 0 ∧
      velocity₀ ≠ velocity₁ := by
  norm_num

end SimpleZeroVelocity

section AbstractZeroFamily

variable {Parameter Zero : Type*}

structure RemoteZeroControl
    (admissible : Parameter → Prop) (zeroAt : Parameter → Zero → Prop)
    (height : Zero → ℕ) (real simple : Zero → Prop) : Prop where
  radius : ℕ
  remote_real : ∀ parameter zero,
    admissible parameter → zeroAt parameter zero → radius < height zero → real zero
  remote_simple : ∀ parameter zero,
    admissible parameter → zeroAt parameter zero → radius < height zero → simple zero

def SpectralInflux
    (admissible : Parameter → Prop) (zeroAt : Parameter → Zero → Prop)
    (height : Zero → ℕ) (nonreal : Zero → Prop) : Prop :=
  ∀ radius, ∃ parameter zero,
    admissible parameter ∧ zeroAt parameter zero ∧
      nonreal zero ∧ radius < height zero

def CollisionFree
    (admissible : Parameter → Prop) (zeroAt : Parameter → Zero → Prop)
    (simple : Zero → Prop) : Prop :=
  ∀ parameter zero, admissible parameter → zeroAt parameter zero → simple zero

/-- Uniform remote reality on a parameter region rules out nonreal influx
from unbounded height throughout that region. -/
theorem no_spectralInflux_of_remoteZeroControl
    (admissible : Parameter → Prop) (zeroAt : Parameter → Zero → Prop)
    (height : Zero → ℕ) (real nonreal simple : Zero → Prop)
    (hdisjoint : ∀ zero, real zero → ¬ nonreal zero)
    (control : RemoteZeroControl admissible zeroAt height real simple) :
    ¬ SpectralInflux admissible zeroAt height nonreal := by
  intro hinflux
  obtain ⟨parameter, zero, hadmissible, hzero, hnonreal, hremote⟩ :=
    hinflux control.radius
  exact hdisjoint zero
    (control.remote_real parameter zero hadmissible hzero hremote) hnonreal

end AbstractZeroFamily

section IndependentGates

def boundedCollisionZeroAt (_ : Unit) (zero : ℕ) : Prop := zero = 0

def boundedCollisionSimple (zero : ℕ) : Prop := zero ≠ 0

theorem noInflux_does_not_imply_collisionFree :
    let admissible : Unit → Prop := fun _ => True
    let real : ℕ → Prop := fun _ => True
    let nonreal : ℕ → Prop := fun _ => False
    (¬ SpectralInflux admissible boundedCollisionZeroAt id nonreal) ∧
      ¬ CollisionFree admissible boundedCollisionZeroAt boundedCollisionSimple := by
  dsimp
  constructor
  · intro hinflux
    obtain ⟨_, zero, _, hzero, hnonreal, _⟩ := hinflux 0
    exact hnonreal
  · intro hcollisionFree
    exact hcollisionFree () 0 trivial rfl (by simp [boundedCollisionSimple])

def influxZeroAt (_ : Unit) (_ : ℕ) : Prop := True

theorem collisionFree_does_not_imply_noInflux :
    let admissible : Unit → Prop := fun _ => True
    let nonreal : ℕ → Prop := fun _ => True
    let simple : ℕ → Prop := fun _ => True
    CollisionFree admissible influxZeroAt simple ∧
      SpectralInflux admissible influxZeroAt id nonreal := by
  dsimp
  constructor
  · intro parameter zero hadmissible hzero
    trivial
  · intro radius
    exact ⟨(), radius + 1, trivial, trivial, trivial, by omega⟩

end IndependentGates

end MariciFormal
