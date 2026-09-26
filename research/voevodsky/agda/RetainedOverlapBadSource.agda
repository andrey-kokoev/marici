{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedOverlapBadSource where
open import Cubical.Foundations.Prelude
open import RetainedLocalTidalOverlap
bad : Cited.packet newtonian ≡ Cited.packet rosen
bad = refl
