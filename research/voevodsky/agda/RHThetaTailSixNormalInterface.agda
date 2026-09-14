{-# OPTIONS --safe --cubical --guardedness #-}
module RHThetaTailSixNormalInterface where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma
open import RHThetaSixNormalIncidenceAudit using (NormalPort)
open import RHThetaTailEndpointMateSquare

-- Six normal labels, two polarities, and two supported frame variants give the
-- 24 checked endpoint frames without identifying them with theta observers.
data Polarity : Type where plus minus : Polarity
data FrameVariant : Type where primary secondary : FrameVariant

Frame24 : Type
Frame24 = NormalPort × Polarity × FrameVariant

-- This is the exact missing constructor.  Its fields require every framed
-- endpoint reading to factor through the theta-current/control/tail route.
record ThetaTailSixNormalCertificate : Type₁ where
  field
    correspondence : ThetaTailCorrespondence {ℓ-zero}
    endpointAction : RelativeEndpointAction (Tail correspondence)
    frameScale : Frame24 → Scale endpointAction
    framedReading : Frame24 → Current correspondence → Boundary endpointAction
    sourceFactorization : (k : Frame24) (ν : Current correspondence) →
      framedReading k ν ≡
      boundary endpointAction (selectedTail correspondence ν) (frameScale k)

open ThetaTailSixNormalCertificate public

asFramedEndpointPort : (C : ThetaTailSixNormalCertificate) →
  FramedEndpointPort (correspondence C) (endpointAction C)
asFramedEndpointPort C = record
  { Frame = Frame24
  ; frameScale = frameScale C
  ; observe = framedReading C
  ; observeFactors = sourceFactorization C
  }

-- Every pair of frame scales then inherits the finite reciprocal mate square.
allFramedMateSquares : (C : ThetaTailSixNormalCertificate) →
  (ν : Current (correspondence C)) (j k : Frame24) →
  combine (endpointAction C)
    (boundary (endpointAction C) (selectedTail (correspondence C) ν)
      (frameScale C j))
    (boundary (endpointAction C)
      (translate (endpointAction C) (frameScale C j)
        (selectedTail (correspondence C) ν))
      (frameScale C k))
  ≡ combine (endpointAction C)
    (boundary (endpointAction C) (selectedTail (correspondence C) ν)
      (frameScale C k))
    (boundary (endpointAction C)
      (translate (endpointAction C) (frameScale C k)
        (selectedTail (correspondence C) ν))
      (frameScale C j))
allFramedMateSquares C ν j k =
  thetaEndpointMateSquare (correspondence C) (endpointAction C) ν
    (frameScale C j) (frameScale C k)
