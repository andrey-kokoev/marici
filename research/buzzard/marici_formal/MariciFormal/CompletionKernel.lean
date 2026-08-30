import Mathlib

namespace MariciFormal.CompletionKernel

inductive CanonicalExtensionMechanism where
  | boundedContinuous | closableGraph | friedrichsForm
  deriving DecidableEq, Repr

variable (F X Xhat Y Yhat : Type*) [Field F]
  [AddCommGroup X] [Module F X] [AddCommGroup Xhat] [Module F Xhat]
  [AddCommGroup Y] [Module F Y] [AddCommGroup Yhat] [Module F Yhat]

/-- Algebraic portion of a completion contract. Density/topology remain external fields. -/
structure OperatorSquare where
  sourceEmbedding : X →ₗ[F] Xhat
  targetEmbedding : Y →ₗ[F] Yhat
  sourceOperator : X →ₗ[F] Y
  completedOperator : Xhat →ₗ[F] Yhat
  sourceEmbedding_injective : Function.Injective sourceEmbedding
  targetEmbedding_injective : Function.Injective targetEmbedding
  mechanism : CanonicalExtensionMechanism
  commutes : completedOperator.comp sourceEmbedding =
    targetEmbedding.comp sourceOperator

variable {F X Xhat Y Yhat}

/-- Restriction of the commuting square gives the canonical descended-kernel map. -/
def descendedKernelMap (c : OperatorSquare F X Xhat Y Yhat) :
    LinearMap.ker c.sourceOperator →ₗ[F] LinearMap.ker c.completedOperator where
  toFun x := ⟨c.sourceEmbedding x, by
    change c.completedOperator (c.sourceEmbedding x) = 0
    have hs := LinearMap.congr_fun c.commutes x
    simpa [x.property] using hs⟩
  map_add' x y := by
    apply Subtype.ext
    exact c.sourceEmbedding.map_add x y
  map_smul' a x := by
    apply Subtype.ext
    exact c.sourceEmbedding.map_smul a x

theorem descendedKernelMap_injective (c : OperatorSquare F X Xhat Y Yhat) :
    Function.Injective (descendedKernelMap c) := by
  intro x y h
  apply Subtype.ext
  apply c.sourceEmbedding_injective
  simpa [descendedKernelMap] using congrArg Subtype.val h

/-- Ordinary completed zero modes modulo those descending from the source kernel. -/
abbrev CompletionOnlyKernel (c : OperatorSquare F X Xhat Y Yhat) :=
  LinearMap.ker c.completedOperator ⧸ LinearMap.range (descendedKernelMap c)

/-- A derived obstruction is separately typed and cannot be inferred from the quotient. -/
structure DerivedObstruction where
  TorObject : Type*
  evidenced : Nonempty TorObject

/-- Carrier completion data has no operator field. -/
structure CarrierCompletion (A Ahat : Type*) where
  embed : A → Ahat
  injective : Function.Injective embed

structure BareOperatorExtension (A Ahat B Bhat : Type*) where
  sourceEmbedding : A → Ahat
  targetEmbedding : B → Bhat
  sourceOperator : A → B
  completedOperator : Ahat → Bhat
  commutes : ∀ x, completedOperator (sourceEmbedding x) =
    targetEmbedding (sourceOperator x)

/-- Hostile model: completion of a carrier cannot manufacture an impossible operator. -/
theorem completion_does_not_manufacture_operator :
    Nonempty (CarrierCompletion Unit Unit) ∧
      IsEmpty (BareOperatorExtension Unit Unit Unit Empty) := by
  constructor
  · exact ⟨⟨id, fun _ _ h ↦ h⟩⟩
  · constructor
    intro e
    exact (e.completedOperator ()).elim

section FiniteModels

/-- Finite algebraic model of a zero-kernel core acquiring `n` ordinary modes. -/
def zeroCoreSquare (n : Nat) :
    OperatorSquare ℚ (Fin 0 → ℚ) (Fin n → ℚ) (Fin 0 → ℚ) (Fin 0 → ℚ) where
  sourceEmbedding := 0
  targetEmbedding := LinearMap.id
  sourceOperator := LinearMap.id
  completedOperator := 0
  sourceEmbedding_injective := by
    intro x y _
    funext i
    exact Fin.elim0 i
  targetEmbedding_injective := Function.injective_id
  mechanism := .boundedContinuous
  commutes := by ext x i; exact Fin.elim0 i

theorem zeroCoreSquare_sourceKernel (n : Nat) :
    LinearMap.ker (zeroCoreSquare n).sourceOperator = ⊥ := by
  exact LinearMap.ker_id

theorem zeroCoreSquare_completedKernel (n : Nat) :
    LinearMap.ker (zeroCoreSquare n).completedOperator = ⊤ := by
  exact LinearMap.ker_zero

/-- Magnetic contract's `0 → 21` kernel dimensions, as a finite algebraic model only. -/
example : LinearMap.ker (zeroCoreSquare 21).sourceOperator = ⊥ ∧
    LinearMap.ker (zeroCoreSquare 21).completedOperator = ⊤ := by
  exact ⟨zeroCoreSquare_sourceKernel 21, zeroCoreSquare_completedKernel 21⟩

/-- Theta contract's `0 → 1` kernel dimensions, as a finite algebraic model only. -/
example : LinearMap.ker (zeroCoreSquare 1).sourceOperator = ⊥ ∧
    LinearMap.ker (zeroCoreSquare 1).completedOperator = ⊤ := by
  exact ⟨zeroCoreSquare_sourceKernel 1, zeroCoreSquare_completedKernel 1⟩

end FiniteModels

end MariciFormal.CompletionKernel
