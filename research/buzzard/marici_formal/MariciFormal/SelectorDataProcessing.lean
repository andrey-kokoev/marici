/-!
Coefficient-side data-processing core of Grothendieck's selector resonance
packet. Normal cores and finite-group resonance labels remain separate
interfaces.
-/

namespace MariciFormal

def RightStabilizes {G X : Type*} [Mul G]
    (selector : G → X) (shift : G) : Prop :=
  ∀ g, selector (g * shift) = selector g

/-- Deterministic post-processing can only enlarge the right stabilizer. -/
theorem rightStabilizer_mono_under_postprocessing
    {G X Y : Type*} [Mul G]
    (selector : G → X) (process : X → Y) (shift : G)
    (hstabilizes : RightStabilizes selector shift) :
    RightStabilizes (process ∘ selector) shift := by
  intro g
  simp only [Function.comp_apply]
  rw [hstabilizes g]

/-- If post-processing is injective on all selector values, it preserves the
stabilizer exactly. -/
theorem rightStabilizer_preserved_by_injective_postprocessing
    {G X Y : Type*} [Mul G]
    (selector : G → X) (process : X → Y)
    (hprocess : Function.Injective process) (shift : G) :
    RightStabilizes (process ∘ selector) shift ↔
      RightStabilizes selector shift := by
  constructor
  · intro hprocessed g
    apply hprocess
    exact hprocessed g
  · exact rightStabilizer_mono_under_postprocessing selector process shift

end MariciFormal
