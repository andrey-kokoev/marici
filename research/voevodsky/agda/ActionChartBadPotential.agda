{-# OPTIONS --safe --cubical --guardedness #-}
module ActionChartBadPotential where
open import Cubical.Foundations.Prelude
open import ActionChartComparison
bad : potential-only (fixture ratio) ≡ observe (fixture ratio)
bad = refl
