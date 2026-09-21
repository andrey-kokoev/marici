{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidSignedLiftRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit
open import Cubical.Data.Empty using (⊥)
open import DGPyramidBoundary
open import DGPyramidFiller
open import DGPyramidFixture
open import DGPyramidSignedLiftAudit

-- Reuse the existing explicitly nonphysical fixture, not an alleged
-- implementation of semilocal positivity or analytic completion.
module Horn = SignedHorn (idEquiv Unit) tt

module Good = FramedComparison toyBoundary toyFrame Horn.Completion
  (λ _ → Horn.forcedCompletion)

goodRemaining : Good.RemainingAt Horn.forcedCompletion
goodRemaining = equivFun
  (Good.remainingEquivalence Horn.completionContractible) toyFiller

-- Same signed horn, same DG differential, but no support witness.
blockedFrame : PyramidFrame toyBoundary
PyramidFrame.JFzero blockedFrame = Unit
PyramidFrame.deltaFiller blockedFrame _ = tt
PyramidFrame.PreservesSupport blockedFrame _ = ⊥
PyramidFrame.PreservesEndpoints blockedFrame _ = Unit
PyramidFrame.PreservesGenericQ blockedFrame _ = Unit
PyramidFrame.PreservesReesCartier blockedFrame _ = Unit

module Blocked = FramedComparison toyBoundary blockedFrame Horn.Completion
  (λ _ → Horn.forcedCompletion)

unframedExists : BoundaryFiller toyBoundary blockedFrame
unframedExists = tt , refl

noBlockedFiller : AdmissibleFiller toyBoundary blockedFrame → ⊥
noBlockedFiller (_ , _ , support , _) = support

noBlockedRemaining : Blocked.RemainingAt Horn.forcedCompletion → ⊥
noBlockedRemaining r = noBlockedFiller
  (equivFun (invEquiv
    (Blocked.remainingEquivalence Horn.completionContractible)) r)

-- These two tests have precisely the SAME contractible signed completion.
-- Thus signed contractibility alone cannot decide structured inhabitance.
-- Neither test establishes absence or existence of the physical lift.
