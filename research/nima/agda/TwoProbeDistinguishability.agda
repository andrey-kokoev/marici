{-# OPTIONS --safe --cubical --guardedness #-}
module TwoProbeDistinguishability where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sigma.Base using (_×_)
import BoundaryGeneratedQuestions as B
import RetainedComparisonSeries as R
import WholePackageSigmaPi as Whole

trace : R.Filler → R.Point → Bool × Bool
trace f x = fst x , R.pull f fst x
native-trace-agrees : (f : R.Filler)
  → (λ x → fst x , R.native-pull f fst x) ≡ trace f
native-trace-agrees f = refl

-- The existing marked preparation is fixed by every admitted pointed filler.
anchor-invisible : (f : R.Filler) → trace f (false , false) ≡ (false , false)
anchor-invisible f = cong (λ y → false , fst y) (snd f)
challenge-distinguishes : trace R.id-filler (false , true)
  ≡ trace B.swap-filler (false , true) → ⊥
challenge-distinguishes p = false≢true (cong snd p)

-- Off-anchor challenges are explicit NEW complete boundary packages.
module W = Whole.Universe ℓ-zero
prepared : R.Point → W.Complete
prepared x = W.pack (W.atom R.Point) x
repoint : (f : R.Filler) (x : R.Point)
  → B.Filler (prepared x) (prepared (R.pull f (λ y → y) x))
repoint f x = fst f , refl

-- A pointed controlled flip, not a Clifford or linear-algebra assumption.
twist : R.Point → R.Point
twist (false , b) = false , b
twist (true , false) = true , true
twist (true , true) = true , false
twist-square : (x : R.Point) → twist (twist x) ≡ x
twist-square (false , b) = refl
twist-square (true , false) = refl
twist-square (true , true) = refl
twist-iso : Iso R.Point R.Point
twist-iso = record { fun = twist ; inv = twist ; rightInv = twist-square ; leftInv = twist-square }
twist-filler : R.Filler
twist-filler = isoToEquiv twist-iso , refl
coarse-collision : (x : R.Point) → R.pull twist-filler fst x ≡ fst x
coarse-collision (false , b) = refl
coarse-collision (true , false) = refl
coarse-collision (true , true) = refl

then-swap : R.Filler → R.Filler
then-swap f = B.compose {a = B.fourQ} {b = B.fourQ} {c = B.fourQ} f B.swap-filler
continuation-separates : R.pull (then-swap R.id-filler) fst (true , false)
  ≡ R.pull (then-swap twist-filler) fst (true , false) → ⊥
continuation-separates p = false≢true p

signature : R.Point → Bool × Bool
signature x = R.pull R.id-filler fst x , R.pull B.swap-filler fst x
signature-recovers : (x : R.Point) → signature x ≡ x
signature-recovers (a , b) = refl
signature-faithful : (x y : R.Point) → signature x ≡ signature y → x ≡ y
signature-faithful x y p = sym (signature-recovers x) ∙ p ∙ signature-recovers y
