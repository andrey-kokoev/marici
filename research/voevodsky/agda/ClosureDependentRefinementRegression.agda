{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureDependentRefinementRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (idfun)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence
open import Cubical.Data.Unit
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Bool using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties using (false≢true; true≢false)
open import Cubical.Data.Sum.Base using (inl; inr)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.HITs.Pushout.Base using (cofib)
import Cubical.HITs.Pushout.Base as PO
open import Cubical.HITs.S1.Base using (S¹; base; loop)
open import ClosureCanonicalRejoin using (module Naturality)
open import ClosureProductBoundary using (module PointedModel; module DependentCounterexample)
open import ClosureDependentRefinementTrees

module MixedOutput where
  module D = DependentCounterexample

  Payload : Type
  Payload = Σ D.P D.R

  -- Two outputs, each a family value together with its dependent residual.
  X : Type
  X = Bool → Payload

  x₀ : X
  x₀ _ = D.p₀ , tt

  module Root = PointedModel X x₀

  swapColumns : X → X
  swapColumns q j = q (not j)

  module N = Naturality Root.f Root.g swapColumns

  child : Tree Payload 1
  child = sigmaNode (idEquiv Payload) (λ p → leaf)

  outputs : Tree (cofib Root.g) 2
  outputs = piNode (invEquiv Root.coneEquiv) (λ _ → child)

  inputs : Tree (cofib Root.g) 0
  inputs = leaf

  module T = Realization inputs outputs N.Lower.direct

  sample : X
  sample false = D.p₀ , tt
  sample true = D.p₁ , true

  swappedFirst : T.realize T.fullCut (PO.inr sample) false ≡ (D.p₁ , true)
  swappedFirst = refl

  swappedSecond : T.realize T.fullCut (PO.inr sample) true ≡ (D.p₀ , tt)
  swappedSecond = refl

  partialChildren : (j : Bool) → Cut child
  partialChildren false = inl tt
  partialChildren true = full child

  partialCut : T.Cuts
  partialCut = tt , inr partialChildren

  cycle : T.Views.Cuts.Route T.rootCut T.rootCut
  cycle = T.Views.Cuts.step T.rootCut (T.Views.Cuts.step T.fullCut
    (T.Views.Cuts.step partialCut (T.Views.Cuts.stay T.rootCut)))

  cycleIsTrivial :
    T.Views.closedCycle cycle (T.Views.Cuts.canonical T.rootCut) ≡ refl
  cycleIsTrivial = T.Views.closedCycleIsTrivial cycle (T.Views.Cuts.canonical T.rootCut)

module TwistedBoundary where
  flipIso : Iso Bool Bool
  flipIso = iso not not (λ { false → refl ; true → refl })
    (λ { false → refl ; true → refl })

  flipEquiv : Bool ≃ Bool
  flipEquiv = isoToEquiv flipIso

  -- A genuinely higher-indexed dependent family, not merely a finite list
  -- of different types: traversing the base circle swaps the boundary.
  Cover : S¹ → Type
  Cover base = Bool
  Cover (loop i) = ua flipEquiv i

  Total : Type
  Total = Σ S¹ Cover

  module Root = PointedModel Total (base , false)

  tree : Tree (cofib Root.g) 1
  tree = sigmaNode (invEquiv Root.coneEquiv) (λ p → leaf)

  unfolded : At tree (full tree) ≃ cofib Root.g
  unfolded = frame tree (full tree)

  monodromy : (b : Bool) → transport (cong Cover loop) b ≡ not b
  monodromy b = uaβ flipEquiv b

  -- The two boundary values can be connected while the base traverses its
  -- loop; they are NOT identified inside the single fixed fiber Bool.
  liftedBaseLoop : Path Total (base , false) (base , true)
  liftedBaseLoop i = loop i , ua-gluePath flipEquiv {x = false} {y = true} refl i

  noFixedPoint : (b : Bool) → not b ≡ b → ⊥
  noFixedPoint false p = true≢false p
  noFixedPoint true p = false≢true p

  noSection : ((p : S¹) → Cover p) → ⊥
  noSection s = noFixedPoint (s base)
    (ua-ungluePath flipEquiv (λ i → s (loop i)))

  noCoherentTrivialization : ((p : S¹) → Cover p ≃ Bool) → ⊥
  noCoherentTrivialization trivialize = noSection (λ p → invEq (trivialize p) false)

  observe : cofib Root.g → S¹
  observe z = fst (equivFun Root.coneEquiv z)

  basePreserved : (z : Total) → observe (equivFun unfolded z) ≡ fst z
  basePreserved z = refl

  realizedLiftedLoop : Path (cofib Root.g)
    (PO.inr (base , false)) (PO.inr (base , true))
  realizedLiftedLoop i = equivFun unfolded (liftedBaseLoop i)

  -- Rule out any constant residual over this observable in the ACTUAL
  -- cofiber realization. A product split would create a forbidden section.
  noProductAtRoot : (R : Type) (e : cofib Root.g ≃ (S¹ × R)) →
    ((z : cofib Root.g) → fst (equivFun e z) ≡ observe z) → ⊥
  noProductAtRoot R e over = noSection forbiddenSection
    where
    r₀ : R
    r₀ = snd (equivFun e (PO.inr (base , false)))

    forbiddenSection : (p : S¹) → Cover p
    forbiddenSection p = subst Cover
      (sym (over (invEq e (p , r₀))) ∙ cong fst (secEq e (p , r₀)))
      (snd (equivFun Root.coneEquiv (invEq e (p , r₀))))

-- Finite DEPTH does not mean finitely many branch indices: the last node
-- is indexed by S¹. No uniform residual or global section was smuggled in.
