{-# OPTIONS --safe --cubical --guardedness #-}
module MarkedTriangleCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Equiv.Properties using (equivAdjointEquiv)
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Path using
  (compPathlEquiv; compPathrEquiv; compPathl-isEquiv; compPathr-isEquiv; symIso)
open import Cubical.Foundations.GroupoidLaws using (rCancel)
open import Cubical.Data.Unit.Base using (tt)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Empty.Base using (⊥)
open import GradedBoundaryCoherence using
  (module Tower; plain-filler; twisted-filler; marked-fillers-distinct)

module Triangles {ℓ : Level} (A : Type ℓ) where
  Triangle : {x y z : A} → x ≡ y → y ≡ z → x ≡ z → Type ℓ
  Triangle p q r = p ∙ q ≡ r

  -- All three vertices and two selected edges are fixed in each horn.
  MissingDiagonal : {x y z : A} → x ≡ y → y ≡ z → Type ℓ
  MissingDiagonal {x} {y} {z} p q = Σ[ r ∈ (x ≡ z) ] Triangle p q r

  diagonal-completion : {x y z : A} (p : x ≡ y) (q : y ≡ z)
    → isContr (MissingDiagonal p q)
  diagonal-completion p q = (p ∙ q , refl) , λ { (r , a) i → a i , (λ j → a (i ∧ j)) }

  MissingSecond : {x y z : A} → x ≡ y → x ≡ z → Type ℓ
  MissingSecond {x} {y} {z} p r = Σ[ q ∈ (y ≡ z) ] Triangle p q r

  second-completion : {x y z : A} (p : x ≡ y) (r : x ≡ z)
    → isContr (MissingSecond {y = y} p r)
  second-completion p r = equiv-proof (compPathl-isEquiv p) r

  MissingFirst : {x y z : A} → y ≡ z → x ≡ z → Type ℓ
  MissingFirst {x} {y} {z} q r = Σ[ p ∈ (x ≡ y) ] Triangle p q r

  first-completion : {x y z : A} (q : y ≡ z) (r : x ≡ z)
    → isContr (MissingFirst {x = x} q r)
  first-completion q r = equiv-proof (compPathr-isEquiv q) r

  -- Equivalent readings preserve the chosen face witness, not merely existence.
  solve-second : {x y z : A} (p : x ≡ y) (q : y ≡ z) (r : x ≡ z)
    → Triangle p q r ≃ (q ≡ sym p ∙ r)
  solve-second p q r = invEquiv (equivAdjointEquiv (compPathlEquiv p))

  solve-first : {x y z : A} (p : x ≡ y) (q : y ≡ z) (r : x ≡ z)
    → Triangle p q r ≃ (p ≡ r ∙ sym q)
  solve-first p q r = invEquiv (equivAdjointEquiv (compPathrEquiv q))

  -- Cyclically relabel vertices x,y,z as y,z,x and reverse the two necessary
  -- edge orientations. This is an equivalence of marked face-witness spaces.
  rotate : {x y z : A} (p : x ≡ y) (q : y ≡ z) (r : x ≡ z)
    → Triangle p q r ≃ Triangle q (sym r) (sym p)
  rotate p q r = compEquiv (solve-second p q r)
    (compEquiv (isoToEquiv symIso)
      (compEquiv (invEquiv (equivAdjointEquiv (compPathrEquiv r)))
        (isoToEquiv symIso)))

  rotation-recovery : {x y z : A} (p : x ≡ y) (q : y ≡ z) (r : x ≡ z)
    (a : Triangle p q r)
    → invEq (rotate p q r) (equivFun (rotate p q r) a) ≡ a
  rotation-recovery p q r = retEq (rotate p q r)

  -- Comparison with the previous globular tower retains the factorization
  -- p,q as parameters. It is a fiber equivalence, not boundary erasure.
  module G = Tower A
  globular-boundary : {x y z : A} (p : x ≡ y) (q : y ≡ z) (r : x ≡ z)
    → G.Boundary 2
  globular-boundary {x} {y} {z} p q r = (lift tt , x , z) , (p ∙ q) , r

  globular-filler-equivalence : {x y z : A} (p : x ≡ y) (q : y ≡ z) (r : x ≡ z)
    → Triangle p q r ≃ G.Fill 2 (globular-boundary p q r)
  globular-filler-equivalence p q r = idEquiv _

  -- Free inner-horn completion, with all supplied horn data held fixed.
  Horn : Type ℓ
  Horn = Σ[ x ∈ A ] Σ[ y ∈ A ] Σ[ z ∈ A ] ((x ≡ y) × (y ≡ z))

  Completion : Horn → Type ℓ
  Completion (x , y , z , p , q) = MissingDiagonal p q

  complete-unique : (h : Horn) → isContr (Completion h)
  complete-unique (x , y , z , p , q) = diagonal-completion p q

  Filled : Type ℓ
  Filled = Σ[ h ∈ Horn ] Completion h

  complete : Horn → Filled
  complete h = h , fst (complete-unique h)

  forget : Filled → Horn
  forget = fst

  forget-complete : (h : Horn) → forget (complete h) ≡ h
  forget-complete h = refl

  complete-forget : (t : Filled) → complete (forget t) ≡ t
  complete-forget (h , c) i = h , snd (complete-unique h) c i

  horn-iso : Iso Filled Horn
  horn-iso = record
    { fun = forget ; inv = complete
    ; rightInv = forget-complete ; leftInv = complete-forget }

  -- The recovery homotopy never moves the supplied horn.
  horn-fixed : (t : Filled) → cong forget (complete-forget t) ≡ refl
  horn-fixed t = refl

  dependent-interpretation-iso : {ℓ' : Level} (Y : Horn → Type ℓ')
    → Iso ((t : Filled) → Y (forget t)) ((h : Horn) → Y h)
  dependent-interpretation-iso Y = record
    { fun = λ g h → g (complete h)
    ; inv = λ f t → f (forget t)
    ; rightInv = λ f → refl
    ; leftInv = λ g → funExt λ { (h , c) →
        cong (λ c' → g (h , c')) (snd (complete-unique h) c) } }

  DependentExtension : {ℓ' : Level} (Y : Horn → Type ℓ')
    (f : (h : Horn) → Y h) → Type (ℓ-max ℓ ℓ')
  DependentExtension Y f = Σ[ g ∈ ((t : Filled) → Y (forget t)) ]
    ((λ h → g (complete h)) ≡ f)

  unique-dependent-extension : {ℓ' : Level} (Y : Horn → Type ℓ') (f : (h : Horn) → Y h)
    → isContr (DependentExtension Y f)
  unique-dependent-extension Y f =
    equiv-proof (snd (isoToEquiv (dependent-interpretation-iso Y))) f

  interpretation-iso : {ℓ' : Level} (Y : Type ℓ') → Iso (Filled → Y) (Horn → Y)
  interpretation-iso Y = dependent-interpretation-iso (λ _ → Y)

  Extension : {ℓ' : Level} (Y : Type ℓ') (f : Horn → Y) → Type (ℓ-max ℓ ℓ')
  Extension Y f = DependentExtension (λ _ → Y) f

  unique-extension : {ℓ' : Level} (Y : Type ℓ') (f : Horn → Y)
    → isContr (Extension Y f)
  unique-extension Y f = unique-dependent-extension (λ _ → Y) f

  -- A triangle with all vertices marked retains every edge and its face proof.
  MarkedTriangle : (x y z : A) → Type ℓ
  MarkedTriangle x y z = Σ[ p ∈ (x ≡ y) ] Σ[ q ∈ (y ≡ z) ] MissingDiagonal p q

  first-edge : {x y z : A} → MarkedTriangle x y z → x ≡ y
  first-edge = fst

  diagonal : {x y z : A} → MarkedTriangle x y z → x ≡ z
  diagonal t = fst (snd (snd t))

module Types = Triangles (Type ℓ-zero)

-- Equal return edge, but distinct retained factorizations.
ordinary twisted : Types.MarkedTriangle Bool Bool Bool
ordinary = refl , refl , refl , rCancel refl
twisted = twisted-filler , sym twisted-filler , refl , rCancel twisted-filler

same-diagonal : Types.diagonal ordinary ≡ Types.diagonal twisted
same-diagonal = refl

different-factorizations : ordinary ≡ twisted → ⊥
different-factorizations p = marked-fillers-distinct (cong Types.first-edge p)

no-diagonal-recovery : (recover : (Bool ≡ Bool) → Types.MarkedTriangle Bool Bool Bool)
  → ((t : Types.MarkedTriangle Bool Bool Bool) → recover (Types.diagonal t) ≡ t)
  → ⊥
no-diagonal-recovery recover law = different-factorizations (sym (law ordinary) ∙ law twisted)

-- Fixing the third edge too is a different question and may obstruct filling.
unfillable-triangle : Types.Triangle refl refl twisted-filler → ⊥
unfillable-triangle a = marked-fillers-distinct (sym (rCancel refl) ∙ a)
