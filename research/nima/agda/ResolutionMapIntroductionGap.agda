{-# OPTIONS --safe --cubical --guardedness #-}
module ResolutionMapIntroductionGap where
open import Cubical.Foundations.Prelude renaming (_∙_ to trans)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥; rec)
open import Cubical.Data.Unit.Base using (Unit; tt)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution

module Gap (ℓ : Level) where
  open Whole.Universe ℓ
  open Resolution.Generators ℓ
  map-root : Code → Bool
  map-root (maps _ _) = true
  map-root _ = false

  -- Exhaustive inspection of the actual twelve schemas: none introduces a
  -- package with a bare maps constructor at the root.
  rule-not-map : (r : Rule) → map-root (expression (output r)) ≡ false
  rule-not-map (E-rule I F i) = refl
  rule-not-map (Pi-rule I F) = refl
  rule-not-map (compare-rule a b e p) = refl
  rule-not-map (identity-rule a) = refl
  rule-not-map (inverse-rule a b e p) = refl
  rule-not-map (compose-rule a b c e f p q) = refl
  rule-not-map (higher-rule Q x y p q alpha) = refl
  rule-not-map (reflexivity-rule Q x) = refl
  rule-not-map (path-lift-rule Q R e x y) = refl
  rule-not-map (distribution-rule I J F v) = refl
  rule-not-map (E-congruence-rule I F G e p i) = refl
  rule-not-map (Pi-congruence-rule I F G e p) = refl

  map-root-must-be-seeded : {S : Complete → Type (ℓ-suc ℓ)} {q : Complete}
    → Resolve S q → map-root (expression q) ≡ true → S q
  map-root-must-be-seeded (seed s) p = s
  map-root-must-be-seeded (apply r ds) p =
    rec (false≢true (trans (sym (rule-not-map r)) p))

  map-package-must-be-seeded : {S : Complete → Type (ℓ-suc ℓ)}
    (Q R : Code) (f : El Q → El R)
    → Resolve S (map-package Q R f) → S (map-package Q R f)
  map-package-must-be-seeded Q R f d = map-root-must-be-seeded d refl

  EmptySeeds : Complete → Type (ℓ-suc ℓ)
  EmptySeeds q = Lift ⊥
  no-unseeded-map-package : (Q R : Code) (f : El Q → El R)
    → Resolve EmptySeeds (map-package Q R f) → ⊥
  no-unseeded-map-package Q R f d = lower (map-package-must-be-seeded Q R f d)

-- The opposite semantic control: with a unit seed, the unrestricted index
-- parameters can encode ANY SUPPLIED function, under E/Pi rather than maps.
-- Therefore the head-tag theorem is not a semantic expressivity obstruction.
module SuppliedFunction (A B : Type) (f : A → B) where
  open Whole.Universe ℓ-zero
  open Resolution.Generators ℓ-zero
  unitQ : Complete
  unitQ = pack (atom Unit) tt
  data Seeds : Complete → Type₁ where
    unit-seed : Seeds unitQ
  family : A → Complete
  family a = E-package B (λ _ → unitQ) (f a)
  family-derived : (a : A) → Resolve Seeds (family a)
  family-derived a = apply (E-rule B (λ _ → unitQ) (f a)) (λ _ → seed unit-seed)
  encoded : Complete
  encoded = Pi-package A family
  encoded-derived : Resolve Seeds encoded
  encoded-derived = apply (Pi-rule A family) (λ { (lift a) → family-derived a })
  supplied-function-recovered : (a : A) → fst (value encoded a) ≡ f a
  supplied-function-recovered a = refl

