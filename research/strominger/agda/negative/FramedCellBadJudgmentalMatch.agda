{-# OPTIONS --safe --cubical --guardedness #-}
module FramedCellBadJudgmentalMatch where
open import Cubical.Foundations.Prelude
open import InternalSourceComparisons using (Mode)
import ForwardCertifiedPrograms as P
import FiniteComparisonTrees as F
open import CertifiedFramedCells
bad : {m : Mode} {a b : F.Object}
  (ca : P.Certificate (snd a)) (cb : P.Certificate (snd b)) (f : F.Full m a b)
  → evaluate (Certificate.producer (certify ca cb f)) ≡ f
bad ca cb f = refl
