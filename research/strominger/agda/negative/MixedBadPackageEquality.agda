{-# OPTIONS --safe --cubical --guardedness #-}
module MixedBadPackageEquality where
open import Cubical.Foundations.Prelude
import FiniteComparisonTrees as F
import NativeComposeHistoryBridge as H
bad : (a : F.Object) → H.Bridge.retainedPackage (F.identity a) (F.identity a)
  ≡ H.Bridge.compiledPackage (F.identity a) (F.identity a)
bad a = refl
