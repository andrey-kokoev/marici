{-# OPTIONS --safe --cubical --guardedness #-}
module TickRelativeLocality where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties using (false≢true)
import Cubical.Data.Empty as Empty
open import Cubical.Data.Sigma.Base using (_×_; Σ)
open import Cubical.Algebra.Ring.Base
import TickRelativeSourceContract as C

module Locality (K : Ring ℓ-zero) (half angularScale : fst K)
  (Time : Type) (phase : Time → fst K) where
  open RingStr (snd K)
  module D = C.Relative K half angularScale Time phase
  open D using (Vector; generator; spectral-leg; DerivedComponents)
  module V = D.V

  Fiber = Bool → fst K
  fiber-generator : Fiber → Fiber
  fiber-generator v x = angularScale · (half · (v x + (- v (not x))))
  fiber-leg : Time → Fiber → Fiber
  fiber-leg t v x = v x + ((phase t + (- 1r)) · (half · (v x + (- v (not x)))))

  -- No cross-factor samples occur: the other coordinate is held fixed.
  left-generator-slice : (v : Vector) (y : Bool)
    → (λ x → generator V.L v (x , y)) ≡ fiber-generator (λ x → v (x , y))
  left-generator-slice v y = refl
  right-generator-slice : (v : Vector) (x : Bool)
    → (λ y → generator V.R v (x , y)) ≡ fiber-generator (λ y → v (x , y))
  right-generator-slice v x = refl
  left-leg-slice : (t : Time) (v : Vector) (y : Bool)
    → (λ x → spectral-leg V.L t v (x , y)) ≡ fiber-leg t (λ x → v (x , y))
  left-leg-slice t v y = refl
  right-leg-slice : (t : Time) (v : Vector) (x : Bool)
    → (λ y → spectral-leg V.R t v (x , y)) ≡ fiber-leg t (λ y → v (x , y))
  right-leg-slice t v x = refl

  rename : Bool → Bool → Bool
  rename false x = x
  rename true x = not x

  rename-not : (b x : Bool) → not (rename b x) ≡ rename b (not x)
  rename-not false x = refl
  rename-not true x = refl

  -- Every injective Bool renaming, hence every Bool bijection, occurs here.
  classify-values : (f : Bool → Bool) (u v : Bool)
    → f false ≡ u → f true ≡ v
    → ((x y : Bool) → f x ≡ f y → x ≡ y)
    → Σ Bool (λ b → f ≡ rename b)
  classify-values f false false p q injective = Empty.rec (false≢true (injective false true (p ∙ sym q)))
  classify-values f false true p q injective = false , funExt λ { false → p ; true → q }
  classify-values f true false p q injective = true , funExt λ { false → p ; true → q }
  classify-values f true true p q injective = Empty.rec (false≢true (injective false true (p ∙ sym q)))

  classify-renaming : (f : Bool → Bool)
    → ((x y : Bool) → f x ≡ f y → x ≡ y)
    → Σ Bool (λ b → f ≡ rename b)
  classify-renaming f = classify-values f (f false) (f true) refl refl

  reindex : (Bool × Bool → Bool × Bool) → Vector → Vector
  reindex h v q = v (h q)
  relabel : Bool → Bool → Vector → Vector
  relabel b c = reindex (λ { (x , y) → rename b x , rename c y })
  exchange : Vector → Vector
  exchange = reindex (λ { (x , y) → y , x })

  delta-relabel : (b u x : Bool) → V.delta u (rename b x) ≡ V.delta (rename b u) x
  delta-relabel false u x = refl
  delta-relabel true false false = refl
  delta-relabel true false true = refl
  delta-relabel true true false = refl
  delta-relabel true true true = refl

  basis-relabel : (b c : Bool) (u v : Bool)
    → relabel b c (V.basis (u , v)) ≡ V.basis (rename b u , rename c v)
  basis-relabel b c u v = funExt λ { (x , y) →
    cong₂ _·_ (delta-relabel b u x) (delta-relabel c v y) }

  -- Polynomial construction transports every flip intertwiner.
  generator-natural : (h : Bool × Bool → Bool × Bool) (A B : Vector → Vector)
    → ((v : Vector) → reindex h (A v) ≡ B (reindex h v))
    → (v : Vector) → reindex h (generator A v) ≡ generator B (reindex h v)
  generator-natural h A B commute v = funExt λ q →
    cong (λ z → angularScale · (half · (v (h q) + (- z))))
      (cong (λ f → f q) (commute v))

  leg-natural : (h : Bool × Bool → Bool × Bool) (A B : Vector → Vector)
    → ((v : Vector) → reindex h (A v) ≡ B (reindex h v))
    → (t : Time) (v : Vector) → reindex h (spectral-leg A t v) ≡ spectral-leg B t (reindex h v)
  leg-natural h A B commute t v = funExt λ q →
    cong (λ z → v (h q) + ((phase t + (- 1r)) · (half · (v (h q) + (- z)))))
      (cong (λ f → f q) (commute v))

  left-relabel : (b c : Bool) (v : Vector) → relabel b c (V.L v) ≡ V.L (relabel b c v)
  left-relabel b c v = funExt λ { (x , y) → cong (λ z → v (z , rename c y)) (rename-not b x) }
  right-relabel : (b c : Bool) (v : Vector) → relabel b c (V.R v) ≡ V.R (relabel b c v)
  right-relabel b c v = funExt λ { (x , y) → cong (λ z → v (rename b x , z)) (rename-not c y) }

  left-generator-relabel : (b c : Bool) (v : Vector)
    → relabel b c (generator V.L v) ≡ generator V.L (relabel b c v)
  left-generator-relabel b c = generator-natural _ V.L V.L (left-relabel b c)
  right-generator-relabel : (b c : Bool) (v : Vector)
    → relabel b c (generator V.R v) ≡ generator V.R (relabel b c v)
  right-generator-relabel b c = generator-natural _ V.R V.R (right-relabel b c)
  left-leg-relabel : (b c : Bool) (t : Time) (v : Vector)
    → relabel b c (spectral-leg V.L t v) ≡ spectral-leg V.L t (relabel b c v)
  left-leg-relabel b c = leg-natural _ V.L V.L (left-relabel b c)
  right-leg-relabel : (b c : Bool) (t : Time) (v : Vector)
    → relabel b c (spectral-leg V.R t v) ≡ spectral-leg V.R t (relabel b c v)
  right-leg-relabel b c = leg-natural _ V.R V.R (right-relabel b c)

  exchange-left-generator : (v : Vector) → exchange (generator V.L v) ≡ generator V.R (exchange v)
  exchange-left-generator = generator-natural _ V.L V.R (λ v → refl)
  exchange-right-generator : (v : Vector) → exchange (generator V.R v) ≡ generator V.L (exchange v)
  exchange-right-generator = generator-natural _ V.R V.L (λ v → refl)
  exchange-left-leg : (t : Time) (v : Vector) → exchange (spectral-leg V.L t v) ≡ spectral-leg V.R t (exchange v)
  exchange-left-leg = leg-natural _ V.L V.R (λ v → refl)
  exchange-right-leg : (t : Time) (v : Vector) → exchange (spectral-leg V.R t v) ≡ spectral-leg V.L t (exchange v)
  exchange-right-leg = leg-natural _ V.R V.L (λ v → refl)

  exchange-ordered-composite : (t u : Time) (v : Vector)
    → exchange (spectral-leg V.R u (spectral-leg V.L t v))
      ≡ spectral-leg V.L u (spectral-leg V.R t (exchange v))
  exchange-ordered-composite t u v = exchange-right-leg u (spectral-leg V.L t v)
    ∙ cong (spectral-leg V.L u) (exchange-left-leg t v)

  -- Transport to any candidate admitted by the relative contract.
  module ForCandidate (candidate : DerivedComponents) where
    open D.DerivedComponents candidate
    candidate-left-local : (t : Time) (v : Vector) (y : Bool)
      → (λ x → left-leg t v (x , y)) ≡ fiber-leg t (λ x → v (x , y))
    candidate-left-local t v y = cong (λ F → λ x → F t v (x , y)) left-leg-derived
      ∙ left-leg-slice t v y
    candidate-right-local : (t : Time) (v : Vector) (x : Bool)
      → (λ y → right-leg t v (x , y)) ≡ fiber-leg t (λ y → v (x , y))
    candidate-right-local t v x = cong (λ F → λ y → F t v (x , y)) right-leg-derived
      ∙ right-leg-slice t v x
    candidate-left-generator-local : (v : Vector) (y : Bool)
      → (λ x → left-generator v (x , y)) ≡ fiber-generator (λ x → v (x , y))
    candidate-left-generator-local v y = cong (λ F → λ x → F v (x , y)) left-generator-derived
      ∙ left-generator-slice v y
    candidate-right-generator-local : (v : Vector) (x : Bool)
      → (λ y → right-generator v (x , y)) ≡ fiber-generator (λ y → v (x , y))
    candidate-right-generator-local v x = cong (λ F → λ y → F v (x , y)) right-generator-derived
      ∙ right-generator-slice v x
    candidate-left-relabel : (b c : Bool) (t : Time) (v : Vector)
      → relabel b c (left-leg t v) ≡ left-leg t (relabel b c v)
    candidate-left-relabel b c t v = cong (λ F → relabel b c (F t v)) left-leg-derived
      ∙ left-leg-relabel b c t v
      ∙ sym (cong (λ F → F t (relabel b c v)) left-leg-derived)
    candidate-right-relabel : (b c : Bool) (t : Time) (v : Vector)
      → relabel b c (right-leg t v) ≡ right-leg t (relabel b c v)
    candidate-right-relabel b c t v = cong (λ F → relabel b c (F t v)) right-leg-derived
      ∙ right-leg-relabel b c t v
      ∙ sym (cong (λ F → F t (relabel b c v)) right-leg-derived)
    candidate-exchange : (t : Time) (v : Vector)
      → exchange (left-leg t v) ≡ right-leg t (exchange v)
    candidate-exchange t v = cong (λ F → exchange (F t v)) left-leg-derived
      ∙ exchange-left-leg t v
      ∙ sym (cong (λ F → F t (exchange v)) right-leg-derived)
