{-# OPTIONS --safe --cubical --guardedness #-}
module PartialBadMergedObserver where
open import Cubical.Foundations.Prelude
import TransportObservationPartialCorrespondence as P
bad : P.Forget.Accepted
bad = P.Forget.accept (λ _ _ _ → refl)
