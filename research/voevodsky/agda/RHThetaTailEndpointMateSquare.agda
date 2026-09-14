{-# OPTIONS --safe --cubical --guardedness #-}
module RHThetaTailEndpointMateSquare where

open import Cubical.Foundations.Prelude

-- The source-to-tail correspondence keeps the intermediate types visible.
-- It does not identify Euler currents, theta forcing, and tail states.
record ThetaTailCorrespondence {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Current Control ThetaSource Tail : Type ℓ
    evaluateCurrent : Current → Control
    insertForcing : Control → ThetaSource
    resolveTail : ThetaSource → Tail

open ThetaTailCorrespondence public

selectedTail : {ℓ : Level} (C : ThetaTailCorrespondence {ℓ}) →
  Current C → Tail C
selectedTail C ν = resolveTail C (insertForcing C (evaluateCurrent C ν))

-- Relative endpoint data live on a translation action.  The boundary value is
-- retained with its translated coefficient state through the cocycle law.
record RelativeEndpointAction {ℓ : Level} (Tail : Type ℓ) : Type (ℓ-suc ℓ) where
  field
    Scale Boundary : Type ℓ
    _⊕_ : Scale → Scale → Scale
    scaleCommutes : (a b : Scale) → a ⊕ b ≡ b ⊕ a
    translate : Scale → Tail → Tail
    boundary : Tail → Scale → Boundary
    combine : Boundary → Boundary → Boundary
    cocycle : (G : Tail) (a b : Scale) →
      combine (boundary G a) (boundary (translate a G) b)
        ≡ boundary G (a ⊕ b)

open RelativeEndpointAction public

-- The finite p,q mate square.  Its proof uses transported coefficient states;
-- replacing either translated term by a fixed-state scalar trace would not
-- have this type.
endpointMateSquare : {ℓ : Level} {Tail : Type ℓ} →
  (A : RelativeEndpointAction Tail) (G : Tail) (a b : Scale A) →
  combine A (boundary A G a) (boundary A (translate A a G) b)
    ≡ combine A (boundary A G b) (boundary A (translate A b G) a)
endpointMateSquare A G a b =
  cocycle A G a b ∙
  cong (boundary A G) (scaleCommutes A a b) ∙
  sym (cocycle A G b a)

-- Pulling the square back along the typed theta-to-tail correspondence gives
-- the exact common-source cell available before completion.
thetaEndpointMateSquare : {ℓ : Level}
  (C : ThetaTailCorrespondence {ℓ})
  (A : RelativeEndpointAction (Tail C))
  (ν : Current C) (a b : Scale A) →
  combine A
    (boundary A (selectedTail C ν) a)
    (boundary A (translate A a (selectedTail C ν)) b)
  ≡ combine A
    (boundary A (selectedTail C ν) b)
    (boundary A (translate A b (selectedTail C ν)) a)
thetaEndpointMateSquare C A ν = endpointMateSquare A (selectedTail C ν)

-- A framed endpoint observer is lawful only by evaluation on this tail route.
record FramedEndpointPort {ℓ : Level}
  (C : ThetaTailCorrespondence {ℓ})
  (A : RelativeEndpointAction (Tail C)) : Type (ℓ-suc ℓ) where
  field
    Frame : Type ℓ
    frameScale : Frame → Scale A
    observe : Frame → Current C → Boundary A
    observeFactors : (k : Frame) (ν : Current C) →
      observe k ν ≡ boundary A (selectedTail C ν) (frameScale k)

open FramedEndpointPort public
