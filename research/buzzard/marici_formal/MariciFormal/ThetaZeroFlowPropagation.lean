import Mathlib.Tactic

/-!
Logical propagation interface for Grothendieck's completed-theta support flow.

The analytic small-window theorem and finite-parameter no-influx theorem enter
only through explicit premises.  The remaining collision premise is not
derived here.
-/

namespace MariciFormal

/-- A first off-seam zero at the next stage must come from an earlier off-seam
zero, a finite collision, or influx through the chosen exhaustion boundary. -/
structure ZeroFormationBoundary where
  offSeam : ℕ → Prop
  collision : ℕ → Prop
  influx : ℕ → Prop
  formation : ∀ n, offSeam (n + 1) →
    offSeam n ∨ collision n ∨ influx (n + 1)

def InitiallyReal (flow : ZeroFormationBoundary) : Prop :=
  ¬ flow.offSeam 0

def CollisionFreeFlow (flow : ZeroFormationBoundary) : Prop :=
  ∀ n, ¬ flow.collision n

def NoInfluxFlow (flow : ZeroFormationBoundary) : Prop :=
  ∀ n, ¬ flow.influx n

/-- Once the initial divisor is real, every later off-seam zero would require
either a finite collision or influx.  Excluding both prevents off-seam zeros
at every finite stage. -/
theorem offSeam_absent_of_initial_noInflux_collisionFree
    (flow : ZeroFormationBoundary)
    (hinitial : InitiallyReal flow)
    (hcollision : CollisionFreeFlow flow)
    (hinflux : NoInfluxFlow flow) :
    ∀ n, ¬ flow.offSeam n := by
  intro n
  induction n with
  | zero => exact hinitial
  | succ n ih =>
      intro hoff
      rcases flow.formation n hoff with hprevious | hcollisionAt | hinfluxAt
      · exact ih hprevious
      · exact hcollision n hcollisionAt
      · exact hinflux (n + 1) hinfluxAt

/-! Each premise is independent, witnessed by a finite-state hostile model. -/

def collisionHostile : ZeroFormationBoundary where
  offSeam := fun n => n = 1
  collision := fun n => n = 0
  influx := fun _ => False
  formation := by
    intro n hoff
    right
    left
    omega

theorem collision_gate_cannot_be_omitted :
    InitiallyReal collisionHostile ∧
      NoInfluxFlow collisionHostile ∧
      (∃ n, collisionHostile.offSeam n) := by
  refine ⟨by simp [InitiallyReal, collisionHostile], ?_, ⟨1, rfl⟩⟩
  intro n
  simp [collisionHostile]

def influxHostile : ZeroFormationBoundary where
  offSeam := fun n => n = 1
  collision := fun _ => False
  influx := fun n => n = 1
  formation := by
    intro n hoff
    right
    right
    omega

theorem noInflux_gate_cannot_be_omitted :
    InitiallyReal influxHostile ∧
      CollisionFreeFlow influxHostile ∧
      (∃ n, influxHostile.offSeam n) := by
  refine ⟨by simp [InitiallyReal, influxHostile], ?_, ⟨1, rfl⟩⟩
  intro n
  simp [influxHostile]

def initialBoundaryHostile : ZeroFormationBoundary where
  offSeam := fun n => n = 0
  collision := fun _ => False
  influx := fun _ => False
  formation := by
    intro n hoff
    omega

theorem initial_reality_gate_cannot_be_omitted :
    CollisionFreeFlow initialBoundaryHostile ∧
      NoInfluxFlow initialBoundaryHostile ∧
      (∃ n, initialBoundaryHostile.offSeam n) := by
  refine ⟨?_, ?_, ⟨0, rfl⟩⟩
  · intro n
    simp [initialBoundaryHostile]
  · intro n
    simp [initialBoundaryHostile]

end MariciFormal
