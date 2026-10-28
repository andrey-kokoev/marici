{-# OPTIONS --safe --cubical --guardedness #-}
module NativeWordBadReset where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import Cubical.Data.List.Base using ([]; _∷_)
import NativeQueryWordRealization as W
import NativeSeedTransitionProbe as Q
bad : snd (W.native-run (W.QAB ∷ W.QAB ∷ []) (Q.ABC , false)) ≡ true
bad = refl
