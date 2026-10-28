{-# OPTIONS --safe --cubical --guardedness #-}
module NativeRecorderBadBlank where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false)
import NativeQueryControlledRecorder as R
import NativeSeedTransitionProbe as Q
import SeedAttachedObserver as S
bad : snd (R.native-record S.A S.B (Q.ABC , false)) ≡ false
bad = refl
