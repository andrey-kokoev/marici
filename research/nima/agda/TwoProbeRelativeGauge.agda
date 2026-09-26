{-# OPTIONS --safe --cubical --guardedness #-}
module TwoProbeRelativeGauge where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sigma.Base using (_×_; fst; snd)
import BoundaryGeneratedQuestions as B
import RetainedComparisonSeries as R
import TwoProbeDistinguishability as T

-- The earlier continuation-separates proof in TwoProbeDistinguishability
-- already establishes: id+swap and twist+swap have different fst readings
-- at (true,false). That is the discrete phase difference.

-- twist composed with twist gives identity.
twist-twice : (x : R.Point) → R.pull T.twist-filler (λ y → R.pull T.twist-filler (λ z → z) y) x ≡ x
twist-twice (false , b) = refl
twist-twice (true , false) = refl
twist-twice (true , true) = refl

-- swap composed with swap gives identity on fst and snd separately.
swap-twice-fst : (x : R.Point) → R.pull B.swap-filler (R.pull B.swap-filler fst) x ≡ fst x
swap-twice-fst x = refl

swap-twice-snd : (x : R.Point) → R.pull B.swap-filler (R.pull B.swap-filler snd) x ≡ snd x
swap-twice-snd x = refl