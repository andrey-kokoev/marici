{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureTypedRealizationRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (idfun)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Bool using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.HITs.Pushout.Base
open import Cubical.HITs.S1.Base using (S¹; base; loop)
open import ClosureTypedRealization
import ClosureFiltrationMapRegression as R

module T = CofiberOperation
  R.LoopSquares.f R.LoopSquares.g R.LoopSquares.f′ R.LoopSquares.g
  R.LoopSquares.u (idfun S¹) (idfun S¹)
  (λ _ → loop) (λ _ → loop)

sourceFace : T.realizationPath i0 ≡ T.expanded
sourceFace = refl

targetFace : T.realizationPath i1 ≡ T.rejoined
targetFace = refl

retainsTypePath : cong fst T.realizationPath ≡ ua T.Old.operationEquivalence
retainsTypePath = refl

retainsOriginalProof :
  ua-ungluePath T.Old.operationEquivalence T.operationAlongTypes ≡
  T.Old.chosenOperationComparison
retainsOriginalProof = T.preservedOriginalComparison

-- Application of the changing operation to a changing input is type-correct
-- all along the path, and has the original input/output values at its faces.
evaluationSourceFace : (x : T.Old.S.Quotient) →
  T.evaluationAlongTypes x i0 ≡ T.Old.F4 x
evaluationSourceFace x = refl

evaluationTargetFace : (x : T.Old.S.Quotient) →
  T.evaluationAlongTypes x i1 ≡ T.Old.F1 (T.Old.S.rejoin x)
evaluationTargetFace x = refl

domainLoop : Path T.Old.S.Quotient
  (T.Old.S.cut (inr base)) (T.Old.S.cut (inr base))
domainLoop i = T.Old.S.cut (R.LoopSquares.loopInCofiber i)

-- A whole loop of inputs gives a dependent family of typed-output paths.
loopUnderRealizationChange : PathP
  (λ s → Path TypedRealization
    (T.Old.T.Quotient , T.Old.F4 (domainLoop s))
    (cofib R.LoopSquares.g , T.Old.F1 (T.Old.S.rejoin (domainLoop s))))
  (T.evaluatedRealizationPath (T.Old.S.cut (inr base)))
  (T.evaluatedRealizationPath (T.Old.S.cut (inr base)))
loopUnderRealizationChange s = T.evaluatedRealizationPath (domainLoop s)

module TypePathMatters where
  flipIso : Iso Bool Bool
  flipIso = iso not not (λ { false → refl ; true → refl })
    (λ { false → refl ; true → refl })

  flipEquiv : Bool ≃ Bool
  flipEquiv = isoToEquiv flipIso

  module Flip = AlongEquivalence flipEquiv {a = false} {b = true} refl

  -- Type returns to Bool, but along its nontrivial swap path. The VALUE
  -- changes from false to true WITHOUT asserting false=true inside Bool.
  typedSwap : Path TypedRealization (Bool , false) (Bool , true)
  typedSwap = Flip.together

  swapValue : PathP (λ i → ua flipEquiv i) false true
  swapValue = Flip.valuePath

  -- The same endpoints cannot be connected over the identity realization.
  noIdentityValueSwap : PathP (λ i → ua (idEquiv Bool) i) false true → ⊥
  noIdentityValueSwap p = false≢true (ua-ungluePath (idEquiv Bool) p)
