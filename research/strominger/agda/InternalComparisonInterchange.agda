{-# OPTIONS --safe --cubical --guardedness #-}
module InternalComparisonInterchange where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv)
open import Cubical.Data.Maybe.Base using (Maybe; just; nothing)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Relation.Nullary.Base using (¬_)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open import NativeExtensionFamilyAudit using (Vertex; A; B; C; D; AD; CA; Seeds; sigmaEquiv)
open import SourceIndexedExtensionFamilies using (Out)
open import InternalSourceComparisons
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- A comparison graph retains its equality witness. Contracting the graph
-- fiber gives an equivalence, NOT literal equality of retained Code objects.
graphIso : {X Y : Type} (e : X ≃ Y)
  → Iso (Σ X (λ x → Σ Y (λ y → equivFun e x ≡ y))) X
Iso.fun (graphIso e) = fst
Iso.inv (graphIso e) x = x , equivFun e x , refl
Iso.rightInv (graphIso e) x = refl
Iso.leftInv (graphIso e) (x , y , p) i = x , p i , (λ j → p (i ∧ j))
graphEquiv : {X Y : Type} (e : X ≃ Y)
  → (Σ X (λ x → Σ Y (λ y → equivFun e x ≡ y))) ≃ X
graphEquiv e = isoToEquiv (graphIso e)

outerE : Code → Bool
outerE (E _ _) = true
outerE _ = false

module Interchange (m : Mode) (v : Vertex)
  (a : Body v) (b : Body (act m v))
  (e : El (expression (package a)) ≃ El (expression (package b)))
  (p : equivFun e (value (package a)) ≡ value (package b))
  (h : (x : El (expression (package a))) → act m (reader a x) ≡ reader b (equivFun e x)) where

  oldComparison : Body (act m v)
  oldComparison = compare m a b e p h
  attachmentEquiv : (o : Out v)
    → El (expression (package (attach a o))) ≃ El (expression (package (attach b (edgeMap m o))))
  attachmentEquiv o = Σ-cong-equiv (edgeEquiv m v) (λ _ → loopEquiv e p)
  abstract
    attachmentPoint : (o : Out v)
      → equivFun (attachmentEquiv o) (value (package (attach a o)))
        ≡ value (package (attach b (edgeMap m o)))
    attachmentPoint o i = edge-computes m v o i , loop-refl e p i
  attachmentPorts : (o : Out v) (x : El (expression (package (attach a o))))
    → act m (reader (attach a o) x)
      ≡ reader (attach b (edgeMap m o)) (equivFun (attachmentEquiv o) x)
  attachmentPorts o (edge , loop) = edge-target m v edge

  compareAfterAttach : (o : Out v) → Body (act m (fst o))
  compareAfterAttach o = compare m (attach a o) (attach b (edgeMap m o))
    (attachmentEquiv o) (attachmentPoint o) (attachmentPorts o)
  attachAfterCompare : (o : Out v) → Body (act m (fst o))
  attachAfterCompare o = attach oldComparison (edgeMap m o)

  oldGraphEquiv : El (expression (package oldComparison)) ≃ El (expression (package a))
  oldGraphEquiv = graphEquiv e
  oldLoopEquiv : (value (package oldComparison) ≡ value (package oldComparison))
    ≃ (value (package a) ≡ value (package a))
  oldLoopEquiv = loopEquiv oldGraphEquiv refl
  backward-loop-refl : invEq oldLoopEquiv refl ≡ refl
  backward-loop-refl = cong (invEq oldLoopEquiv) (sym (loop-refl oldGraphEquiv {x = value (package oldComparison)} {y = value (package a)} refl))
    ∙ retEq oldLoopEquiv refl

  -- Both routes are compared through their retained graph and loop structure.
  -- No new arbitrary filler or reset of the input derivations is supplied.
  interchangeEquiv : (o : Out v)
    → El (expression (package (compareAfterAttach o)))
      ≃ El (expression (package (attachAfterCompare o)))
  interchangeEquiv o = compEquiv (graphEquiv (attachmentEquiv o))
    (Σ-cong-equiv (edgeEquiv m v) (λ _ → invEquiv oldLoopEquiv))
  abstract
    interchangePoint : (o : Out v)
      → equivFun (interchangeEquiv o) (value (package (compareAfterAttach o)))
        ≡ value (package (attachAfterCompare o))
    interchangePoint o i = edge-computes m v o i , backward-loop-refl i
  interchangePorts : (o : Out v)
    (z : El (expression (package (compareAfterAttach o))))
    → reader (compareAfterAttach o) z
      ≡ reader (attachAfterCompare o) (equivFun (interchangeEquiv o) z)
  interchangePorts o (x , y , w) = sym (cong (λ z → fst (fst z)) w)

  interchange : (o : Out v) → Body (act m (fst o))
  interchange o = compare stay (compareAfterAttach o) (attachAfterCompare o)
    (interchangeEquiv o) (interchangePoint o) (interchangePorts o)

  orders-not-equal : (o : Out v)
    → ¬ (package (compareAfterAttach o) ≡ package (attachAfterCompare o))
  orders-not-equal o p = false≢true (cong (λ q → outerE (expression q)) p)

Total : Type₁
Total = Σ Vertex Body
closure : Total → Closure Seeds
closure (v , a) = package a , derivation a
comparisonOperands : Closure Seeds → Maybe (Closure Seeds × Closure Seeds)
comparisonOperands (_ , apply (compare-rule a b e p) ds) =
  just ((a , ds (lift true)) , (b , ds (lift false)))
comparisonOperands _ = nothing

module Retention (m : Mode) (v : Vertex)
  (a : Body v) (b : Body (act m v))
  (e : El (expression (package a)) ≃ El (expression (package b)))
  (p : equivFun e (value (package a)) ≡ value (package b))
  (h : (x : El (expression (package a))) → act m (reader a x) ≡ reader b (equivFun e x)) where
  open Interchange m v a b e p h
  both-routes-retained : (o : Out v)
    → comparisonOperands (closure (act m (fst o) , interchange o))
      ≡ just (closure (act m (fst o) , compareAfterAttach o)
             , closure (act m (fst o) , attachAfterCompare o))
  both-routes-retained o = refl

reified : Total → Whole.Universe.Complete (ℓ-suc ℓ-zero)
reified a = Whole.Universe.pack (Whole.Universe.atom (Total × Closure Seeds)) (a , closure a)
recovery : (a : Total) → Whole.Universe.value (reified a) ≡ (a , closure a)
recovery a = refl

-- Concrete nonidentity instance: source attachment AD is transported to BC.
module Example = Interchange exchange A (seedBody A) (seedBody B) sigmaEquiv refl (λ x → refl)
example : Body C
example = Example.interchange (D , AD)
continuedExample : Body A
continuedExample = attach example (A , CA)
continued-native : Resolve Seeds (package continuedExample)
continued-native = derivation continuedExample
