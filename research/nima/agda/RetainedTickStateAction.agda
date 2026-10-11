{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedTickStateAction where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.List.Base using (List; []; _∷_; _++_)
import RetainedSquareConeClock as Clock

-- A genuine action of the existing source-attached Tick histories.
-- The interpretation step is an INPUT, not selected physical dynamics.
module Attached {ℓ ℓs : Level} (O R : Type ℓ) (e : O ≃ R)
                (source : O × O) (State : Type ℓs) where
  module B = Clock.Bridge O R e
  module A = B.AtSource source

  module Policy (step : A.Tick → State → State) where
    act : A.History → State → State
    act [] x = x
    act (t ∷ ts) x = act ts (step t x)

    identity : (x : State) → act [] x ≡ x
    identity x = refl

    compose : (h k : A.History) (x : State)
            → act (h ++ k) x ≡ act k (act h x)
    compose [] k x = refl
    compose (t ∷ ts) k x = compose ts k (step t x)

    -- Encoding does not execute another Tick or erase its witnesses.
    cone-act : A.ConeHistory → State → State
    cone-act cs x = act (A.decode-history cs) x

    encoding-preserves-action : (h : A.History) (x : State)
      → cone-act (A.encode-history h) x ≡ act h x
    encoding-preserves-action h x = cong (λ hs → act hs x) (A.history-recovered h)

    -- The observer is not allowed to replace the retained history by its
    -- final state. Distinct equal-effect histories remain in this record.
    record Execution (initial : State) : Type (ℓ-max ℓ ℓs) where
      constructor execution
      field
        history : A.History
        final : State
        attached : final ≡ act history initial

    run : (h : A.History) (x : State) → Execution x
    run h x = execution h (act h x) refl

    history-recovered : (h : A.History) (x : State)
      → Execution.history (run h x) ≡ h
    history-recovered h x = refl

    extend : {x : State} (r : Execution x) (k : A.History) → Execution x
    extend r k = execution (Execution.history r ++ k)
      (act k (Execution.final r))
      (cong (act k) (Execution.attached r)
       ∙ sym (compose (Execution.history r) k _))

    -- Presentation changes are not a second physical intervention.
    -- Transport the SAME supplied policy through a lossless view.
    module Views {ℓv : Level} (V : Type ℓv)
                 (encode : State → V) (decode : V → State)
                 (recover : (x : State) → decode (encode x) ≡ x)
                 (complete : (v : V) → encode (decode v) ≡ v) where
      view-step : A.Tick → V → V
      view-step t v = encode (step t (decode v))

      step-square : (t : A.Tick) (x : State)
        → view-step t (encode x) ≡ encode (step t x)
      step-square t x = cong (λ y → encode (step t y)) (recover x)

      view-act : A.History → V → V
      view-act h v = encode (act h (decode v))

      action-square : (h : A.History) (x : State)
        → view-act h (encode x) ≡ encode (act h x)
      action-square h x = cong (λ y → encode (act h y)) (recover x)

      view-identity : (v : V) → view-act [] v ≡ v
      view-identity = complete

      view-compose : (h k : A.History) (v : V)
        → view-act (h ++ k) v ≡ view-act k (view-act h v)
      view-compose h k v =
        cong encode (compose h k (decode v))
        ∙ sym (cong (λ y → encode (act k y)) (recover (act h (decode v))))

      cone-view-square : (h : A.History) (x : State)
        → encode (cone-act (A.encode-history h) x) ≡ view-act h (encode x)
      cone-view-square h x =
        cong encode (encoding-preserves-action h x) ∙ sym (action-square h x)

  -- Every native record may drive an external policy, but the source does
  -- not choose between policies. Constant no-motion is always admissible.
  stationary : A.Tick → State → State
  stationary t x = x

  module Still = Policy stationary

  stationary-history : (h : A.History) (x : State) → Still.act h x ≡ x
  stationary-history [] x = refl
  stationary-history (t ∷ ts) x = stationary-history ts x
