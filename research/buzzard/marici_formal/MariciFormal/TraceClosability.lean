import Mathlib

/-!
Sequential trace closability and persistence of a nonclosability witness under
faithful continuous target transport.
-/

namespace MariciFormal

section AbstractWitness

variable {V D E : Type*}
  [Zero V] [TopologicalSpace V]
  [Zero D] [TopologicalSpace D]
  [Zero E] [TopologicalSpace E]

/-- A sequential graph witness violating closability at source zero. -/
structure NonclosableWitness (trace : V → D) where
  sequence : Nat → V
  targetLimit : D
  sourceTendsToZero : Filter.Tendsto sequence Filter.atTop (nhds 0)
  traceTendsToTarget :
    Filter.Tendsto (fun n => trace (sequence n)) Filter.atTop (nhds targetLimit)
  targetLimit_ne_zero : targetLimit ≠ 0

/-- Sequential form of the zero-graph criterion for closability. -/
def SequentiallyClosable (trace : V → D) : Prop :=
  ∀ sequence : Nat → V, ∀ targetLimit : D,
    Filter.Tendsto sequence Filter.atTop (nhds 0) →
    Filter.Tendsto (fun n => trace (sequence n)) Filter.atTop (nhds targetLimit) →
    targetLimit = 0

theorem nonclosableWitness_refutes_closability
    {trace : V → D} (witness : NonclosableWitness trace) :
    ¬ SequentiallyClosable trace := by
  intro closable
  exact witness.targetLimit_ne_zero
    (closable witness.sequence witness.targetLimit witness.sourceTendsToZero
      witness.traceTendsToTarget)

/-- A faithful continuous target embedding transports, rather than repairs, a
nonclosability witness. -/
def nonclosableWitness_postcompose
    {trace : V → D} (witness : NonclosableWitness trace)
    (embed : D → E) (continuousEmbed : Continuous embed)
    (embedZero : embed 0 = 0) (faithful : Function.Injective embed) :
    NonclosableWitness (fun v => embed (trace v)) := by
  refine
    { sequence := witness.sequence
      targetLimit := embed witness.targetLimit
      sourceTendsToZero := witness.sourceTendsToZero
      traceTendsToTarget := (continuousEmbed.tendsto witness.targetLimit).comp
        witness.traceTendsToTarget
      targetLimit_ne_zero := ?_ }
  intro hzero
  apply witness.targetLimit_ne_zero
  apply faithful
  simpa [embedZero] using hzero

theorem faithfulTargetTransport_does_not_repair
    {trace : V → D} (witness : NonclosableWitness trace)
    (embed : D → E) (continuousEmbed : Continuous embed)
    (embedZero : embed 0 = 0) (faithful : Function.Injective embed) :
    ¬ SequentiallyClosable (fun v => embed (trace v)) :=
  nonclosableWitness_refutes_closability
    (nonclosableWitness_postcompose witness embed continuousEmbed embedZero faithful)

end AbstractWitness

section FiniteHostile

/-- A two-state source equipped below with the indiscrete topology. -/
inductive IndiscreteBit
  | zero
  | one
  deriving DecidableEq

instance : Zero IndiscreteBit := ⟨IndiscreteBit.zero⟩
instance : TopologicalSpace IndiscreteBit := ⊤

def bitTrace : IndiscreteBit → Real
  | .zero => 0
  | .one => 1

/-- In the indiscrete source topology, the constant nonzero state converges to source zero. -/
def bitTrace_nonclosableWitness : NonclosableWitness bitTrace where
  sequence := fun _ => IndiscreteBit.one
  targetLimit := 1
  sourceTendsToZero := by
    rw [nhds_top]
    exact le_top
  traceTendsToTarget := by simp [bitTrace]
  targetLimit_ne_zero := by norm_num

theorem bitTrace_not_sequentiallyClosable :
    ¬ SequentiallyClosable bitTrace :=
  nonclosableWitness_refutes_closability bitTrace_nonclosableWitness

/-- Even the isometric inclusion `y ↦ (y,0)` leaves the hostile limit nonzero. -/
theorem bitTrace_pairEmbedding_not_sequentiallyClosable :
    ¬ SequentiallyClosable (fun bit => (bitTrace bit, (0 : Real))) := by
  apply faithfulTargetTransport_does_not_repair bitTrace_nonclosableWitness
    (fun y : Real => (y, (0 : Real)))
  · fun_prop
  · rfl
  · intro x y h
    exact congrArg Prod.fst h

end FiniteHostile

end MariciFormal
