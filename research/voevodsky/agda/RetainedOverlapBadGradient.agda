{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedOverlapBadGradient where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import RetainedLocalTidalOverlap
bad : snd (equivFun loose-equivalence (fine-reading newtonian))
    ≡ snd (fine-reading newtonian)
bad = refl
