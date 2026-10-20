{-# OPTIONS --safe --cubical --guardedness #-}
module InterchangeBadEndpointOnlyCoherence where
open import Cubical.Foundations.Prelude
open import InterchangeHiddenFiberObstruction

-- Both maps preserve the selected point and every port, but that is not
-- sufficient to identify their action on additional retained witness content.
bad : identityEquiv ≡ swapEquiv
bad = refl
