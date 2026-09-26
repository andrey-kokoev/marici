{-# OPTIONS --safe --cubical --guardedness #-}
module NativeRadarBadEvidence where
open import NativeRadarReadout
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (pos)
open import Cubical.Data.Bool.Base using (Bool; true; false)
sample : Rows
sample _ _ = clocks (pos 0) (pos 0)
-- Two distinct supplied labels; neither is declared a physical witness here.
module A = Admitted (λ _ _ → Bool) 0 sample true
module B = Admitted (λ _ _ → Bool) 0 sample false
bad : G.encode-package A.old-source ≡ G.encode-package B.old-source
bad = refl
