import MariciFormal.WitnessChain

namespace MariciFormal.TemporalAuthority.LinearConsumption

/-! Arbitrary finite concurrent histories refining fenced sequential execution. -/

structure TimedFencedOperation where
  operationId : Nat
  token : Nat
  interval : OperationInterval

def runTimedFencedOrder : FencedEffectState → List TimedFencedOperation →
    List (Nat × Bool)
  | _, [] => []
  | state, operation :: rest =>
      let step := attemptFencedEffect state operation.token
      (operation.operationId, step.2) :: runTimedFencedOrder step.1 rest

def RealTimeOrdered (operations : List TimedFencedOperation) : Prop :=
  operations.Pairwise fun earlier later =>
    ¬ RealTimePrecedes later.interval earlier.interval

def OperationIdsUnique (operations : List TimedFencedOperation) : Prop :=
  (operations.map TimedFencedOperation.operationId).Nodup

structure FiniteConcurrentFencedHistory where
  operations : List TimedFencedOperation
  observed : List (Nat × Bool)

structure FiniteConcurrentRefinement (history : FiniteConcurrentFencedHistory) where
  order : List TimedFencedOperation
  sameOperations : order.Perm history.operations
  agrees : history.observed = runTimedFencedOrder initialFencedEffect order
  respectsRealTime : RealTimeOrdered order

/-- Faithfulness of event identity is an additional condition, not a consequence
of having some sequential explanation. -/
structure FaithfulFiniteConcurrentRefinement
    (history : FiniteConcurrentFencedHistory)
    extends FiniteConcurrentRefinement history where
  uniqueOperationIds : OperationIdsUnique history.operations

def finiteOpA : TimedFencedOperation :=
  ⟨0, 4, interval 0 3 (by decide)⟩

def finiteOpB : TimedFencedOperation :=
  ⟨1, 4, interval 1 2 (by decide)⟩

def finiteOpC : TimedFencedOperation :=
  ⟨2, 5, interval 4 5 (by decide)⟩

def threeOperationHistory : FiniteConcurrentFencedHistory where
  operations := [finiteOpA, finiteOpB, finiteOpC]
  observed := [(0, true), (1, false), (2, true)]

def threeOperationHistoryRefines :
    FaithfulFiniteConcurrentRefinement threeOperationHistory where
  order := [finiteOpA, finiteOpB, finiteOpC]
  sameOperations := .refl _
  agrees := rfl
  respectsRealTime := by
    simp [RealTimeOrdered, finiteOpA, finiteOpB, finiteOpC,
      RealTimePrecedes, interval]
  uniqueOperationIds := by
    simp [OperationIdsUnique, threeOperationHistory, finiteOpA, finiteOpB,
      finiteOpC]

theorem finite_refinement_preserves_operation_count
    (history : FiniteConcurrentFencedHistory)
    (w : FiniteConcurrentRefinement history) :
    w.order.length = history.operations.length :=
  w.sameOperations.length_eq

theorem three_operation_refinement_has_two_effects :
    (runFencedTrace initialFencedEffect [4, 4, 5]).successes = 2 ∧
      (runFencedTrace initialFencedEffect [4, 4, 5]).finalState.effectCount = 2 := by
  decide

/-! Real-time ordering is independent of sequential outcome agreement. -/

def lateLeft : TimedFencedOperation :=
  ⟨0, 4, interval 2 3 (by decide)⟩

def earlyRight : TimedFencedOperation :=
  ⟨1, 4, interval 0 1 (by decide)⟩

theorem sequential_agreement_does_not_imply_real_time_order :
    [(0, true), (1, false)] =
        runTimedFencedOrder initialFencedEffect [lateLeft, earlyRight] ∧
      ¬ RealTimeOrdered [lateLeft, earlyRight] := by
  constructor
  · rfl
  · simp [RealTimeOrdered, lateLeft, earlyRight, RealTimePrecedes, interval]

/-! Duplicate operation identities make an otherwise explainable trace unfaithful. -/

def duplicateIdFirst : TimedFencedOperation :=
  ⟨7, 4, interval 0 2 (by decide)⟩

def duplicateIdSecond : TimedFencedOperation :=
  ⟨7, 5, interval 3 4 (by decide)⟩

def duplicateIdentityHistory : FiniteConcurrentFencedHistory where
  operations := [duplicateIdFirst, duplicateIdSecond]
  observed := [(7, true), (7, true)]

def duplicateIdentityHasSequentialExplanation :
    FiniteConcurrentRefinement duplicateIdentityHistory where
  order := [duplicateIdFirst, duplicateIdSecond]
  sameOperations := .refl _
  agrees := rfl
  respectsRealTime := by
    simp [RealTimeOrdered, duplicateIdFirst, duplicateIdSecond,
      RealTimePrecedes, interval]

theorem duplicate_identity_history_has_no_faithful_refinement :
    IsEmpty (FaithfulFiniteConcurrentRefinement duplicateIdentityHistory) := by
  constructor
  intro w
  have h := w.uniqueOperationIds
  simp [OperationIdsUnique, duplicateIdentityHistory, duplicateIdFirst,
    duplicateIdSecond] at h

end MariciFormal.TemporalAuthority.LinearConsumption
