{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureFourPresentationsRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (idfun)
open import Cubical.HITs.Pushout.Base
open import Cubical.HITs.S1.Base using (S¹; base; loop)
open import ClosureFourPresentations
import ClosureFiltrationMapRegression as R

-- Reuse the nontrivial ladder with circle-loop witnesses for BOTH squares.
-- No compatibility of the four presentations is installed as test input.
module P = Presentations
  R.LoopSquares.f R.LoopSquares.g R.LoopSquares.f′ R.LoopSquares.g
  R.LoopSquares.u (idfun S¹) (idfun S¹)
  (λ _ → loop) (λ _ → loop)

compatiblePairComparison : P.independentLift ≡ P.transportedLift
compatiblePairComparison = P.liftIdentification

-- Verify both faces of the higher comparison: it starts at the originally
-- proved naturality square and ends at the reassembly square of the
-- transported presentation. The square witness is not silently discarded.
originalSquareFace : (x : P.S.Quotient) →
  Path (P.T.rejoin (P.F4 x) ≡ P.F3 x)
    (λ j → P.squareCoherence i0 j x) (P.independentSquare x)
originalSquareFace x = refl

transportedSquareFace : (x : P.S.Quotient) →
  Path (P.T.rejoin (P.F2 (P.S.rejoin x)) ≡ P.F3 x)
    (λ j → P.squareCoherence i1 j x)
    (P.outputReassembly (P.S.rejoin x))
transportedSquareFace x = refl

-- Travel along the retained circle in the source cofiber, lifted by cut.
domainLoop : Path P.S.Quotient
  (P.S.cut (inr base)) (P.S.cut (inr base))
domainLoop i = P.S.cut (R.LoopSquares.loopInCofiber i)

comparisonAlongLoop : PathP
  (λ i → P.F4 (domainLoop i) ≡ P.F2 (P.S.rejoin (domainLoop i)))
  (P.F4-as-transport (P.S.cut (inr base)))
  (P.F4-as-transport (P.S.cut (inr base)))
comparisonAlongLoop i = P.F4-as-transport (domainLoop i)
