import Mathlib.Data.Finsupp.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite atomic-current pushforward from Grothendieck's primitive/square theta
incidence packet. Completion riggings remain distinct types.
-/

namespace MariciFormal

noncomputable section

section FinitePushforward

variable {Label Scale R : Type*}
variable [CommSemiring R]

/-- Push a finitely supported labelled coefficient packet to the common scale
axis, adding weights that land at the same scale. -/
noncomputable def atomicScalePushforward
    (scale : Label → Scale) (source : Label →₀ R) : Scale →₀ R :=
  by
    classical
    exact source.mapDomain scale

def currentReadout (test : Scale → R) (current : Scale →₀ R) : R :=
  current.sum fun q weight => weight * test q

def sourceReadout
    (scale : Label → Scale) (test : Scale → R)
    (source : Label →₀ R) : R :=
  source.sum fun label weight => weight * test (scale label)

def testReadoutHom (test : Scale → R) (q : Scale) : R →+ R where
  toFun := fun weight => weight * test q
  map_zero' := zero_mul _
  map_add' := fun x y => add_mul x y (test q)

/-- Finite spectral evaluation commutes exactly with atomic scale
pushforward. -/
theorem currentReadout_atomicScalePushforward
    (scale : Label → Scale) (test : Scale → R)
    (source : Label →₀ R) :
    currentReadout test (atomicScalePushforward scale source) =
      sourceReadout scale test source := by
  classical
  simpa [currentReadout, atomicScalePushforward, sourceReadout,
    testReadoutHom] using
      (Finsupp.sum_mapDomain_index_addMonoidHom
        (f := scale) (s := source) (h := testReadoutHom test))

end FinitePushforward

section SineReadout

def finiteSineReadout (t : ℝ) (current : ℝ →₀ ℝ) : ℝ :=
  2 * currentReadout (fun q => Real.sin (t * q)) current

theorem finiteSineReadout_pushforward
    {Label : Type*}
    (scale : Label → ℝ) (source : Label →₀ ℝ) (t : ℝ) :
    finiteSineReadout t (atomicScalePushforward scale source) =
      2 * sourceReadout scale (fun q => Real.sin (t * q)) source := by
  rw [finiteSineReadout, currentReadout_atomicScalePushforward]

end SineReadout

section CompletionRiggings

structure ExponentialScaleCurrent where
  current : ℝ →₀ ℝ

structure TemperedScaleCurrent where
  current : ℝ →₀ ℝ

def primitiveFiniteCurrent (current : ℝ →₀ ℝ) : ExponentialScaleCurrent :=
  ⟨current⟩

def squareFiniteCurrent (current : ℝ →₀ ℝ) : TemperedScaleCurrent :=
  ⟨current⟩

end CompletionRiggings

section CollisionHostile

def collisionScale : Fin 2 → PUnit := fun _ => PUnit.unit

def cancellingLabelPacket : Fin 2 →₀ ℤ :=
  Finsupp.single 0 1 + Finsupp.single 1 (-1)

theorem cancellingLabelPacket_ne_zero : cancellingLabelPacket ≠ 0 := by
  intro hzero
  have hfirst := congrArg (fun packet => packet 0) hzero
  norm_num [cancellingLabelPacket] at hfirst

/-- Distinct labels that collide on the same scale can cancel under
pushforward, so atomic aggregation is not automatically label-faithful. -/
theorem atomicScalePushforward_not_faithful_hostile :
    atomicScalePushforward collisionScale cancellingLabelPacket = 0 := by
  simp [atomicScalePushforward, collisionScale, cancellingLabelPacket,
    Finsupp.mapDomain_add]

end CollisionHostile

end MariciFormal
