{-# OPTIONS --safe --cubical --guardedness #-}
module ActionChartBadSixth where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (pos)
import ActionChartComparison
bad : pos 512 ≡ pos 0
bad = refl
