{-# OPTIONS --safe --cubical --guardedness #-}
module ModeBadJudgmentalNormalization where
open import Cubical.Foundations.Prelude
open import RetainedPackageFeedback using (Total)
import ForwardSourceLiftComposition as F
import SourceChainOverlap as C
bad : (c : Total) → F.forward-square c ≡ C.square c
bad c = refl
