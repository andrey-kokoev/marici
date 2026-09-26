{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedComparisonSeries where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import QBooleanity using (D; eta)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Sigma.Base using (_×_)
import BoundaryGeneratedQuestions as B
import NativeTableRegression as Native
import WholePackageSigmaPi as Whole
import ObserverCoherenceCube as Observer

Point : Type
Point = Bool × Bool
Filler : Type
Filler = B.Filler B.fourQ B.fourQ
id-filler : Filler
id-filler = B.identity B.fourQ

-- Evaluate the ACTUAL retained equivalence; the observer acts contravariantly.
pull : {A : Type} → Filler → (Point → A) → Point → A
pull f v x = v (equivFun (fst f) x)
pull-identity : {A : Type} (v : Point → A) → pull id-filler v ≡ v
pull-identity v = refl
pull-compose : {A : Type} (f g : Filler) (v : Point → A)
  → pull (B.compose {a = B.fourQ} {b = B.fourQ} {c = B.fourQ} f g) v
    ≡ pull f (pull g v)
pull-compose f g v = refl
pull-inverse : {A : Type} (f : Filler) (v : Point → A)
  → pull (B.inverse {a = B.fourQ} {b = B.fourQ} f) (pull f v) ≡ v
pull-inverse f v = funExt (λ x → cong v (Iso.rightInv (equivToIso (fst f)) x))
pull-higher : {A : Type} {f g : Filler} → f ≡ g
  → (v : Point → A) → pull f v ≡ pull g v
pull-higher p v = cong (λ f → pull f v) p
pull-pointwise : {A D E : Type} (op : A → D → E) (f : Filler)
  (u : Point → A) (v : Point → D)
  → pull f (λ x → op (u x) (v x)) ≡ (λ x → op (pull f u x) (pull f v x))
pull-pointwise op f u v = refl

-- Coefficients of the formal series G_f(z)=sum z^n pull_f^n.
coefficient : {A : Type} → Filler → ℕ → (Point → A) → Point → A
coefficient f zero v = v
coefficient f (suc n) v = pull f (coefficient f n v)
first-coefficient : {A : Type} (f : Filler) (v : Point → A)
  → coefficient f 1 v ≡ pull f v
first-coefficient f v = refl
swap-square : {A : Type} (v : Point → A) → pull B.swap-filler (pull B.swap-filler v) ≡ v
swap-square v = funExt (λ { (x , y) → refl })
swap-period-two : {A : Type} (n : ℕ) (v : Point → A)
  → coefficient B.swap-filler (suc (suc n)) v ≡ coefficient B.swap-filler n v
swap-period-two n v = swap-square (coefficient B.swap-filler n v)

-- Reification and the established native-table bridge keep the same readout.
retained-pull : {A : Type} (f : Filler) (v : Point → A)
  → pull (Whole.Universe.value (B.retain-filler B.fourQ B.fourQ f)) v ≡ pull f v
retained-pull f v = refl
native-pull : {A : Type} → Filler → (Point → A) → Point → A
native-pull f v x = v (equivFun (fst
  (equivFun (Native.actual-filler-equivalence B.fourQ B.fourQ) f)) x)
native-pull-agrees : {A : Type} (f : Filler) (v : Point → A) → native-pull f v ≡ pull f v
native-pull-agrees f v = refl

-- Machine-readable finite images are checked against imported source witnesses.
code : Point → ℕ
code (false , false) = 0
code (false , true) = 1
code (true , false) = 2
code (true , true) = 3
images : Filler → ℕ × (ℕ × (ℕ × ℕ))
images f = pull f code (false , false) , pull f code (false , true) ,
  pull f code (true , false) , pull f code (true , true)
identity-image-codes : images id-filler ≡ (0 , 1 , 2 , 3)
identity-image-codes = refl
swap-image-codes : images B.swap-filler ≡ (0 , 2 , 1 , 3)
swap-image-codes = refl

-- The first operator coefficient does not factor through the old truth quotient.
no-truth-factor : (w : D Filler → Bool)
  → ((f : Filler) → w (eta f) ≡ pull f fst (false , true)) → ⊥
no-truth-factor w law = false≢true
  (sym (law id-filler) ∙ cong w B.truth-identifies-fillers ∙ law B.swap-filler)

-- Do not relabel a different comparison as a nonzero original schedule square.
module SquareControl (O R : Type) (e : O ≃ R) where
  module Cells = Observer.Geometry O R e
  readout-equal : {A : Type} (v : R × R → A)
    → Path (O × O → A) (λ s → v (Cells.run Cells.leftFirst s))
      (λ s → v (Cells.run Cells.rightFirst s))
  readout-equal v i s = v (Cells.route-homotopy i s)
