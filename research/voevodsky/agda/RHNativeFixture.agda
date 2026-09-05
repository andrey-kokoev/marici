{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module RHNativeFixture where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Int
open import Cubical.Data.Empty using (⊥; rec)

open import CyclicCoherence
open import PastingComplex
open import CompletionPreservation
open import ResidualPromotion

integerVertex : Vertex
Vertex.P integerVertex = ℤ
Vertex.O integerVertex = ℤ
Vertex.R integerVertex = ℤ
Vertex.generate integerVertex x = x
Vertex.cohere integerVertex x = x

integerLaxCycle : LaxCycle
LaxCycle.A integerLaxCycle = integerVertex
LaxCycle.B integerLaxCycle = integerVertex
LaxCycle.C integerLaxCycle = integerVertex
LaxCycle.T-A integerLaxCycle x = x
LaxCycle.T-B integerLaxCycle x = x
LaxCycle.T-C integerLaxCycle x = x

integerCompletion : CompletionCone ℤ
Completed integerCompletion = ℤ
inject integerCompletion x = x

integerAdapter : CompletionMap integerCompletion integerCompletion
integerAdapter = identityCompletionMap integerCompletion

residualChild : ChildTower
ChildTower.State residualChild = ℤ
ChildTower.residualStep residualChild x = x

residualParent : ParentTower
ParentTower.State residualParent = ℤ

-- The current fixture has no admitted promotion constructor: its authority
-- type is empty. A later admission must supply a distinct gate.
closedPromotionGate : PromotionGate residualChild residualParent
Authority closedPromotionGate = ⊥
promote closedPromotionGate authority = rec authority

fixture-middle-exact :
  (v : ℤ³) → ∂₂ v ≡ 0 → Σ[ u ∈ ℤ³ ] ∂₁ u ≡ v
fixture-middle-exact = middle-exact

fixture-filler-unique-mod-adjustment :
  (f g : ℤ³) → ∂₂ f ≡ ∂₂ g → Σ[ u ∈ ℤ³ ] f ≡ ∂₁ u +³ g
fixture-filler-unique-mod-adjustment = unique-mod-adjustment

fixture-completion-preserved :
  (x : ℤ) → map integerAdapter (inject integerCompletion x) ≡ inject integerCompletion x
fixture-completion-preserved = preserves-completion integerAdapter

fixture-cube : CommonFiber.fillerType {X = ℤ} 0
fixture-cube = CommonFiber.fillerInhabited {X = ℤ} 0
