{-# OPTIONS --safe --cubical --guardedness #-}
module DependentNormalizationCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.HLevels using (isContr→isContrPath)
import WholePackageSigmaPi as Whole
import DependentPackageNormalization as Normal

module Coherence (ℓ : Level) (Q : Whole.Universe.Code ℓ) where
  open Whole.Universe ℓ
  module N = Normal.Normalization ℓ

  -- A presentation includes a faithful equivalence to the SAME complete
  -- normal value type. Equality of mere endpoint signatures is insufficient.
  record Presentation : Type (ℓ-suc ℓ) where
    constructor presentation
    field
      expression : Code
      coordinates : El expression ≃ N.Value (N.normal Q)
  open Presentation

  original : Presentation
  original = presentation Q (N.normalize-equiv Q)

  normal : Presentation
  normal = presentation (N.reexpress (N.normal Q)) (idEquiv _)

  CoherentMap : Presentation → Presentation → Type ℓ
  CoherentMap P R = (x : El (expression P)) →
    Σ[ y ∈ El (expression R) ] (equivFun (coordinates R) y ≡ equivFun (coordinates P) x)

  map-center : (P R : Presentation) → CoherentMap P R
  map-center P R x = equivCtr (coordinates R) (equivFun (coordinates P) x)

  map-contractible : (P R : Presentation) → isContr (CoherentMap P R)
  map-contractible P R = map-center P R ,
    (λ f t x → equivCtrPath (coordinates R) (equivFun (coordinates P) x) (f x) t)

  identity : (P : Presentation) → CoherentMap P P
  identity P x = x , refl

  compose : {P R T : Presentation} → CoherentMap P R → CoherentMap R T → CoherentMap P T
  compose f g x = fst (g (fst (f x))) , snd (g (fst (f x))) ∙ snd (f x)

  normalize-map : CoherentMap original normal
  normalize-map x = N.normalize Q x , refl

  reconstruct-map : CoherentMap normal original
  reconstruct-map x = N.reconstruct Q x , N.normal-roundtrip Q x

  compare-maps : {P R : Presentation} (f g : CoherentMap P R) → f ≡ g
  compare-maps {P} {R} = isContr→isProp (map-contractible P R)

  higher-comparison : {P R : Presentation} {f g : CoherentMap P R}
    (p q : f ≡ g) → p ≡ q
  higher-comparison {P} {R} {f} {g} =
    isContr→isProp (isContr→isContrPath (map-contractible P R) f g)

  -- Every existing equivalence gives a coordinate-preserving step into its
  -- transported presentation. The coordinates themselves are retained.
  advance : (P : Presentation) (R : Code) → El (expression P) ≃ El R → Presentation
  advance P R e = presentation R (compEquiv (invEquiv e) (coordinates P))

  advance-map : (P : Presentation) (R : Code) (e : El (expression P) ≃ El R)
    → CoherentMap P (advance P R e)
  advance-map P R e x = equivFun e x , cong (equivFun (coordinates P)) (retEq e x)

  data Route : Presentation → Presentation → Type (ℓ-suc ℓ) where
    stop : {P : Presentation} → Route P P
    next : {P R T : Presentation} → CoherentMap P R → Route R T → Route P T

  evaluate : {P R : Presentation} → Route P R → CoherentMap P R
  evaluate (stop {P}) = identity P
  evaluate (next {P} {R} {T} f route) = compose {P} {R} {T} f (evaluate route)

  route-comparison : {P R : Presentation} (a b : Route P R) → evaluate a ≡ evaluate b
  route-comparison {P} {R} a b = compare-maps {P} {R} (evaluate a) (evaluate b)

  -- Route records are retained; only their interpreted complete maps are
  -- compared. These constructors do not identify raw route syntax.
  record Certificate : Type (ℓ-suc ℓ) where
    constructor certificate
    field
      source target : Presentation
      first second : Route source target
      witness : evaluate first ≡ evaluate second

  certify : {P R : Presentation} → Route P R → Route P R → Certificate
  certify {P} {R} a b = certificate P R a b (route-comparison a b)

  reify-certificate : Certificate → Whole.Universe.Complete (ℓ-suc ℓ)
  reify-certificate c = Whole.Universe.pack (Whole.Universe.atom Certificate) c

  -- A uniform operation on a contractibility witness supplies the next
  -- higher comparison level, and can be iterated at any specified height.
  lift-contractibility : {A : Type ℓ} → isContr A → (x y : A) → isContr (x ≡ y)
  lift-contractibility = isContr→isContrPath
